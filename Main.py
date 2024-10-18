from echeancier import Echeancier

global NbBus, NbBusRep, AireQc, AireQr, AireBr, Qc, Qr, Bc, Br, DateSimu
import random

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
    echeancier.add_event(ArriveeBus,DateSimu+random.expovariate(3/4),0)
    echeancier.add_event(FinSimulation,40.0,0)

def FinSimulation():
    


def MaJAires(D1,D2):
    global AireQc, AireQr, AireBr ,Qc, Qr, Br
    AireQC = AireQc + (D2 - D1)*Qc
    AireQr = AireQr + (D2 - D1)*Qr
    AireBr = AireBr + (D2 - D1)*Br

#Simulateur
DateSimu = float(0)
echeancier = Echeancier()
echeancier.add_event(DebSimulation, DateSimu,10000)
while echeancier.notvide() : #Nom à changer
    couple = echeancier.get_next_event() #Nom à changer
    MaJAires(DateSimu,couple[1])
    DateSimu = couple[1]
    func = globals()[couple[0]]
    func()

