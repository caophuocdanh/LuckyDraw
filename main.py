import tkinter as tk
from tkinter import font, messagebox
import json, random, math, os, sys
import threading
import pygame  # Thêm pygame để phát nhạc

class LuckyDrawApp:
    def __init__(self, root):
        self.root = root
        self.config = self.load_config()
        if not self.config:
            self.root.destroy(); return

        self.settings = self.config['settings']
        self.prizes_config = self.config['prizes']
        if sum(p['count'] for p in self.prizes_config) > self.settings['total_numbers']:
            messagebox.showerror("Lỗi", "Số lượng giải thưởng nhiều hơn số lượng người tham gia!")
            self.root.destroy(); return

        self.all_numbers = list(range(1, self.settings['total_numbers'] + 1))
        self.available_numbers = self.all_numbers.copy()
        self.prize_queue = [dict(p) for p in reversed(self.prizes_config) for _ in range(p['count'])]
        self.number_labels, self.result_widgets = {}, []
        self.results_file = "results.json"
        self.is_drawing, self.animation_id, self.flashed_labels = False, None, []
        self.is_blinking = False

        pygame.mixer.init()

        self.setup_ui()
        self.create_number_grid()
        self.left_frame.bind("<Configure>", self.redraw_number_grid)
        self.load_previous_results()
        self.add_top_right_buttons()

    def play_sound(self, file="win_sound.mp3"):
        def _play():
            try:
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
            except Exception as e:
                print("Lỗi phát nhạc:", e)
        threading.Thread(target=_play).start()

    def load_config(self):
        try:
            with open("config.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            messagebox.showerror("Lỗi", "Không thể đọc file config.json!")
            return None

    def load_previous_results(self):
        if not os.path.exists(self.results_file):
            open(self.results_file, "w", encoding="utf-8").close(); return
        try:
            with open(self.results_file, "r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip(): continue
                    result = json.loads(line)
                    number = result['number']
                    prize = next((p for p in self.prizes_config if p['name'] == result['prize']), None)
                    if prize and number in self.available_numbers:
                        self.available_numbers.remove(number)
                        self.prize_queue.remove(next(p for p in self.prize_queue if p['name'] == prize['name']))
                        self.add_result_to_list(prize, number, loading=False)
                        if number in self.number_labels:
                            self.number_labels[number].config(bg=prize['color'], fg="white")
        except Exception:
            open(self.results_file, "w", encoding="utf-8").close()

    def save_result_to_file(self, prize, number):
        try:
            with open(self.results_file, "a", encoding="utf-8") as f:
                f.write(json.dumps({"prize": prize['name'], "number": number}, ensure_ascii=False) + "\n")
        except Exception as e:
            print("Lỗi ghi file:", e)

    def reset_app(self):
        if os.path.exists(self.results_file): os.remove(self.results_file)
        self.root.destroy(); os.execl(sys.executable, sys.executable, *sys.argv)

    def add_top_right_buttons(self):
        frame = tk.Frame(self.root, bg="#ffffff")
        frame.place(relx=1.0, rely=0.0, anchor="ne")
        for text, cmd in [("❌", self.root.destroy), ("🔄", self.reset_app)]:
            tk.Button(frame, text=text, font=("Helvetica", 16), command=cmd,
                      bg="#ffffff", bd=0, relief=tk.FLAT, cursor="hand2"
            ).pack(side=tk.RIGHT, padx=5, pady=5)

    def setup_ui(self):
        self.root.title(self.settings.get('title', "Quay Số May Mắn"))
        self.root.configure(bg="#ffffff")
        self.root.attributes('-fullscreen', True)

        container = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        container.pack(fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=0)

        self.left_frame = tk.Frame(container, bg="#ffffff")
        self.left_frame.grid(row=0, column=0, sticky="nsew")

        self.right_frame = tk.Frame(container, bg="#ffffff", width=400)
        self.right_frame.grid(row=0, column=1, sticky="ns")
        self.right_frame.grid_propagate(False)

        self.setup_right_panel()

    def setup_right_panel(self):
        self.right_frame.grid_rowconfigure(0, weight=0)
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        button_frame = tk.Frame(self.right_frame, bg="#ffffff")
        button_frame.grid(row=0, column=0, sticky="n")

        icon_font = font.Font(family="Segoe UI Emoji", size=60, weight="bold")
        self.draw_button = tk.Button(
            button_frame, text="🎁", font=icon_font, fg="white",
            command=self.start_draw, bg="#f72585", activebackground="#0056b3",
            activeforeground="white", relief=tk.FLAT, borderwidth=0, cursor="hand2", width=7, height=2
        )
        self.draw_button.pack(pady=(35, 30))

        self.results_wrapper = tk.Frame(self.right_frame, bg="#ffffff", width=350)
        self.results_wrapper.grid(row=1, column=0, sticky="n")
        self.results_wrapper.grid_propagate(False)

        self.results_frame = tk.Frame(self.results_wrapper, bg="#ffffff")
        self.results_frame.pack(fill="both", expand=True)

    def create_number_grid(self):
        shuffled = self.all_numbers.copy(); random.shuffle(shuffled)
        self.label_font = font.Font(family="Helvetica", size=30)
        for number in shuffled:
            self.number_labels[number] = tk.Label(
                self.left_frame, text=f"{number:02d}", font=self.label_font,
                bg="white", fg="black", relief=tk.SOLID, borderwidth=1
            )

    def redraw_number_grid(self, event=None):
        w, h, n = self.left_frame.winfo_width(), self.left_frame.winfo_height(), len(self.all_numbers)
        if w < 50 or h < 50 or n == 0: return
        cols = max(1, int(math.sqrt(n * (w / h)))); rows = math.ceil(n / cols)
        for i in range(rows): self.left_frame.grid_rowconfigure(i, weight=1)
        for i in range(cols): self.left_frame.grid_columnconfigure(i, weight=1)
        for i, number in enumerate(self.number_labels):
            self.number_labels[number].grid(row=i//cols, column=i%cols, sticky="nsew", padx=2, pady=2)

    def start_draw(self):
        if self.is_drawing or self.is_blinking or not self.prize_queue or not self.available_numbers:
            messagebox.showinfo("Thông báo", "Hết giải rồi, quay cái chi nữa mà bấm!"); return
        self.is_drawing = True
        self.draw_button.config(state=tk.DISABLED, cursor="", fg="gray")
        self.current_prize = self.prize_queue.pop(0)
        self.animate_cells()
        self.root.after(self.settings['draw_duration_seconds'] * 1000, self.finish_draw)

    def animate_cells(self):
        if not self.is_drawing: return
        for lbl, bg, fg in self.flashed_labels:
            lbl.config(bg=bg, fg=fg)
        self.flashed_labels.clear()

        num_to_flash = max(1, len(self.available_numbers) // 5)
        flashing = random.sample(self.available_numbers, min(num_to_flash, len(self.available_numbers)))
        for num in flashing:
            lbl = self.number_labels[num]
            self.flashed_labels.append((lbl, lbl.cget("bg"), lbl.cget("fg")))
            lbl.config(bg="#FFD700", fg="black")
        self.animation_id = self.root.after(100, self.animate_cells)

    def finish_draw(self):
        self.is_drawing = False
        if self.animation_id:
            self.root.after_cancel(self.animation_id); self.animation_id = None
        for lbl, bg, fg in self.flashed_labels:
            lbl.config(bg=bg, fg=fg)
        self.flashed_labels.clear()

        if not self.available_numbers: 
            self.draw_button.config(state=tk.NORMAL, cursor="hand2", fg="white")
            return

        winner = random.choice(self.available_numbers)
        self.available_numbers.remove(winner)
        lbl = self.number_labels[winner]
        lbl.config(bg=self.current_prize['color'], fg="white")
        self.is_blinking = True
        self.blink_label(lbl, times=6, callback=lambda: self.on_blink_done(lbl, winner))

    def on_blink_done(self, lbl, number):
        self.is_blinking = False
        self.add_result_to_list(self.current_prize, number)
        self.save_result_to_file(self.current_prize, number)
        self.play_sound()  # Gọi nhạc sau khi quay xong
        self.draw_button.config(state=tk.NORMAL, cursor="hand2", fg="white")

    def blink_label(self, label, times, callback):
        def toggle(c):
            if c <= 0:
                label.config(bg=self.current_prize['color'], fg="white")
                if callback: callback()
                return
            curr = label.cget("bg")
            label.config(bg="white" if curr != "white" else self.current_prize['color'], fg="black" if curr != "white" else "white")
            self.root.after(200, lambda: toggle(c - 1))
        toggle(times)

    def add_result_to_list(self, prize, number, loading=True):
        label = tk.Label(
            self.results_frame, text=f"{prize['name']}: {number:02d}",
            bg=prize['color'], fg="white", font=("Helvetica", 16, "bold"),
            padx=20, pady=20, anchor="c", width=22
        )
        if loading:
            self.result_widgets.insert(0, label)
        else:
            self.result_widgets.append(label)
        for widget in self.results_frame.winfo_children(): widget.pack_forget()
        for widget in self.result_widgets: widget.pack(fill='x', pady=2)

if __name__ == "__main__":
    root = tk.Tk()
    LuckyDrawApp(root)
    root.mainloop()
