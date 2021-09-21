from itertools import permutations

string, number = input().split()
print(*[''.join(x) for x in list(permutations(sorted(string), int(number)))], sep='\n')
