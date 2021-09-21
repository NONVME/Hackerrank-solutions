from itertools import combinations_with_replacement

word, line = input().split()
result = combinations_with_replacement(sorted(word), int(line))
for i in result:
    print(f"{''.join(i)}")
