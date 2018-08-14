from random import shuffle

#make a deck of cards

class card:
	rank = "X"
	suit = "X"
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
	def __repr__(self):
		return "{} of {}".format(self.rank, self.suit)
	# def show(self):
	# 	# print "{} of {}".format(self.rank, self.suit)
	# 	print ("({} {})").format(self.rank, self.suit)

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

	def deal(self):
		#deals out 5 cards
		if len(self.contents) >= 5:
			for i in range(20):
				shuffle(self.contents)
			self.contents = self.contents[:-5]

			hand = self.contents[-5:]
			return hand
		else:
			print "< one hand remains in the deck. EMPTY"

if __name__=="__main__":

	ranks = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
	Suits = ["Hearts","Clubs","Diamonds","Spades"]

	cardlist = []

	for suit in Suits:
		for rank in ranks:
			currentcard = card(rank, suit)
			cardlist.append(currentcard)

	deck = stack(cardlist)
	print deck

