#!/usr/local/bin/python
#hangman!


import os
import time
import random
from rich.console import Console


random.seed()
terminal = Console()


words_list = ['MOUSE', 'TRAIN', 'BICYCLE', 'ENGINE', 'BRIDGE', 'THEATER', 'CHURCH', 'POCKET', 'PRESIDENT', 'PERSON',
              'PRIEST', 'REPORTER', 'HEAVEN', 'WEDDING', 'ELECTION', 'CONTRACT', 'INSTRUMENT', 'BATHROOM', 'GARDEN',
              'CAMERA', 'SHOULDER', 'DISEASE', 'OCEAN', 'BEACH', 'ELECTRIC', 'PROGRAM', 'DIAMOND', 'TEMPERATURE',
              'PATTERN', 'STRAIGHT', 'SUMMER', 'HANGMAN', 'EXPENSIVE', 'SHALLOW', 'FAMOUS', 'BEDROOM', 'MANAGER',
              'SOCCER', 'RUSSIAN', 'NOVEL', 'ICECREAM', 'CREATIVE', 'HOLLYWOOD', 'RETURN', 'RANDOM', 'LOBSTER']



def random_word():
    seed = random.randint(0, len(words_list) - 1)
    return words_list[seed]
    


def draw_hangman(step):
    if step == 1:
        print('''



                                +---+
                                |   |
                                    |
                                    |
                                    |
                                    |
                              =========
        ''')

    elif step == 2:
        print('''



                                +---+
                                |   |
                                o   |
                                    |
                                    |
                                    |
                              =========
        ''')

    elif step == 3:
        print('''



                                +---+
                                |   |
                                o   |
                                |   |
                                    |
                                    |
                              =========
        ''')

    elif step == 4:
        print('''



                                +---+
                                |   |
                                o   |
                               /|   |
                                    |
                                    |
                              =========
        ''')

    elif step == 5:
        print(r'''



                                +---+
                                |   |
                                o   |
                               /|\  |
                                    |
                                    |
                              =========
        ''')

    elif step == 6:
        print(r'''



                                +---+
                                |   |
                                o   |
                               /|\  |
                               /    |
                                    |
                              =========
        ''')

    elif step == 7:
        terminal.print(r'''



                                +---+
                                |   |
                                o   |
                               /|\  |
                               / \  |
                                    |
                              =========
        ''')

    else:
        raise ValueError('wrong arguments. select between 1-7.')



def draw_word(selected_word):
    terminal.print('\n\n\t\t\t    ', end=' ')

    for letter in selected_word:
        terminal.print(letter, end=' ')



def welcome():
    os.system('clear' or 'cls')

    terminal.print(r'''
           _   _   ___   _   _ _____ ___  ___  ___   _   _ 
          | | | | / _ \ | \ | |  __ \|  \/  | / _ \ | \ | |
          | |_| |/ /_\ \|  \| | |  \/| .  . |/ /_\ \|  \| |
          |  _  ||  _  || . ` | | __ | |\/| ||  _  || . ` |
          | | | || | | || |\  | |_\ \| |  | || | | || |\  |
          \_| |_/\_| |_/\_| \_/\____/\_|  |_/\_| |_/\_| \_/
    ''', style='bold green')

    time.sleep(1)
    os.system('clear' or 'cls')

    terminal.print(r'''
           _   _   ___   _   _ _____ ___  ___  ___   _   _ 
          | | | | / _ \ | \ | |  __ \|  \/  | / _ \ | \ | |
          | |_| |/ /_\ \|  \| | |  \/| .  . |/ /_\ \|  \| |
          |  _  ||  _  || . ` | | __ | |\/| ||  _  || . ` |
          | | | || | | || |\  | |_\ \| |  | || | | || |\  |
          \_| |_/\_| |_/\_| \_/\____/\_|  |_/\_| |_/\_| \_/
    ''', style='bold blue')

    time.sleep(1)
    os.system('clear' or 'cls')

    terminal.print(r'''
           _   _   ___   _   _ _____ ___  ___  ___   _   _ 
          | | | | / _ \ | \ | |  __ \|  \/  | / _ \ | \ | |
          | |_| |/ /_\ \|  \| | |  \/| .  . |/ /_\ \|  \| |
          |  _  ||  _  || . ` | | __ | |\/| ||  _  || . ` |
          | | | || | | || |\  | |_\ \| |  | || | | || |\  |
          \_| |_/\_| |_/\_| \_/\____/\_|  |_/\_| |_/\_| \_/
    ''', style='bold red')

    time.sleep(1)



def main():
    print('\x1b[8;22;68t') #set terminal size
    welcome()

    welcome_request = input('\n\n\n\t\t    Are You Ready? (yes/no) : ')
    os.system('clear' or 'cls')

    if welcome_request == 'yes':

        end_value = 0
        lose_value = 1
        word_array = []
        my_word = random_word()

        for letter in range(len(my_word)):
            word_array.append('-')

        del letter
        
        while lose_value <= 7:
            os.system('clear' or 'cls')
            draw_hangman(lose_value)
            draw_word(word_array)

            lose_counter = 0
            guess = input('\n\n\n\t\t\t      Guess : ')

            if guess.upper() == my_word:
                time.sleep(1.5)
                os.system('clear' or 'cls')
                terminal.print(f'\n\n\n\n\n\n\n\n\n<{my_word}>', style='bold magenta', justify='center')
                terminal.print('YOU WIN', style='bold green', justify='center')
                time.sleep(3)
                os.system('clear' or 'cls')
                end_value = 1
                break
            else:
                for _index, letter in enumerate(my_word):
                    if letter == guess.upper():
                        word_array.pop(_index)
                        word_array.insert(_index, letter)
                        lose_counter = 2
                    else:
                        if lose_counter == 2:
                            pass
                        else:
                            lose_counter = 1

                if lose_counter == 1:
                    lose_value += 1


            if word_array.count('-') == 0:
                time.sleep(1.5)
                os.system('clear' or 'cls')
                terminal.print(f'\n\n\n\n\n\n\n\n\n<{my_word}>', style='bold magenta', justify='center')
                terminal.print('YOU WIN', style='bold green', justify='center')
                time.sleep(3)
                os.system('clear' or 'cls')
                end_value = 1
                break

        
        if end_value == 1: ...
        else:
            time.sleep(1.5)
            os.system('clear' or 'cls')
            terminal.print(f'\n\n\n\n\n\n\n\n\n<{my_word}>', style='bold magenta', justify='center')
            terminal.print('YOU LOSE', style='bold red', justify='center')
            time.sleep(3)
            os.system('clear' or 'cls')


    elif welcome_request == 'no': ...
    else: ...


if __name__ == "__main__":
    main()

