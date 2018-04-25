def think(hands, history, old_games):
	koromo = Koromo(hands, history)
	return koromo.think()

class Koromo:
	def __init__(self, hands, history):
		self.hands = hands
		self.history = history

	def think(self):
		rival_hands = self.getRivalHands()

		rival_best_hand = self.getBestHand(rival_hands, self.hands)
		counter_hands = self.getCounterHands(rival_best_hand)

		return self.getWorstHand(counter_hands, rival_hands)

	def getRivalHands(self):
		rival_hands = ['1', '2', '3', '4', '5', '!']
		for one in self.history:
			rival_hands.remove(one[-1])
		return rival_hands

	def getBestHand(self, my_hands, rival_hands):
		best_hand = ''
		best_count = 0

		for my_hand in my_hands:
			win_count = 0
			for rival_hand in rival_hands:
				win_count += self.match(my_hand, rival_hand)

			if win_count > best_count:
				best_hand = my_hand
				best_count = win_count

		return best_hand

	def getCounterHands(self, rival_hand):
		win_hands = []
		for my_hand in self.hands:
			if self.match(my_hand, rival_hand) == 2:
				win_hands.append(my_hand)

		if len(win_hands) == 0:
			win_hands = self.hands

		return win_hands
		
	def getWorstHand(self, my_hands, rival_hands):
		worst_hand = ''
		worst_count = 10

		for my_hand in my_hands:
			win_count = 0
			for rival_hand in rival_hands:
				win_count += self.match(my_hand, rival_hand)

			if win_count < worst_count:
				worst_hand = my_hand
				worst_count = win_count

		return worst_hand

	def match(self, my_hand, rival_hand):
		if my_hand == rival_hand:
			return 1
		
		if my_hand == '1' and rival_hand == '5':
			return 2
		if my_hand == '5' and rival_hand == '1':
			return 0
		
		if my_hand == '!':
			if rival_hand == '2' or rival_hand == '4':
				return 2
			else:
				return 0
		if rival_hand == '!':
			if my_hand == '2' or my_hand == '4':
				return 0
			else:
				return 2
			
		if my_hand > rival_hand:
			return 2
		else:
			return 0

print(think(['3', '4', '5', '!'], [['1', '!'], ['2', '5']], []))