from sys import stdin
num0 = int(stdin.readline())
for i in range(num0):
	num1 = int(stdin.readline())
	num1 *= 567
	num1 /= 9
	num1 += 7492
	num1 *= 235
	num1 /= 47
	num1 -= 498
	num1 = num1//1
	num1 = str(num1)
	num1 = list(num1)
	
	num1.reverse()
	print (num1[3])