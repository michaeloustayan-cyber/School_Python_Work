import random

question = input("What is Your Question? ")

try:
    # Validate the question is a yes/no question
    if not question.endswith("?"):
        raise ValueError("Try again, must be a yes or no question")

    # Random number 1–9 for 9 possible answers
    num = random.randint(1, 9)
    print(num)

    if num == 1:
        print("Yes - definitely")
    elif num == 2:
        print("It is decidedly so")
    elif num == 3:
        print("Without a doubt")
    elif num == 4:
        print("Reply hazy, try again")
    elif num == 5:
        print("Ask later")
    elif num == 6:
        print("My sources say no")
    elif num == 7:
        print("Very doubtful")
    elif num == 8:
        print("Concentrate and ask again")
    else:  # num == 9
        print("Outlook not so good")

except ValueError as error:
    print(error)
