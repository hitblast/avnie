# SPDX-License-Identifier: MIT


# Import first-party Python libraries.
from pathlib import Path

# Import third-party Python libraries.
import PyInstaller.__main__

# Define the PyInstaller options.
HERE = Path(__file__).parent.absolute()
path_to_main = str(HERE / "main.py")

# Define the PyInstaller command.
PyInstaller.__main__.run(
    [
        "--onefile",
        "--console",
        "--clean",
        path_to_main,
    ]
)
