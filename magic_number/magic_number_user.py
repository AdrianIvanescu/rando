# 
# guess a number between 1 and 100 << user input version >>
# 
from .utils import generate_random, print_win
from colorama.ansi import Fore, Style

def isBounded(answer) -> bool:
    if (answer > 0 and answer < 101):
        return True

def guess_number_user():
    number = int(generate_random(1,100))
    for answer in range(1,100):
        try:
            answer = int(input('Guess a number between 1-100: '))
            if (not isBounded(answer)):
                print ('>> input between [1..100]')
        except ValueError as e:
            print('>> this should be an integer')
        if ( answer > number and isBounded(answer) and isinstance(answer,int)):
            print("Try again. Go lower...")
        if ( answer < number and isBounded(answer) and isinstance(answer,int)):
            print("Try again. Go higher...")
        if ( answer == number and isBounded(answer) and isinstance(answer,int)):
            print_win(answer)
            number = generate_random(1,100)
            break