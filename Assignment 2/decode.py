from __future__ import division
import re
from collections import Counter

ciphertext = re.sub('', '', open("ciphertext.txt").read().rstrip().lower())

freq_table = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
                'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
actual_table = dict([('a', 8.167), ('b', 1.492), ('c', 2.782), ('d', 4.253), ('e', 12.702), ('f', 2.228), ('g', 2.105), ('h', 6.094), ('i', 6.966),
                        ('j', 0.153), ('k', 0.772), ('l', 4.025), ('m', 2.406), ('n', 6.749), ('o', 7.507), ('p', 1.929), ('q', 0.095), ('r', 5.987),
                        ('s', 6.327), ('t', 9.056), ('u', 2.758), ('v', 0.978), ('w', 2.360), ('x', 0.150), ('y', 1.974), ('z', 0.074)])
top_cipher = []
top_english = []
def get_table(word):
    for letter in word:
        freq_table[letter] += 1
    length = len(word)
    for i in freq_table.keys():
        freq_table[i] = (freq_table[i] / length) * 100
get_table(ciphertext.replace(" ", ""))

def print_tables():
    fmt = '{:<8}{:<13}{}'
    print(fmt.format('', 'Actual', 'Encoded'))
    for i in range(0,26):
        print(fmt.format(chr(i+97), actual_table[chr(i+97)], "%.3f") % freq_table[chr(i+97)])

def most_common():
    print "Most common in ciphertext:"
    for k, v in Counter(freq_table).most_common(5):
        print '%s: %.2f' % (k, v)
        top_cipher.append(k)

    print "Most common in English:"
    for k, v in Counter(actual_table).most_common(5):
        print '%s: %.2f' % (k, v)
        top_english.append(k)

def least_common():
    print "Least common in ciphertext:"
    for k, v in Counter(freq_table).most_common()[:-4:-1]:
        print '%s: %.2f' % (k, v)

    print "Least common in English:"
    for k, v in Counter(actual_table).most_common()[:-4:-1]:
        print '%s: %.2f' % (k, v)

def replace_top3():
    return ciphertext.replace(top_cipher[0], top_english[0].upper()).replace(top_cipher[1], top_english[1].upper()).replace(top_cipher[2], top_english[2].upper())

def top_bigrams():
    top = Counter(zip(*[ciphertext.replace(" ", "")[i:] for i in range(2)])).most_common(3)
    print "Top bigrams:"
    print top

def top_trigrams():
    top = Counter(zip(*[ciphertext.replace(" ", "")[i:] for i in range(3)])).most_common(3)
    print "Top trigrams:"
    print top

def decode(ciphertext):
    key = [line.rstrip('\n') for line in open("key.txt")]
    for i in range(0,26):
        ciphertext = ciphertext.replace(chr(i+97), key[i])
    with open("plaintext.txt", "w") as f:
        f.write(ciphertext)

def recover_key():
    key = [line.rstrip('\n') for line in open("key.txt")]
    print key
    with open("key.txt", "w") as f:
        for i in range(0,26):
            f.write(str(chr(key.index(chr(i+97).upper()) + 97)).upper() + "\n")

# Check frequency tables
print_tables()
# Most common patterns in ciphertext and in English
most_common()
top_bigrams()
top_trigrams()
# print replace_top3(). Automatically replacing the top matches is not correct in this case
# Apply key from key.txt to ciphertext
decode(ciphertext)
# And finally
recover_key()
