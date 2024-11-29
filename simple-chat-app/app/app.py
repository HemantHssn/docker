from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for chat messages
messages = []

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/send", methods=["POST"])
def send_message():
    content = request.json
    user = content.get("user", "Anonymous")
    text = content.get("message", "")
    if text.strip():
        messages.append({"user": user, "message": text})
    return jsonify(success=True)

@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify(messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

