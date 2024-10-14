def max_in_list(l):
    """ This function returns the maximum value in the list l. """
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0], max_in_list(l[1:]))


def mystery(x):
    if len(x) == 1:
        return x[0]
    else:
        y = mystery(x[1:])
        if x[0] > y:
            return x[0]
        else:
            return y


def mistero(x):
    a = len(x)
    if a == 1:
        return x[0]
    else:
        y = mistero(x[:a // 2])
        z = mistero(x[a // 2:])
        if z > y:
            return z
        else:
            return y


def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)


def can_make_change(amount, coins):
    # base case: success
    if amount == 0:
        return True

    # base case: failure
    if amount < 0 or len(coins) == 0:
        return False

    # recursive case: handle two possibilities, either:
    # 1. another of this coin value gets used, or
    # 2. we don't need another coin of this value
    coin = coins[-1]
    return (can_make_change(amount - coin, coins)
            or can_make_change(amount, coins[:-1]))

>> > flatten_list([[0, 1], 2, [3, 4, [5, 6, [7], 8]]])
[0, 1, 2, 3, 4, 5, 6, 7, 8]

products = []
for type in ["laptop", "desktop", "tablet"]:
    for color in ["red", "green", "blue"]:
        for storage in ["128GB", "256GB", "512GB"]:
            for price in ["$100", "$200", "$300"]:
                products.append(f"{color} {storage} {type} {price}")
