# 
# guess a number between 1 and 100 << auto version >>
# 

from utilsfolder.utils import generate_random, print_number, print_win, print_line
from colorama.ansi import Fore, Style

class MagicNumberAuto:
    def __init__(self,lower_limit,higher_limit):
        self.lower_limit = lower_limit
        self.higher_limit = higher_limit

    def guess_number_auto(self):
        number = generate_random(self.lower_limit,self.higher_limit)
        answer = generate_random(self.lower_limit,self.higher_limit)
        print (f'initial answer: {Fore.YELLOW}{answer}{Style.RESET_ALL}')

        while answer != number:
            if answer > number:
                self.higher_limit = answer - 1
                answer = generate_random(self.lower_limit,self.higher_limit)
                print_number(answer,'lower')
                print_line()        
            if answer < number:
                self.lower_limit = answer + 1
                answer = generate_random(self.lower_limit,self.higher_limit)
                print_number(answer,'higher')
                print_line()
            
            if answer == number:
                print_win(answer)
                break



