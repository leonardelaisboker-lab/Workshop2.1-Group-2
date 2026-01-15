import time

import camara2
import camera
import coinFliping

# state of the coin
coin_in_origin = True


# Here we analyze whether the coin is at the point of origin
def coinOriginPosition():
    global coin_in_origin

    if coin_in_origin:
        print("🪙 Coin is in the origin position.")
        return True
    else:
        print("❌ Coin is NOT in the origin position.")

        # read coin side (camera 1)
        camera.readCoinSide()

        # detect coin position (camera 2)
        camara2.detectCoinPosition()

        return False


def FlipTheCoin():
    global coin_in_origin
    print("🎲 start flip coin")

    # call fliping function
    coinFliping.flipCoinRandom()

    # the coin is no longer in origin position
    coin_in_origin = False


def coinToOrigin():
    global coin_in_origin

    # print al principio con el estado de la cara
    print(f"📷 Coin side detected: {coinFliping.coin_side}")

    print("🔄 returning coin to origin position")
    coin_in_origin = True


while True:
    if coinOriginPosition():
        FlipTheCoin()
    time.sleep(
        5
    )  # wait 5 seconds before the next check, u can delete the time an call from terminal maybe
