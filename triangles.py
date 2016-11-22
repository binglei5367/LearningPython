def triangles():
    L = [1]
    yield L
    while True:
        L = [1] + [L[i] +L[i + 1] for i in range(len(L) - 1)] + [1]
        yield L