# SPDX-License-Identifier: MIT
# Makefile

# Define the default shell
SHELL := /bin/bash

# Define the command to build the project.
build:
	@echo "Building the project..."
	@poetry run nuitka --clang --onefile avnie/main.py

test:
	@poetry run pytest .

install:
	@poetry install --sync