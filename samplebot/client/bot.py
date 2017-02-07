import apiai,keys
import random,json

ai = apiai.ApiAI(keys.CLIENT_ACCESS_TOKEN)
SESSION_ID = str(random.randint(2,999))


def print_bot_message(message):
    print "Bot  ::  "+message

def send_message_to_apiai(message):
    """
    Sends all user utterances to apiai and gets json response
    """
    #create text_request obj, attach unique session_id, user message & contexts
    request = ai.text_request()
    request.session_id = SESSION_ID
    request.query = message
    #make request & get response
    response = request.getresponse()
    raw_response = response.read()
    return json.loads(raw_response)

def get_reply_message(response):
    """
    parses through the response json and returns reply_message
    """
    reply_message = ""
    if response["status"]["code"] == 200 or response["status"]["code"] == 206:
        try:
            reply_message = response["result"]["fulfillment"]["speech"]
        except KeyError:
            reply_message = response["result"]["fulfillment"]["messages"][0]["speech"]
    return reply_message


#conversation loop
while True:
    #get a user utterance/message
    message = raw_input("User ::  ")
    reply_message = ""
    #send message to apiai & print response message
    response = send_message_to_apiai(message)
    reply_message = get_reply_message(response)
    print_bot_message(reply_message)
