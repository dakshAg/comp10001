import itertools

aussie_animals = ["Possum", "Echidna", "Emu", "Koala", "Platypus", "Wombat"]
for key, group in itertools.groupby(sorted(aussie_animals), lambda x: x[0]):
    print(key, list(group))
