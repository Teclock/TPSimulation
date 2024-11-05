from echeancier import Echeancier
import random

global NbBus, NbBusRep, AireQc, AireQr, AireBr, Qc, Qr, Bc, Br, DateSimu, TempsSimulateur


def ArriveeBus():
    global NbBus, DateSimu

    heure = DateSimu + random.expovariate(1 / 0.75)
    echeancier.add_event("ArriveeBus", heure)
    NbBus += 1
    echeancier.add_event("ArriveeFileC", DateSimu)


def ArriveeFileC():
    global Qc, Bc, DateSimu
    Qc = Qc + 1
    if Bc == 0:
        echeancier.add_event("AccesControle", DateSimu)


def AccesControle():
    global Qc, Bc, DateSimu
    Qc -= 1
    Bc = 1
    heure = DateSimu + random.uniform(1 / 4, 13 / 12)
    echeancier.add_event("DepartControle", heure)


def DepartControle():
    global Qc, Bc, DateSimu
    Bc = 0
    if Qc > 0:
        echeancier.add_event("AccesControle", DateSimu)
    reparation = random.randint(1, 10)
    if reparation <= 3:  # 30% de chance
        echeancier.add_event("ArriveeFileR", DateSimu)


def ArriveeFileR():
    global Qr, NbBusRep, Br, DateSimu

    Qr += 1
    NbBusRep += 1
    if Br < 2:
        echeancier.add_event("AccesReparation", DateSimu)


def AccesReparation():
    global Qr, Br, DateSimu

    Qr -= 1
    Br += 1
    heure = DateSimu + random.uniform(2.8, 5.5)
    echeancier.add_event("DepartReparation", heure)


def DepartReparation():
    global Qr, Br, DateSimu

    Br -= 1
    if Qr > 0:
        echeancier.add_event("AccesReparation", DateSimu)


def DebSimulation():
    global NbBus, NbBusRep, AireQc, AireQr, AireBr, Qc, Qr, Bc, Br, DateSimu, TempsSimulateur
    NbBus = 0
    NbBusRep = 0
    AireQc = 0
    AireQr = 0
    AireBr = 0
    Qc = 0
    Qr = 0
    Bc = 0
    Br = 0
    echeancier.add_event("ArriveeBus", DateSimu + random.expovariate(1 / (3 / 4)), 0)
    echeancier.add_event("FinSimulation", TempsSimulateur, 0)


def FinSimulation():
    global TmpMoyenAvContr, TmpMoyenAvRep, TauxUtilCentreRep, TempsSimulateur, TailleMoyFileC, TailleMoyFileR
    echeancier.clear()
    TmpMoyenAvContr = AireQc / NbBus
    TmpMoyenAvRep = AireQr / NbBusRep
    TailleMoyFileC = AireQc / TempsSimulateur
    TailleMoyFileR = AireQr / TempsSimulateur
    TauxUtilCentreRep = AireBr / (2 * TempsSimulateur)


def MaJAires(D1, D2):
    global AireQc, AireQr, AireBr, Qc, Qr, Br
    AireQc = AireQc + (D2 - D1) * Qc
    AireQr = AireQr + (D2 - D1) * Qr
    AireBr = AireBr + (D2 - D1) * Br

nbSimu = 1000

# Fichier csv stockant les variables statistiques
file = open("stat.csv", 'w')
file.write("Temps simulation; 40h;;;;;; 80h;;;;;; 160h;;;;;; 240h\n")
file.write("Variable; TmpMoyenAvContr; TailleMoyFileC; TmpMoyenAvRep; TailleMoyFileR; TauxUtilCentreRep; NbBus;" +
           "TmpMoyenAvContr; TailleMoyFileC; TmpMoyenAvRep; TailleMoyFileR; TauxUtilCentreRep; NbBus; " +
           "TmpMoyenAvContr; TailleMoyFileC; TmpMoyenAvRep; TailleMoyFileR; TauxUtilCentreRep; NbBus; " +
           "TmpMoyenAvContr; TailleMoyFileC; TmpMoyenAvRep; TailleMoyFileR; TauxUtilCentreRep; NbBus\n")

