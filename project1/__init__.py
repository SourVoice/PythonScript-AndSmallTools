import string

guess_girl = input("input a age possibly be an age:")
if str.isdigit(guess_girl):
    print('right input')
else:
    print('error input!')

if guess_girl == 25:
    print('!!!')
