#Coin Toss
countHeads = 0
countTails = 0

def coinToss(countHeads, countTails):


    for i in range (0, 10):
        import random
        random_num = random.randint(0, 1)

        if random_num == 0:
            countHeads+= 1
            print "It's a heads!" + "...Got " + str(countHeads) + "head(s) so far and " + str(countTails) + " tail(s) so far"

        if random_num == 1:
            countTails+= 1
            print "It's a tails!" + "...Got " + str(countHeads) + "head(s) so far and " + str(countTails) + " tail(s) so far"


coinToss(countHeads, countTails)