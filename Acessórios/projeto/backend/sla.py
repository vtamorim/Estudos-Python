from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)



@app.route('/mensagem')

def mensagem():
    return jsonify({"msg":"It's me, guys! Yeah, Victor Miguel! This Message is from backend"})


if __name__ == "__main__":
    app(debug=True)