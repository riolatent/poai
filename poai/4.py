def minimax(depth , node , max , values):
	if depth == 3 :
		return values[node]
	if max :
		best = float('-inf')
		for i in range(2):
			val = minimax(depth+1 , node * 2 + i , False ,values)
			best = max(best , val)
		return best
	else:
		best = float('inf')
		for i in range(2):
			val = minimax(depth+1 , node * 2 + i , True ,values)
			best = min(best , val)
		return best


values = [3, 5, 6, 9, 1, 2, 0, -1]
optimal_value = minimax(0 ,0 ,True , values )
print(optimal_value)
