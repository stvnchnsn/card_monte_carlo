import hand
import deck
import matplotlib.pyplot as plt
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
def draw_from_shuffled_deck():
    new_deck = deck.Deck()
    new_deck.shuffle_deck()
    new_hand = hand.Hand(new_deck.draw(num_of_cards=5))
    #new_hand.show_hand()
    hand_rank = new_hand.hand_ranking()
    return hand_rank
def deal_multiple(num_of_players = 9):
    '''not working, only out puts 'high card' rank'''
    new_deck = deck.Deck()
    new_deck.shuffle_deck()
    player_hands = []
    highest_rank = 'high card'
    for p in range(num_of_players):
        new_hand =hand.Hand(new_deck.draw(num_of_cards=5))
        if hand_rank_dic[new_hand.hand_ranking()] < hand_rank_dic[highest_rank]:
            highest_rank = new_hand.hand_ranking()
        player_hands.append(hand_rank_dic[new_hand.hand_ranking()])
    #print('Highest Rank = '+highest_rank)
    return highest_rank
    #print("highest rank = "+ str((hand_rank_dic[min(player_hands])))


class Monte_Simulator:
    def __init__(self, protocol = draw_from_shuffled_deck,iterations = 10000):
        ''' Will run protocol however many iterations and plot results'''
        self.iterations = iterations
        self.protocol = protocol
        self.list_of_ranks = {}

        for i in range(11):
            self.list_of_ranks[i] = 0
        self.hand_rank_tally={
            'royal flush':0,
            'straight flush':0,
            'four kind':0,
            'full house': 0,
            'flush': 0,
            'straight':0,
            'three kind':0,
            'two pair': 0,
            'pair':0,
            'high card':0
            }
        for i in range(self.iterations):
            self.hand_rank_tally[protocol()]+=1
        #print('hand rand dic =',self.hand_rank_tally)
        self.rank_by_percent = {}
        for k,v in self.hand_rank_tally.items():
            self.rank_by_percent[k] = 100*(v/self.iterations)
        
    def plot_results(self,by_percent = True):
        if by_percent == True:
            self.plot_dic_values = self.rank_by_percent
        else:
            self.plot_dic_values = self.hand_rank_tally#list_of_ranks
        #print(self.plot_dic_values)
        plt.bar(range(len(self.plot_dic_values)), list(self.plot_dic_values.values()), align='center')
        plt.xticks(range(len(self.plot_dic_values)), list(self.plot_dic_values.keys()),rotation='vertical')
        plt.title("monte_carlo_01 simulation")
        plt.tight_layout()
        plt.show()
    def return_results(self,by_percent = True):
        if by_percent == True:
            return self.rank_by_percent
        else:
            return self.hand_rank_tally
if __name__ == '__main__':
    monte_s = Monte_Simulator(protocol=deal_multiple,iterations=1000)
    print(monte_s.return_results(by_percent=True))
    print(monte_s.return_results(by_percent=False))
    monte_s.plot_results(by_percent=True)
    #deal_multiple(num_of_players = 8)