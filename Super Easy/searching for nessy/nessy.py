from sys import stdin
beam = 0
num0 = int(stdin.readline())
for i in range(num0):
    num1 = stdin.readline()
    num1 = num1.split(" ")
    num1 = [x.strip() for x in num1]
    num1 = [int(x) for x in num1]
    num1[0] = num1[0] - 1
    num1[1] = num1[1] - 1
    matrix = [[0 for x in range(num1[0])] for y in range(num1[1])]
    for i in range(num1[0]):
        for i in range(num1[1]):
            beam = beam + 1

            
            num1[1] = num1[1] - 2

    num1[0] = num1[0] - 2
print(beam)


