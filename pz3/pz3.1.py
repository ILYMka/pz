def is_point_in_fourth_quadrant(x, y):
    """Проверяет, лежит ли точка (x, y) в четвертой координатной четверти. """
    return x > 0 > y


if __name__ == "__main__":
    x = float(input("Введите координату x: "))
    y = float(input("Введите координату y: "))

    if is_point_in_fourth_quadrant(x, y):
        print("Точка лежит в четвертой координатной четверти. ")
    else:
        print("Точка не лежит в четвертой координатной четверти. ")
