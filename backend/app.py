from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from model import get_ai_response

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        ai_response = get_ai_response(user_message)
        return jsonify({"reply": ai_response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    os.environ["GOOGLE_API_KEY"] = "api key here i used gemini ai "

    app.run(debug=True)
