# 각 알파벳으로 만들 수 있는 길이 5 단어
# permutations?
from itertools import product
def solution(word):
    word_list = []
    dictionary = []
    for i in range(1, 6):
        word_list.append(list(product(['A', 'E', 'I', 'O', 'U'], repeat=i)))
    
    for words in word_list:
        for w in words:
            dictionary.append("".join(w))
    dictionary = sorted(set(dictionary))
    
    return dictionary.index(word) + 1