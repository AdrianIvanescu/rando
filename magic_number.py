import random
from colorama.ansi import Fore, Style

def generate_random(min, max) -> int:
    return random.randint(min,max)

number = generate_random(1,100)
# print(f'>>The magic number is: {Fore.GREEN}{number}{Style.RESET_ALL}')
# print('-------------------------------------------')

def guess_number_user():
    for answer in range(1,100):
        answer = int(input('Guess a number between 1-100: '))
        if answer > number:
            print("Try again. Go lower...")
        if answer < number:
            print("Try again. Go higher...")
        if answer == number:
            print(f">>You win! The magic number is: {Fore.GREEN}{answer}{Style.RESET_ALL}")
            break

# not working as expected:
def guess_number_auto():
    initial_answer = answer = generate_random(1,100)
    print (f'initial answer: {initial_answer}')
    answer_set  = set()
    
    while answer != number:
        answer_set.add(answer)
        if answer > number:
            answer = generate_random(1,answer-1)
            if answer in answer_set:
                answer = generate_random(1,answer-1)
            answer_set.add(answer)
            print(f"Try again. Go lower... revised answer: {answer}")
        
        if answer < number:
            answer = generate_random(answer+1,100)
            if answer in answer_set:
                answer = generate_random(answer+1,100)
            answer_set.add(answer)
            print(f"Try again. Go higher... revised answer: {answer}")
        
        if answer == number:
            print(f">>You win! The mugic number is: {answer}")
            break

def print_limit(lower_limit,higher_limit):
    print (f'>>lower_limit: {lower_limit}')
    print (f'>>higher_limit: {higher_limit}')

def guess_number_auto_v2():
    lower_limit = 1
    higher_limit = 100
    initial_answer = answer = generate_random(1,100)
    print (f'initial answer: {Fore.YELLOW}{initial_answer}{Style.RESET_ALL}')

    while answer != number:
        if answer > number:
            higher_limit = answer - 1
            answer = generate_random(lower_limit,higher_limit)
            print(f"Try again. Go lower... revised answer: {Fore.RED}{answer}{Style.RESET_ALL}")
            # print_limit(lower_limit,higher_limit)
        
        if answer < number:
            lower_limit = answer + 1
            answer = generate_random(lower_limit,higher_limit)
            print(f"Try again. Go higher... revised answer: {Fore.RED}{answer}{Style.RESET_ALL}")
            # print_limit(lower_limit,higher_limit)
        
        print('-------------------------------------------')
        
        if answer == number:
            print(f">>You win! The magic number is: {Fore.GREEN}{answer}{Style.RESET_ALL}")
            break

# guess_number_user()
guess_number_auto_v2()


