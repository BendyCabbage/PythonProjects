import os
import random

guessedLetters = []
guessingWord = []
wordList = []
lives = 10

def DictFinder():
    wordsList = []
    DictLocation = input("Input the location of a dictionary (must be a text file): ")
    Dictlocation = DictLocation.lower()
    if os.path.exists(DictLocation):
        for line in open(DictLocation):
            wordsList.append(line[:-1])
        return wordsList
    else:
        os.system('cls')
        print("Invalid location")
        DictFinder()


def WordGetter(wordsList):
    guessedLetters = []
    guessingWord = []
    wordList = []
    lives = 10
    word = random.choice(wordsList)
    print(f"This is the chosen word: {word}")
    for i in range(len(word)):
        guessingWord.append("_")
    for i in word:
        wordList.append(i)
    print(properPrint(guessingWord))
    return word


def Guess(lives):
    indexCount = -1
    success = False
    letter = input("Choose a letter: ")
    letter.lower()
    #Check whether it is a valid character
    if len(letter) != 1 or not letter.isalpha():
        print("That is not a valid letter.")
        Guess(lives)
    #Check if the letter has been previously guessed
    if letter in guessedLetters:
        print("You've already guessed that letter.")
        Guess(lives)
    else:
        guessedLetters.append(letter)
        guessedLetters.sort()
    #Check if the letter is in the word
    for i in word:
        indexCount += 1
        if letter == i:
            print(guessingWord)
            guessingWord.insert(indexCount,letter)
            del guessingWord[indexCount+1]
            success = True
    #If the letter was in the word
    if success == True:
        if guessingWord == wordList:
            playAgain = input("Congratulations, you won! Would you like to play again? ") 
            playAgain = playAgain.lower()
            if "y" in playAgain or "yes" in playAgain:
                os.system('cls')
                WordGetter(wordsList)
            else:
                quit()
        os.system("cls")
        print("Correct!")
        print(properPrint(guessingWord))
        Guess(lives)
    else:
        lives -= 1
        if lives <= 0:
            playAgain = input("You ran out of lives, would you like to play again? ") 
            playAgain = playAgain.lower()
            if "y" in playAgain or "yes" in playAgain:
                os.system('cls')
                WordGetter(wordsList)
            else:
                quit()
        else:
            print("Incorrect")
            print(f"Guessed letters: {properPrint(guessedLetters)}")
            print(properPrint(guessingWord))
            Guess(lives)
    return guessingWord            

        
def properPrint(List):
    Str = ""
    for i in List:
        Str += i
        Str += " "
    return Str




wordsList = DictFinder()
word = WordGetter(wordsList)
Guess(lives)





