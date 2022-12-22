from random_word import RandomWords
import os

from hangman_arts import gameover_logo, hangman_logo, hangman_stages, hangman_lives


clear_terminal = lambda: os.system('clear')

letters_allowed = [
    'A','B','C','D','E',
    'F','G','H','I','J',
    'K','L','M','N','O',
    'P','Q','R','S','T',
    'U','V','W','X','Y','Z'
]

def setup_the_game():

    words = RandomWords()
    random_word = str(words.get_random_word()).upper()

    blank_spaces = ['_' for char in random_word]
    letters = [char for char in random_word]
    indexes = [index for index in range(len(letters))]


    letters_left = len(letters)

    stages = hangman_stages()
    lives = hangman_lives()

    attempts_left = len(hangman_stages())
    lives_left = attempts_left-1

    start_logo = True
    gameover = False

    tried_letters = []
    return random_word, blank_spaces, letters, indexes, letters_left, stages, lives, attempts_left, lives_left, start_logo, gameover, tried_letters


random_word, blank_spaces, letters, indexes, letters_left, stages, lives, attempts_left, lives_left, start_logo, gameover, tried_letters = setup_the_game()


def list_to_string(list_of_chars):
    string = ' '.join(list_of_chars)
    return string

clear_terminal()
while True:
    if start_logo:
        hangman_logo()
    guessed_letter = str(input('Guess a letter: ')).upper()
    start_logo = False
    if guessed_letter not in letters_allowed:
        clear_terminal()
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

    if attempts_left == 0:
        clear_terminal()
        gameover_logo()
        print(f'The word was {random_word}\n')
        play_again = input('Would you like to play again? Type "no" to exit or press enter to play it again. ')
        if play_again == 'no':
            break
        clear_terminal()

        random_word, blank_spaces, letters, indexes, letters_left, stages, lives, attempts_left, lives_left, start_logo, gameover, tried_letters = setup_the_game()

    if '_' not in blank_spaces:
        print('You won!')
        break