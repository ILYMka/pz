def can_form_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def main():
    try:
        a, b, c = map(int, input("Введите длины сторон a, b и c через пробел: ").split())
    except ValueError:
        print("Ошибка: введите целые числа. ")
        return

    if can_form_triangle(a, b, c):
        print("Существует треугольник со сторонами a, b и c. ")
    else:
        print("Треугольник со сторонами a, b и c не существует. ")


if __name__ == "__main__":
    main()
