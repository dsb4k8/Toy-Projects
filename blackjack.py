from random import shuffle
import time

#Algorithm:
# initialize a player and dealer
# dealer's default show is one card up one card down
# player's default is init in definition
# while True:
    # ask user if they want to hit or stay
    # display user hand and total
    # if hit:
    # if player.busted:
    # break
    # elif not player.busted:
        # continue
    # if player stays:
        # break
    # else:
        # continue
    # while dealer's total is less than 17:
        # dealer hits


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
        def __len__(self):
                return self.size
	def top(self):
		return self.contents[-1]
	def shuffle(self):
		for i in range(200):
			shuffle(self.contents)
		return self.contents
        def is_full(self):
           return self.size == 52
                

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
            self.WD.size -= 1
            result = l.append(added)
            self.hand = l
            return l

        def is_busted(self):
            return self.total() > 21
        def cleanup(self,discard_deck):
            if self.is_busted():
                for i in self.hand:
                    discard_deck.contents.append(i)
                print "Discard deck: {}".format(discard_deck.contents)
                self.hand = []
        def has_empty_hand(self):
            return self.hand == []


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
        def can_hit(self):
            return self.total() < 17

        


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
        print "__________________________________________________________"
        print "Play_Deck: {}".format(len(play_deck))
        print "Discarded: {}".format(len(discard_deck))

        print"___________________________________________________________" 
        
        #Using counter for for 2 player game. (for 2 players, if counter % 2 == 0 -> even, 
        # it is the DEALERS MOVE,This means that c = 1 == p1, c = 2 == dlr... c = p1+n % 2 == p1)

        
        COUNT = 1 
        
        # Game Rules
        while True:
            if COUNT % 2 != 0:
                if p1.has_empty_hand():
                    p1.hit()
                    p1.hit()
                    print "Player had empty hand. New hand -> {}".format(p1.hand)
                print "Player Hand: {}".format(p1)
                print "Dealer Hand: {}".format(dlr.showing_before_play())
                print 
                give_option = input('Hit(1) or Stay(0): ')
                if give_option == 1:
                    p1.hit()
                print "__________________________________________________________"
                # print "Play_Deck: {}".format(len(play_deck))
                # print "Discarded: {}".format(len(discard_deck))
                print"___________________________________________________________" 
 
                # print p1



            #Play logic:
            #If player has over 21
                if p1.is_busted():
                    print "Busted."
                    COUNT +=1

                #add players hand to empty / lesser discard deck
                    p1.cleanup(discard_deck)
                    continue
                
            # If you win your hand:
                elif p1.total == 21:
                    print "Black Jack!"
            # If you want to stay/ dont want to risk busting
                elif give_option == 0:
                    COUNT +=1 
                    continue
                else:
                    continue
                print("Discarded: {}".format(discard_deck))


           # For dealer
            else:

                print "+Dealers HAND:"
                print 
                print "Player Hand: {}".format(p1)
                print "Dealer Hand: {}".format(dlr.showing_before_play())
                print 
                while dlr.can_hit():
                    time.sleep(1)
                    print "dlr had to hit"
                    dlr.hit()
                    print "{}, Total: {}".format(dlr.hand, dlr.total())
                    if dlr.is_busted():
                        print "Dealer Busted... You won"
                        COUNT +=1
                        break
                    else:
                        time.sleep(1)
                        print "Dealer did not bust... Total: {}".format(dlr.total())
                        continue
#                 print "Dealer did not bust... Total: {}".format(dlr.total())
                # COUNT +=1
                break
                    
               


                # give_option = input('Hit(1) or Stay(0): ') %(dlr.total())
                # if give_option == 1:
                    # dlr.hit()
                print "__________________________________________________________"
                # print "Play_Deck: {}".format(len(play_deck))
                # print "Discarded: {}".format(len(discard_deck))
                print"___________________________________________________________" 
 
#                 print p1
            # #Play logic:
            # #If player has over 21
                # if p1.is_busted():
                    # print "Busted."
                # #add players hand to empty / lesser discard deck
                    # p1.cleanup(discard_deck)
                    # COUNT +=1
                    # break
                
            # # If you win your hand:
                # elif p1.total == 21:
                    # print "Black Jack!"
            # # If you want to stay/ dont want to risk busting
                # elif give_option == 0:
                    # break 
                # else:
                    # continue


            
if __name__=="__main__":

    play()

