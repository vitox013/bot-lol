import sys
from cx_Freeze import setup, Executable

bdist_msi_options = {
        "author": "Vitor Muller",
        "comments": "https://github.com/vitox013/bot-lol"
    }

setup(
    name="Bot Fila",
    options = {"build_exe":{"packages": ["os"], "includes": ["tkinter"], "include_files": ["imgs/", "LICENSE", "README.md"]},
    "bdist_msi": {'summary_data':bdist_msi_options}},
    version="4.0.0",
    description="Lol queue acceptor",
    executables=[Executable("bot.py", 
    shortcut_name="Bot Fila",
    shortcut_dir="DesktopFolder", 
    base="Win32GUI",icon="imgs/botIcon.ico")]
)