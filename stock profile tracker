import random
import spacy
from flask import Flask, request, jsonify

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Sample responses
responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What’s on your mind?"],
    "farewell": ["Goodbye! Have a great day!", "See you later! Take care!"],
    "default": ["I'm not sure I understand. Can you rephrase that?", "Hmm, can you clarify?"]
}

def get_intent(text):
    doc = nlp(text.lower())
    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey"]:
            return "greeting"
        elif token.lemma_ in ["bye", "goodbye"]:
            return "farewell"
    return "default"

def chatbot_response(user_input):
    intent = get_intent(user_input)
    return random.choice(responses[intent])

# Flask API setup
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    bot_reply = chatbot_response(user_message)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
