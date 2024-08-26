def find_ints(text):
    words = text.split()
    results = []
    for i, word in enumerate(words):
        word_cut_off = word.lstrip("+").lstrip("-")
        if word_cut_off.isdigit():
            results.append(i + 1)
    return results


def contains_diamonds(board):
    for row in board:
        if "d" in row:
            return True
    return False


def make_you_mine(board):
    diamonds = 0
    while True:
        user_input = input("where mine?")
        x, y = user_input.split()
        x = int(x)
        y = int(y)

        board_item = board[x][y]
        if board_item == "e":
            print("Empty!")
        elif board_item == "b":
            print("BOMB!! GAME OVER")
            break
        else:
            diamonds += 1
            print("Found Diamond")
            board[x][y] = "e"
            if not contains_diamonds(board):
                print("You WON!! Congratulations")
                break


def any_palindrome(words):
    for word in words:
        if word == word[::-1]:
            return True
    return False
