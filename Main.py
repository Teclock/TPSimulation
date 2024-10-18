from echeancier import Echeancier
global NbBus, NbBusRep, AireQc, AireQr, AireBr, Qc, Qr, Bc, Br, DateSimu
import random

def ArriveeBus():
    global NbBus, DateSimu

    heure = DateSimu + random.expovariate(1/0.75)
    echeancier.add_event("ArriveeBus", heure)
    NbBus += 1
    echeancier.add_event("ArriveeFileC", DateSimu)

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
    echeancier.add_event(ArriveeBus,DateSimu+random.expovariate(1/(3/4)),0)
    echeancier.add_event(FinSimulation,40.0,0)

def FinSimulation():
    echeancier.clear()
    TmpMoyenAvContr = AireQc / NbBus # Temps d'attente moyen avant contrôle
    TmpMoyenAvRep = AireQr / NbBusRep # Temps d'attente moyen avant réparation
    TmpUtilCentreRep = AireBr / (2 * 160) # Taux d'utilisation du centre de réparation

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

print("TmpMoyenAvContr : ", TmpMoyenAvContr)
print("TmpMoyenAvRep : ", TmpMoyenAvRep)
print("TmpUtilCentreRep : ", TmpUtilCentreRep)