def get_parent(index):
    if index > 0:
        return int((index - 1) / 2)
    elif index == 0:
        return 0


def insert_value(heap, value):
    heap.append(value)
    if len(heap) > 1:
        index = len(heap) - 1
        parent = get_parent(index)
        while value < heap[parent]:
            heap[index], heap[parent] = heap[parent], heap[index]
            index = get_parent(index)
            parent = get_parent(index)


def build_heap(arr):
    heap = []
    for value in arr:
        insert_value(heap, value)
    return ''.join([str(val) + ' ' for val in heap])


file = open("input.txt", "r")
line = file.readline()
array = [int(num) for num in line.split(' ')]
file.close()

file = open("output.txt", "w")
file.write(build_heap(array) + '\n')
file.write(build_heap(array[::-1]))
file.close()
