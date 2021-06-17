import random


# Creates randomized cards for the game
class cards:
    def __init__(self, points=0, priceOfCard=None, totalCardPrice=0, color=None):
        self.points = random.randrange(5)
        self.color = random.randrange(5)
        if priceOfCard is None:
            priceOfCard = [0] * 6
        self.totalCardPrice = totalCardPrice
        # creates the total amount of resources that will be spent on a card
        if self.points == 1:
            self.totalCardPrice = 4
        elif self.points == 2:
            self.totalCardPrice = random.randint(5, 6)
        else:
            self.totalCardPrice = random.randint(7, 8)
        self.priceOfCard = priceOfCard
        for resourcespot in range(self.totalCardPrice):
            resource = random.randrange(5)
            self.priceOfCard[resource] += 1

    def getimage(self):
        imageColor = None
        if self.color == 0:
            imageColor = 'G'
        elif self.color == 1:
            imageColor = 'B'
        elif self.color == 2:
            imageColor = 'R'
        elif self.color == 3:
            imageColor = 'W'
        else:
            imageColor = 'b'
        cardarray = []
        cardarray.append('____________')
        cardarray.append('|' + str(self.points) + '        ' + imageColor + '|')
        cardarray.append('|          |')
        cardarray.append('|G:' + str(self.priceOfCard[0]) + '       |')
        cardarray.append('|B:' + str(self.priceOfCard[1]) + '       |')
        cardarray.append('|R:' + str(self.priceOfCard[2]) + '       |')
        cardarray.append('|W:' + str(self.priceOfCard[3]) + '       |')
        cardarray.append('|Bl:' + str(self.priceOfCard[4]) + '      |')
        cardarray.append('------------')
        return cardarray

    def getpoints(self):
        return self.points




