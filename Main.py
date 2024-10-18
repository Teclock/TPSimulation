import random

global NbBus, NbBusRep, AireQc, AireQr, AireBr, Qc, Qr, Bc, Br, DateSimu

def ArriveeBus():
    global NbBus, DateSimu

    heure = DateSimu + random.expovariate(1/0.75)
    echeancier.add_event("ArriveeBus", heure)
    NbBus += 1
    echeancier.add_event("ArriveeFileC", DateSimu)

def ArriveeFileC():


def AccesControle():


def DepartControle():  


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
    NbBus = 0
    NbBusRep = 0
    AireQc = 0
    AireQr = 0
    AireBr = 0
    Qc = 0
    Qr = 0
    Bc = 0
    Br = 0

    # 4
    # 5

def FinSimulation():
    


def MaJAires(D1, D2):
    AireQc += (D2-D1)*Qc
    AireQr += (D2-D1)*Qr
    AireBr += (D2-D1)*Br


DebSimulation()
# Simulateur
DateSimu = 0