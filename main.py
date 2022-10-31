from flask import Flask, jsonify
from flask_pydantic import validate
from pydantic import BaseModel
from dataclasses import dataclass

app = Flask(__name__)


class BioValidator(BaseModel):
    slackUserName : str
    Backend: bool
    Age: int
    bio: str


@app.route('/', methods=['GET'])
@validate()
def index():
    slack = "offisial"
    back = True
    age=20
    bio = "I am a Python Flask Backend developer"
    bio = BioValidator(
        slackUserName=slack,
        Backend=True,
        Age=age,
        bio=bio
    )

    return bio


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=8080) 



      


