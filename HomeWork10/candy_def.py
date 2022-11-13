import random

def chek_candy(answer, n):
    num = answer
    if num.isdigit():
        num = int(num)
    else:
        return False
    if num >= n:
        return num
    else:
        return False


def chek_nums(answer, candy, take):
    num = answer
    if num.isdigit():
        num = int(num)
    else:
        return False
    if num > candy:
        return False
    if num <= 0:
        return False
    if num > take:
        return False
    return num

def howmuch(candy, take):
    import random
    if take >= candy:
        return candy
    num = candy % (take + 1)
    if num > 0:
        return num
    return random.randint(1, take)