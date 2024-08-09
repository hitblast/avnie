<!-- SPDX-License-Identifier: MIT -->

<div align="center">

# <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" height="40px"/> avnie

A fast & user-friendly command-line interface (CLI) for **avro.py**.

[![Downloads](https://static.pepy.tech/personalized-badge/avnie?period=total&units=international_system&left_color=grey&right_color=black&left_text=Downloads)](https://pepy.tech/project/avnie)
![Python Version](https://img.shields.io/pypi/pyversions/avro.py.svg?color=black&label=Python)
![License](https://img.shields.io/pypi/l/avnie.svg?color=black&label=License)

<br>

<img src="https://github.com/hitblast/avnie/blob/main/assets/banner.png?raw=True" style="width: 500px; height: auto;"><br>

[![Unit Tests](https://github.com/hitblast/avnie/actions/workflows/unit-tests.yml/badge.svg?branch=main)](https://github.com/hitblast/avnie/actions/workflows/unit-tests.yml)
[![Nightly Builds](https://github.com/hitblast/avnie/actions/workflows/nightly.yml/badge.svg?branch=main)](https://github.com/hitblast/avnie/actions/workflows/nightly.yml)
[![Linting](https://github.com/hitblast/avnie/actions/workflows/linting.yml/badge.svg)](https://github.com/hitblast/avnie/actions/workflows/linting.yml)
[![Formatting](https://github.com/hitblast/avnie/actions/workflows/formatting.yml/badge.svg)](https://github.com/hitblast/avnie/actions/workflows/formatting.yml)

<br>

</div>

---

<br>

## ⚡ Overview

**avnie** provides a fast and sleek command-line based user interface for the [avro.py](https://github.com/hitblast/avro.py) Python package. It allows you to easily do all of the necessary functions avro.py provides - parsing from English, reversing to Bengali, converting to other formats, you name it! And, avnie does this without the need of writing any actual code.

The project is also built on top of the same Python version that avro.py is based on, so that you can have both of these installed on your local machine without needing to cross-interpret between them.

## ✨ ... but for whom?

The project is made for those who'd like to use their terminal as a way of quickly and conveniently typing Avro Keyboard-based Bengali text without the need for a hefty frontend UI, or for all the terminal geeks out there.

<br>

## 🔨 Installation

- ### Pip
This package requires **Python 3.8 or higher** to be used inside your development environment.

```sh
# Install / upgrade.
$ pip install avnie
```

- ### Prebuilt Binaries

Prebuilt binaries are available for **Windows, macOS, and Linux**. You can download the latest binary from the [Releases](https://github.com/hitblast/avnie/releases) section for your respective platform. After downloading, you can add the binary to your `PATH` variable for easy access.

<br>

## 🚀 Usage

### 🔸 Command Mode

The usage of avnie is pretty straightforward. You can either use `avro` or `avnie` as the keyword for executing avnie commands. Here are some examples:

```sh
# Get basic help regarding usage.
# This also provides additional functionality like autocompletion (TBA).
$ avnie --help
$ avro --help  # or

# Parse a given English text to Bengali.
$ avro parse "ami banglay gan gaite bhalObasi"

# Reverse a given Bengali text to English.
$ avro reverse "আমি বাংলায় গান গাইতে ভালোবাসি"
```

More commands and features will be available as the project progresses in its development phase. For now, you can use the commands above to get started with the basic functionalities. Additional options can be found by running `avnie <command> --help`.

Some **universal flags** for each commands include:
```sh
# Automatically copy the output to clipboard.
$ avnie parse "oiTa ke?" --copy-on-success  # or -c

# Get text from clipboard.
$ avnie parse --from-clip # or -f

# Toggle between remap and full manual mode.
$ avnie parse "wikipedia"  # remap
$ avnie parse "wikipedia" --ignore-remap  # no remap (can also use --i)

# Convert to Bijoy on output.
$ avnie parse "tumi ke?" --bijoy  # or -b
```

---

### 🔸 Interactive Mode

There is also a dedicated **"Interactive Mode"** in case you don't like typing the same command over and over again. This is enabled in prebuilt binaries by default. 

You can start the interactive mode by running the following command:
```sh
$ avnie interactive
```

If you'd like to make it the default way of using the tool, set the `AVRO_INTERACTIVE` environment variable to `1` in your shell configuration file (e.g. `.bashrc`, `.zshrc`, etc.).

```sh
# Add this to your shell configuration file.
export AVRO_INTERACTIVE=1
```

<br>

## 🔨 Building for Python

If you'd like to build the project from source for your local Python installation, you can follow the steps given below to get started:

#### Requirements
- [Python 3.8](https://www.python.org) or higher
- The [Poetry](https://python-poetry.org) package manager

#### Steps

```sh
# Create a virtual environment using the venv command.
$ python -m venv venv && source venv/bin/activate

# Install the required dependencies and optionally update them.
$ make install # or poetry install --sync
$ poetry update

# Start using it!
$ avnie --help

# Optionally, you can also build the Python package locally.
$ poetry build
```

Optionally, run unit tests to ensure everything is working as expected:

```sh
# This uses the inclued Makefile.
$ make test

# or, run the pytest framework from poetry directly.
$ poetry run pytest .
```

<br>

## ⚒️ Compiling to Binaries

If you'd like to compile the project to a binary for your respective platform, you can follow the steps given below to get started:

#### Requirements
- [Python 3.12](https://www.python.org) or higher
- The [Poetry](https://python-poetry.org) package manager
- [Clang](https://clang.llvm.org) (preferred C compiler, you can use others as well)

#### Steps
```sh
# Create a virtual environment using the venv command.
$ python -m venv venv && source venv/bin/activate

# Install the required dependencies and optionally update them.
$ make install && poetry update

# Compile using Nuitka. This uses the included Makefile.
$ make build
```

After running the command above, you should either see a `main.bin` or a `main.exe` file in the project directory depending on what platform you're compiling for. You can then use this binary to run the project on your local machine.

---

<br>

## 📋 License

Licensed under the [MIT License](https://github.com/hitblast/avnie/blob/main/LICENSE).
