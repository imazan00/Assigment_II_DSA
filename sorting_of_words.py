import string


def sort_by_character(arr, ind, length):
    possible_characters = ' ' + string.ascii_lowercase
    letter_count = dict.fromkeys(possible_characters, [])
    for word in arr:
        char = word[length - ind - 1]
        letter_count[char] = letter_count[char] + [word]
    return [w for ch in possible_characters for w in letter_count[ch]]


def radix_sort(arr):
    max_len = len(max(arr, key=len))
    arr = [str(word) + (' ' * (max_len - len(word))) for word in arr]
    for ind in range(max_len):
        arr = sort_by_character(arr, ind, max_len)
    return ''.join([word.replace(' ', '') + ' ' for word in arr])


file = open("input.txt", "r")
line = file.readline()
array = [word for word in line.split(' ')]
file.close()

file = open("output.txt", "w")
print(radix_sort(array))
file.write(radix_sort(array))
file.close()
