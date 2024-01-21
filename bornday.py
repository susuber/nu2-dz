# день рождения А.С Пушкина

def bornday() -> str:
    try:
        year = int(input("Введите год рождения Пушкина: "))
    except ValueError:
        return "Вы ввели не число"

    if year != 1799:
        return "Неверный год рождения"

    try:
        month = int(input("Введите месяц рождения Пушкина: "))
        if month > 12:
            return "Неверный ввод"
        day = int(input("Введите день рождения Пушкина: "))
        if day > 31:
            return "Неверный ввод"
    except ValueError:
        return "Вы ввели не число"

    if month > 12 or day > 31:
        return "Неверный ввод"

    if month == 6 and day == 6:
        return "Верно"
    else:
        return "Неверный день рождения"


if __name__ == '__main__':
    print(bornday())
