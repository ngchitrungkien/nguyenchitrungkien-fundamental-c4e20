rabbits = {0: 1, 1: 2}

for i in range (3):
    rabbits[i + 2] = rabbits[i] + rabbits[i + 1]

for key, value in rabbits.items():
    print('Month {}: {} pair(s) of rabbit'.format(key, value))