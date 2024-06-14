def has_all_ingredients(curr_drink_recipe) -> bool:
    """Определяет, в наличии имеются ли все ингредиенты.

    Принимает рецепты текущего напитка и проверяет
    по базе, если какой-то ингредиент не хватает
    возвращает False, в противном случае True.

    :param curr_drink_recipe: Рецепт текущего напитка.
    :return: True если все в наличии, иначе False.
    """
    global in_stock

    for ingredient in curr_drink_recipe:
        if in_stock.get(ingredient) - curr_drink_recipe.get(ingredient) < 0:
            return False
    return True


def order(*args):
    global in_stock
    # Меню и рецепт каждого напитка.
    menu: dict[str, dict] = {
        "Эспрессо": {
            "coffee": 1,
        },
        "Капучино": {
            "coffee": 1,
            "milk": 3,
        },
        "Макиато": {
            "coffee": 2,
            "milk": 1,
        },
        "Кофе по-венски": {
            "coffee": 1,
            "cream": 2,
        },
        "Латте Макиато": {
            "coffee": 1,
            "milk": 2,
            "cream": 1,
        },
        "Кон Панна": {
            "coffee": 1,
            "cream": 1,
        },
    }

    # Нужно понять, был ли успешно выполненный заказ.
    has_order: bool = False

    for drink in args:
        ingredients = menu.get(drink)
        if not has_all_ingredients(ingredients):
            continue

        # Если до этой строчки дошли, значит есть хотя бы один заказ.
        has_order = True

        for ingredient in ingredients:
            available_quantity: int = in_stock.get(ingredient)
            required_quantity: int = ingredients.get(ingredient)
            in_stock[ingredient] = available_quantity - required_quantity

        return drink

    # Если не было ни одного успешного заказа
    if not has_order:
        return "К сожалению, не можем предложить Вам напиток"


if __name__ == "__main__":
    in_stock = {"coffee": 0, "milk": 0, "cream": 0}
    print(order("Капучино", "Макиато", "Эспрессо"))
    print(order("Капучино", "Макиато", "Эспрессо"))
    print(order("Капучино", "Макиато", "Эспрессо"))

    # Пример словаря
    product: dict = {
        "id": 10,
        "title": "Товар",
        "favorites": 18843,
        "reviews": {
            1: {
                "user_id": 464783457,
                "text": "Отзыв от пользователя 1",
            },
            2: {
                "user_id": 89656,
                "text": "Отзыв от пользователя 2",
            },
        }

    }
