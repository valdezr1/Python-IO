import random

print("Hello, I'm the Addition Genie. ")
print("What is your name?")

userName = input()

print("Wonderful to meet you, " + userName + ".")
print("Now, time to get you better at Addition.")

correctArr = [userName + ", are you sure you aren't an addition wizz?" , "Booyah!", "You're a human calculator!",
              "Giving ya a Virtual Thumbs-Up!", "Add 'em, Cowboy!", "Bow-chika-wow-wow", "Awwww Yeahhhhh", "Sweetness!"]
incorrectArr = ["YOU SHALL NOT PASS! Try again...", "So close...yet so far", "Not quite", "Better luck next try",
                "Nice try...", "Try again, " + userName, "Even the best get it wrong sometimes", "Missed it!"]

while True:
    first = random.randint(0, 1000)
    second = random.randint(0, 1000)

    firstStr = str(first)
    secondStr = str(second)

    print("Question: " + firstStr + " + " + secondStr + " =  ?")
    print("Your Answer:")

    answer = input()

    if answer == str(first + second):
        print(correctArr[random.randint(0, 7)])
    else:
        print("Correct Answer: " + str(first + second))
        print(incorrectArr[random.randint(0, 7)])

    print("Onto the next Question!\n")
