# The game POP AND TOC!
# Multiples of 3's are POP
# multiples of 5's are TOC
# Multiples of 3 and 5 are POP TOC

# As a user I should be ask for a number,
# So i can play the game with my input
# As a player i should see the game counting up to my number and substituting the multiples of 3 and 5 with the appropriate vales
# So i can see if it is working.
# As a player, I should be able to exit the game using a key word so that i can stop.

user_input1 = input('Would you like to play?')
while user_input1 != 'exit':
    counter = 0
    user_input2 = int((input('What number would you like sir or madam? ')))
    while counter < user_input2:
        counter += 1
        if counter%3 == 0 and counter%5 == 0:
            print('POPTOC!')
        elif counter%3 == 0:
            print('POP!')
        elif counter%5 == 0:
            print('TOC!')
        else:
            print(counter)

    user_input1 = input('Would you like to play?')
