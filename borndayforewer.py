# день рождения А.С Пушкина

from bornday import bornday

def borndayforewer():
    while True:
        born_day = bornday()
        if born_day == "Верно":
            print(born_day)
            break
        else:
            print(born_day)
            print("\n\nПопробуй снова\n\n")


if __name__ == "__main__":
    borndayforewer()