from itertools import groupby

word = input()
result = [(len(list(g)), int(k)) for k, g in groupby(word)]
print(" ".join(map(str, result)))
