def print_formatted(number):
    lenth = number.bit_length()
    for i in range(1, number + 1):
        print(f'{i:{lenth}d} {i:{lenth}o} {i:{lenth}X} {i:{lenth}b}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
