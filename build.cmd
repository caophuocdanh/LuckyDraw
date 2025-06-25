pip install PySide6 pygame
pyinstaller --windowed --icon="luckydraw.ico" --name "LuckyDraw" --hidden-import "win32timezone" main.py

copy background_music.mp3 dist\LuckyDraw\_internal
copy win_sound.mp3 dist\LuckyDraw\_internal
copy config.json dist\LuckyDraw\_internal

