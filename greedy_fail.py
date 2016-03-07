
def greedy_cost(move_dict, n, greedy_dict): 
	legal_move = [move for move in move_dict.keys() if n % move == 0]
	ratios = [float(move/move_dict[move]) for move in legal_move]
	move_index = 0
	for i in range(len(ratios)):
		if ratios[i] > ratios[move_index]:
			move_index = i; 
		if ratios[i] == ratios[move_index] and legal_move[i] > legal_move[move_index]:
			move_index = i; 
	
	move = legal_move[move_index]
	if move == 1:
		dest = n - 1 
	else: 
		dest = n/move
	cost = move_dict[move] + greedy_dict[dest]
	return cost 

def optimal_cost(move_dict, n, optimal_dict): 
	legal_move = [move for move in move_dict.keys() if n % move == 0]
	legal_dest = [n/move if move != 1 else n-1 for move in legal_move]
	cost_arr = []
	for i in range(0, len(legal_move)):
		cost_arr.append(move_dict[legal_move[i]] + optimal_dict[legal_dest[i]])
		move_index = cost_arr.index(min(cost_arr))
	return cost_arr[move_index]
	
def is_greedy_optimal(n, instance):
	greedy_cost_local = greedy_cost(n, instance)
	optimal_cost_local = optimal_cost(n, instance)
	print("greedy_cost = " + str(greedy_cost_local))
	print("optimal_cost = " + str(optimal_cost_local))
	return greedy_cost_local == optimal_cost_local
	
def min_greedy_failure(instance):
	n = 0
	greedy_dict = {0:0}
	optimal_dict = {0:0}
	g_cost = 0
	o_cost = 0
	while g_cost == o_cost: 
		#print("n = " + str(n))
		n += 1
		g_cost = greedy_cost(instance, n, greedy_dict)
		#print("Greedy Cost = " + str(g_cost))
		o_cost = optimal_cost(instance, n, optimal_dict)
		#print("Optimal Cost = " + str(o_cost))
		greedy_dict[n] = g_cost
		optimal_dict[n] = o_cost
	return n 

print("(3, 1) (2,1) w/ n= 321 greedy cost should be 11. ")
#print(greedy_cost({3:1, 2:1}, 321, {0:0}))

print("(3, 1) (2,1) w/ n= 321 optimal cost should be 10. ")
#print(min_greedy_failure({1:1, 3:1, 2:1}))

print("The smallest n for (211,2) (210,1) is 4740960. ")
#print(min_greedy_failure({1:1, 211: 2, 210: 1}))

print("The smallest n for (174, 3), (172, 3), (156, 5), (142, 11), (150, 7) is 1562. ")
#print(min_greedy_failure({1:1, 174: 3, 172: 3, 156: 5, 142: 11, 150: 7}))

print("Solutions: ")
print(min_greedy_failure({1:1, 179: 1, 69: 6}))
print(min_greedy_failure({1:1, 172: 4, 190:14, 32:12, 128:11, 142:17}))
print(min_greedy_failure({1:1, 139:15, 53: 18, 151: 3, 71: 12, 141: 2, 191: 1}))
print(min_greedy_failure({1:1, 100: 3, 66: 6, 194: 15}))
print(min_greedy_failure({1:1, 175: 5, 17: 15, 79: 9, 61: 2}))
print(min_greedy_failure({1:1, 6: 6, 66: 18, 14: 12, 36: 14, 130: 8, 178: 7, 2: 7}))
print(min_greedy_failure({1:1, 33: 13, 181: 9, 149: 14, 167: 16, 3: 19, 165: 2, 73: 7, 107: 13}))
print(min_greedy_failure({1:1, 82: 3, 152: 7, 184: 13, 72: 10, 8: 18, 144: 19, 88: 7, 158: 2, 182: 15}))
print(min_greedy_failure({1:1, 131: 2, 130: 1}))
print(min_greedy_failure({1:1, 190: 2, 189: 1}))






























