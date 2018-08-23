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

class player:
	def __init__(self, WholeDeck):
                self.WD = WholeDeck
                self.hand = self.WD.contents[-2:]
                
        	self.WD.contents = self.WD.contents[:-2]
	def __repr__(self):
           return "%s, Total: %d " %(self.hand[:len(self.hand)], self.total())

        def total(self):
            result = 0
            for n in self.hand[:len(self.hand)]:
                if n.rank == "J" or n.rank == "Q" or n.rank == "K":
                   result = result + 10
                elif n.rank == "A":
                    if result + 11 <= 21:
                        result  = result + 11
                    else:       
                        result = result + 1
                else:
                    result = result + int(n.rank)
            return result

        def hit(self):
            
            l = self.hand
            added = self.WD.contents[-1]
            self.WD.contents = self.WD.contents[:-1]
            result = l.append(added)
            self.hand = l
            return l
        def is_busted(self):
            return self.total() > 21
            
           

class dealer(player):
        d = {
                "K": 10,
                "J": 10,
                "Q": 10,
                "A": 11
                }

        def __repr__(self):
            return "{}, Total: {}".format(self.hand, self.total())
        def showing_before_play(self):
            return "{},{}, Showing {}".format(self.hand[:len(self.hand)-1], blocker, self.dealer_total()[0])
        def dealer_total(self):
            result = []
            # faces = ["J","Q","K"]
            # ace = "A"
            for card in self.hand:
                if card.rank in self.d.keys():
                    if self.d.get(card.rank) == 10:
                        result.append(10)
                    elif card.rank == "A":
                        if sum(result) + 11 <= 21:
                            result.append(11)
                        else:
                            result.append(1)

                else:
                    result.append(card.rank)
            return result

#                     result +=10
                # elif card.rank == ace:
                    # if result + 11 <= 21:
                        # result +=11
                    # else:
                        # result += 1
                # else:
                    # result += card.rank
            # return result 


        def total(self):
            result = 0
            for n in self.hand[:len(self.hand)]:
                if n.rank == "J" or n.rank == "Q" or n.rank == "K":
                   result = result + 10
                elif n.rank == "A":
                    if result + 11 <= 21:
                        result  = result + 11
                    else:       
                        result = result + 1
                else:
                    result = result + int(n.rank)
            return result

        


def play():

        ranks = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
        Suits = ["Hearts","Clubs","Diamonds","Spades"]
	cardlist = []
        empty = []
        #populate new play_deck
	for suit in Suits:
		for rank in ranks:
			currentcard = card(rank, suit)
			cardlist.append(currentcard)
        play_deck = stack(cardlist)
        for i in range(10):
            play_deck.shuffle()
        discard_deck = stack(empty)
        # play_deck.shuffle()
        p1 = player(play_deck)
        dlr = dealer(play_deck)

        # Game Rules
        while True:
            print "Player Hand: {}".format(p1)
            print "Dealer Hand: {}".format(dlr.showing_before_play())
            print 
            give_option = input('Hit(1) or Stay(0): ') %(p1.total())
            if give_option == 1:
                p1.hit()
                print p1
            elif give_option == 0:
                pass
            break





            
if __name__=="__main__":

    play()

       #  ranks = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
	# Suits = ["Hearts","Clubs","Diamonds","Spades"]

        # play_deck = stack(cardlist)
        # discard_deck = stack(empty)
        # play_deck.shuffle()
        # p1 = player(play_deck)
        # print "PLAYER!________________________________"
        # print 
        # print p1
        # print "Busted: {}".format(p1.is_busted())        
        # p1.hit()
        # print 
        
        # print p1
        # print "Busted: {}".format(p1.is_busted())        
        # print 
        # p1.hit()
        # print p1
        # print "Busted: {}".format(p1.is_busted())
        # p1.hit()
        # print
        # print p1
        # print "Busted: {}".format(p1.is_busted())
        # print  "_______________________________________"

        # dlr = dealer(play_deck)
        # print "Dealer: ________________________________"
        # print dlr.showing_before_play()
        # dlr.hit()
        # dlr.hit()
        # print dlr
        # print "________________________________________"

