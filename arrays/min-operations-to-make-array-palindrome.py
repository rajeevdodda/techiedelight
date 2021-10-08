# Find the minimum number of merge operations to make an array palindrome

def merge(array: list) -> int:
    i = 0
    j = len(array) - 1
    count = 0
    while i < j:
        if array[i] > array[j]:
            array[j-1] += array[j]
            count += 1
            j -= 1
        elif array[i] < array[j]:
            array[i+1] += array[i]
            i += 1
            count += 1
        else:
            i += 1
            j -= 1
    print(count)



merge([6, 1, 3, 7])
merge( [6, 1, 4, 3, 1, 7])
merge([1, 3, 3, 1])
