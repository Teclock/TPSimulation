import random
import scipy.stats

from Ex4 import tmps_controle


def testkhi():
    tmps_arrivee = []
    tmps_controle = []
    tmps_arrivee_traitee = []
    try:
        fichier = open('references/Donnees Controle.txt', 'r')
        ligne = fichier.readline()
        while ligne:
            valeurs = ligne.split(" ")
            tmps_arrivee.append(float(valeurs[0])) #Donnée mal fournie : il faut soustraire la valeur d'avant à celle d'après*
            tmps_controle.append(float(valeurs[1]))
            ligne = fichier.readline()

        # Code pour afficher des
        # plt.hist(tmps_arrivee, bins = 8)
        # plt.title("temps arrivee")
        # plt.show()

        for i in range(1, len(tmps_arrivee)):
            tmps_arrivee_traitee.append(round(tmps_arrivee[i]-tmps_arrivee[i-1],2))

        # plt.hist(tmps_arrivee_traitee, bins = 10)
        # plt.title("temps arrivee")
        # plt.show()
        
    except:
        print("Erreur")
    finally:
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

    # Génération des valeurs théoriques

    for _ in range(n):
        expected.append(random.expovariate(1 / 0.75))

    intervalles = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]

    for i in tmps_arrivee_traitee:
        if (0.00 <= i < 0.376):
            intervalles[0].append(i)
        elif (0.376 <= i < 0.752):
            intervalles[1].append(i)
        elif (0.752 <= i < 1.128):
            intervalles[2].append(i)
        elif (1.128 <= i < 1.504):
            intervalles[3].append(i)
        elif (1.504 <= i < 1.880):
            intervalles[4].append(i)
        elif (1.880 <= i < 2.256):
            intervalles[5].append(i)
        elif (2.256 <= i < 2.632):
            intervalles[6].append(i)
        elif (2.632 <= i < 3.008):
            intervalles[7].append(i)
        elif (3.008 <= i < 3.384):
            intervalles[8].append(i)
        else:
            intervalles[9].append(i)

    # Placement des valeurs du fichier

    intervalles_expected = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]

    for i in expected:
        if (0.00 <= i < 0.376):
            intervalles_expected[0].append(i)
        elif (0.376 <= i < 0.752):
            intervalles_expected[1].append(i)
        elif (0.752 <= i < 1.128):
            intervalles_expected[2].append(i)
        elif (1.128 <= i < 1.504):
            intervalles_expected[3].append(i)
        elif (1.504 <= i < 1.880):
            intervalles_expected[4].append(i)
        elif (1.880 <= i < 2.256):
            intervalles_expected[5].append(i)
        elif (2.256 <= i < 2.632):
            intervalles_expected[6].append(i)
        elif (2.632 <= i < 3.008):
            intervalles_expected[7].append(i)
        elif (3.008 <= i < 3.384):
            intervalles_expected[8].append(i)
        else:
            intervalles_expected[9].append(i)

    #Ici la condition que tous les intervalles doivent avoir un effectif > 5
    all_correct = all(len(intervalles[i]) >= 5 and len(intervalles_expected[i]) >= 5 for i in range(len(intervalles)))
    print(all_correct)
    while not all_correct:
        for i in range(1, len(intervalles)):
            if len(intervalles[i]) < 5 or len(intervalles_expected[i]) < 5:
                intervalles[i-1] += intervalles[i]
                del intervalles[i]
                print(intervalles)
                intervalles_expected[i - 1] += intervalles_expected[i]
                del intervalles_expected[i]
                break
        all_correct = all(len(intervalles[i]) >= 5 and len(intervalles_expected[i]) >= 5 for i in range(len(intervalles)))

    k = len(intervalles)
    error = 0
    for i in range (len(intervalles)):
        error += sum([pow(len(intervalles[i]) - len(intervalles_expected[i]), 2) / len(intervalles_expected[i])])

    print("error =", error)

    khi = scipy.stats.chi2.ppf(1 - 0.05, df=k - 1)
    print("khi result =", khi)

    if (khi < error):
        return False
    else:
        return True

compteur_accepte = 0
compteur_rejete = 0
for i in range(0,100):
    print("itération n°",i+1)
    if testkhi()==True:
        compteur_accepte += 1
    else:
        compteur_rejete += 1

print("Nombre d'acceptations :", compteur_accepte)
print("Nombre de rejets :", compteur_rejete)

