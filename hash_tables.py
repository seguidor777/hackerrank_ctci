import hashlib
from operator import itemgetter

table = [None] * 30000

def gen_index(word):
    return hash(word) % 30000

def get_word_index(index, word):
    words = list(map(itemgetter(0), table[index]))
    try:
        return words.index(word)
    except ValueError:
        return -1

def populate_table(words):
    for word in words:
        index = gen_index(word)
        if isinstance(table[index], list):
            word_index = get_word_index(index, word)
            if word_index >= 0:
                table[index][word_index][1] += 1
            else:
                table[index].append([word, 1])
        else:
            table[index] = [[word, 1]]

def find_words(words):
    for word in words:
        index = gen_index(word)
        if isinstance(table[index], list):
            word_index = get_word_index(index, word)
            if word_index == -1 or table[index][word_index][1] == 0:
                return False
            else:
                table[index][word_index][1] -= 1
    return True

def ransom_note(magazine, ransom):
    populate_table(magazine)
    return find_words(ransom)

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)

if(answer):
    print("Yes")
else:
    print("No")
    

