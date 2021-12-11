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
        number = int(generate_random(self.lower_limit,self.higher_limit))
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
            if didWeGuess(number,answer):
                print_win(answer)
                break