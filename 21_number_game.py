import random

'''
21, Bagram, or Twenty plus one is a game which progresses by counting up 1 to 21, with the player who calls “21” is eliminated.

The game illustrated here is between the player and the computer. There can be many variations in the game.
    The player can choose to start first or second.
    The list of numbers is shown before the Player takes his turn so that it becomes convenient.
    If consecutive numbers are not given in input then the player is automatically disqualified.
    The player loses if he gets the chance to call 21 and wins otherwise.
    Rule: player can count up to 3 numbers each time.


???? Winning against the computer can be possible by choosing to play second. (design this way, could be more random in real life)
computer always try to reach the near multiple.
allowed numbers to count: 1~3
The strategy is to call numbers till the multiple of 4 which would eventually lead to 21 on computer hence making the player the winner. 
'''
# 难点：how does computer count the numbers?

# My improvements:
# 1. check for valid inputs (Eg. inputs that contain non-integers)
# 2. computer randomly counts 1-3 numbers if plays first
# >> 3. combine 'enter number of input from user' with 'enter the user inputs'


def nearestMultiple(num):
    if num > 4:
        near = num + (4-(num%4))
    else: 
        near = 4
    return near


# lose and end the program
def lose():
    print('\nYOU LOSE!')
    print('Better luck next time!')
    exit(0) ## why have this


# check whether the numbers are consecutive
def check(xyz):
    for i in range(len(xyz)-1):
        if xyz[i+1] != xyz[i]+1:
            return False
    return True


# starts the game
def start():
    xyz = [] # a list to store the numbers count
    last = 0
    while True: 
        print("Enter 'F' to take the first chance")
        print("Enter 'S' to take the second chance")
        chance = input ('> ').upper()

        # player takes the first chance
        if chance == 'F':
            while True: 
                if last == 20: 
                    lose()
                else: 
                    print('\n Your Turn.')
                   
                    while True:
                        try: 
                            print('How many numbers do you wish to enter? (Max: 3)')
                            inp = int(input('> '))
                            # check the user counts right amt of numbers
                            if inp > 0 and inp <= 3: 
                                comp = 4 - inp
                                break
                            else:
                                print('Wrong input. You are disqualified from the game.')
                                lose()                                                               
                        except ValueError: 
                            print('Please enter numbers')                    

                    i, j = 1, 1
                    print('Please enter the values')
                    while i <= inp:
                        try: 
                            a = int(input('> '))
                            xyz.append(a)
                            i += 1
                        except ValueError: 
                            print('Please enter numbers')
                    
                    #update last
                    last = xyz[-1]

                    # check whether the input numbers are consecutive
                    if not check(xyz):
                        print('\nYou did not input consecutive integers.')
                        lose()
                    else:
                        if last == 21:
                            lose()
                        
                        # computer's turn
                        else: 
                            while j <= comp:
                                xyz.append(last+j)
                                j += 1
                            print("Order of inputs after computer's turn is: ")
                            print(xyz)
                            last = xyz[-1]
        
        # player takes the second chance
        elif chance == "S":
            # computer randomly give 1-3 when take the first chance
            comp = random.randint(1, 3)
            last = 0
            while last < 20:
                # computer's turn
                j = 1
                while j <= comp:
                    xyz.append(last+j)
                    j += 1
                print("Order of inputs after computer's turn is: ")
                print(xyz)
                
                last = xyz[-1]
                if last == 20:
                    lose()
                else:
                    print('\n Your Turn.')

                    while True:
                        try: 
                            print('How many numbers do you wish to enter? (Max: 3)')
                            inp = int(input('> '))                           
                            # check the user counts right amt of numbers
                            if inp < 0 and inp > 3: 
                                print('Wrong input. You are disqualified from the game.')
                                lose()
                            else:
                                break
                        except ValueError: 
                            print('Please enter numbers')
                    
                    i = 1
                    print('Please enter the values')
                    while i <= inp:                        
                        try: 
                            xyz.append(int(input('> ')))
                            i += 1
                        except ValueError: 
                            print('Please enter numbers')
                    
                    if check(xyz):
                        near = nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        print("\nYou did not input consecutive numbers.")
                        lose()
            print("\nCONGRATULATIONS!!")
            print("YOU WON!!")
            exit()
        else:
            print("Wrong choice")



# run the game
while True:
    print("Do you want to play the 21 number game with computer?(Yes/No)")
    print("Rule: You can count at most 3 number each turn.")
    print("Reminder: Please enter consecutive numbers or you'll be disqualified and lose.")
    ans = input('> ').lower()
    if ans == "yes":
        start()
    else:
        print('Do you want to quit the game? (Yes/No)')
        num = input("> ").lower()
        if num == "yes":
            print('You are quitting the game...')
            exit()
        elif num == "no":
            print('Continuing...')
        else:
            print('Wrong choice')