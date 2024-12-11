from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get user input from the frontend
        data = request.json
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"error": "Message is required"}), 400

        # Generate a response using OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        # Extract the assistant's reply
        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

CORS(app)

