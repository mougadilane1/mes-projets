from donnees import DONNEES
from classifieur import entrainer, predire

test = DONNEES[::5]
apprentissage = [p for i, p in enumerate(DONNEES) if i % 5 != 0]
modele = entrainer(apprentissage)

bonnes = 0
for phrase, vraie in test:
    reponse = predire(phrase, modele)
    if reponse == vraie:
        bonnes += 1
    else:
        print("Erreur :", phrase, "->", reponse)

print(bonnes, "bonnes réponses sur", len(test))
print("Précision :", round(100 * bonnes / len(test)), "%")
