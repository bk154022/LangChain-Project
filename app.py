'''from flask import Flask, request, jsonify
from Hugging_face_model import generate_response

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    response = generate_response(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)'''

#from Hugging_face_model import generate_response

#response = generate_response("What is the capital of France?")
#print(response)

from flask import Flask, render_template, request
from Hugging_face_model import generate_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = generate_response(user_input)
        return render_template("index.html", user_input=user_input, response=response)
    return render_template("index.html", user_input="", response="")

if __name__ == "__main__":
    app.run(debug=True)


