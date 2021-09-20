if __name__ == '__main__':
    list_of_names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_of_names.append([name, score])
    second_score = sorted(list({x[1] for x in list_of_names}))[1]
    names_for_score = [x for x in list_of_names if second_score in x]
    result = [x[0] for x in names_for_score]
    result.sort()
    for i in result:
        print(i)
