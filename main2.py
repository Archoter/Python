#12 f
#11 s

class Matrix:
    """dostring"""

    def __init__(self, x, y, matr):
        """Constructor"""
        self.x = x
        self.y = y
        self.matr = matr
        pass


def get_inputX():
    while True:
        try:
            return int(input("X:"))
        except Valueint as exc:
            print("Not int")


def get_inputY():
    while True:
        try:
            return int(input("Y:"))
        except Valueint as exc:
            print("Not int")


def print_output(y):
    print(f"{y}")


def create_matryx(x, y):
    matr = [[1] * y] * x
    return matr


def printmatr(matr, x ,y):
    for i in range(0, x):
        for j in range(0, y):
            print(f"{matr[i][j]} ", end = "")
        print()


def izmenenie(matrx, newY, newX):
    oldX = matrx.x
    oldY = matrx.y
    newmatr = matrx.matr
    x = newX
    y = newY
    print(newmatr)
    if (oldX < x):
        nX = x - oldX
        for i in range(0, nX):
            newmatr.append([0] * x)
            #print(newmatr)
    else:
        nX = oldX - x
        for j in range (1, nX + 1):
            del newmatr[oldX-nX]
            print(newmatr)
    if (oldY < y):
        nY = y - oldY
        for i in range(0, nY):
            #for j in range(0, nX):
            newmatr[i].append(0)
        print(newmatr)
    else:
        nY = oldY - y
        #for i in range(0, oldY):
        for j in range(0, nY):
            del newmatr[j][oldY-j-1]
        print(newmatr)
    matrx.x = x
    matrx.y = y
    matrx.matr = newmatr
    print(newmatr)
    return matrx


def podmatr(matrx, x, y):
    for i in range(0, x):
        for j in range(0, y):
            print(f"{matrx[i][j]} ", end = "")
        print()

    
def main():
    while True:

        print("1. Создание матрицы")
        print("2. Просмотр матрицы")
        print("3. Изменение размерности матрицы")
        print("4. Методы класса")
        print("5. Вывод подматрицы")
        print("0. Выход")

        cmd = input("Выберите пункт: ")
        if cmd == "1":
            x = get_inputX() 
            y = get_inputY() 
            matrx = Matrix(x, y, create_matryx(x, y))
        elif cmd == "2":
            printmatr(matrx.matr, matrx.x, matrx.y)
        elif cmd == "3":
            x = get_inputX() 
            y = get_inputY() 
            matrx = izmenenie(matrx, x, y)
            printmatr(matrx.matr, matrx.x, matrx.y)            
        elif cmd == "4":
            print(dir(matrx))
        elif cmd == "5":
            x = get_inputX() 
            y = get_inputY() 
            podmatr(matrx.matr, x, y)
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")


if __name__ == "__main__":
    main()
