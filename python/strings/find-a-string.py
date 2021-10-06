def count_substring(string, sub_str):
    counter = 0
    for i in range(0, len(string)):
        if string[i] == sub_str[0] and string[i:i + len(sub_str)] == sub_str:
            counter += 1
    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
