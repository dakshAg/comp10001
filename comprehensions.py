import itertools


def anagram(word1, word2):
    for p in itertools.permutations(word1):
        if "".join(p) == word2:
            return True
    return False


print(anagram("astroner", "moonstarer"))
