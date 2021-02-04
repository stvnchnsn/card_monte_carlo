
class Card:
  def __init__(self,rank,suit):
    self.rank = rank
    self.suit = suit
    if type(self.rank) == int:
        royal_rank = {14:'A',13:'K',12:'Q',11:'J'}
        if self.rank in royal_rank.keys():
            self.royalty = royal_rank[self.rank]
            self.rank = self.rank
        else:
            self.royalty = False  
    else:
        royal_rank = {'A':14,'K':13,'Q':12,'J':11}
        if self.rank in royal_rank.keys():
            self.royalty = self.rank
            self.rank = royal_rank[self.rank]
        else:
            self.royalty = False  
  def return_rank(self):
    return self.rank
  def return_suit(self):
    return self.suit
  def name_of_card(self):
    return self.rank,self.suit,self.royalty