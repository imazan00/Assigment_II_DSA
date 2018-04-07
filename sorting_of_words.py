import string


def counting_sort(arr, ind):
    letter_count = dict.fromkeys(string.ascii_lowercase, 0)
    letter_count[' '] = 0
    for word in arr:
        letter_count[word[ind]] += 1
    return [(w + ' ') * letter_count[w[ind]] for w in arr if letter_count[w[ind]] > 0]


def radix_sort(arr):
    max_len = len(max(arr, key=len))
    arr = [str(word) + (' ' * (max_len - len(word))) for word in arr]
    for it in range(max_len):
        counting_sort(arr, it)
    return ''.join(word.replace(' ', '') + ' ' for word in arr)


file = open("input.txt", "r")
line = file.readline()
array = [word for word in line.split(' ')]
file.close()

file = open("output.txt", "w")
file.write(radix_sort(array))
file.close()
