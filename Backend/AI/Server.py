import sys
import os
from flask import Flask, request, jsonify
from Agent import AI
from flask_cors import CORS
from Resources import WebLinks_Generator,WebYoutubeGenerator
from Humanize import Humanize
app = Flask(__name__)
CORS(app)

@app.route("/search", methods=["POST"])
def search_api():
    data = request.get_json() or request.data.decode("utf-8").strip()
    if not data:
        return jsonify({"error": "Empty input", "status": 300}), 300
    
    query = data.get("query") if isinstance(data, dict) else data
    
    if not query:
        return jsonify({"error": "Query is required", "status": 300}), 300

    result = AI(query)
    return jsonify({"input": query, "output": result, "status": "success"}),200



@app.route("/webResources", methods=["POST"])
def webResources():
    data = request.get_json() or request.data.decode("utf-8").strip()
    if not data:
        return jsonify({"error": "Empty input", "status": 300}), 300
    
    query = data.get("query") if isinstance(data, dict) else data
    
    if not query:
        return jsonify({"error": "Query is required", "status": 300}), 300

    yt = WebYoutubeGenerator()
    result_youtube=yt.forward(query)
    wt = WebLinks_Generator()
    result_web= wt.forward(query)
    return jsonify({"input": query, "webLinks":result_web,"youtube_videos":result_youtube, "status": "success"})


@app.route("/humanize", methods=["POST"])
def Humanize():
    data = request.get_json() or request.data.decode("utf-8").strip()
    if not data:
        return jsonify({"error": "Empty input", "status": 300}), 300
    
    query = data.get("query") if isinstance(data, dict) else data
    
    if not query:
        return jsonify({"error": "Query is required", "status": 300}), 300

    wt = Humanize()
    response= wt.forward(query)
    return jsonify({"input": query, "output":response, "status": "success"})

if __name__ == "__main__":
    app.run(debug=True,threaded=True)
