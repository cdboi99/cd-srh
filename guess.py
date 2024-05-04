import random



name = input("What is your name")
intro = 'This is a guessing game ,  pick a number number between 1 - 10'
print(f' welcome player {name}, {intro}')

x = random.randrange(1,11)
y = int(input("Enter a number"))
if 0 < y <=10:
    if y == x :
        print(f'yOU WON {name}')
    else: print(f'You lose {name} the number is {x}')
else: print(f'Pick a number in the range {name}')
