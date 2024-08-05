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

> [!IMPORTANT]
> avnie is currently in development and not yet recommended for production use, however you can take part in shaping it's future by [submitting an issue](https://github.com/hitblast/avnie/issues) to let us know what you think.

---

<br>

## ⚡ Overview

**avnie** provides a fast and sleek command-line based user interface for the [avro.py](https://github.com/hitblast/avro.py) Python package. It allows you to easily do all of the necessary functions avro.py provides - parsing from English, reversing to Bengali, converting to other formats, you name it! And, avnie does this without the need of writing any actual code.

The project is also built on top of the same Python version that avro.py is based on, so that you can have both of these installed on your local machine without needing to cross-interpret between them.

## ✨ ... but for whom?

The project is made for those who'd like to use their terminal as a way of quickly and conveniently typing Avro Keyboard-based Bengali text without the need for a hefty frontend UI, or for all the terminal geeks out there.

<br>

## 🔨 Installation

#### Pip
This package requires **Python 3.8 or higher** to be used inside your development environment.

```sh
# Install / upgrade.
$ pip install avnie
```

<br>

## 🚀 Usage

The usage of avnie is pretty straightforward. You can either use `avro` or `avnie` as the keyword for executing avnie commands. Here are some examples:

```sh
# Get basic help regarding usage.
# This also provides additional functionality like autocompletion (TBA).
$ avnie --help
$ avro --help  # or

# Parse a given English text to Bengali.
$ avro parse "ami banglay gan gaite bhalobasi"

# Reverse a given Bengali text to English.
$ avro reverse "আমি বাংলায় গান গাইতে ভালবাসি"
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
$ avnie parse "আমি বাংলায় গান গাইতে ভালবাসি" --bijoy  # or -b
```

<br>

## 🔨 Building

#### Requirements
- [Python 3.8](https://www.python.org) or higher
- The [Poetry](https://python-poetry.org) package manager


#### Steps

```sh
# Create a virtual environment using the venv command.
$ python -m venv venv && source venv/bin/activate

# Install the required dependencies.
$ poetry install --sync

# (Optional) Update the dependencies.
$ poetry update
```

#### Running Unit Tests

```sh
# Use the following command to run the unit tests.
$ poetry run pytest .
```

<br>

---

## 📋 License

Licensed under the [MIT License](https://github.com/hitblast/avnie/blob/main/LICENSE).
