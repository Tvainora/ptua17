def puzzle_pieces(a, b):
    if len(a) != len(b):
        return False

    sums = []
    for i in range(len(a)):
        sums.append(a[i] + b[i])

    if len(set(sums)) == 1:
        return True
    else:
        return False