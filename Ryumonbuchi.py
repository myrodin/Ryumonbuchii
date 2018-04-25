def think(hands, history, old_games):
	rival_hands = getRivalHands(history)

	return getBestHand(hands, rival_hands)

def getBestHand(my_hands, rival_hands):
	best_hand = ''
	best_count = 0

	for my_hand in my_hands:
		win_count = 0
		for rival_hand in rival_hands:
			win_count += match(my_hand, rival_hand)

		if win_count > best_count:
			best_hand = my_hand
			best_count = win_count

	return best_hand

def getRivalHands(history):
	rival_hands = ['1', '2', '3', '4', '5', '!']
	for one in history:
		rival_hands.remove(one[-1])
	return rival_hands

def match(my_hand, rival_hand):
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