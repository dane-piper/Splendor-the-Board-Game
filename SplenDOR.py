import math
import random


class Player:
    def __init__(self, player=1, pile=[], points=0):
        player = player
        pile = pile
        points = points

    def getplayer(self):
        return self.player

    def getpile(self):
        return self.pile

    def getpoints(self):
        return self.points


class Aristocrats:
    def __init__(self, cost=[], points=0):
        cost = cost
        points = points


def deck():
    colors = ['r', 'w', 'b', 'B', 'g']
    deck = []
    highcards = []
    mediumcards = []
    lowcards = []
    # creates 20 low cost cards with a random number generator
    for x in range(50):
        value = random.randint(0, 2)
        if value < 2:
            # this is the card array, 1st number is the value in points, 2nd is the color of card, the rest are the
            # price of the card
            card = []
            card.append('0')
            while len(card) < 5:
                color = random.randint(1, 10)
                if color == 1 or color == 2:
                    card.append('r')
                elif color == 3 or color == 4:
                    card.append('w')
                elif color == 5 or color == 6:
                    card.append('b')
                elif color == 7 or color == 8:
                    card.append('B')
                else:
                    card.append('g')
            lowcards.append(card)
        else:
            card = []
            card.append('1')
            while len(card) < 6:
                color = random.randint(1, 10)
                if color == 1 or color == 2:
                    card.append('r')
                elif color == 3 or color == 4:
                    card.append('w')
                elif color == 5 or color == 6:
                    card.append('b')
                elif color == 7 or color == 8:
                    card.append('B')
                else:
                    card.append('g')
            lowcards.append(card)
    for x in range(30):
        value = random.randint(0, 2)
        if value < 2:
            # this is the card array, 1st number is the value in points, 2nd is the color of card, the rest are the
            # price of the card
            card = []
            card.append('2')
            while len(card) < 7:
                color = random.randint(1, 10)
                if color == 1 or color == 2:
                    card.append('r')
                elif color == 3 or color == 4:
                    card.append('w')
                elif color == 5 or color == 6:
                    card.append('b')
                elif color == 7 or color == 8:
                    card.append('B')
                else:
                    card.append('g')
            lowcards.append(card)
        else:
            card = []
            card.append('3')
            while len(card) < 8:
                color = random.randint(1, 10)
                if color == 1 or color == 2:
                    card.append('r')
                elif color == 3 or color == 4:
                    card.append('w')
                elif color == 5 or color == 6:
                    card.append('b')
                elif color == 7 or color == 8:
                    card.append('B')
                else:
                    card.append('g')
            mediumcards.append(card)
    for x in range(20):
        value = random.randint(0, 2)
        if value < 2:
            # this is the card array, 1st number is the value in points, 2nd is the color of card, the rest are the
            # price of the card
            card = []
            card.append('4')
            while len(card) < 9:
                color = random.randint(1, 10)
                if color == 1 or color == 2:
                    card.append('r')
                elif color == 3 or color == 4:
                    card.append('w')
                elif color == 5 or color == 6:
                    card.append('b')
                elif color == 7 or color == 8:
                    card.append('B')
                else:
                    card.append('g')
            lowcards.append(card)
        else:
            card = []
            card.append('5')
            while len(card) < 10:
                color = random.randint(1, 10)
                if color == 1 or color == 2:
                    card.append('r')
                elif color == 3 or color == 4:
                    card.append('w')
                elif color == 5 or color == 6:
                    card.append('b')
                elif color == 7 or color == 8:
                    card.append('B')
                else:
                    card.append('g')
            highcards.append(card)
    deck.append(lowcards)
    deck.append(mediumcards)
    deck.append(highcards)
    print(deck)
    return deck


def printboard():
    allcards = deck()
    lowcards = allcards[0]
    mediumcards = allcards[1]
    highcards = allcards[2]
    # first 3 high cards being printed out
    highcardarray = []
    highcardarray.append(highcards[0])
    highcardarray.append(highcards[1])
    highcardarray.append(highcards[2])
    print(highcardarray)

    print(' __________    __________    __________')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|__________|  |__________|  |__________|')
    print(' __________    __________    __________')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|__________|  |__________|  |__________|')
    print(' __________    __________    __________')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|__________|  |__________|  |__________|')
    print(' __________    __________    __________')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|          |  |          |  |          |')
    print('|__________|  |__________|  |__________|')


def main():
    printboard()


main()
