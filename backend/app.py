from flask import Flask, request, jsonify
from flask_cors import CORS
from youtube_api import extract_video_id, get_comments
from sentiment_analysis import analyze_sentiment  # IndoBERT version

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    youtube_url = data.get("url")

    if not youtube_url:
        return jsonify({"error": "URL tidak ditemukan"}), 400

    video_id = extract_video_id(youtube_url)
    if not video_id:
        return jsonify({"error": "Video ID tidak valid"}), 400

    comments = get_comments(video_id)
    if not comments:
        return jsonify({"error": "Komentar tidak ditemukan"}), 404

    sentiment_result = analyze_sentiment(comments)

    return jsonify(sentiment_result)

if __name__ == "__main__":
    app.run(debug=True)
