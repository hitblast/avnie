# SPDX-License-Identifier: MIT

# This is the interactive (TUI-based) version of the CLI.


# Import third-party Python modules.
from dataclasses import dataclass
from typing import Union

import avro
import pyclip
from rich.console import Console
from rich.prompt import Confirm, Prompt

# Import the version number.
from avnie import __version__


# Define the dataclass for prompt options.
@dataclass
class PromptOptions:
    skip_all: bool = True
    ignore_remap: bool = False
    copy_on_success: bool = True
    bijoy_output: bool = False


# Helper functions for the interactive function.
def _common_prompts() -> Union[PromptOptions, None]:
    skip_all = not Confirm.ask("Use advanced options?", default=False)

    if skip_all:
        return

    copy_on_success = Confirm.ask("Copy output to clipboard?", default=PromptOptions.copy_on_success)
    ignore_remap = Confirm.ask("Skip remapping the words?", default=PromptOptions.ignore_remap)

    return PromptOptions(
        skip_all=skip_all,
        ignore_remap=ignore_remap,
        copy_on_success=copy_on_success,
    )


# Define the interactive function.
def interactive(console: Console) -> None:
    while True:
        console.clear()
        console.print(f"avnie [bold green]v{__version__}[/bold green]\n")
        action = Prompt.ask("What do you want to do?", choices=["parse", "reverse", "exit"])

        if action == "exit":
            break

        text = Prompt.ask(f"Enter the text to {'parse' if action == 'parse' else 'reverse'}:")

        console.clear()
        options = _common_prompts() or PromptOptions()

        bijoy = False
        if action == "parse" and not options.skip_all:
            bijoy = Confirm.ask("Convert the text to Bijoy layout?", default=bijoy)

        console.clear()
        output = (
            avro.parse(text, bijoy=bijoy, remap_words=not options.ignore_remap)
            if action == "parse"
            else avro.reverse(text, remap_words=not options.ignore_remap)
        )

        console.print("Output:", output)
        if options.copy_on_success:
            pyclip.copy(output)
            console.print("\n[bold green]Output copied to the clipboard.[/bold green]")

        if not Confirm.ask("Continue?", default=True):
            break


# Define the interactive function.
def main() -> None:
    console = Console()
    interactive(console)


# Run the main function if this script is executed.
if __name__ == "__main__":
    main()
