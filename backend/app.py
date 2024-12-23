from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from summarizer import summarization  # Import your summarization function

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from React

# Load CSV data
data = pd.read_csv('backend/champions_lore.csv')

@app.route("/summarize", methods=["POST"])
def summarize():
    req_data = request.get_json()
    champion_name = req_data.get("champion_name")

    # Find champion story
    champion_row = data[data['champion'].str.lower() == champion_name.lower()]
    if champion_row.empty:
        return jsonify({"summary": "Champion not found."})

    full_story = champion_row.iloc[0]["story"]

    # Summarize story using your script
    summarized_story = summarization(full_story)

    return jsonify({"summary": summarized_story})

if __name__ == "__main__":
    app.run(debug=True)
