from random import shuffle

#make a deck of cards
blocker = "***************"
class card:
	rank = "X"
	suit = "X"

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
	def __repr__(self):
		return "{} of {}".format(self.rank, self.suit)

class stack:
	def __init__(self, cards):
		self.contents = [card for card in cards]
		self.size = len(self.contents)
	def __repr__(self):
		return "{}".format([x for x in self.contents])
	def top(self):
		return self.contents[-1]
	def shuffle(self):
		for i in range(200):
			shuffle(self.contents)
		return self.contents

	# def deal(self):
	# 	#deal out 5 cards
	# 	if len(self.contents) >= 2:
	# 		for i in range(20):
	# 			shuffle(self.contents)
	# 		self.contents = self.contents[:-2]

	# 		hand = self.contents[-2:]
	# 		return hand
	# 	else:
	# 		print "< one hand remains in the deck. EMPTY"

class player:
	def __init__(self, WholeDeck):
                self.hand = WholeDeck.contents[-2:]
                
        	WholeDeck.contents = WholeDeck.contents[:-2]
		self.hit = self.hand.append(WholeDeck.top)
	def __repr__(self):
           return "%s, Total: %d " %(self.hand[:len(self.hand)-1], self.total())

        def total(self):
            result = 0
            result_w_ace = ()
            for n in self.hand[:len(self.hand)-1]:
                if n.rank == "J" or n.rank == "Q" or n.rank == "K":
                   result = result + 10
                elif n.rank == "A":
                    if result + 11 <= 21:
                        result  = result + 11
                    else:       
                        result_w_ace  = (result + 1, result + 11)
                        return result_w_ace
                else:
                    # print int(n.rank)
                    result = result + int(n.rank)
            return result




class dealer(player):
        def __repr__(self):
            return "{}".format(self.hand[0], blocker)


            
if __name__=="__main__":

	ranks = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
	Suits = ["Hearts","Clubs","Diamonds","Spades"]

	cardlist = []
        empty = []

	for suit in Suits:
		for rank in ranks:
			currentcard = card(rank, suit)
			cardlist.append(currentcard)
        play_deck = stack(cardlist)
        discard_deck = stack(empty)
        # print deck
        play_deck.shuffle()
        # print deck
        p1 = player(play_deck)
        print p1
        print len(p1.hand)

