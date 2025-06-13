from openai import OpenAI
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Use OpenAI client with Groq base URL
client = OpenAI(
    api_key="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",  # Replace with your Groq key
    base_url="https://api.groq.com/openai/v1"
)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.get_json().get("message", "")

    try:
        chat_response = client.chat.completions.create(
            model="llama3-8b-8192",  # Supported by Groq
            messages=[
                {"role": "system", "content": "You are a helpful assistant that helps clients understand Python development and data analysis services provided by me vinay kishor i am a freelancer who provides these services. always greet the client . ask questions to the clients. give only 1 sentence reply"},
                {"role": "user", "content": user_message}
            ]
        )
        reply = chat_response.choices[0].message.content
        return jsonify({'response': reply})

    except Exception as e:
        return jsonify({'response': f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
