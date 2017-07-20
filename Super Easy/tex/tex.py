from sys import stdin

a = 0
newquote = ""
left = True
file = open("input.txt", "r")
lines = file.readlines()#(1 for line in open('input.txt'))

for line in lines:
    #quote = stdin.readline()
    #quote = list(quote)
    

    for character in line:
        
       
    
    """
        if quote[a] == "\"" and left == True:
            newquote += "``"
            left = False 
            a = a + 1
        elif quote[a] == "\"" and left == False:
            newquote += "\'\'"
            left = True 
            a = a + 1
        else:
            newquote += quote[a]
            a = a + 1 
            """
    a = 0
print (newquote)

"""
x = 0
for i in range(1000):
    if "\"" in quote:
      quote = quote.replace("\"", "``", 1)
      x = x + 1
    if "\"" in quote:
      quote = quote.replace("\"", "\'\'", 1)
      x = x + 1
                """
#print(quote, end = "")
#print (x)
#print (x%2)
"""
for i in range(1000):

    for i in range(1):

        for i in range(1000):
            if x%2 == 0:
                if "\"" in quote:
                    quote = quote.replce("\"", "``", 1)
                    x = x + 1a
            if x%2 == 1:
                if "\"" in quote:
                    quote = quote.replace("\"", "\'\'", 1)
                    x = x + 1


        
        
    print(quote, end = "")
    quote = stdin.readline() 
"""