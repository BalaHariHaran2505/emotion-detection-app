import pytest
from emotion_app import detect_emotion, format_output


def test_detect_emotion_valid():
    result = detect_emotion("I am very happy today!")
    assert isinstance(result, dict)
    assert "joy" in result


def test_format_output_valid():
    emotions = {"joy": 0.9, "sadness": 0.1}
    output = format_output(emotions)
    assert "Joy" in output
    assert "Sadness" in output


def test_format_output_invalid():
    emotions = {
        "joy": None,
        "sadness": None,
        "anger": None,
        "fear": None,
        "disgust": None,
    }
    output = format_output(emotions)
    assert output == "Invalid text! Please try again!"


def test_error_handling():
    error_dict = {"error": "Some API error"}
    output = format_output(error_dict)
    assert "Error" in output
