import sys
from cx_Freeze import setup, Executable

base = None

#if sys.platform == "win32" : base = "Win32GUI"

exe = Executable(script = "main.py", base= base)

setup(
    name = 'main',
    version = '0.1', 
    description = 'ファイルを共有します。',
    executables = [exe]
)