from sys import stdin
num0 = int(stdin.readline())
case = 0
for i in range(num0):
    case += 1
    fit = "good"
    suit = stdin.readline()
    suit = suit.split(" ")
    suit = [x.strip() for x in suit]
    suit = [int(x) for x in suit]
    if suit[0] > 20:
        fit = "bad"
    if suit[1] > 20:
        fit = "bad"
    if suit[2] > 20:
        fit = "bad"
    print("Case ", end = "")
    print(case, end = "")
    print(": ", end = "")
    print(fit)


