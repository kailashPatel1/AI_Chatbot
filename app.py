from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Simple rule-based chatbot
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
        "name": "I am your AI chatbot assistant."
    }
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    return "I'm sorry, I didn't understand that. Can you please rephrase?"

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        response = chatbot_response(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
