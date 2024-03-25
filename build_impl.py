import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--windowed',  # This prevents the console from appearing
    '--name=ImplSearch',  # name of the .exe file
    '--icon=C:\\Users\\yanap\\PycharmProjects\\ImplSearch\\myicon1.png',
])
