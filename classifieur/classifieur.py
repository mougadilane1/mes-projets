import math
from collections import Counter
from donnees import DONNEES

def mots(phrase):
    for c in ",.!?'":
        phrase = phrase.replace(c, " ")
    return phrase.lower().split()

def entrainer(donnees):
    compte, nb_phrases, vocab = {}, Counter(), set()
    for phrase, classe in donnees:
        nb_phrases[classe] += 1
        compte.setdefault(classe, Counter())
        for m in mots(phrase):
            compte[classe][m] += 1
            vocab.add(m)
    return compte, nb_phrases, vocab

def predire(phrase, modele):
    compte, nb_phrases, vocab = modele
    total = sum(nb_phrases.values())
    meilleur, meilleur_score = None, -math.inf
    for classe in nb_phrases:
        score = math.log(nb_phrases[classe] / total)
        total_mots = sum(compte[classe].values())
        for m in mots(phrase):
            score += math.log((compte[classe][m] + 1) / (total_mots + len(vocab)))
        if score > meilleur_score:
            meilleur, meilleur_score = classe, score
    return meilleur

if __name__ == "__main__":
    modele = entrainer(DONNEES)
    for test in ["j'adore ce repas", "service horrible", "journée nul"]:
        print(test, "->", predire(test, modele))
