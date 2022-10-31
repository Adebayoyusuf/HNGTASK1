# from flask_pydantic import validate
# from pydantic import BaseModel
# from flask import Flask

# schema = {
#     'type': 'object',
#     'properties': {
#         'name': {'type': 'string'},
#         'email': {'type': 'string'},
#         'password': {'type': 'string'}
#     },
#     'required': ['email', 'password']
# }


# class BioData(BaseModel):
#     slackUserName: str
#     Backend: bool
#     Age: int
#     bio: str

# app = Flask(__name__)

# @app.route("/", methods=["GET"])
# @validate()
# def get():
#     new_profile = {
#     "slackUserName": "offisial",
#     "Backend": True,
#     "Age":20,
#     "bio":"I am backend developer"
#     }
#     response = BioData(**new_profile)
#     return response

# if __name__ == "__main__":
#     app.run(host='127.0.0.1', port=5000, debug=True)




from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
import json

app = Flask(__name__)

dotenv_path = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path)


cors = CORS(app)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response

@app.route("/")
def get():
    return json.dumps(
        { "slackUsername": "offisial", 
            "backend": True,
            "age": 24,
            "bio":  "I am a Backend Developer"
        }, sort_keys=False), 200, {"content-type": "application/json"}

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)