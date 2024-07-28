# SPDX-License-Identifier: MIT


# Import first-party Python modules.
import subprocess


# Test cases.
def test_parse_english_to_bengali(mocker):
    mocker.patch(
        "subprocess.run",
        return_value=subprocess.CompletedProcess(
            args=["avni", "parse", "hello"], returncode=0, stdout="হ্যালো"
        ),
    )
    result = subprocess.run(["avni", "parse", "hello"], capture_output=True, text=True)
    assert result.stdout.strip() == "হ্যালো"


def test_reverse_bengali_to_english(mocker):
    mocker.patch(
        "subprocess.run",
        return_value=subprocess.CompletedProcess(
            args=["avni", "reverse", "হ্যালো"], returncode=0, stdout="hello"
        ),
    )
    result = subprocess.run(["avni", "reverse", "হ্যালো"], capture_output=True, text=True)
    assert result.stdout.strip() == "hello"
