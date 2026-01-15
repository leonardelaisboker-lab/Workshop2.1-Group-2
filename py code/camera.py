import coinFliping


def readCoinSide():
    side = coinFliping.coin_side
    print(f"📷 camera reads: {side}")

    # Import local to avoid circular dependency

    return side
