import itertools


def is_anagram(s1, s2):
    s1_anagrams = itertools.permutations(s1, len(s1))
    print(tuple(s2))
    if tuple(s2) in s1_anagrams:
        return True
    return False


print(is_anagram("astronomer", "moonstarer"))
