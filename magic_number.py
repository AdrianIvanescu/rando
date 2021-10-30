import random
number = random.randint(1,101)
# print(number)

for answer in range(1,100):
    answer = int(input('Guess a number between 1-100: '))
    if answer > number:
        print("Try again. Go lower...")
    if answer < number:
        print("Try again. Go higher...")
    if answer == number:
        print("You win!")
        break
