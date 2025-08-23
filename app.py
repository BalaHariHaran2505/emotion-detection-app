from flask import Flask, request, jsonify
from emotion_package.emotion_app import detect_emotion, format_output

app = Flask(__name__)

@app.route("/emotion", methods=["POST"])
def emotion():
    data = request.get_json()
    text = data.get("text", "") if data else ""
    emotions = detect_emotion(text)
    output = format_output(emotions)
    return jsonify({"emotions": emotions, "formatted": output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
