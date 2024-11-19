import random
import matplotlib.pyplot as plt
import numpy as np
import scipy

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

# Generation des donnees theoriques

for _ in range(n):
    expected.append(random.uniform(3 / 12, 13 / 12))

categories = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0]
]

# Calcul des effectifs observees et theoriques

for i in range(n):
    indice_observed = int((observed[i] - 3 / 12) / (1 / 6))
    categories[indice_observed][0] += 1
    indice_expected = int((expected[i] - 3 / 12) / (1 / 6))
    categories[indice_expected][1] += 1


# Merge categories if eff < 5

all_correct = all(categories[i][0] >= 5 and categories[i][1] >= 5 for i in range(len(categories)))
while not all_correct:
    for i in range(len(categories) - 1):
        if categories[i][0] < 5 or categories[i][1] < 5:
            categories[i][0] += categories[i + 1][0]
            categories[i][1] += categories[i + 1][1]
            del categories[i + 1]
            break
    all_correct = all(categories[i][0] >= 5 and categories[i][1] >= 5 for i in range(len(categories)))

print(categories)

# compute error and khi var

k = len(categories)
error = sum(pow(categories[i][0] - categories[i][1], 2) / categories[i][1] for i in range(len(categories)))

khi = scipy.stats.chi2.ppf(1 - 0.05, df=k - 1)

print(f"khi={khi:.3}")
print(f"error={error:.3}")

# conclusion

if error > khi:
    print("Les données ne correspondent pas à la distribution supposée")
else:
    print("Les données correspondent à la distribution supposée")
