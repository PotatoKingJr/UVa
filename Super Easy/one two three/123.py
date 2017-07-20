from sys import stdin
num0 = int(stdin.readline())
one = 0


for i in range(num0):
	one = 0
	misspell = stdin.readline()
	misspell = misspell.strip()
	misspell = list(misspell)
	if len(misspell) == 5:
		print("3")
	else:
		print 
		if misspell[0] == "o":
			one += 1
		if misspell[1] == "n":
			one += 1
		if misspell[2] == "e":
			one += 1
		if one >= 2:
			print("1")
		else:
			print("2")
		