# Résultats des simulations
liste_TmpMoyAvContr = []
liste_TailleMoyFileC = []
liste_TmpMoyAvRep = []
liste_TailleMoyFileR = []
liste_TauxUtilCentreRep = []
liste_NbBus = []
for i in range(0,nbSimu):
    csvLine = "Simulation n°" + str(i + 1) + ";"
    # Résultats pour chaque temps de simulation
    TmpsMoyAvContr_TmpSimu = []
    TmpsMoyAvRep_TmpSimu = []
    TailleMoyFileC_TmpSimu = []
    TailleMoyFileR_TmpSimu = []
    TauxUtilCentreRep_TmpSimu = []
    NbBus_TmpSimu = []
    for j in [40, 80, 160, 240]:

        #Simulateur
        TempsSimulateur = j
        DateSimu = float(0)
        echeancier = Echeancier()
        DebSimulation()
        while echeancier.size() > 0:
            couple = echeancier.get_next_event()
            MaJAires(DateSimu, couple[1])
            DateSimu = couple[1]
            func = globals()[couple[0]]
            func()

        csvLine += (str(round(TmpMoyenAvContr, 3)) + "; " +
                    str(round(TailleMoyFileC, 3)) + "; " +
                    str(round(TmpMoyenAvRep, 3)) + "; " +
                    str(round(TailleMoyFileR, 3)) + "; " +
                    str(round(TauxUtilCentreRep, 3)) + "; " +
                    str(round(NbBus, 3)) + "; ")
        TmpsMoyAvContr_TmpSimu.append(TmpMoyenAvContr)
        TailleMoyFileC_TmpSimu.append(TailleMoyFileC)
        TmpsMoyAvRep_TmpSimu.append(TmpMoyenAvRep)
        TailleMoyFileR_TmpSimu.append(TailleMoyFileR)
        TauxUtilCentreRep_TmpSimu.append(TauxUtilCentreRep)
        NbBus_TmpSimu.append(NbBus)
    file.write(csvLine + "\n")
    liste_TmpMoyAvContr.append(TmpsMoyAvContr_TmpSimu)
    liste_TailleMoyFileC.append(TailleMoyFileC_TmpSimu)
    liste_TmpMoyAvRep.append(TmpsMoyAvRep_TmpSimu)
    liste_TailleMoyFileR.append(TailleMoyFileR_TmpSimu)
    liste_TauxUtilCentreRep.append(TauxUtilCentreRep_TmpSimu)
    liste_NbBus.append(NbBus_TmpSimu)
    #print("Simulation #", i+1, " pour ", j, " heures")
    #print("TmpMoyenAvContr : ", TmpMoyenAvContr)
    #print("TmpMoyenAvRep : ", TmpMoyenAvRep)
    #print("TauxUtilCentreRep : ", TauxUtilCentreRep, "\n")

# Calcul des esperences
esperance_TmpMoyAvContr = []
esperance_TailleMoyFileC = []
esperance_TmpMoyAvRep = []
esperance_TailleMoyFileR = []
esperance_TauxUtilCentreRep = []
esperance_NbBus = []
file.write(";")
for i in range(len(liste_TmpMoyAvContr[0])):
    esperance_TmpMoyAvContr.append(0)
    esperance_TailleMoyFileC.append(0)
    esperance_TmpMoyAvRep.append(0)
    esperance_TailleMoyFileR.append(0)
    esperance_TauxUtilCentreRep.append(0)
    esperance_NbBus.append(0)
    for j in range(len(liste_TmpMoyAvContr)):
        esperance_TmpMoyAvContr[i] += liste_TmpMoyAvContr[j][i]
        esperance_TailleMoyFileC[i] += liste_TailleMoyFileC[j][i]
        esperance_TmpMoyAvRep[i] += liste_TmpMoyAvRep[j][i]
        esperance_TailleMoyFileR[i] += liste_TailleMoyFileR[j][i]
        esperance_TauxUtilCentreRep[i] += liste_TauxUtilCentreRep[j][i]
        esperance_NbBus[i] += liste_NbBus[j][i]
    esperance_TmpMoyAvContr[i] /= nbSimu
    esperance_TailleMoyFileC[i] /= nbSimu
    esperance_TmpMoyAvRep[i] /= nbSimu
    esperance_TailleMoyFileR[i] /= nbSimu
    esperance_TauxUtilCentreRep[i] /= nbSimu
    esperance_NbBus[i] /= nbSimu
    print("esp_TmpMoyAvContr ", i, " : ", esperance_TmpMoyAvContr[i])
    print("esp_TailleC ", i, " : ", esperance_TailleMoyFileC[i])
    print("esp_TmpMoyAvRep ", i, " : ", esperance_TmpMoyAvRep[i])
    print("esp_TailleR ", i, " : ", esperance_TailleMoyFileR[i])
    print("esp_TauxUtilCentreRep ", i, " : ", esperance_TauxUtilCentreRep[i])
    print("esp_NbBus ", i, " : ", esperance_NbBus[i], "\n")
    file.write(str(esperance_TmpMoyAvContr[i]) + ";" + 
                str(esperance_TailleMoyFileC[i]) + ";" + 
                str(esperance_TmpMoyAvRep[i]) + ";" + 
                str(esperance_TailleMoyFileR[i]) + ";" + 
                str(esperance_TauxUtilCentreRep[i]) + ";" +
                str(esperance_NbBus[i]) + "; ")
file.close()
