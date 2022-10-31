from flask_pydantic import validate
from pydantic import BaseModel
from flask import Flask

schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'email': {'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['email', 'password']
}


class BioData(BaseModel):
    slackUserName: str
    Backend: bool
    Age: int
    bio: str

app = Flask(__name__)

@app.route("/", methods=["GET"])
@validate()
def get():
    new_profile = {
    "slackUserName": "offisial",
    "Backend": True,
    "Age":20,
    "bio":"I am backend developer"
    }
    response = BioData(**new_profile)
    return response

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
