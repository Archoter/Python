def get_inputX():
    while True:
        try:
            return int(input("Элемент первого кортежа под номером:"))
        except Valuefloat as exc:
            print("Not int")


def get_inputS():
    while True:
        try:
            return int(input("Номер студента:"))
        except Valueint as exc:
            print("Not int")


def print_output(y):
    print(f"{y}")


def obeed(a, b):
    return a + b


def srez(c):
    return c[15:38]


def main():
    a = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
    b = ('Баравлев','Баранов','Боодей',
         'Васильчиков','Деркачёв','Дубровин',
         'Жигалин','Злобин','Казаков',
         'Канаев','Катетунов','Косарев',
         'Куликов','Ли','Осетров',
         'Радченко','Рукавченко','Савков',
         'Семёнов','Сергин','Тупейко',
         'Туралин','Федоров','Янчаускас',
         'Кусков')
    while True:
        print("1. Просмотр студента под номером")
        print("2. Вывод объединения кортежей")
        print("3. Просмотр первого кортежа")
        print("4. Срез затрагивающий оба кортежа")
        print("0. Выход")
        cmd = input("Выберите пункт: ")
        if cmd == "1":
            print_output(b[get_inputS()])
        elif cmd == "2":
            c = obeed(a, b)
            print_output(c)
        elif cmd == "3":
            print_output(a[get_inputX()])
        elif cmd == "4":
            c = obeed(a, b)
            z = srez(c)
            print_output(z)
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")


if __name__ == "__main__":
    main()
