import random
from operator import contains

colors = ["R","G","B","Y","W","O"]
tries = 10
code_len = 4

def generate_code():
    code = []
    for _ in range(code_len):
        color = random.choice(colors)
        code.append(color)
    return code

def Guess_code():

    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != 4:
            print(f"You must guess {code_len} colors.")
            continue

        for color in guess:
            if color not in colors:
                print(f"Invalid Color: {color}. Try again")
                break
        else:
            break

    return guess

def check_code(guess,real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos,incorrect_pos
def game():
    print(f"Welcome to the Mind_Game. You have {tries} to Guess the Code...")
    print("The Valid colors are",colors)

    code = generate_code()
    for attempts in range(1,tries + 1):
        guess = Guess_code()
        correct_pos, incorrect_pos =check_code(guess,code)
        if correct_pos == code_len:
            print(f"You guessed the code in {attempts} tries.")
            break

        print(f"Correct Positions: {correct_pos}| incorrect Positions: {incorrect_pos}")

    else:
        print("you ran out of tries, the code was: ",code)

game()