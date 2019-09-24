## Control Flow - If statements

# COntrols wher the code result is going to go
#depending on the result of the evaluations that return True or False, it runs a block of code or not


# Syntax

# if <condition>:
    # block
# elif <condition>:
    #block
    # do stuff
# else:
    # block


# weather = 'rainy and stormy and snowie' # have the most specific condition at the top
#
# if weather == 'rainy':
#     print('take an umbrella')
# elif weather == 'Snowie':
#     print('where boots and a scarf')
# else:
#     print('take shades')

# age = int(input('What is your age? '))
# driver_licence = bool(input('Do you have a drivers license? '))
# # - You can vote and drive
# # - You can vote
# # - You can drive
# # - You can't legally drink but your mates/uncle might hav your back (bigger 16)
# # - Your're too young, go back to school!
#
# if age >= 18 and driver_licence is True:
#     print('You can vote and drive and drink')
# elif 17 <= age <= 18 and driver_licence is True:
#     print('you cant legally drink but your mates/uncle might have your back', 'But you can drive')
# else:
#     print ("Your're too young, go back to school!")

# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg, General viewing, but some scenes may be unsuitable for young children
  ## 12, Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15, No one younger than 15 may see a 15 film in a cinema.
  ## 18, No one younger than 18 may see an 18 film in a cinema.

rating = input('What is the rating of the movie? ').lower().strip()
if rating == 'universal':
    print('Everyone can watch')
elif rating == 'PG':
    print('PG: General viewing but some scenes may be unsuitable for you children')
elif rating == '12A':
    print('12A: 12, Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12' )
elif rating == '15':
    print('No one younger than 15 may see a 15 film in a cinema.')
elif rating == '18':
    print('No one younger than 18 may see an 18 film in a cinema.')
else:
    print('Unable to determine rating')