import sys
import os
import json
from cx_Freeze import setup, Executable

base_path = 'Win32GUI' if sys.platform == 'win32' else None
# Specify the path to the appropriate base for Windows
build_exe_options = {"packages": ["tkinter"], "include_files": ["buttons.json"]}
if base_path is not None:
    build_exe_options["base"] = base_path
    build_exe_options["targetName"] = ["soundboard.exe"]

# Create an executable for the soundboard
executables = [Executable("main.py")]

# Check if data.json file exists and create it if not
basedir = os.path.dirname(os.path.abspath(__file__))
if not os.path.isfile(os.path.join(basedir, 'buttons.json')):
    with open(os.path.join(basedir, 'buttons.json'), 'w') as f:
        json.dump({'buttons': []}, f)

include_files = ['buttons.json']
# Specify the build options for cx_Freeze
build_options = {"build_exe": {"packages": ["tkinter"], "include_files": include_files}}

# Create a setup script for the soundboard
setup(
    name="Soundboard",
    version="1.0",
    description="A simple soundboard application",
    options=build_options,
    executables=executables
)
