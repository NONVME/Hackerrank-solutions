def swap_case(s):
    result = ''
    for i in s:
        result += i.upper() if i.islower() else i.lower()
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
