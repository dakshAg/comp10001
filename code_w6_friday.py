def find_ints(text):
    """This function finds the indices of the
    words that are integers in a given text"""

    words = text.split()
    result = []

    for i, word in enumerate(words):
        if word[0] == "+" or word[0] == "-":
            word = word[1:]
        if word.isdigit():
            result.append(i + 1)

    return result


def any_palindrome(words):
    """This function checks if the list of
    words contain a palindrome"""

    # This is a comment
    for word in words:
        if word == word[::-1]:
            return True
    return False


def contains_diamonds(board):
    for row in board:
        if "d" in row:
            return True
    return False
def make_you_mine(board):
    """
    Game Minesweeper Simplified
    """
    num_diamonds = 0
    while True:
        u = input("Where mine?")
        coords = u.split()
        x, y = coords
        x = int(x)
        y = int(y)

        item = board[x][y]
        if item == "e":
            continue
        elif item == "b":
            print("GAME OVER")
            break
        else:
            num_diamonds += 1
            print("You mined", num_diamonds, "diamonds")
            board[x][y] = "e"
            if not contains_diamonds(board):
                print("YOU WIN", num_diamonds)
                break
