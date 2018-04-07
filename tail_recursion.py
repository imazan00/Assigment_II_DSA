def partition(arr, begin, end):
    pivot = arr[end]
    ind = begin - 1
    for j in range(begin, end):
        if arr[j] <= pivot:
            ind += 1
            arr[ind], arr[j] = arr[j], arr[ind]
    arr[ind + 1], arr[end] = arr[end], arr[ind + 1]
    return ind + 1


def tail_recursive_quicksort(arr, begin, end):
    while begin < end:
        part = partition(arr, begin, end)
        tail_recursive_quicksort(arr, begin, part - 1)
        begin = part + 1
    return ''.join(str(num) + ' ' for num in arr)


file = open("input.txt", "r")
line = file.readline()
array = [int(num) for num in line.split(' ')]
file.close()

file = open("output.txt", "w")
file.write(tail_recursive_quicksort(array, 0, len(array) - 1))
file.close()
