from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RAPIDAPI_HOST = "youtube-mp36.p.rapidapi.com"
RAPIDAPI_KEY = "f707dd8d67mshaf3d42fbdfe97c8p1d93d4jsnd8b8ceb0121e"

@app.route('/convert', methods=['GET'])
def convert_video():
    video_id = request.args.get('id')
    if not video_id:
        return jsonify({"error": "Missing video ID"}), 400

    url = f"https://{RAPIDAPI_HOST}/dl?id={video_id}"
    headers = {
        'x-rapidapi-host': RAPIDAPI_HOST,
        'x-rapidapi-key': RAPIDAPI_KEY
    }

    response = requests.get(url, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
