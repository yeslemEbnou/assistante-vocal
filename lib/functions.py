from difflib import SequenceMatcher

def hsaniya_to_ar(lListe, words) :
    #lListe = list(string.split(' ')) # liste de mots de la phrase
    nListe = [] # nouveau liste
    for w in range(len(lListe)): # parcourir liste de mots
        nListe.append(words.get(lListe[w]) and (words.get(lListe[w])) or lListe[w])
    return ' '.join(str(x) for x in nListe)


def hsaniya_google_to_hasniya_general(text, words):
    lListe = list(text.split(' ')) # liste de mots de la phrase
    nListe = []
    indexDictKeys = -1
    ratio = 0 # ration initial
    
    for i in range(len(lListe)):
        
        for w in range(len(list(words.keys()))):
            ratio_preced = SequenceMatcher(None, lListe[i], list(words.keys())[w]).ratio()
            if ratio_preced >= ratio:
                ratio = ratio_preced
                indexDictKeys = w
        if(indexDictKeys != -1):
            nListe.append(list(words.keys())[indexDictKeys])
    
    return hsaniya_to_ar(nListe, words)