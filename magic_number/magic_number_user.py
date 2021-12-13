"""
guess a number between 1 and 100 << user input version >>
"""
from db_layer.insert_field import save_to_db
from utilsfolder.utils import didWeGuess
from utilsfolder.utils import generate_random
from utilsfolder.utils import print_win


def isBounded(answer) -> bool:
    if answer > 0 and answer < 101:
        return True


class MagicNumberUser:
    def __init__(self, lower_limit, higher_limit):
        self.lower_limit = lower_limit
        self.higher_limit = higher_limit

    def guess_number_user(self):
        int_answer = 0
        num_of_tries = 1
        number = int(generate_random(self.lower_limit, self.higher_limit))
        while not didWeGuess(number, int_answer):
            answer = input("Guess a number between 1-100 (or q to quit): ")
            if answer == "q":
                break
            try:
                int_answer = int(answer)
                if not isBounded(int_answer):
                    print(">> input between [1..100]")
            except ValueError:
                print(">> this should be an integer")

            if (
                int_answer > number
                and isBounded(int_answer)
                and isinstance(int_answer, int)
            ):
                print("Try again. Go lower...")
                num_of_tries += 1
            if (
                int_answer < number
                and isBounded(int_answer)
                and isinstance(int_answer, int)
            ):
                print("Try again. Go higher...")
                num_of_tries += 1
            if didWeGuess(number, int_answer):
                print_win(int_answer)
                save_to_db(number, num_of_tries, "user")
                break
