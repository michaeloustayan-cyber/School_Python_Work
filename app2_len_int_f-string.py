course = "Python Programming"
print(len(course))
# [0] is first character of string. The " is not part of the string. It defines the string. it should habve output of print "P"
print(course[0])
# -1 means last character of string. it is g
print(course[-1])
# new string first 3 characters. should be Pyt
print(course[0:3])
# [0:] will result in character from start to end of string to print
print(course[0:])
# [:3] will be same result of [0:3]. python automatically fills in 0.
print(course[:3])
# [:] pulls from start to finish. Python automatically picks beginning and end characters of string.
print(course[:])
Name = input('what is your name? ')
Age = int(input('How old are you? '))
print(f'Hello {Name}, you are {Age} years old')
