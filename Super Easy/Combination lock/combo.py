from sys import stdin
while True:
	full_combination = stdin.readline()
	full_combination = full_combination.split(" ")
	full_combination = [x.strip() for x in full_combination]
	full_combination = [int(x) for x in full_combination]
	if full_combination[0] == 0 and full_combination[1] == 0 and full_combination[2] == 0 and full_combination[3] == 0:
		break
	else:
		#9 degrees per number
		deg = 80
		if full_combination[0] > full_combination[1]:
			to_add = full_combination[0] - full_combination[1]
		elif full_combination[0] < full_combination[1]:
			to_add1 = full_combination[1] - full_combination[0]
			to_add = 40 - to_add1
		else: 
			to_add = 0
		deg = deg + to_add
		deg = deg + 40
		if full_combination[1] < full_combination[2]:
			to_add = full_combination[2] - full_combination[1]
		elif full_combination[1] > full_combination[2]:
			to_add1 = full_combination[1] - full_combination[2]
			to_add = 40 - to_add1
		else:
			to_add = 0
		deg = deg + to_add
		if full_combination[2] > full_combination[3]:
			to_add = full_combination[2] - full_combination[3]
		elif full_combination[2] < full_combination[3]:
			to_add1 = full_combination[3] - full_combination[2]
			to_add = 40 - to_add1
		else:
			to_add = 0
		deg = deg + to_add
		deg = deg * 9
		print (deg)
