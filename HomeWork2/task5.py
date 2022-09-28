from random import randrange as r

def mix_list(list):
    new_list = []
    for _ in range(len(list)):
        i = r(len(list))
        new_list.append(list[i])
        del list[i]
    return new_list

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = mix_list(nums)
print(nums)