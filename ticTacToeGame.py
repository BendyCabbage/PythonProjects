import os 

xSymbol = "X"
oSymbol = "O"
blankSymbol = "_"



os.system("cls")

def start():
    os.system("cls")
    game = [blankSymbol,blankSymbol,blankSymbol,blankSymbol,blankSymbol,blankSymbol,blankSymbol,blankSymbol,blankSymbol]
    xTurn(game)

def xTurn(game):
    print(f"It is x's turn\n{gameStyling(game)}")
    try:
        position = int(input("Input the number of the square you want to place your piece on (left to right, top to bottom from 1-9): "))
        if game[position-1] == blankSymbol:
            game[position-1] = xSymbol
            os.system("cls")
    except:
        os.system("cls")
        print("Invalid character/position, try again")
        xTurn(game)
    if not checkWin(game):
        oTurn(game)
    else:
        print("x won!")
        if "yes" in input("Would you like to play again? "):
            os.system("cls")
            start()
        else:
            quit()


def oTurn(game):
    print(f"It is o's turn\n{gameStyling(game)}")
    try:
        position = int(input("Input the number of the square you want to place your piece on (left to right, top to bottom from 1-9): "))
        if game[position-1] == blankSymbol:
            game[position-1] = oSymbol
            os.system("cls")          
    except:
        os.system("cls")
        print("Invalid character/position, try again")
        oTurn(game)
    if not checkWin(game):
        xTurn(game)
    else:
        print("o won!")
        if ("y" or "yes") in input("Would you like to play again? "):
            os.system("cls")
            start()
        else:
            quit()

def checkWin(game):
    if game[0] == game[1] == game[2] and game[0] != blankSymbol:
        return True
    elif game[3] == game[4] == game[5] and game[3] != blankSymbol:
        return True
    elif game[6] == game[7] == game[8] and game[6] != blankSymbol:
        return True
    elif game[0] == game[4] == game[8] and game[0] != blankSymbol:
        return True
    elif game[2] == game[4] == game[6] and game[2] != blankSymbol:
        return True
    elif game[0] == game[3] == game[6] and game[0] != blankSymbol:
        return True
    elif game[1] == game[4] == game[7] and game[1] != blankSymbol:
        return True
    elif game[2] == game[5] == game[8] and game[2] != blankSymbol:
        return True
    else:
        for i in game:
            if i == blankSymbol:
                return False
        if "yes" in input("It's a draw! Would you like to play again? "):
            start()
        else:
            quit()
    

def gameStyling(game):
    styledGame = (f"| {game[0]} | {game[1]} | {game[2]} |\n| {game[3]} | {game[4]} | {game[5]} |\n| {game[6]} | {game[7]} | {game[8]} |")
    return styledGame








start()
