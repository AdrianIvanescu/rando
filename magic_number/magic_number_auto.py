# 
# guess a number between 1 and 100 << auto version >>
# 
import random
from colorama.ansi import Fore, Style

from shell import MyPrompt

def generate_random(min, max) -> int:
    return random.randint(min,max)

number = generate_random(1,100)

def print_limit(lower_limit,higher_limit):
    print (f'>>lower_limit: {lower_limit}')
    print (f'>>higher_limit: {higher_limit}')

def print_number(number,limit):
    print(f"Try again. Go {limit}... revised answer: {Fore.RED}{number}{Style.RESET_ALL}")

def print_win(number):
    print(f">>You win! The magic number is: {Fore.GREEN}{number}{Style.RESET_ALL}")

def guess_number_auto():
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
            break

def main():
    MyPrompt().cmdloop()

