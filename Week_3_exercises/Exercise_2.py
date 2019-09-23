# I want you to use operators
# Equate somrthing

# As a user. I want to be able to guess a number and know if I got it correct or not. So that i can know if i have won money

## 1) I need to assign a number to the magic number
## 2) I need to ask user for input.
## 3) I need to check if this input matches the magic number
## 4) I need to let the user know if the response was right or not

magic_number = 7

user_num_guess = int(input('Pick a number, any number! '))

print('Your guess was ... ', str(user_num_guess == magic_number), '!')
