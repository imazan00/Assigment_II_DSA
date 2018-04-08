def count_pin_codes(n):
    connected = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4],
                 0: [4, 6]}
    count = {}
    for number in range(10):
        count[number] = 1

    for j in range(n - 1):
        new_count = {}
        for key in count:
            sum_of_counts = 0
            for val in connected[key]:
                sum_of_counts += count[val]
            new_count[key] = sum_of_counts
        count = new_count

    combinations = 0
    for key in count:
        combinations += count[key]
    return combinations


file = open("input.txt", "r")
num = int(file.readline())
file.close()

file = open("output.txt", "w")
file.write(str(count_pin_codes(num)))
file.close()
