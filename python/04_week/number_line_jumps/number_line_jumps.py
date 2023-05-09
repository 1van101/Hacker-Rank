def kangaroo(x1, v1, x2, v2):
    loc_diff = x2 - x1
    jumps_diff = v2 - v1

    if jumps_diff > 0 and loc_diff % jumps_diff == 0:
        return 'YES'
    else:
        return 'NO'
print(kangaroo(0, 2, 5, 3))