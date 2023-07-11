balance = 1000
user_name = "Andrei"
is_active = True
friends = ["Timofey", "Grigorii", "Nikita", "Konstantin"]

balance = balance - 500
print(balance)

print(user_name.upper())

if is_active:
    print("Пользователь активен")

    for friend in friends:
        print(friend)
else:
    print("Пользователь неактивен")


def my_print(user_name: str) -> None:
    print("Функция my_print")
    print(user_name.upper())


my_print(user_name)
