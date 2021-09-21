quantity_numbers = input()
numbers = list(map(int, input().split()))
print(bool(all([x > 0 for x in numbers]) and list(filter(lambda x: str(x) == str(x)[::-1], numbers))))
