from flask import jsonify
import connexion
from flask_cors import CORS

# Create the application instance
app = connexion.App(__name__, specification_dir="./")
CORS(app.app)
# Read the yaml file to configure the endpoints
app.add_api("cpu.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "It's working!"}
    return jsonify(msg)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5050)