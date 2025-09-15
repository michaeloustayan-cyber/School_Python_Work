# Initialize house scores
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# Q1
try:
    q1 = int(input("""Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk
Enter 1 or 2: """))
    if q1 == 1:
        gryffindor += 1
        ravenclaw += 1
    elif q1 == 2:
        hufflepuff += 1
        slytherin += 1
    else:
        print("Wrong input.")
except ValueError:
    print("Wrong input.")

# Q2
try:
    q2 = int(input("""\nQ2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold
Enter 1 to 4: """))
    if q2 == 1:
        hufflepuff += 2
    elif q2 == 2:
        slytherin += 2
    elif q2 == 3:
        ravenclaw += 2
    elif q2 == 4:
        gryffindor += 2
    else:
        print("Wrong input.")
except ValueError:
    print("Wrong input.")

# Q3
try:
    q3 = int(input("""\nQ3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
Enter 1 to 4: """))
    if q3 == 1:
        slytherin += 4
    elif q3 == 2:
        hufflepuff += 4
    elif q3 == 3:
        ravenclaw += 4
    elif q3 == 4:
        gryffindor += 4
    else:
        print("Wrong input.")
except ValueError:
    print("Wrong input.")

# Final scores
print("\nFinal House Scores:")
print(f"Gryffindor: {gryffindor}")
print(f"Ravenclaw:  {ravenclaw}")
print(f"Hufflepuff: {hufflepuff}")
print(f"Slytherin:  {slytherin}")
