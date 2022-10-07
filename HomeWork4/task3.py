def nonrepeat(lst):
    el = {}
    for i in lst:
        el[i] = el.get(i, 0) + 1
    
    nonrepeatLst = []
    for key, val in el.items():
        if val == 1:
            nonrepeatLst.append(key)
    return nonrepeatLst

myList = [1, 2, 2, 3, 4, 5, 6, 6, 7, 4, 8, 9, 7]
print(" ".join(map(str, nonrepeat(myList))))

    