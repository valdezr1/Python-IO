import random

print("Hello, I'm the *+- Genie. ")

userName = input("What is your name?\n")

print("Wonderful to meet you, " + userName + ".")

operatorChoice = input("Which operator do you want to use?\n\t1: Addition\n\t2: Subtraction\n\t3: Multiplication\n")

try:
    if int(operatorChoice) != 1 | int(operatorChoice) != 2 | int(operatorChoice) != 3 :
        print("Invalid value entered so defaulting to Addition")
        operatorChoice = "1"
except ValueError:
    print("Invalid value entered so defaulting to Addition")
    operatorChoice = "1"

MAX = input("Max number you want to be performing chosen operator with: ")
MIN = input("Min number you want to be performing chosen operator with: ")

print("Now, time to get started!.")

choiceArr = [" + ", " - ", " * ",]
correctArr = [userName + ", are you sure you aren't a math wizz?" , "Booyah!", "You're a human calculator!",
              "Giving ya a Virtual Thumbs-Up!", "Add 'em, Cowboy!", "Bow-chika-wow-wow", "Awwww Yeahhhhh", "Sweetness!"]
incorrectArr = ["YOU SHALL NOT PASS! Try again...", "So close...yet so far", "Not quite", "Better luck next try",
                "Nice try...", "Try again, " + userName, "Even the best get it wrong sometimes", "Missed it!"]

swapMinMax = MAX
if MIN > MAX:
    print("Min is greater than Max...switching their values.")
    swapMinMax = MAX
    MAX = MIN
    MIN = swapMinMax

while True:
    first = random.randint(int(MIN), int(MAX))
    second = random.randint(int(MIN), int(MAX))

    firstStr = str(first)
    secondStr = str(second)

    print("Question: " + firstStr + choiceArr[int(operatorChoice) - 1] + secondStr + " =  ?")
    print("Your Answer:")

    if int(operatorChoice) - 1 == 0:
        rightAnswer = first + second
    elif int(operatorChoice) - 1 == 1:
        rightAnswer = first - second
    else:
        rightAnswer = first * second

    answer = input()

    if answer == str(rightAnswer):
        print(correctArr[random.randint(0, 7)])
    else:
        print("Correct Answer: " + str(rightAnswer))
        print(incorrectArr[random.randint(0, 7)])

    print("Onto the next Question!\n")
