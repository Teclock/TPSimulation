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

