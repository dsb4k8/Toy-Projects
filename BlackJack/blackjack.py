from random import shuffle
import time

#Algorithm:
# initialize a player and dealer
# dealer's default show is one card up one card down
# player's default is init in definition
# while True:
    # ask user if they want to hit or stay
        # Keep asking if hit or stay is not selected
    # display user hand and total
    # if hit:
    #    if player.busted:
    #       break
    #   elif not player.busted:
        # continue
    # if player stays:
        # break
    # else:
        # continue
    # while dealer's total is less than 17:
        # dealer hits
#         if dealer busts:
            # print dealer busts
        # else:
            # continue
 #     if player > dealer:
        # player wins
    # if dealer > player:
        # dealer wins
    # if dealer == player:
        # both dealer and player lose
    # ask user for another round
    # if user plays another round:
        # continue
    # else:
        # pass
# print thank you for playing
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
            busted = "BUSTED"
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
            if result > 21:
                return(result,busted)
            else:
                return(result)
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
        def black_jacks(self):
            return self.total() == 21
        def cleanup(self,discard_deck):
            for i in self.hand:
                discard_deck.contents.append(i)
                # print "Discard deck: {}".format(discard_deck.contents)
                self.hand = []

        def has_empty_hand(self):
            return self.hand == []
        def can_hit(self):
            return self.total() < 21 


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
            return "{},{}, Showing A Possible: {}".format(self.hand[0], blocker, self.dealer_total()[0]+ 10)
        def dealer_total(self):
            result = []
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
            busted = "BUSTED"
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
            if result > 21:
                return(result,busted)
            else:
                return(result)

            
        def can_hit(self):
            return self.total() < 17

        def cleanup(self,discard_deck):
                for i in self.hand:
                    discard_deck.contents.append(i)
                # print "Discard deck: {}".format(discard_deck.contents)
                self.hand = []

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
        count = 1
        p1_round_score = 0

        while True:
            while count <= 1:
                print "_NEW_ROUND________________________________________________"
                print 
                print "Play_Deck: {}".format(len(play_deck.contents))
                print "Discarded: {}".format(len(discard_deck.contents))

                print"___________________________________________________________"
                print
         #        play = input("Play? Yes(1), No(0) ")
                playing = input("Play Hand? Yes(1), No(0): ")
                count += 1
            while playing != 1 and playing != 0:
                print "Please enter 1 for 'Yes' or 0 for 'No'"
                playing = input("Play Hand? Yes(1), No(0)")
                continue

            if playing == 1:
                print 
                print 
                print "Playing Hands:"

                if p1.has_empty_hand():
                    p1.hit()
                    time.sleep(1)
                    print
                    print "Dealer Delt a {}".format(p1.hand[-1])
                    print 
                    p1.hit()
                    time.sleep(1)
                    print "Dealer Delt a {}".format(p1.hand[-1])
                    print
                if dlr.has_empty_hand():
                    dlr.hit()
                    time.sleep(1)
                    print
                    print "Dealer Delt a {}".format(dlr.hand[-1])
                    print 
                    dlr.hit()
                    time.sleep(1)
                    print
                    print "Dealer Delt A Face Down Card}"                    
                    print

                
                time.sleep(1)
                print "Your Hand: {} Total: {} ".format(p1.hand, p1.total())
                print "Opponents: {}".format(dlr.showing_before_play())

                if p1.black_jacks():
                    print
                    print "Nice Black Jack! You Win"
                    print
                    pass

                hit = input ("Draw Card? Yes(1), No(0): ")
                while hit != 1 and hit != 0:
                    print "Please enter 1 for 'Hit' or 0 for 'Stay'"
                    time.sleep(1)
                    hit = input ("Draw Card? Yes(1), No(0): ")
                if hit == 1:
                    p1.hit()
                    print
                    time.sleep(1)
                    if p1.black_jacks():
                        print "You Drew A {}".format(p1.hand[-1])
                        print " You Win! You got a BLACK JACK!"
                        pass
                    elif p1.is_busted():
                        print "You Drew A {}".format(p1.hand[-1])
                        time.sleep(1)
                        print"You Lost. You Busted"
                        pass
                    else:
                        print "You Drew A {}".format(p1.hand[-1])
                        continue
                    print
                elif hit == 0:
                    pass

            print "__Dealer's Turn__"
            time.sleep(1)
            while dlr.total() <= 17:
                print 
                print "Dealer's hand {}".format(dlr.hand)
                dlr.hit()
                print
                print "Dealer hit and got a {}".format(dlr.hand[-1])
                time.sleep(1)
                print "Dealer's hand {}".format(dlr.hand) 
                if dlr.is_busted() and not p1.is_busted():
                    time.sleep(1)
                    print "You won! Dealer Busted With {}".format(dlr.total()[0])
                    print 
                    pass
                else:
                    continue
        

        #End game tally
            
            if p1.is_busted() and dlr.is_busted():
                print 
                print "Draw Game: Both Players Busted"
                print

            elif p1.total() > dlr.total() and not p1.is_busted():
                print 
                print "Player Hand {}".format(p1.hand)
                print "Player 1 won this round: {} to {}".format(p1.total(), dlr.total())
                print
            elif dlr.total() > p1.total() and not dlr.is_busted():
                print 
                print "Dealer's Hand {}".format(p1.hand)

                print "Dealer won this round: {} to {}".format(dlr.total(), p1.total())

                print
            elif dlr.total() == p1.total():
                print
                print "Tie game"
                print
            
            # Hand is spent

            busted = "BUSTED"

            print "Player's Final: {}".format(p1.total())
            print "Dealer's Final: {}".format(dlr.total())
            print 

            playing = input("Play Another Hand? Yes(1), No(0): ")

            if playing  == 1:
                print "_______________________________________________"
                print "Alright.. New Round"
                p1.cleanup(discard_deck)
                dlr.cleanup(discard_deck)
                play_deck.shuffle()
                print
                continue
            elif playing == 0:
                break

        print
        print "Thanks for playing! "
            
if __name__=="__main__":

    play()
