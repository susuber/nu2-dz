# год рождения А.С Пушкина

def bornyear():
    try:
        year = int(input("Введите год рождения Пушкина: "))
    except ValueError:
        return "Вы ввели не число"
    else:
        if year == 1799:
            return "Верно"
        else:
            return "Неверно"



if __name__ == '__main__':
    print(bornyear())