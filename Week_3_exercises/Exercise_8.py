## Stupid School Teacher
#Create a program to have a conversation with your teacher. This is how he reacts to your responses
# if you responde to your school teacher:
    # Go back to school!
# if you ask a questions
    # HAHAHA! AHAHAHAHHA!! OMG! WHAT a silly question! Go back TO SCHOOL!
# if your respond with something ending with !
    # YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!
# if your response is 'I'm a doctor'
    # WELLL DONE! YOU can now talk to me
    # Exits
teacher_says = input('teacher says:')
my_response = ''

while my_response.strip().lower() != "I'm a Doctor".strip().lower():

    my_response = input('Guess what?')
    if '?' in my_response:
        print('HAHAHA! AHAHAHAHHA!! OMG! WHAT a silly question! Go back TO SCHOOL!')
    elif '!' in my_response:
        print('YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!')

    elif type(my_response) == str and my_response != "I'm a doctor".strip().lower() and '?'not in my_response and '!' not in  my_response:
        print('Go back to school!')
else:
    print('Well done! Now you can talk to me!')


