from nltk.corpus import wordnet

def get_meaning(word):
    syns = wordnet.synsets(word)
    try:
        return syns[0].definition()
    except IndexError:
        return "Is that a proper word ? I can't find its meaning"
def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms[0]

def get_antonyms(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return list(set(antonyms))[0]
