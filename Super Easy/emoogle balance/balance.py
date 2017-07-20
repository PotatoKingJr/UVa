from sys import stdin
case = 0
count = 0
while True:
    num1 = int(stdin.readline())
    if num1 == 0:
        break
    else:
        count = 0
        balance = stdin.readline()
        balance = balance.split(" ")
        balance = [x.strip() for x in balance]
        balance = [int(x) for x in balance]
        case += 1
        for i in range(num1):
            num1 -= 1
            
            if num1 < 0 :
                break
            else:
                if balance[num1] == 0:
                    count -= 1
                else:
                    count += 1
    print("Case ", end = "")
    print(case, end = "")
    print(": ", end = "")
    print(count)

