donnees = [
    ("j'adore ce produit", "positif"),
    ("très bon service", "positif"),
    ("super qualité, je recommande", "positif"),
    ("c'est nul", "negatif"),
    ("service très mauvais", "negatif"),
    ("je déteste, ça ne marche pas", "negatif"),
]

def decouper(phrase):
    return phrase.lower().replace(",", "").split()

compteurs = {"positif": {}, "negatif": {}}

for phrase, categorie in donnees:
    for mot in decouper(phrase):
        if mot in compteurs[categorie]:
            compteurs[categorie][mot] += 1
        else:
            compteurs[categorie][mot] = 1

def predire(phrase):
    mots = decouper(phrase)
    vocabulaire = set(compteurs["positif"]) | set(compteurs["negatif"])
    scores = {}
    for categorie in compteurs:
        total = sum(compteurs[categorie].values())
        score = 1.0
        for mot in mots:
            nb = compteurs[categorie].get(mot, 0)
            score *= (nb + 1) / (total + len(vocabulaire))
        scores[categorie] = score
    return max(scores, key=scores.get)

while True:
    texte = input("Écris une phrase (ou 'q' pour quitter) : ")
    if texte == "q":
        break
    print(predire(texte))
