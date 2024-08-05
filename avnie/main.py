# SPDX-License-Identifier: MIT


# Import first-party Python libraries.
from typing import Optional

# Import third-party Python libraries.
import avro
import pyclip
import typer
from typing_extensions import Annotated

# Setup the Typer app.
app = typer.Typer(
    name="avnie",
    help="A modern Pythonic implementation of Avro Phonetic.",
)


# Helper function for CLI actions.
def _cli_action(
    text: str,
    *,
    bijoy: bool = False,
    remap_words: bool = True,
    from_clipboard: bool = False,
    copy_on_success: bool = False,
    reverse: bool = False,
) -> Optional[str]:
    if not text:
        if not from_clipboard:
            typer.secho("No text provided.", fg=typer.colors.RED, err=True)
            raise typer.Exit(1)
        else:
            if not (text := pyclip.paste(text=True).strip()):
                typer.secho(
                    "No text found in the clipboard.", fg=typer.colors.RED, err=True
                )
                raise typer.Exit(1)

    if reverse:
        output = avro.reverse(text, remap_words=remap_words)
    else:
        output = avro.parse(text, remap_words=remap_words)
        if bijoy:
            output = avro.to_bijoy(output)

    if copy_on_success:
        pyclip.copy(output)

    typer.echo(output)


# Define the CLI commands.


# avro parse <text> [--bijoy] [--ignore-remap] [--from-clipboard] [--copy-on-success]
@app.command()
def parse(
    text: str = typer.Argument(None, help="The text to be converted."),
    bijoy: Annotated[
        bool, typer.Option("--bijoy", "-b", help="Convert the text to Bijoy layout.")
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
        typer.Option(
            "--copy-on-success", "-c", help="Copy the output to the clipboard."
        ),
    ] = False,
) -> None:
    _cli_action(
        text,
        bijoy=bijoy,
        remap_words=not ignore_remap,
        from_clipboard=from_clipboard,
        copy_on_success=copy_on_success,
    )


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
        typer.Option(
            "--copy-on-success", "-c", help="Copy the output to the clipboard."
        ),
    ] = False,
) -> None:
    _cli_action(
        text,
        remap_words=not ignore_remap,
        from_clipboard=from_clipboard,
        copy_on_success=copy_on_success,
        reverse=True,
    )
