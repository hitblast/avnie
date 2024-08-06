# SPDX-License-Identifier: MIT

# Import third-party Python modules.
from typer.testing import CliRunner

# Import the module containing the CLI commands.
from avnie.main import app

# Test cases.
# This uses the typer.testing.CliRunner class to test the CLI commands.
runner = CliRunner()


def test_conversion_bijoy_func():
    result = runner.invoke(app, ["tobijoy", "আমি বাংলায় গান গাই;"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Avwg evsjvq Mvb MvB;"


def test_full_sentences():
    result = runner.invoke(app, ["parse", "ami banglay gan gai;"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "আমি বাংলায় গান গাই;"

    result = runner.invoke(app, ["parse", "--bijoy", "ami banglay gan gai;"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Avwg evsjvq Mvb MvB;"

    result = runner.invoke(app, ["reverse", "আমি বাংলায় গান গাই।"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "ami banglay gan gai."
