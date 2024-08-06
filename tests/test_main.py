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

    result = runner.invoke(
        app, ["parse", "ami banglar gan gai.", "ami amar amike cirodin ei banglay khu^je pai."]
    )
    assert result.exit_code == 0
    assert result.stdout.strip() == "আমি বাংলার গান গাই।\nআমি আমার আমিকে চিরদিন এই বাংলায় খুঁজে পাই।"

    result = runner.invoke(app, ["parse", "--bijoy", "ami banglay gan gai;"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Avwg evsjvq Mvb MvB;"

    result = runner.invoke(
        app, ["parse", "--bijoy", "ami banglar gan gai.", "ami amar amike cirodin ei banglay khu^je pai!"]
    )
    assert result.exit_code == 0
    assert result.stdout.strip() == "Avwg evsjvi Mvb MvB|\nAvwg Avgvi Avwg‡K wPiw`b GB evsjvq Lyu‡R cvB!"

    result = runner.invoke(app, ["reverse", "আমি বাংলায় গান গাই।"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "ami banglay gan gai."

    result = runner.invoke(
        app, ["reverse", "রহিম, তোমাকে করিম ডাকছে। এখন কি রওনা দেবে?", "রওনা দিলে আমাকে বলে যেও।"]
    )
    assert result.exit_code == 0
    assert (
        result.stdout.strip()
        == "rohim, tomake korim dakche. ekhon ki rowna debe?\nrowna dile amake bole zew."
    )
