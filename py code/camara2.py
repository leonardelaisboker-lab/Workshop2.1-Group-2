import random

# Stores the last detected position of the coin (x, y)
# Example: (2.3, -1.1)
coin_position = None


def detectCoinPosition():
    """
    Simulates a camera detecting the coin position in space.
    Generates random (x, y) coordinates and stores them
    as the current coin position.
    """
    global coin_position

    # Simulated workspace limits (can be adjusted later)
    x = round(random.uniform(-5.0, 5.0), 2)
    y = round(random.uniform(-5.0, 5.0), 2)

    # Save detected position
    coin_position = (x, y)

    print(f"📍 camara2 detected coin position → x={x}, y={y}")
    import coin_flip

    coin_flip.coinToOrigin()
    return coin_position


def getCoinPosition():
    """
    Returns the last detected coin position.
    If the coin has not been detected yet, returns None.
    """

    return coin_position
