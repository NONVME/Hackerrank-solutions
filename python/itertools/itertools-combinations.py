from itertools import combinations

string, number = input().split()
for i in range(1, int(number) + 1):
    print(*[''.join(x) for x in list(combinations(sorted(string), int(i)))], sep='\n')
