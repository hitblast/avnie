# SPDX-License-Identifier: MIT

# Import third-party Python modules.
from typer.testing import CliRunner

# Import the module containing the CLI commands.
from avnie.main import app


# Test cases.
def test_parse_english_to_bengali():
    runner = CliRunner()
    result = runner.invoke(app, ["parse", "hyalO"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "হ্যালো"


def test_reverse_bengali_to_english():
    runner = CliRunner()
    result = runner.invoke(app, ["reverse", "আমি বাংলায় গান গাই"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "ami banglay gan gai"
