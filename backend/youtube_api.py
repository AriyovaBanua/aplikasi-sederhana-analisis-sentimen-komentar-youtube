import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

def extract_video_id(youtube_url):
    if "v=" in youtube_url:
        return youtube_url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in youtube_url:
        return youtube_url.split("youtu.be/")[1].split("?")[0]
    return None

def get_comments(video_id, max_total=1000):
    comments = []
    base_url = "https://www.googleapis.com/youtube/v3/commentThreads"
    params = {
        "part": "snippet",
        "videoId": video_id,
        "key": API_KEY,
        "maxResults": 100,  # maksimal per page adalah 100
        "textFormat": "plainText"
    }

    while len(comments) < max_total:
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print("Error fetching comments:", response.status_code, response.text)
            break

        data = response.json()

        for item in data.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)
            if len(comments) >= max_total:
                break

        # Ambil token untuk halaman berikutnya
        next_page_token = data.get("nextPageToken")
        if not next_page_token:
            break  # tidak ada komentar lebih lanjut
        params["pageToken"] = next_page_token

    return comments
