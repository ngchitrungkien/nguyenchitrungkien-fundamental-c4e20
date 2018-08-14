from random import randint
def is_inside(point, rect):
    if point[0] >= rect[0]:
        return True

    elif point[1] >= rect[1]:
        return True

    elif point[0] <= rect[0] + rect[2]:
        return True

    elif point[1] <= rect[1] + rect[3]:
        return True

    else:
        return False