def mode_of_number(list1):
    frequency = {}
    for i in list1:
        frequency.setdefault(i, 0)
        frequency[i]+=1

    frequent = max(frequency.values())
    for i, j in frequency.items():
        if j == frequent:
            mode = i
    return mode

l = [1, 5, 3, 6, 3, 9, 0, 9]
print(mode_of_number(l))  # Output: 3
    
