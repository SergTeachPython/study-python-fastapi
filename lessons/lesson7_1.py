import random

LEVELS = {
    "easy": 1,
    "medium": 2,
    "hard": 3,
}


def get_attempt_number(input_word: str, game_lever: int) -> int | float:
    match game_lever:
        case LEVELS("easy"):
            return let(input_word) * 2
        case LEVELS("medium"):
            return len(input_word) * 1.5
        case LEVELS("hard"):
            return len(input_word) * 1.3
        case _:
            return len(input_word) * 1


words = ["Dog", "Cat", "Helicopter", "Pyton", "Turtle", "Parrot"]
secret_word = random.choice(words)
attempts_counter = 0
allowed_attempts = len(secret_word)

encoded_word_letters = ["-"] * len(secret_word)

#print(encoded_word_letters)

while  True:

    print(" ".join(encoded_word_letters))

    if "".join(encoded_word_letters).lower() == secret_word.lower():
        print(f"You guessed the secret word! Word: {secret_word}\nAttempts: {attempts_counter}.")
        break

    input_text = input("Enter a letter of full word: ").strip().lower()

    attempts_counter += 1

    if len(input_text) == 1:
        if input_text.isalpha() and input_text in secret_word.lower():
            for letter_index in range(len(secret_word)):
                if secret_word[letter_index].lower() == input_text:
                    encoded_word_letters[letter_index] = input_text

    elif input_text == secret_word.lower():
        print(f"You guessed the secret word! Word: {secret_word}\nAttempts: {attempts_counter}.")
        break

    else:
        print("You guessed wrong! Try again.")










