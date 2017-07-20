from sys import stdin
def main():
    num0 = int(stdin.readline())
    for i in range(num0):
        code = int(stdin.readline())
        
        if code == 1 or code == 4 or code == 78:
            print ("+")
        else:
            code1 = [int(x) for x in str(code)]
            length = len(code1)
            length -= 1
            if code1[length] == 5:
                length -= 1
                if code1[length] == 3:
                    print("-")
            elif code1[0] == 9 and code1[length] == 4:
                print("*")
            else:
                print("?")

if __name__ == '__main__':
    main()