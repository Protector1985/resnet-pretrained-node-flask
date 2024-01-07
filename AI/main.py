from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
import os

#get the dotenv. path since it's one folder structure up.
dotenv_path = os.path.join(os.path.dirname(__file__),"..", ".env")

#loads the dotenv file
load_dotenv(dotenv_path)  

#get the environment variable for the flask port.
port = os.getenv("FLASK_PORT")
print(port)
app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/data", methods=["POST"])
def processor():
    if request.method == "POST":
        data = request.json
        print("DATA RCEIVED!!!!!!!!!!!!!!")
        return "OK"
    else:
        return "Can't process GET"
    

if __name__ == "__main__":
    app.run(port=port, debug=True)