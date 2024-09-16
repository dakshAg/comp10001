def big_ratio(nums, n):
    """ Calculates and returns the ratio of numbers
    in non-empty list `nums`which are larger than `n`"""
    greater_n = 0
    total = 0
    for number in nums:
        if number > n:
            greater_n += 1
        total += 1
    return greater_n / total


nums = [1, 2, 3, 4, 5, 6]
low = 4
print(f"{100 * big_ratio(nums, low)}% of numbers are greater than {low}")
