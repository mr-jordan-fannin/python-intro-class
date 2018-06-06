'''ReadInts.py by Jordan Fannin. 5-29-18.'''


def main():
    int_array = []
    try:
        with open('integers.txt') as file:
            for line in file:
                int_array.append(line)
    except FileNotFoundError:
        print('The file "integers.txt" does not exist.')
        exit()
    finally:
        total = 0
        for number in int_array:
            total += int(number)
            print(number.rstrip())
        average = total / len(int_array)
        print('Total:', total)
        print('Average:', average)


if __name__ == '__main__':
    main()