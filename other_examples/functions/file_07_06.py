# arguments | args - Позиционные аргументы
# keyword arguments | kwargs Именованные аргументы


def validate(data: dict):
    if "login" not in data:
        raise ValueError("Укажите логин")

    if "password" not in data:
        raise ValueError("Укажите пароль")

    return data


def frontend(*args, **kwargs):
    # print(f'ARGS: {args} {type(args)}')
    # print(f'KWARGS: {kwargs} {type(kwargs)}')

    data: dict = validate(kwargs)
    return data


def backend(validated_data: dict) -> str:
    validate(validated_data)

    user_login: str | None = validated_data.get("login", None)
    user_password: str | None = validated_data.get("password", None)
    last_name: str = validated_data.get("last_name", "")

    # if user_login == db.user_login:
    #     pass
    #
    # if user_password == db.user_password:
    #     pass

    result: str = f'Login: {user_login} Password: {user_password}'

    if last_name:
        result += f' Last Name: {last_name}'

    return result


if __name__ == "__main__":
    data_front = frontend(
        "abba", [10, 20], True, None,
        login="test_user",
        password="MyStrongPass123"
    )

    data_front_2 = frontend(
        "abba", [10, 20], True, None,
        login="ivan",
        password="Bestpass123",
        last_name="Ivanov"
    )

    print(backend(data_front))
    print(backend(data_front_2))
