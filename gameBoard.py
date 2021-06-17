import queue
import cards
import random
#create card decks

class constructBoard:
    def __init__(self, lowLevelCards = queue.Queue(), midLevelCards = queue.Queue(), highLevelCards = queue.Queue()):
        self.lowlevelcards = lowLevelCards
        self.midlevelcards = midLevelCards
        self.highlevelcards = highLevelCards
        for size in range(100):
            card = cards.cards()
            if card.getpoints() == 0:
                lowLevelCards.put(card)
            elif card.getpoints() == 1 or card.getpoints() == 2:
                midLevelCards.put(card)
            else:
                highLevelCards.put(card)
    def printboard(self):
        cardslots = []
        cardslots.append(self.highlevelcards.get())
        image1 = cardslots[0].getimage()
        cardslots.append(self.highlevelcards.get())
        image2 = cardslots[1].getimage()
        cardslots.append(self.highlevelcards.get())
        image3 = cardslots[2].getimage()
        cardslots.append(self.highlevelcards.get())
        image4 = cardslots[3].getimage()
        print(image1[0] + ' '+ image2[0] + ' ' + image3[0] + ' ' + image4[0] + ' ')
        print(image1[1] + ' ' + image2[1] + ' ' + image3[1] + ' ' + image4[1] + ' ')
        print(image1[2] + ' ' + image2[2] + ' ' + image3[2] + ' ' + image4[2] + ' ')
        print(image1[3] + ' ' + image2[3] + ' ' + image3[3] + ' ' + image4[3] + ' ')
        print(image1[4] + ' ' + image2[4] + ' ' + image3[4] + ' ' + image4[4] + ' ')
        print(image1[5] + ' ' + image2[5] + ' ' + image3[5] + ' ' + image4[5] + ' ')
        print(image1[6] + ' ' + image2[6] + ' ' + image3[6] + ' ' + image4[6] + ' ')
        print(image1[7] + ' ' + image2[7] + ' ' + image3[7] + ' ' + image4[7] + ' ')
        print(image1[8] + ' ' + image2[8] + ' ' + image3[8] + ' ' + image4[8] + ' ')
        mtop1 = self.midlevelcards.get()
        mimage1 = mtop1.getimage()
        mtop2 = self.midlevelcards.get()
        mimage2 = mtop2.getimage()
        mtop3 = self.midlevelcards.get()
        mimage3 = mtop3.getimage()
        mtop4 = self. midlevelcards.get()
        mimage4 = mtop4.getimage()
        print(mimage1[0] + ' ' + mimage2[0] + ' ' + mimage3[0] + ' ' + mimage4[0] + ' ')
        print(mimage1[1] + ' ' + mimage2[1] + ' ' + mimage3[1] + ' ' + mimage4[1] + ' ')
        print(mimage1[2] + ' ' + mimage2[2] + ' ' + mimage3[2] + ' ' + mimage4[2] + ' ')
        print(mimage1[3] + ' ' + mimage2[3] + ' ' + mimage3[3] + ' ' + mimage4[3] + ' ')
        print(mimage1[4] + ' ' + mimage2[4] + ' ' + mimage3[4] + ' ' + mimage4[4] + ' ')
        print(mimage1[5] + ' ' + mimage2[5] + ' ' + mimage3[5] + ' ' + mimage4[5] + ' ')
        print(mimage1[6] + ' ' + mimage2[6] + ' ' + mimage3[6] + ' ' + mimage4[6] + ' ')
        print(mimage1[7] + ' ' + mimage2[7] + ' ' + mimage3[7] + ' ' + mimage4[7] + ' ')
        print(mimage1[8] + ' ' + mimage2[8] + ' ' + mimage3[8] + ' ' + mimage4[8] + ' ')
        ltop1 = self.lowlevelcards.get()
        limage1 = ltop1.getimage()
        ltop2 = self.lowlevelcards.get()
        limage2 = ltop2.getimage()
        ltop3 = self.lowlevelcards.get()
        limage3 = ltop3.getimage()
        ltop4 = self.lowlevelcards.get()
        limage4 = ltop4.getimage()
        print(limage1[0] + ' ' + limage2[0] + ' ' + limage3[0] + ' ' + limage4[0] + ' ')
        print(limage1[1] + ' ' + limage2[1] + ' ' + limage3[1] + ' ' + limage4[1] + ' ')
        print(limage1[2] + ' ' + limage2[2] + ' ' + limage3[2] + ' ' + limage4[2] + ' ')
        print(limage1[3] + ' ' + limage2[3] + ' ' + limage3[3] + ' ' + limage4[3] + ' ')
        print(limage1[4] + ' ' + limage2[4] + ' ' + limage3[4] + ' ' + limage4[4] + ' ')
        print(limage1[5] + ' ' + limage2[5] + ' ' + limage3[5] + ' ' + limage4[5] + ' ')
        print(limage1[6] + ' ' + limage2[6] + ' ' + limage3[6] + ' ' + limage4[6] + ' ')
        print(limage1[7] + ' ' + limage2[7] + ' ' + limage3[7] + ' ' + limage4[7] + ' ')
        print(limage1[8] + ' ' + limage2[8] + ' ' + limage3[8] + ' ' + limage4[8] + ' ')
def main():
    board = constructBoard()
    board.printboard()
main()