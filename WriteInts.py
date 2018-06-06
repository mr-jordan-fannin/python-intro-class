'''WriteInts.py by Jordan Fannin. 5-29-18.'''


def main():
    print('Please enter 10 integers.')
    int_array = []
    with open('integers.txt', 'w') as file:
        for entry in range(10):
            try:
                number = int(input('Enter a number: '))
                int_array.append(number)
                file.write(str(number) + '\n')
                print(number, 'has been entered into the file.')
            except ValueError:
                print('Try again.')
                entry -= 1


if __name__ == '__main__':
    main()