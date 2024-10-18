global NbBus, NbBusRep, AireQc, AireQr, AireBr, Qc, Qr, Bc, Br, DateSimu

def ArriveeBus():


def ArriveeFileC():
    global QC, BC, DateSimu
    QC = QC + 1
    if BC == 0:
        echeancier.add_event("AccesControle", DateSimu)

def AccesControle():
    global QC, BC, DateSimu
    QC -= 1
    BC = 1
    DateSimu += random.uniform(1 / 4, 13 / 12)
    echeancier.add_event("DepartContrôle", DateSimu)

def DepartControle():
    global QC, BC, DateSimu
    BC = 0
    if QC > 0:
        echeancier.add_event("AccèsContrôle", DateSimu)
    reparation = random.randint(10)
    if reparation <= 3:  # 30% de chance
        echeancier.add_event("ArrivéeFileR", DateSimu)

def ArriveeFileR():


def AccesReparation():


def DepartReparation():



def DepartReparation():



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

    # 4
    # 5

def FinSimulation():
    


def MaJAires():




DebSimulation()
# Simulateur
DateSimu = 0

import random

DateSimu = 0
QC = 0
BC = 0
