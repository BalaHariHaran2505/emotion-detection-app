from flask import Flask, request, jsonify
from emotion_app import detect_emotion

app = Flask(__name__)


@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Analyze emotions from given text input.
    """
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Text is required"}), 400

    emotions = detect_emotion(data["text"])
    return jsonify({"result": emotions})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
