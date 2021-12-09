# 
# guess a number between 1 and 100 << user input version >>
# 
from .utils import generate_random, print_win
from colorama.ansi import Fore, Style

def guess_number_user():
    number = generate_random(1,100)
    for answer in range(1,100):
        answer = int(input('Guess a number between 1-100: '))
        if answer > number:
            print("Try again. Go lower...")
        if answer < number:
            print("Try again. Go higher...")
        if answer == number:
            print_win(answer)
            number = generate_random(1,100)
            break

