def validate(string):
    result = []
    result.append(True) if [x for x in string if x.isalnum()] else result.append(False)
    result.append(True) if [x for x in string if x.isalpha()] else result.append(False)
    result.append(True) if [x for x in string if x.isdigit()] else result.append(False)
    result.append(True) if [x for x in string if x.islower()] else result.append(False)
    result.append(True) if [x for x in string if x.isupper()] else result.append(False)
    return result


if __name__ == '__main__':
    # s = input()
    s = 'qA2'
    print(*validate(s), sep='\n')
