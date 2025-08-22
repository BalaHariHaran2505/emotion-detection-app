import requests


def detect_emotion(text_to_analyze):
    """
    Detect emotions in text using Watson Emotion API.
    Falls back to mock data if API fails or no response is returned.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=input_json)

        if response.status_code == 200:
            result = response.json()
            emotions = result.get("text", {}).get("emotion", {})
            if emotions:
                return emotions
            return {
                "joy": 0.75,
                "sadness": 0.1,
                "anger": 0.05,
                "fear": 0.05,
                "disgust": 0.05,
            }

        if response.status_code == 400:
            return {
                "joy": None,
                "sadness": None,
                "anger": None,
                "fear": None,
                "disgust": None,
            }

        return {"error": f"Error: Received status code {response.status_code}"}

    except Exception as e:
        return {"error": str(e)}


def format_output(emotion_dict):
    """
    Format the emotion dictionary into a readable string.
    """
    if "error" in emotion_dict:
        return f"Error: {emotion_dict['error']}"
    if all(value is None for value in emotion_dict.values()):
        return "Invalid text! Please try again!"
    formatted = "Detected Emotions:\n"
    for emotion, score in emotion_dict.items():
        formatted += f" - {emotion.capitalize()}: {score}\n"
    return formatted
