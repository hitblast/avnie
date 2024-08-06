# SPDX-License-Identifier: MIT

# Import first-party Python libraries.

# Import third-party Python libraries.
import avro
import pyclip
import requests
import typer
from typing_extensions import Annotated

# Import local modules.
from . import __version__

# Setup the Typer app.
app = typer.Typer(
    name="avnie",
    help="A fast & user-friendly command-line interface (CLI) for avro.py.",
)


# Helper function for handling "no text" error.
def _handle_no_text(
    text: str,
    from_clipboard: bool,
) -> str:
    if not text:
        if not from_clipboard:
            typer.secho("No text provided.", fg=typer.colors.RED, err=True)
            raise typer.Exit(1)
        else:
            if not (text := pyclip.paste(text=True).strip()):
                typer.secho("No text found in the clipboard.", fg=typer.colors.RED, err=True)
                raise typer.Exit(1)
    return text


# Define the CLI commands.
# avro parse <text> [--bijoy] [--ignore-remap] [--from-clipboard] [--copy-on-success]
@app.command()
def parse(
    text: str = typer.Argument(None, help="The text to be converted."),
    bijoy: Annotated[
        bool,
        typer.Option("--bijoy", "-b", help="Convert the text to Bijoy layout."),
    ] = False,
    ignore_remap: Annotated[
        bool, typer.Option("--ignore-remap", "-i", help="Skip remapping the words.")
    ] = False,
    from_clipboard: Annotated[
        bool,
        typer.Option("--from-clipboard", "-f", help="Get the text from the clipboard."),
    ] = False,
    copy_on_success: Annotated[
        bool,
        typer.Option("--copy-on-success", "-c", help="Copy the output to the clipboard."),
    ] = False,
) -> None:
    text = _handle_no_text(text, from_clipboard)

    output = avro.parse(text, remap_words=not ignore_remap)
    if bijoy:
        output = avro.to_bijoy(output)

    typer.echo(output)
    if copy_on_success:
        pyclip.copy(output)


# avro reverse <text> [--ignore-remap] [--from-clipboard] [--copy-on-success]
@app.command()
def reverse(
    text: str = typer.Argument(None, help="The text to be converted."),
    ignore_remap: Annotated[
        bool, typer.Option("--ignore-remap", "-i", help="Skip remapping the words.")
    ] = False,
    from_clipboard: Annotated[
        bool,
        typer.Option("--from-clipboard", "-f", help="Get the text from the clipboard."),
    ] = False,
    copy_on_success: Annotated[
        bool,
        typer.Option("--copy-on-success", "-c", help="Copy the output to the clipboard."),
    ] = False,
) -> None:
    text = _handle_no_text(text, from_clipboard)
    output = avro.reverse(text, remap_words=not ignore_remap)

    typer.echo(output)
    if copy_on_success:
        pyclip.copy(output)


# avro tobijoy <text> [--from-clipboard] [--copy-on-success]
# do not use _cli_action here as it is a simple wrapper
@app.command()
def tobijoy(
    text: str = typer.Argument(None, help="The text to be converted."),
    from_clipboard: Annotated[
        bool,
        typer.Option("--from-clipboard", "-f", help="Get the text from the clipboard."),
    ] = False,
    copy_on_success: Annotated[
        bool,
        typer.Option("--copy-on-success", "-c", help="Copy the output to the clipboard."),
    ] = False,
) -> None:
    text = _handle_no_text(text, from_clipboard)
    output = avro.to_bijoy(text)

    typer.echo(output)
    if copy_on_success:
        pyclip.copy(output)


# avro checkupdate
@app.command()
def checkupdate() -> None:
    typer.echo("Checking for updates...")
    response = requests.get("https://pypi.org/pypi/avnie/json")

    if response.status_code != 200:
        typer.secho("Failed to check for updates.", fg=typer.colors.RED, err=True)
        typer.echo("Please try again later.")
        raise typer.Exit(1)

    latest_version = response.json()["info"]["version"]

    if latest_version != __version__:
        typer.secho("An update is available.", fg=typer.colors.YELLOW)
        typer.echo("Please run `pip install --upgrade avnie` to update.")
    else:
        typer.secho("No updates available.", fg=typer.colors.GREEN)
        typer.echo("You are already using the latest version.")
    raise typer.Exit(0)
