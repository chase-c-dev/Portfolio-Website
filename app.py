from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app) # allows cross origin resource sharing

@app.get("/") # sets up an app route for functions
def index_get():
    return render_template("base.html") # renders base html file

@app.post("/predict")
def predict():
   text = request.get_json().get("message") 
    # TODO: check if text is valid
   response = get_response(text)
   message = {"answer": response}
   return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)

