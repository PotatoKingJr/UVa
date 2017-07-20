file1 = open("input.txt","r+")
file2 = open("output.txt","r+")
num0 = int(file1.readline())
for i in range(num0):
    num1 = str(file1.readline())
    num1.split(" ")
    print (num1[0])
    print (num1[1])