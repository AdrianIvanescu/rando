"""
guess a number between 1 and 100 << binary version >>
"""
from colorama.ansi import Fore
from colorama.ansi import Style

from db_layer.insert_field import save_to_db
from utilsfolder.utils import didWeGuess
from utilsfolder.utils import generate_random
from utilsfolder.utils import print_line
from utilsfolder.utils import print_number
from utilsfolder.utils import print_win


class MagicNumberBinary:
    def __init__(self, lower_limit, higher_limit):
        self.lower_limit = lower_limit
        self.higher_limit = higher_limit

    def guess_number_binary(self):
        number = generate_random(self.lower_limit, self.higher_limit)
        answer = self.higher_limit // 2
        num_of_tries = 0
        print(f"initial answer: {Fore.YELLOW}{answer}{Style.RESET_ALL}")

        if didWeGuess(number, answer):
            num_of_tries += 1
            print_win(answer)
            save_to_db(number, num_of_tries, "auto")

        while answer != number:
            if answer > number:
                self.higher_limit = answer - 1
                answer = (self.lower_limit + self.higher_limit) // 2
                print_number(answer, "lower")
                num_of_tries += 1
                print_line()
            if answer < number:
                self.lower_limit = answer + 1
                answer = (self.lower_limit + self.higher_limit) // 2
                print_number(answer, "higher")
                num_of_tries += 1
                print_line()
           
            if didWeGuess(number, answer):
                print_win(answer)
                save_to_db(number, num_of_tries, "binary")
                break
