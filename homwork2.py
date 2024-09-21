a = [5,3,6,37,5455,63546,546,456,56,7]
def InsertionSort(a):
    for i in range(1, len(a)):
        b = a[i]
        c = i - 1

        while c >= 0 and b > a[c]:
            a[c+1] = a[c]
            c -= 1
        a[c+1] = b
    
print('Unsorted: ', a)
InsertionSort(a)
print('Sorted: ', a)
