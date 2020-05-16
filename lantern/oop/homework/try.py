def _reduce_saturation_level(value):
    saturation_level = 50
    print(saturation_level - value)


def run(hours):
    distance = 6 * hours
    if distance <= 25:
        _reduce_saturation_level(2)
    elif 25 < distance <= 50:
        _reduce_saturation_level(5)
    elif 50 < distance <= 100:
        _reduce_saturation_level(15)
    elif 100 < distance <= 200:
        _reduce_saturation_level(25)
    elif distance > 200:
        _reduce_saturation_level(50)
    print(f"Your cat run {distance} km")

run(50)
