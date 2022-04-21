# num = int(input())
# while num <= 5:
#     print("Вы ввели число больше 4")
#     num = int(input())
# print("Вы ввели число меньше 5")


login = input("Введите логин: ")
password = input("Введите пароль: ")
password_check = input("Подтвердите пароль: ")
for i in range(3):
    if password == password_check:
        print("Регистрация успешна")
        print("Заходите на наш сайт!")
    else:
        print("Не совпадение паролей. Попробуйте ещё раз")
        password_check = input("Подтвердите пароль: ")
if password != password_check:
    print("Попробуйте проверить изначально введенный пароль")
