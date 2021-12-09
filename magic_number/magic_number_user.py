# 
# guess a number between 1 and 100 << user input version >>
# 
import random
from colorama.ansi import Fore, Style

def generate_random(min, max) -> int:
    return random.randint(min,max)

def print_win(number):
    print(f">>You win! The magic number is: {Fore.GREEN}{number}{Style.RESET_ALL}")    

number = generate_random(1,100)

def guess_number_user():
    for answer in range(1,100):
        answer = int(input('Guess a number between 1-100: '))
        if answer > number:
            print("Try again. Go lower...")
        if answer < number:
            print("Try again. Go higher...")
        if answer == number:
            print_win(answer)
            break

