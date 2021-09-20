if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    max_val = max(arr)
    while max(arr) == max_val:
        arr.remove(max_val)
        if max_val not in arr:
            print(max(arr))
