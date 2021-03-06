from flask import Flask
from flask import request
from flask import make_response
import json
import actions
app = Flask(__name__)

#app.run(debug=True)
# import sys
# thismodule = sys.modules[__name__]
# methodToCall = getattr(action_methods,action)
# outcome = methodToCall(entitiy)

def processRequest(req):
    entity = None
    response_message = None
    comapany_key = None
    contextOut = req["result"]["contexts"]
    if req["result"]["action"] == "get_meaning":
        entity = req["result"]["parameters"]["word"]
        print entity
        response_message = actions.get_meaning(entity)

    return {"speech": response_message,
            "displayText": response_message,
            # "data": data,
            "contextOut": contextOut,
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
