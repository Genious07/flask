from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'

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

