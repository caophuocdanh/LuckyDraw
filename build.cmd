pip install PySide6 pygame
pyinstaller --onefile --windowed --icon="luckydraw.ico" --hidden-import "win32timezone" --name="Lucky Draw" main.py