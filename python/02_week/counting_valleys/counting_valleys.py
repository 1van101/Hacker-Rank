path_dct = {
    'U': lambda x: x + 1,
    'D': lambda x: x - 1
}

steps = 12
path = list('DDUUDDUDUUUD')

valleys_traversed = 0
sea_level = 0
under_sea_level = False

for step in path:
    sea_level = path_dct[step](sea_level)
    if sea_level < 0:
        under_sea_level = True
        continue

    if under_sea_level:
        under_sea_level = False
        valleys_traversed += 1

print(valleys_traversed)