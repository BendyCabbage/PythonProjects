import random
import time
import os


def questionAsker(operator,firstInt,secondInt):
    try:
        givenAnswer = int(input(f"{firstInt} {operator} {secondInt} = "))
        return givenAnswer
    except:
        print("Not a valid answer, try again")
        questionAsker(operator,firstInt,secondInt)

def main(highScore):
    evaluation = 0
    wrongAnswers = []

    os.system("cls")
    input("Ready? ")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    os.system("cls")
    start = time.time()

    for questions in range(20):
        operator = random.choice(["+", "-",])
        firstInt = random.randrange(0,20)
        secondInt = random.randrange(0,20)

        givenAnswer = questionAsker(operator,firstInt,secondInt)

        answer = eval(f"{firstInt} {operator} {secondInt}")
        
        if answer == givenAnswer:
            evaluation += 1
        else:
            wrongAnswers.append(questions+1)
            
    end = time.time()
    timeTaken = round(end-start,2)
    perQuestionTime = round(20/timeTaken,2)
    score = round(1000/perQuestionTime*(evaluation/20))

    print(f"You got an accuracy of {evaluation*5}% in {timeTaken}s, answering a question every {round(20/timeTaken,2)}s. This earns you a score of {score} points!")
    if score > highScore:
        print(f"Congratulations, that a new highscore! You beat your previous high score by {score-highScore} points!")
        highScore = score
    else: 
        print(f"You were {highScore-score} points away from beating your highscore.")

    if len(wrongAnswers) > 1:
        print("Unfortunately you got questions " + " ".join(map(str,wrongAnswers)) + " wrong.")
    elif(len(wrongAnswers) == 1):
        print(f"Unfortunately you got question {wrongAnswers[0]} wrong")
    
    if "yes" in input("Do you want to try again?"):
        main(highScore)

main(750)