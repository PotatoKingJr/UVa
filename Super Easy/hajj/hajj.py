from sys import stdin
case = 0
while True:
    hajj = stdin.readline()
    hajj = hajj.strip()
    case += 1
    if hajj == "Hajj":
        print("Case ", end = "")
        print(case, end = "")
        print(": ", end = "")
        print("Hajj-e-Akbar")
    elif hajj == "Umrah":
        print("Case ", end = "")
        print(case, end = "")
        print(": ", end = "")
        print("Hajj-e-Asghar")
    else:
        break