from sys import stdin
row = 0
col = 0
num0 = int(stdin.readline())
for i in range(num0):
    num1 = stdin.readline()
    num1 = num1.split(" ")
    num1 = [x.strip() for x in num1]
    num1 = [int(x) for x in num1]

    row = num1[0]//3
    col = num1[1]//3
    beam = row * col
    print(beam)




