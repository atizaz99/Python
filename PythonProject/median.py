def median_of_number(a):
    a.sort()
    if len(a)%2 == 0:
        return (a[len(a)//2 - 1] + a[len(a)//2])/2
    else:
        return a[len(a)//2]

lst = [34, 67, 89, 45, 89]
print(median_of_number(lst))