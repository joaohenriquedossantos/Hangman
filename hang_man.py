from random_word import RandomWords
import os

from hangman_arts import gameover_logo, hangman_logo, hangman


clear = lambda: os.system('clear')

stop_the_game = lambda blank_spaces: True if '_' not in blank_spaces else False


words = RandomWords()
random_word = str(words.get_random_word()).upper()

blank_spaces = ['_' for char in random_word]
word_letters = [char for char in random_word]
letters_indexes = [index for index in range(len(word_letters))]

letters_letf = len(word_letters)

display = ''
hangman_life = -1
letters_tried = []

clear()
while True:
    guessed_is_wrong = []
    hangman_logo()
    letter_guessed = input('Guess a letter: ').upper()
    if letter_guessed not in letters_tried:
        display = ''
        letters_tried.append(letter_guessed)
        for index in letters_indexes:
            if letter_guessed == word_letters[index]:
                blank_spaces[index] = letter_guessed
                guessed_is_wrong.append(False)
            else:
                guessed_is_wrong.append(True)
    

        for letters in blank_spaces:
            display += letters + ' '

        clear()

        if stop_the_game(blank_spaces):
            break
        
        if False not in guessed_is_wrong:
            hangman_life += 1
            print(hangman(hangman_life))
        
        else:
            if hangman_life >= 0:
                print(hangman(hangman_life))

        if hangman_life == 6:
            print(hangman_life)
            clear()
            gameover_logo()
            print(f'The word was: {random_word} \n')
            break

        print(display + '\n')
        print(f'Guessed letters: {letters_tried}')
    else:
        clear()
        if hangman_life >= 0:
            clear()
            print(hangman(hangman_life))
        print(display + '\n')
        print(f'Guessed letters: {letters_tried}')