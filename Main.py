import random

print("Hello, I'm the Addition Genie. ")
print("What is your name?")

userName = input()

print("Wonderful to meet you, " + userName + ".")
print("Now, time to get you better at Addition.")

while True:
    first = random.randint(0,1000)
    second = random.randint(0,1000)

    firstStr = str(first)
    secondStr = str(second)

    print("Question: " + firstStr + " + " + secondStr + " =  ?")
    print("Answer:")

    answer = input()

    if answer == str(first + second):
        print("BABAM!!! NICE WORK!")
    else:
        print("Not quite")

    print("Onto the next Question!\n")
