import string


def counting_sort(array):
    letter_count = dict.fromkeys(string.ascii_lowercase, 0)
    for ch in array:
        letter_count[ch] += 1
    return ''.join([(c + ' ') * letter_count[c] for c in string.ascii_lowercase if letter_count[c] > 0])


file = open("input.txt", "r")
line = file.readline()
array = [ch for ch in line.split(' ') if 'a' <= ch <= 'z']
file.close()

file = open("output.txt", "w")
file.write(counting_sort(array))
file.close()
