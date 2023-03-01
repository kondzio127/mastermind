import random
import itertools

COLOURS = ['R', 'G', 'Y', 'B', 'W', 'O']
TRIES = 10
COLOUR_LENGTH = 4
COMBINATION_LENGTH = len(COLOURS) ** COLOUR_LENGTH


def generate_secret_code():
    randomised = []
    for i in range(COLOUR_LENGTH):
        colour = random.choice(COLOURS)
        randomised.append(colour)
    return randomised

def check_colours(guess_code, real_code):
    colour_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for colour in real_code:
        if colour not in colour_counts:
            colour_counts[colour] = 0
        colour_counts[colour] += 1

    for guess_colour, real_colour in zip(guess_code, real_code):
        if guess_colour == real_colour:
            correct_pos += 1
            colour_counts[guess_colour] -= 1

    for guess_colour, real_colour in zip(guess_code, real_code):
        if guess_colour in colour_counts:
            if colour_counts[guess_colour] > 0:
                incorrect_pos += 1
                colour_counts[guess_colour] -= 1

    return correct_pos, incorrect_pos


def minimax(combinations):
    # Generate all possible feedback combinations and store them in a list
    all_possible_feedbacks = [(i, j - i) for i in range(5) for j in range(5)]

    print(all_possible_feedbacks)
    best_score = len(combinations)
    print(best_score)
    best_guess = None
    for guess in combinations:
        scores = []
        for feedback in all_possible_feedbacks:
            remaining_codes = [code for code in combinations if check_colours(guess, code) == feedback]
            score = len(remaining_codes)
            scores.append(score)
        guess_score = max(scores)
        if guess_score < best_score:
            best_score = guess_score
            best_guess = guess
    return best_guess


def mastermind_solver():
    combinations = list(itertools.product(COLOURS, repeat=COLOUR_LENGTH))
    secret_code = generate_secret_code()
    print("code =", secret_code)
    guess = minimax(combinations)
    for attempts in range(0, TRIES):
        print(f"Guess {attempts}: {guess}")
        correct_positions, incorrect_positions = check_colours(guess, secret_code)
        if correct_positions == COLOUR_LENGTH:
            print("Secret code found!")
            break
        combinations = [code for code in combinations if check_colours(guess, code) == (correct_positions, incorrect_positions)]
        guess = minimax(combinations)
    else:
        print("You Lose! the code was", *secret_code)


if __name__ == '__main__':
    mastermind_solver()
