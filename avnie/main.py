# SPDX-License-Identifier: MIT

# This is the non-interactive (command-based) version of the CLI.

# Import third-party Python modules.
import os
from typing import Optional

import avro
import click
import pyclip
import requests

# Import the version number from the package.
from avnie import __version__
from avnie import interactive as interactive_mode


# Define the CLI group.
# This uses the Click library to define the CLI commands.
@click.group()
@click.version_option(__version__)
def app():
    pass


# Helper function to handle no text provided exceptions.
def _handle_no_text(text: str, from_clipboard: bool) -> str:
    if not text:
        if not from_clipboard:
            click.secho("No text provided.", fg="red", err=True)
            raise click.Abort()
        else:
            if not (text := pyclip.paste(text=True).strip()):
                click.secho("No text found in the clipboard.", fg="red", err=True)
                raise click.Abort()
    return text


# Define the CLI commands.
@app.command()
def interactive() -> None:
    interactive_mode.main()


@app.command()
@click.argument("text", required=False, type=str)
@click.option("--bijoy", "-b", is_flag=True, help="Convert the text to Bijoy layout.")
@click.option("--ignore-remap", "-i", is_flag=True, help="Skip remapping the words.")
@click.option("--from-clipboard", "-f", is_flag=True, help="Get the text from the clipboard.")
@click.option("--copy-on-success", "-c", is_flag=True, help="Copy the output to the clipboard.")
def parse(
    text: Optional[str], bijoy: bool, ignore_remap: bool, from_clipboard: bool, copy_on_success: bool
) -> None:
    text = _handle_no_text(text, from_clipboard)

    output = avro.parse(text, remap_words=not ignore_remap)
    if bijoy:
        output = avro.to_bijoy(output)

    click.echo(output)
    if copy_on_success:
        pyclip.copy(output)


@app.command()
@click.argument("text", required=False, type=str)
@click.option("--ignore-remap", "-i", is_flag=True, help="Skip remapping the words.")
@click.option("--from-clipboard", "-f", is_flag=True, help="Get the text from the clipboard.")
@click.option("--copy-on-success", "-c", is_flag=True, help="Copy the output to the clipboard.")
def reverse(text: Optional[str], ignore_remap: bool, from_clipboard: bool, copy_on_success: bool) -> None:
    text = _handle_no_text(text, from_clipboard)
    output = avro.reverse(text, remap_words=not ignore_remap)

    click.echo(output)
    if copy_on_success:
        pyclip.copy(output)


@app.command()
@click.argument("text", required=False, type=str)
@click.option("--from-clipboard", "-f", is_flag=True, help="Get the text from the clipboard.")
@click.option("--copy-on-success", "-c", is_flag=True, help="Copy the output to the clipboard.")
def tobijoy(text: Optional[str], from_clipboard: bool, copy_on_success: bool) -> None:
    text = _handle_no_text(text, from_clipboard)
    output = avro.to_bijoy(text)

    click.echo(output)
    if copy_on_success:
        pyclip.copy(output)


@app.command()
def checkupdate() -> None:
    click.echo("Checking for updates...")
    response = requests.get("https://pypi.org/pypi/avnie/json")

    if response.status_code != 200:
        click.secho("Failed to check for updates.", fg="red", err=True)
        click.echo("Please try again later.")
        raise click.Abort()

    latest_version = response.json()["info"]["version"]

    if latest_version != __version__:
        click.secho("An update is available.", fg="yellow")
        click.echo("Please run `pip install --upgrade avnie` to update.")
    else:
        click.secho("No updates available.", fg="green")
        click.echo("You are already using the latest version.")


# Define the main function to run the CLI.
def run() -> None:
    # If AVRO_INTERACTIVE is set, run the interactive mode by default.
    if os.getenv("AVRO_INTERACTIVE") == "1":
        interactive_mode.main()
    else:
        app()
