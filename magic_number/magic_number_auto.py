# 
# guess a number between 1 and 100 << auto version >>
# 

from .utils import generate_random, print_number, print_win
from colorama.ansi import Fore, Style

def guess_number_auto():
    number = generate_random(1,100)
    lower_limit = 1 
    higher_limit = 100
    initial_answer = answer = generate_random(1,100)
    print (f'initial answer: {Fore.YELLOW}{initial_answer}{Style.RESET_ALL}')

    while answer != number:
        if answer > number:
            higher_limit = answer - 1
            answer = generate_random(lower_limit,higher_limit)
            print_number(answer,'lower')        
        if answer < number:
            lower_limit = answer + 1
            answer = generate_random(lower_limit,higher_limit)
            print_number(answer,'higher')
        print('-------------------------------------------')
        
        if answer == number:
            print_win(answer)
            number = generate_random(1,100)
            break



