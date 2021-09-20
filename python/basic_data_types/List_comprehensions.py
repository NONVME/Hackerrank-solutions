if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([x for x in [[xs, ys, zs] for xs in range(x + 1) for ys in range(y + 1) for zs in range(z + 1)] if sum(x) != n])
