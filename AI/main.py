from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
import os
from torchvision import models
from lib.Resnet import Resnet

resnet = Resnet()

#get the dotenv. path since it's one folder structure up.
dotenv_path = os.path.join(os.path.dirname(__file__),"..", ".env")

#loads the dotenv file
load_dotenv(dotenv_path)  

#get the environment variable for the flask port.
port = os.getenv("FLASK_PORT")

app = Flask(__name__)

#allow all origins for simplicity
CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/data", methods=["POST"])
def processor():
    if request.method == "POST":
        file = request.files['file']
        resnet.resnet_processor(file)
        
        return "OK"
    else:
        return "Can't process GET"
    

if __name__ == "__main__":
    app.run(port=port, debug=True)