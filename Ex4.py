import random
import matplotlib.pyplot as plt
import numpy as np

tmps_arrivee = []
tmps_controle = []
try:
    fichier = open('references/Donnees Controle.txt', 'r')
    ligne = fichier.readline()
    while ligne:
        valeurs = ligne.split(" ")
        tmps_arrivee.append(float(valeurs[0]))
        tmps_controle.append(float(valeurs[1]))
        ligne = fichier.readline()
except:
    print("C'est la faute de Benjamin")
finally:
    print(tmps_arrivee)
    print(tmps_controle)
    fichier.close()

# duree de controle
n = len(tmps_controle)
observed = tmps_controle
expected = []
errors = []

# plt.hist(observed, bins=50)
# plt.ylabel('Frequency')
# plt.xlabel('Value')
# plt.show()

for _ in range(n):
    expected.append(random.uniform(1/4, 13/12))

for i in range(n):
    errors.append(pow(observed[i] - expected[i], 2) / expected[i])

error = sum(errors)
# np.random.chisquare()
# todo: diviser les données (obs et the) en intervalles, comparé les différences d'effectifs, khikhi, conclusion, cqfd tmtc tkt