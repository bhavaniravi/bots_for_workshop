print "Bot  :: Hi I am an echobot. I will repeat whatever you say"
while True:
    inputMessage = raw_input("User :: ")
    if inputMessage.lower() == "exit":
        print "Bot  :: Bye !! take care"
        exit()
    print "Bot  :: " + inputMessage[::-1]
