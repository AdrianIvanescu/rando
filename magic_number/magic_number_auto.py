'''
guess a number between 1 and 100 << auto version >>
'''


from utilsfolder.utils import generate_random, print_number, print_win, print_line, didWeGuess
from colorama.ansi import Fore, Style
from db_layer.insert_field import save_to_db

class MagicNumberAuto:
    def __init__(self,lower_limit,higher_limit):
        self.lower_limit = lower_limit
        self.higher_limit = higher_limit
    
    def guess_number_auto(self):
        number = generate_random(self.lower_limit,self.higher_limit)
        initial_answer = answer = generate_random(self.lower_limit,self.higher_limit)
        num_of_tries = 0
        print (f'initial answer: {Fore.YELLOW}{initial_answer}{Style.RESET_ALL}')

        if didWeGuess(number,answer):
            num_of_tries += 1
            print_win(answer)
            save_to_db(number, num_of_tries,'auto')
        
        while answer != number:
            if answer > number:
                self.higher_limit = answer - 1
                answer = generate_random(self.lower_limit,self.higher_limit)
                print_number(answer,'lower')
                num_of_tries += 1
                print_line()        
            if answer < number:
                self.lower_limit = answer + 1
                answer = generate_random(self.lower_limit,self.higher_limit)
                print_number(answer,'higher')
                num_of_tries += 1
                print_line()
            
            if didWeGuess(number,answer):
                print_win(answer)
                save_to_db(number, num_of_tries,'auto')
                break
