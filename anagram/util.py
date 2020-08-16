from itertools import permutations
from PyDictionary import PyDictionary

def dic_words():
    with open('anagram/google-10000-english/google-10000-english.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

def to_str(st):
    s = ""
    for i in st:
        s += i

    st = s
    return s

def solve(ques):
    dictionary=PyDictionary()
    possibilities = list(permutations(ques, len(ques)))
    diction = dic_words()
    solutions = []
    possible = []
    for i in possibilities:
        i = to_str(i)
        if i in diction:
            mean = dictionary.meaning(i)
            syn = dictionary.synonym(i)
            anto = dictionary.antonym(i)

            k = {
                "word": i,
                "meaning": mean,
                "synonym": syn,
                "antonym": anto
            }
            solutions.append(k)
        else:
            possible.append(i)


    result = {
        "possible": possible,
        "solutions": solutions
    }

    return result

def solve2(ques):
    possibilities = list(permutations(ques, len(ques)))
    diction = dic_words()
    solutions = []
    possible = []
    for i in possibilities:
        i = to_str(i)
        if i in diction:
            solutions.append(i)
        else:
            possible.append(i)


    result = {
        "possible": possible,
        "solutions": solutions
    }

    return result
