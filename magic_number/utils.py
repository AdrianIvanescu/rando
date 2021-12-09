import random
from colorama.ansi import Fore, Style

def generate_random(min, max) -> int:
    return random.randint(min,max)

def print_limit(lower_limit,higher_limit):
    print (f'>>lower_limit: {lower_limit}')
    print (f'>>higher_limit: {higher_limit}')

def print_number(number,limit):
    print(f"Try again. Go {limit}... revised answer: {Fore.RED}{number}{Style.RESET_ALL}")

def print_win(number):
    print(f">>You win! The magic number is: {Fore.GREEN}{number}{Style.RESET_ALL}")

