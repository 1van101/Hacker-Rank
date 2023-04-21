import collections


def sockMerchant(n, ar):
    socks_colors = {}

    for el in ar:
        if el not in socks_colors:
            socks_colors[el] = 0
        socks_colors[el] += 1

    socks_colors = [value // 2 for value in socks_colors.values() if value > 1]
    return sum(socks_colors)






print(sockMerchant(5, [10, 20, 20, 10, 10, 30, 50, 10, 20]))