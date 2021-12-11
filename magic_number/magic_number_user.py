'''
guess a number between 1 and 100 << user input version >>
'''
from utilsfolder.utils  import generate_random, print_win, didWeGuess
from colorama.ansi import Fore, Style

def isBounded(answer) -> bool:
    if (answer > 0 and answer < 101):
        return True
class MagicNumberUser:
    def __init__(self,lower_limit,higher_limit):
        self.lower_limit = lower_limit
        self.higher_limit = higher_limit

    def guess_number_user(self):
        answer_int = 0
        number = int(generate_random(self.lower_limit,self.higher_limit))
        while (not didWeGuess(number,answer_int)):
            answer = input('Guess a number between 1-100 (or q to quit): ')
            if answer == 'q':
                break   
            try:
                answer_int = int(answer)
                if (not isBounded(answer_int)):
                    print ('>> input between [1..100]')
            except ValueError as e:
                print('>> this should be an integer')            
            
            if ( answer_int > number and isBounded(answer_int) and isinstance(answer_int,int)):
                print("Try again. Go lower...")
            if ( answer_int < number and isBounded(answer_int) and isinstance(answer_int,int)):
                print("Try again. Go higher...")
            if didWeGuess(number,answer_int):
                print_win(answer_int)
                break