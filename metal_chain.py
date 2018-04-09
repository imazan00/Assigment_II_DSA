def count_of_augment_operations(length, part, min_sum, arr):
    count = 0

    mid_ind = length // 2 - part // 2
    current_sum = sum(arr[mid_ind: mid_ind + part])
    next_ind = 0

    while 0 <= mid_ind <= length - part:
        if current_sum < min_sum and not next_ind:
            for last_i in range(mid_ind, mid_ind + part):
                old = arr[last_i]
                arr[last_i] *= min_sum * 2
                current_sum += arr[last_i] - old

            if current_sum < min_sum:
                return -1

            count += 1
            next_ind = 2 * part - 2
            next_ind = min(next_ind, length - part - mid_ind - 1)
        elif next_ind:
            next_ind -= 1

        if mid_ind + 1 <= length - part:
            current_sum -= arr[mid_ind]
            current_sum += arr[mid_ind + part]
        mid_ind += 1

    mid_ind = length // 2 - part // 2
    current_sum = sum(arr[mid_ind: mid_ind + part])
    next_ind = 0

    while 0 <= mid_ind <= length - part:
        if current_sum < min_sum and not next_ind:
            for last_i in range(mid_ind, mid_ind + part):
                old = arr[last_i]
                arr[last_i] *= min_sum * 2
                current_sum += arr[last_i] - old

            if current_sum < min_sum:
                return -1

            count += 1
            next_ind = 2 * part - 2
        elif next_ind:
            next_ind -= 1

        if mid_ind >= 0:
            current_sum -= arr[mid_ind + part - 1]
            current_sum += arr[mid_ind - 1]
        mid_ind -= 1

    return count


file = open("input.txt", "r")
data = [int(num) for num in file.readline().split(' ')]
array = [int(num) for num in file.readline().split(' ')]
file.close()

file = open("output.txt", "w")
file.write(str(count_of_augment_operations(data[0], data[1], data[2], array)))
# print(count_of_augment_operations(data[0], data[1], data[2], array))
file.close()
