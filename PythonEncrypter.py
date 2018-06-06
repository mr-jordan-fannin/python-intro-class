"""
Python Encrypter Program
Author: Jordan Fannin
Rev: 2018-Jun-6
Dependencies: Python 3.6.5
"""


import os


def clear_screen():
    """ Clears previous terminal screen. """
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def menu_screen():
    """ Prints main menu screen. """
    print('___________________________________\n'
          '|     Python Encrypter Program    |\\\n'
          '|---------------------------------||\n'
          '|    What would you like to do?   ||\n'
          '| [1] Create a new file.          ||\n'
          '| [2] Encrypt a file.             ||\n'
          '| [3] Decrypt a file.             ||\n'
          '| [4] Exit program.               ||\n'
          '|_________________________________||\n'
          '\\_________________________________\\|\n')


def new_file():
    """ Allows user to make a new text file. """
    clear_screen()
    print('___________________________________\n'
          '|         Create New File         |\n'
          '\---------------------------------/')
    file_name = get_filename('New')
    print('Input text below.\n'
          f'Press Enter to close {file_name}.')
    content = input('> ')
    with open(file_name, 'w') as file:
        file.write(content)
    clear_screen()
    print(f'Your file has been saved as {file_name}.txt.')
    main()


def get_filename(task):
    """ Prompts user for file name and checks validity. """
    while True:
        file = input('\nInput file name or press '
                     'Enter to return to main menu: \n')
        if file == '':
            main()
        file_found = os.path.isfile(file)
        if task == 'New':
            if file_found:
                print(f'{file} already exists.')
            else:
                return file
        else:
            if file_found:
                return file
            else:
                print('File does not exist. Please try again.')


def list_files():
    """ Displays all files in current working directory. """
    files = os.listdir('.')
    print('\n             File List             \n'
          '-----------------------------------')
    for file in files:
        print(file)



def crypt_menu(task):
    """ Dual-purpose file alteration function. """
    while True:
        clear_screen()
        print('___________________________________\n'
              f'|          {task} File           |\n'
              '\---------------------------------/')
        list_files()
        file = get_filename(task)
        key = enter_key(task)
        confirm_target(file, task)
        doc = crypt_file(file, key, task)
        print(f'Target file contents:\n{doc}')
        input(f'{task}ion complete. Press Enter to return to main menu.')


def enter_key(task):
    """ Accepts a hashing key from the user. """
    while True:
        key = int(input(f'Enter {task}ion key or '
                        f'press Enter to go back: '))
        if key != '':
            return key
        if key == '':
            crypt_menu(task)


def confirm_target(file, task):
    """ Confirms the user's intention to perform operation on target file. """
    while True:
        proceed = input(f'{task} {file} now? [y/n] ')
        if proceed == 'y':
            return True
        elif proceed == 'n':
            crypt_menu(task)
        else:
            print('Invalid input. Please try again.')


def crypt_file(file, key, task):
    """ Creates an encrypted or decrypted file from the input file. """
    with open(file, 'r') as source:
        with open(f'{file}_{task}ed', 'w') as destination:
            source_doc = source.read()
            print(f'Source file contents:\n{source_doc}')
            dest_doc = ''
            for old_char in source_doc:
                place = ord(old_char)
                if task == 'Encrypt':
                    place += key
                    if place > 127:
                        place -= 127
                if task == 'Decrypt':
                    place -= key
                    if place < 0:
                        place += 127
                dest_doc += chr(place)
            destination.write(dest_doc)
    return dest_doc


def main():
    """ Main program loop. """
    clear_screen()
    menu_screen()
    while True:
        option = input(' ')
        if option == '1':
            new_file()
        elif option == '2':
            crypt_menu('Encrypt')
        elif option == '3':
            crypt_menu('Decrypt')
        elif option == '4':
            print('Stay sneaky.')
            exit()
        else:
            main()


if __name__ == '__main__':
    main()
