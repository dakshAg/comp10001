history = [
    [('Haskell Heroine', 'defend', 'Recursion Rebuff', 2, 0), ('Python Pal', 'item', 'Screen Repair Kit')],
    [('Linux Legend', 'attack', 'Root Reckoning', 4, 2, 5, ['Haskell Heroine', 'Python Pal']),
     ('Binary Bot', 'item', 'Debugging Tool')],
    [('Haskell Heroine', 'attack', 'Lambda Lunge', 3, 1, 0, ['Linux Legend']),
     ('Python Pal', 'item', 'RAM Boost')],
    [('Linux Legend', 'attack', 'Kernel Kick', 4, 1, 3, ['Python Pal']),
     ('Binary Bot', 'swap', 'Network Ninja')]
]
calculate_comprpg_stats(history, "example_game1_stats.csv")
