from flask import Flask
from flask import request
from flask import make_response
import json

app = Flask(__name__)
def processRequest(req):
    response_message = "This is default message"
    return {"speech": response_message,
            "displayText": response_message,
            # "data": data,
            #"contextOut": contextOut,
            "source": "webbot-api"
            }

@app.route('/',methods = ["POST"])
def hello_world():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    print res
    r.headers['Content-Type'] = 'application/json'
    return r
