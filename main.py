num = input('Enter a number (decimal only): ')
decimal = num.find('.')
int(decimal)
decimal = decimal + 1
num1 = num[decimal:]
num1 = str(num1)
dp = len(num1)
print('The number', num, 'has', dp, 'decimal places.')