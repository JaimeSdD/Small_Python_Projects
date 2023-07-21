import random
import os
from hangman_words import word_list
from hangman_words_spanish import words_list_spanish
from hangman_art import stages, logo

print(logo)

language = input(
    "What language do you want the word to be in? Type 'es' for Spanish or 'eng' for English: "
)

if language == "es":
    filtered_spanish_list = [word for word in words_list_spanish if len(word) > 3]
    chosen_word = random.choice(filtered_spanish_list)
elif language == "eng":
    chosen_word = random.choice(word_list)
else:
    print("That's not a valid input. Try 'es' or 'eng'")

end_of_game = False
lives = 6


display = []
for _ in chosen_word:
    display.append(" _ ")
print("\n")
print("".join(display))
print("\n")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system("cls")

    if f" {guess} " in display:
        print(f"You've already guess {guess}, try again")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = f" {letter.upper()} "

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's wrong. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose, the word was: {chosen_word.upper()}")

    print("".join(display))

    if " _ " not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])
