def find_max_k(N):
    # Проверяем,что N больше 1
    if N <= 1:
        print("N должно быть больше 1.")
        return

    # Инициализируем переменные.
    K = 0
    current_sum = 0

    # Находим K, увеличивая его до тех пор, пока сумма не станет больше или равна N
    while current_sum < N:
        K += 1
        current_sum += K

    # Выводим результат
    print("Наибольшее K:", K)
    print("Сумма от 1 до K:", current_sum)


# Пример использования функции.

N = 15
find_max_k(N)
