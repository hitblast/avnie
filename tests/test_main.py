# SPDX-License-Identifier: MIT

# Import first-party Python libraries.
import subprocess


# Test cases.
def test_conversion_bijoy_func():
    result = subprocess.run(["avnie", "tobijoy", "আমি বাংলায় গান গাই;"], capture_output=True, text=True)
    assert result.stdout.strip() == "Avwg evsjvq Mvb MvB;"


def test_full_sentences():
    result = subprocess.run(["avnie", "parse", "ami banglay gan gai;"], capture_output=True, text=True)
    assert result.stdout.strip() == "আমি বাংলায় গান গাই;"

    result = subprocess.run(
        ["avnie", "parse", "ami banglay gan gai;", "--bijoy"], capture_output=True, text=True
    )
    assert result.stdout.strip() == "Avwg evsjvq Mvb MvB;"

    result = subprocess.run(["avnie", "reverse", "আমি বাংলায় গান গাই।"], capture_output=True, text=True)
    assert result.stdout.strip() == "ami banglay gan gai."
