global NbBus, NbBusRep, AireQc, AireQr, AireBr, Qc, Qr, Bc, Br, DateSimu
import random as rd

def ArriveeBus():


def ArriveeFileC():


def AccesControle():


def DepartControle():  


def ArriveeFileR():


def AccesReparation():


def DepartReparation():



def DepartReparation():



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
    echeancier.add_event(ArriveeBus,DateSimu+rd.expovariate(3/4),0)
    echeancier.add_event(FinSimulation,40.0,0)

def FinSimulation():
    


def MaJAires(D1,D2):


# Simulateur
DateSimu = float(0)
echeancier.add_event(DebSimulation, DateSimu,10000)
while echeancier.notvide() : #Nom à changer
    couple = echeancier.get( #Nom à changer
    MaJAires(DateSimu,couple[1])
    DateSimu = couple[1]
    func = globals()[couple[0]]
    func()

