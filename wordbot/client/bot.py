
import dictionary_access as da
print "Bot   :: Hi I am a wordbot. I will give meaning for words you type"
while True:
    #meaning of greet
    #antonym of hello
    sentence = raw_input("User  :: ")
    words = sentence.split()
    if sentence.lower() == "exit":
        print "Bot   :: Bye take care !!"
        exit()
    if "meaning" in words or "define" in words:
        response = da.get_meaning(words[-1])
    elif "antonym" in words or "opposite" in words:
        response = da.get_antonyms(words[-1])
    elif "synonym" in words or "equvivalent" in words:
        response = da.get_synonyms(words[-1])
    else:
        response = "I am not trained to do that yet"
    print "Bot   :: " + response
