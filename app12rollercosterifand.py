height = int(input('what is your height in inches?'))
credits = int(input('how many credits do you have?'))
if height > 60 and credits >= 10:
    print('Welcome!')
elif height >= 60 and credits >= 10:
    print('You are not tall enough')
elif height >= 60 and credits <= 10:
    print('you are tall enough but you need more money')
elif height <= 60 and credits <= 10:
    print('you are too short and have no money')
