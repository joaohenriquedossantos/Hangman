from random_word import RandomWords
import os

from hangman_arts import gameover_logo, hangman_logo, hangman_stages, hangman_lives


clear_terminal = lambda: os.system('clear')

stop_the_game = lambda blank_spaces: True if '_' not in blank_spaces else False


words = RandomWords()
random_word = str(words.get_random_word()).upper()

blank_spaces = ['_' for char in random_word]
letters = [char for char in random_word]
indexes = [index for index in range(len(letters))]

letters_allowed = [
    'A','B','C','D','E',
    'F','G','H','I','J',
    'K','L','M','N','O',
    'P','Q','R','S','T',
    'U','V','W','X','Y','Z'
]

letters_letf = len(letters)

stages = hangman_stages()
lives = hangman_lives()

attempts_left = len(hangman_stages())
lives_left = attempts_left-1

tried_letters = []

def list_to_string(list_of_chars):
    string = ' '.join(list_of_chars)
    return string

clear_terminal()
while not attempts_left == 0:
    guessed_letter = str(input('Guess a letter: ')).upper()
    if guessed_letter not in letters_allowed:
        print(f'Sorry, "{guessed_letter}" is not allowed.')
    else:
        if guessed_letter not in tried_letters:
            tried_letters.append(guessed_letter)
            for index in indexes:
                if guessed_letter == letters[index]:
                    blank_spaces[index] = guessed_letter
            if guessed_letter not in letters:
                clear_terminal()
                print(f'''You've guessed "{guessed_letter}", that's not in the word. You lose a life."''')
                attempts_left -= 1
                lives_left -= 1
                print(f'\nLives left: {lives[lives_left]}')
                print(stages[attempts_left])
                display = list_to_string(blank_spaces)
                print(display)
            else:
                clear_terminal()
                print(f'\nLives left: {lives[lives_left]}')
                if attempts_left < len(hangman_stages()):
                    print(stages[attempts_left])

                display = list_to_string(blank_spaces)
                print(display)
        else:
            print(f'''You've already guessed "{guessed_letter}"''')