class Echeancier:

    def __init__(self):
        self.__echeancier = []

    def add_event(self, event, date, priorite=0):
        """Ajoute un evenement dans l'echeancier

        :param date: date a laquelle declancher l'evenement
        :type date: float
        :param event: evenement a declancher
        :type event: typing.Callable
        :param priorite: priorite de l'event en cas d'egalite dans l'echeancier (plus la priorite est elevee, plus l'event est prioritaire
        :type priorite: int
        """

        # trouver l'index ou inserer l'event
        index = 0
        n = len(self.__echeancier)
        while index < n and (self.__echeancier[index][1] < date or (self.__echeancier[index][1] == date and self.__echeancier[index][2] > priorite)):
            c1 = index < n
            c2 = self.__echeancier[index][1] < date
            c3 = self.__echeancier[index][1] == date
            c4 = self.__echeancier[index][2] > priorite
            index += 1

        # insertion de l'event a l'index voulu
        self.__echeancier.insert(index, (event, date, priorite))

    def get_next_event(self):
        """Retire le prochain event de l'echeancier et le retourne

        :return: evenement a declancher
        :rtype: typing.Callable
        """

        return self.__echeancier.pop(0)

    def clear(self):
        """Vide l'echeancier

        """

        self.__echeancier.clear()

    def size(self):
        """Retourne la taille de l'echeancier

        :return: la taille de l'echeancier
        :rtype: int
        """

        return len(self.__echeancier)

    def __str__(self):
        string = ""
        for (event, date, priorite) in self.__echeancier:
            string += f"[{date}, {event}, {priorite}]\n"
        return string
