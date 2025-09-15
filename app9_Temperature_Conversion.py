try:
    Celsius = float(input('What is the temperature in Celsius? '))
    Fahrenheit = (Celsius * 9/5) + 32
    print('The temperature in Fahrenheit is:', Fahrenheit)
except ValueError:
    print('please input a number')
