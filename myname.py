
a = int(input("Please enter your age"))
if a >= 18:
    print('you can watch the movie')
elif 18 > a >= 16:
    print('you can watch the movie with an adult')
    c = input('an adult with you? Y or N')
    if c== "Y":
        print( 'enjoy')
    else:
        print('no!')
else:
    print('no movie for you')   
print('Done')



import random

name = input("What is your name")
intro = 'This is a guessing game ,  pick a number number between 1 - 10'
print(f' welcome player {name}, {intro}')

x = random.randrange(1,11)
y = int(input("Enter a number"))
if 0 < y <=10:
     if y == x :
        print(f'congratulations ! you won {name}')

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
         
    
        
    
        
          
        

        
        






        
        
