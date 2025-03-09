import re
import google.generativeai as genai
from smolagents import tools, DuckDuckGoSearchTool
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/search", methods=["POST"])
def search_api():
    data = request.get_json() or request.data.decode("utf-8").strip()
    
    if not data:
        return jsonify({"error": "Empty input", "status": 300}), 300
    
    query = data.get("query") if isinstance(data, dict) else data
    
    if not query:
        return jsonify({"error": "Query is required", "status": 300}), 300


    result = dummys()
    return jsonify({"input": query, "output": result, "status": "success"})

# List available models
def dummys():
    return "Welecome"

if __name__ == "__main__":
    app.run(debug=True)
