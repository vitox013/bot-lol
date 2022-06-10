import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter"], "include_files": ["imgs/", "botIcon.ico", "LICENSE", "README.md"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="lol queue acceptor",
    version="3.0.0",
    description="Interface gráfica adicionada",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="bot.py", base= "WIN32GUI", icon="botIcon.ico")],
)