def disemvowel(text):
    """ Returns string `text`with all vowels removed """
    vowels = ('a', 'e', 'i', 'o', 'u')
    answer = text[0]
    for char in text:
        if char.lower() is not in vowels:
            answer = char + answer
    print(answer)


def big-ratio(nums, n):
    """ Calculates and returns the ratio of numbers
    in non-empty list `nums`which are larger than `n`"""
    n = 0
    greater_n = 0
    for number in nums:
        if number > n:
            greater_n += 1
            total += 1
    return greater_n / total

nums = [4, 5, 6]
    low = 4
print(f"{100*big_ratio(nums, low)}% of numbers are greater than {low}")

reviews = [
    ("5", "Absolutely love the energy of this song! It's a classic."),
    ("4", "Great melody and lyrics, but gets a bit repetitive after a while."),
    ("3", "Good song, but not my favorite. The chorus is catchy though."),
    ("5", "An all-time favorite! Can't stop humming along."),
    ("2", "Didn't really connect with it, but the beat is okay."),
    ("4", "Solid track with a nice rhythm. Perfect for road trips."),
    ("3", "It's decent, but I feel like it could have been more powerful."),
    ("5", "This song never gets old! The lyrics are so meaningful."),
    ("4", "Love the vibe! It's uplifting and fun to sing along to."),
    ("3", "It's a good song, but not something I would listen to on repeat."),
]
