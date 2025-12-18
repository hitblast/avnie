<div align="center">

# <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" width="35px"/> avnie

Command-line interface to avro.py; transliteration in the terminal.

[![Downloads](https://static.pepy.tech/personalized-badge/avnie?period=total&units=international_system&left_text=Downloads)](https://pepy.tech/project/avnie)
![Python Version](https://img.shields.io/pypi/pyversions/avro.py.svg?label=Python)
![License](https://img.shields.io/pypi/l/avnie.svg?label=License)
[![Tests & Lints CI](https://github.com/hitblast/avnie/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/hitblast/avnie/actions/workflows/tests.yml)

</div>

## 🔨 Installation

> [!NOTE]
> This package requires **Python 3.9 or higher** to be used inside your development environment.

```sh
# Install using uv.
uv tool install avnie

# Or, using pip:
pip install avnie
```

## 🚀 Usage

### Command Mode

```sh
# Get basic help regarding usage.
$ avnie --help

# Parse from English.
$ avnie parse "ami banglay gan gaite bhalObasi"

# Reverse back!
$ avro reverse "আমি বাংলায় গান গাইতে ভালোবাসি"
```

Some universal flags for each commands include:

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

### 🔸 Interactive Mode

You can start the interactive mode by running the following command:

```sh
$ avnie interactive
```

If you'd like to make it the default way of using the tool, set the `AVRO_INTERACTIVE` environment variable to `1` in your shell configuration file (e.g. `.bashrc`, `.zshrc`, etc.).

```sh
# Add this to your shell configuration file.
export AVRO_INTERACTIVE=1
```

---

## 📋 License

Licensed under the [MIT License](https://github.com/hitblast/avnie/blob/main/LICENSE).
