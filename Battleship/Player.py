class Player:

    def __init__(self, hits=0, shots=0):
        self.__hits = hits
        self.__shots = shots

    def setHits(self, hits):
        self.__hits = hits

    def setShots(self, shots):
        self.__shots = shots

    def getHits(self):
        return self.__hits

    def getShots(self):
        return self.__shots

    def getPercentHit(self):
        return format(self.__hits / self.__shots, "%")

    def __str__(self):
        return "\nName: " + self.__name + \
               "\nHits: " + str(self.__hits) + \
               "\nShots: " + str(self.__shots) + \
               "\nPercent Hit: " + str(format(self.__percentHit, '.2%'))
