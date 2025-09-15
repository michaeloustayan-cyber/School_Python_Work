# if and elif statements learning.
try:
    ph = float(input('Your pH is '))
    if ph > 7:
        print('basic')
    elif ph < 7:
        print('acidic')
    else:
        print('neutral')
except ValueError:
    print('enter a number')
