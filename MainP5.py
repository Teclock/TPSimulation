from echeancier import Echeancier
global NbBus, NbBusRep, AireQc, AireQr, AireBr, Qc, Qr, Bc, Br, DateSimu
import random
import matplotlib.pyplot as plt
import numpy as np

#Donne la liste des moyennes glissantes de W. C'est la moyenne glissante du cours.
def MoyenneGlissantes(ListeDesMoyennes,w):
    m = len(ListeDesMoyennes)
    ListeMoyenneGlissantes = []
    for i in range(1,m+1):
        Somme = 0
        if i <= w:
            for k in range(-(i-1),i-1):
                Somme += ListeDesMoyennes[i+k-1]
            ListeMoyenneGlissantes.append(Somme/(2*i-1))
        elif w+1 <= i <= m-w:
            for k in range(-w,w):
                Somme += ListeDesMoyennes[i+k-1]
            ListeMoyenneGlissantes.append(Somme/(2*w+1))
    return ListeMoyenneGlissantes


def ArriveeBus():
    global NbBus, DateSimu

    heure = DateSimu + random.expovariate(1/0.75)
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
    reparation = random.randint(1,10)
    if reparation <= 3:  # 30% de chance
        echeancier.add_event("ArriveeFileR", DateSimu)

def ArriveeFileR():
    global Qr, NbBusRep, Br, DateSimu

    Qr += 1
    NbBusRep += 1
    if Br < 2 :
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
    if Qr > 0 :
        echeancier.add_event("AccesReparation", DateSimu)

def DebSimulation():
    global NbBus, NbBusRep, AireQc, AireQr, AireBr, Qc, Qr, Bc, Br, DateSimu
    NbBus = 0
    NbBusRep = 0
    AireQc = 0
    AireQr = 0
    AireBr = 0
    Qc = 0
    Qr = 0
    Bc = 0
    Br = 0
    echeancier.add_event("ArriveeBus",DateSimu+random.expovariate(1/(3/4)),0)

def FinSimulation():
    global TmpMoyenAvContr, TmpMoyenAvRep, TmpUtilCentreRep
    echeancier.clear()
    TmpMoyenAvContr = AireQc / NbBus
    TmpMoyenAvRep = AireQr / NbBusRep
    TmpUtilCentreRep = AireBr / (2 * 160)

def MaJAires(D1,D2):
    global AireQc, AireQr, AireBr ,Qc, Qr, Br
    AireQc = AireQc + (D2 - D1)*Qc
    AireQr = AireQr + (D2 - D1)*Qr
    AireBr = AireBr + (D2 - D1)*Br

#Simulateur
#Nombre de réplication n
n=30
#Nombre de bus m
m = 200
#On initialise le tableau des temps moyen avant contrôle qui sera de taille n*m
TabTmpMoyenAvContr = []
for i in range(n):
    LstTmpMoyenAvContr = []
    for j in range(m):
        DateSimu = float(0)
        echeancier = Echeancier()
        DebSimulation()
        while echeancier.size() > 0:
            couple = echeancier.get_next_event()
            MaJAires(DateSimu, couple[1])
            DateSimu = couple[1]
            func = globals()[couple[0]]
            func()
            #Sert à n'ajouter qu'une seule fois l'événement "FinSimulation"
            if NbBus >= m and couple[0] != "FinSimulation":
                echeancier.add_event("FinSimulation", DateSimu, 0)
        #On ajoute le temps moyen dans le tableau
        LstTmpMoyenAvContr.append(TmpMoyenAvContr)
    #On ajoute la liste des temps moyens de cette replications
    TabTmpMoyenAvContr.append(LstTmpMoyenAvContr)

#On fait la moyenne des tmp par bus.
ListeMoyenneTmpMoyenAvContr = []

for i in range(m):
    Somme = 0
    for j in range(n):
        Somme += TabTmpMoyenAvContr[j][i]
    ListeMoyenneTmpMoyenAvContr.append(Somme/n)



print(ListeMoyenneTmpMoyenAvContr)
#On fait à la main les moyennes glissantes.
ListeMoyenneGlissanteAvCtrl = MoyenneGlissantes(ListeMoyenneTmpMoyenAvContr,25)
ListeM = np.arange(1,len(ListeMoyenneGlissanteAvCtrl)+1)
print(ListeMoyenneGlissanteAvCtrl)
print(ListeM)
plt.plot(ListeM,ListeMoyenneGlissanteAvCtrl)
plt.xlabel("Nombre de bus m")
plt.ylabel("Moyenne glissantes des temps d'attente avant controle")
plt.show()







