# год рождения А.С Пушкина

from bornyear import bornyear


def bornyearforewer():
    while True:
        year = bornyear()
        if year == "Верно":
            print(year)
            break
        else:
            print(year)
            print("\n\nПопробуй снова\n\n")


if __name__ == "__main__":
    bornyearforewer()