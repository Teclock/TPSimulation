# TPSimulation

Documentation faite selon la correction de l'exercice 4 et le sujet de TP présents dans le dossier references.

## Organisation

On a un échéancier qui est une classe.\
Cette classe est composée d'une liste de tuples, ces tuples étant des dates et des événements.

Les événements sont modélisés par des fonctions directement dans le main.

### Variables/Indicateurs statistiques

Les variables/indicateus statistiques seront nommés de la manière suivante :

*Date Simu* → L'heure de la simulation

*NbBus* → Nombre de bus arrivés dans la simulation

*NbBusRep* → Nombre de bus réparés

*Qc* → Nombre de bus dans la file de contrôle

*Qr* → Nombre de bus dans la file de réparation

*Bc* → Occupation du poste de contrôle (1 si occupé, 0 sinon)

*Br* → Occupation du poste de réparation (1 si occupé, 0 sinon)

*AireQc* → Aire représentant l'occupation du poste de contrôle

*AireQr* → Aire représentant l'occupation du poste de réparation

*TmpMoyenAvContr* → Temps d'attente moyen avant contrôle

*TmpMoyenAvRep* → Temps d'attente moyen avant réparation

*TmpUtilCentreRep* → Taux d'utilisation du centre de réparation

### Lois

#### Théorie

Les lois à suivre sont les suivantes :

Les bus ont des inter-arrivées exponentielles de paramètre 4/3 d'heures

La durée de réparation soit une loi uniforme entre 2,8 et 5,5 heures

#### Pratique

*random.expovariate(lambda)* : Renvoie un délai selon la loi exponentielle suivant l'espérance lambda (qui est l'inverse de la moyenne)

*random.unfiform(a, b)* : Renvoie un délai selon la loi uniforme suivant les bornes [a, b]

