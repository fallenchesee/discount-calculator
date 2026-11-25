def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Возвращает итоговую цену товара с учётом скидки.

    :param price: исходная цена товара (>= 0)
    :param discount_percent: процент скидки (0 <= discount_percent <= 100)
    :return: итоговая цена
    :raises ValueError: при некорректных входных данных
    :raises TypeError: при нечисловых аргументах
    """
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        raise TypeError("price должно быть числом")
    if not isinstance(discount_percent, (int, float)) or isinstance(discount_percent, bool):
        raise TypeError("discount_percent должно быть числом")

    if price < 0:
        raise ValueError("Цена не может быть отрицательной")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100%")

    return round(price * (1 - discount_percent / 100), 2)