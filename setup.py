import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "include": ["tkinter"], "include_files": ["imgs/", "botIcon.iso"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="lol queue acceptor",
    version="3.0.1",
    description="Interface gráfica adicionada",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="bot.py", base=None, icon="botIcon.ico")],
)