import cards
import deck

def test_main():
    new_deck = deck.Deck()
    new_deck.shuffle_deck()
    hand = Hand(new_deck.draw(num_of_cards=5))
    hand.show_hand()
    hand.hand_ranking()
    #hand.num_of_kind_check()
def test_custom_hand():
    card1 = cards.Card('A','C')
    card2 = cards.Card('J','C')
    card3 = cards.Card('J','H')
    card4 = cards.Card('A','H')
    card5 = cards.Card('A','C')
    card6 = cards.Card('J','D')
    card7 = cards.Card(10,'D')
    card_list = [card1,card2,card3,card4,card5,card6,card7]
    hand = Hand(card_list)
    hand.show_hand()
    print(hand.hand_ranking())
    #hand_rank = hand.num_of_kind_check()
    #print(hand_rank)

protocol = test_main

class Hand:
    def __init__(self,hand):
        self.hand = hand
        self.hand_rank = 'high card' # 1 being Royal Flush, 10 - high card
        self.pull_ranks()
        self.pull_suits()
        self.num_of_kind_check() 
        self.straight_check()
        self.flush_check()
        self.flush_straight()

    def show_hand(self):
        for c in self.hand:
            print(c.name_of_card())
    def pull_ranks(self):
        self.ranks = {}
        for c in self.hand:
            try:
                self.ranks[c.return_rank()] +=1
            except KeyError:
                self.ranks[c.return_rank()]= 0
        self.ranks_list = list(self.ranks.keys())
        self.ranks_list.sort()
    def pull_suits(self):
        self.suits = {}
        for c in self.hand:
            try:
                self.suits[c.return_suit()]+=1
            except KeyError:
                self.suits[c.return_suit()] = 1

    def num_of_kind_check(self):
        self.num_of_kind = {}
        for k in self.ranks.keys():
            if self.ranks[k] != 0:
                self.num_of_kind[k] = self.ranks[k] + 1
        self.full_house_check = 0
        self.two_pair_check = 0
        for k in self.num_of_kind.keys(): # pair, two pair,three kind, four kind
            if self.num_of_kind[k] == 2:
                self.full_house_check +=1
                if self.two_pair_check == 0:
                    self.two_pair_check =1
                    self.hand_rank = 'pair'
                else:
                    self.hand_rank = 'two pair'
                    self.full_house_check = 0
                    pairs = []
                    for k,v in self.num_of_kind.items():    
                        pairs.append(str(k))
                    #print("Two Pair: "+str(pairs))
            if self.num_of_kind[k] == 3:
                self.full_house_check +=1
                self.hand_rank = 'three kind'
            if self.num_of_kind[k] == 4:
                self.hand_rank = 'four kind'
        if self.full_house_check == 1: # full house
            for k,v in self.num_of_kind.items():
                pass
                #print(str(v) + " of a kind: "+str(k))
        if self.full_house_check ==2:   
            #print('Full house ')
            self.hand_rank = 'full house'
            for k,v in self.num_of_kind.items():
                pass    
                #print(str(v)+" of a kind: "+str(k))
        return self.hand_rank
    def straight_check(self):
        if len(self.ranks) == 5: # all unique ranks?
            if max(self.ranks_list) - min(self.ranks_list) == 4: #difference between max and min must be 4
                self.straight= True
            else:
                self.straight = False
        else:
            self.straight = False
    def flush_check(self):
        if len(self.suits) == 1:
            self.flush = True
        else:
            self.flush = False
    def flush_straight(self):
        if min(self.ranks_list) >= 10:
            self.all_royal = True
        else:
            self.all_royal = False
        if (self.straight == True) & (self.flush == True) & (self.all_royal == True):
            self.hand_rank = 'royal flush'
        elif (self.straight == True) & (self.flush == True):
            self.hand_rank = 'straight flush'
        elif self.straight == True:
            self.hand_rank = 'straight'
        elif self.flush == True:
            self.hand_rank = 'flush'
        
        
    def hand_ranking(self):
        hand_rank_dic = {
            'royal flush':1,
            'straight flush':2,
            'four kind':3,
            'full house': 4,
            'flush': 5,
            'straight':6,
            'three kind':7,
            'two pair': 8,
            'pair':9,
            'high card':10,
            'not classified yet':0}
        #print(self.hand_rank)
        return self.hand_rank#hand_rank_dic[self.hand_rank]
    
if __name__ == "__main__":
    protocol()