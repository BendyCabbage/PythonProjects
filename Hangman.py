import os

wordList = []
guessingWord = []
guessedLetters = []
lives = 10

def guess(wordList,guessingWord,guessedLetters,lives):
    letter = input("Guess a letter: ")
    indexCount = -1
    letter = letter.lower()
    success = False
    if len(letter) != 1 or not letter.isalpha():
        os.system('cls')
        print("Try again with a valid letter")
        print(f"Guessed letters: {properPrint(guessedLetters)}")
        print(properPrint(guessingWord))
        guess(wordList,guessingWord,guessedLetters,lives)

    if not letter in guessedLetters:
        guessedLetters.append(letter)
    else:
        os.system('cls')
        print("You've already guessed that letter, try again")
        print(f"Guessed letters: {properPrint(guessedLetters)}")
        print(properPrint(guessingWord))
        guess(wordList,guessingWord,guessedLetters,lives)

    for i in wordList:
        indexCount += 1
        if i == letter:
            guessingWord.insert(indexCount,letter)
            del guessingWord[indexCount+1]
            success = True
    if success == True:
        os.system('cls')
        print("Correct!")
        print(f"Guessed letters: {properPrint(guessedLetters)}")
        if guessingWord == wordList:
            print(properPrint(guessingWord))
            print("Congratulations, you won!")
            playAgain = input("Would you like to play again? ")
            playAgain = playAgain.lower()
            if "y" in playAgain or "yes" in playAgain:
                wordGetter(wordList,guessingWord,guessedLetters,lives)
        else:
            print(properPrint(guessingWord))
            guess(wordList,guessingWord,guessedLetters,lives)
    else:
        lives -= 1
        if lives <= 0:
            playAgain = input("You ran out of lives. Would you like to play again? ")
            playAgain = playAgain.lower()
            if "y" in playAgain or "yes" in playAgain:
                os.system('cls')
                wordGetter(wordList,guessingWord,guessedLetters,lives)
            else:
                quit()
        os.system('cls')
        print(f"Incorrect, you have {lives} lives remaining")
        print(f"Guessed letters: {properPrint(guessedLetters)}")
        print(properPrint(guessingWord))
        guess(wordList,guessingWord,guessedLetters,lives)
    return guessingWord

def properPrint(guessingWord):
    GuessWordStr = ""
    for i in guessingWord:
        GuessWordStr += i
        GuessWordStr += " "
    return GuessWordStr

def wordGetter(wordList,guessingWord,guessedLetters,lives):
    lives = 10
    guessedLetters = []
    guessingWord = []
    wordList = []
    word = input("Enter a word: ")
    word = word.lower()
    for i in word:
        wordList.append(i)
    os.system('cls')
    print("Give the device to another person")
    input("Press enter to continue: ")
    os.system('cls')
    print("_ " * len(wordList))

    for i in range(len(wordList)):
        guessingWord.append("_")
    guessedWord = guess(wordList,guessingWord,guessedLetters,lives)
    print(properPrint(guessedWord))

wordGetter(wordList,guessingWord,guessedLetters,lives)
