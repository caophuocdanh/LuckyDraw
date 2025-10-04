rmdir /s /q build,dist
pip install -r requirements.txt
pyinstaller --windowed --icon="luckydraw.ico" --hidden-import "win32timezone" --name="Lucky Draw" main.py
xcopy assets dist\assets /E /I /Y

