COINS = (50, 25, 10, 5, 2, 1)


def coin_change(money: int) -> int:
    if money == 0:
        return 0
    for coin in COINS:
        coin_count = money // coin
        if coin_count != 0:
            return coin_count + coin_change(money % coin)


assert coin_change(252) == 6
assert coin_change(5) == 1
assert coin_change(58) == 4
assert coin_change(42) == 4
