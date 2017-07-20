from sys import stdin
num0 = int(stdin.readline())
amount = 0
for i in range(num0):
    command = stdin.readline()
    command = command.split(" ")
    command = [x.strip() for x in command]
    if command[0] == "report":
        print(amount)
    else:
        don = int(command[1])
        amount = amount + don

