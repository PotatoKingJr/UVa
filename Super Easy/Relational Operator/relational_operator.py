from sys import stdin
num0 = int(stdin.readline())
for i in range(num0):
    num1 = stdin.readline()
    num1 = num1.split(" ")
    num1 = [x.strip() for x in num1]
    num1 = [int(x) for x in num1]
    
    if num1[0] < num1[1]:
        #print (num1[0])
        print ("<")
        #print (num1[1])
    elif num1[0] > num1[1]:
        #print (num1[0])
        print (">")
        #print (num1[1])
    elif num1[0] == num1[1]:
        #print (num1[0])
        print ("=")
        #print (num1[1])
