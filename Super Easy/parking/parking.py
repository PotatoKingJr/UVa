from sys import stdin
num0 = int(stdin.readline())
for i in range(num0):
    num1 = int(stdin.readline())
    stores = stdin.readline()
    stores = stores.split(" ")
    stores = [x.strip() for x in stores]
    stores = [int(x) for x in stores]
    stores.sort()
    num2 = num1
    num2 -= 1
    park = stores[num2] - stores[0]
    park = park * 2
    print (park)

