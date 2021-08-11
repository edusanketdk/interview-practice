def coin_game(n):
    return "First Player wins the game" if n%6 == 1 else "Second Player wins the game"

"""
the first player wins only when n = 6*m + 1
"""