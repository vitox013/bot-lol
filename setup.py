import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "include_files": ["button.png", "verificaInicio.png", "botIcon.ico"]}

setup(
    name="lol queue acceptor",
    version="1.0",
    description="Aceita a fila do lol automaticamente",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="bot.py", base=None, icon="botIcon.ico")],
)