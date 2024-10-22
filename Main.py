from echeancier import Echeancier
global NbBus, NbBusRep, AireQc, AireQr, AireBr, Qc, Qr, Bc, Br, DateSimu, TempsSimulateur
import random

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
    echeancier.add_event("ArriveeBus",DateSimu+random.expovariate(1/(3/4)),0)
    echeancier.add_event("FinSimulation",TempsSimulateur,0)

def FinSimulation():
    global TmpMoyenAvContr, TmpMoyenAvRep, TauxUtilCentreRep
    echeancier.clear()
    TmpMoyenAvContr = AireQc / NbBus
    TmpMoyenAvRep = AireQr / NbBusRep
    TauxUtilCentreRep = AireBr / (2 * TempsSimulateur)

def MaJAires(D1,D2):
    global AireQc, AireQr, AireBr ,Qc, Qr, Br
    AireQc = AireQc + (D2 - D1)*Qc
    AireQr = AireQr + (D2 - D1)*Qr
    AireBr = AireBr + (D2 - D1)*Br

#Simulateur
for j in [40,80,160,240]:
    for i in range(0,50):
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

        print("Simulation #", i+1, " pour ", j, " heures")
        print("TmpMoyenAvContr : ", TmpMoyenAvContr)
        print("TmpMoyenAvRep : ", TmpMoyenAvRep)
        print("TauxUtilCentreRep : ", TauxUtilCentreRep, "\n")