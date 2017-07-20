from sys import stdin
def main():
    newquote = ""
    left = False
    with open('input.txt') as myfile:
        count = sum(1 for line in myfile)
        for i in range(count):
            quote = stdin.readline()
            quote = quote.strip()
            quote1 = list(quote)
            
            
            amount = len(quote1)
            for f in range(len(quote1)): 
                amount -= 1
                if quote1[amount] == '"' and left == True:
                    newquote += "``"
                    left = False
                elif quote1[amount] == '"' and left == False:
                    newquote += "''"
                    left = True
                else:
                    newquote += quote1[amount]
                    """
            if newquote[0] != " ":
                newquote.insert( 0, " ")
                """
            newquote = newquote[::-1]
            print(newquote, end = "")
            newquote = ""
if __name__ == '__main__':
    main()