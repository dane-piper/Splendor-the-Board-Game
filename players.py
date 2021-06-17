import math
import random


class Player:
    def __init__(self, player=1, pile=[], points=0, hand = []):
        self.points = points
        self.player = player
        self.pile = pile
        self.hand = hand

    def getplayer(self):
        return self.player

    def getpile(self):
        return self.pile

    def getpoints(self):
        return self.points