import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo

print(logo)
# Testing code
print(f"Solution is {chosen_word}.")

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Enter a letter: ").lower()

    if guess in display:
        print(f"You already guessed the letter{guess}")

    # check the letter you guessed
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # checks whether the user has guessed the letter or not
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word, you lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost.")

    print(f"{' '.join(display)}")

    # checks if the user has guessed all the letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_art import stages

    print(stages[lives])