import random

# Variable save side of the coin
coin_side = None  # "heads" o "tails"


def flipCoinRandom():
    global coin_side
    coin_side = random.choice(["heads", "tails"])
    print("🎲 Coin flipped →", coin_side)
