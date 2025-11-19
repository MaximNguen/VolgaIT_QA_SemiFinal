def first_task():
    a = [2025, 3, 11]
    import itertools
    permutations = list(itertools.permutations(a))
    return str(permutations)

def second_task():
    a =  [1, 3, 6, 7, 9, 4, 10, 5, 6, 12, 2, 7, 11]
    res = []
    for i in range(len(a)):
        for j in range(i, len(a) - 1):
            if a[j] < a[j+1]:
                continue
            else:
                res.append(a[i:j+1])
                break

    res.sort()
    return res[0]

def third_task():
    s1 = 'aabbdsaacc'
    s2 = "abadc"
    result = 0
    i = 0

    while s2 != "":
        if s1[i] in s2[0]:
            result += 1
            s2 = s2[1:]
            i+=1
        elif len(s2) > 1 and s1[i] in s2[1]:
            result += 1
            s2 = s2[2:]
            i+=1
        else:
            i+=1

    return str(result)