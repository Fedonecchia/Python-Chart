board = ""

def getinput():

    try:
        row = int(input("How many rows?\n"))
        col = int(input("How many columns?\n"))
        big = int(input("How big each square?\n"))
    except(ValueError) as error:
        print("Please insert a valid input.\n\nNow retry and be careful this time!\n\n\n")
        getinput()


getinput()

for r in range(1, row+2):
    if r == 1:
        for c in range(col):
            board += " " + "_"*(2*big-1)
    else:
        for b in range(1, big+1):
            board += "\n"
            for c in range(1, col+1):
                if b == big:
                    board += "|" + "_"*(2*big-1)
                else:
                    board += "|" + " "*(2*big-1)
                if c == col:
                    board += "|"
print("\nEt voilà\n\n", board, sep="")





