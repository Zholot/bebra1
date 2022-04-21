login = input("Введите логин: ")
password = input("Введите пароль: ")
password_check = input("Подтвердите пароль: ")
if password == password_check:
    for i in password:
        if i in "@#%!&":
            print("Использован запрещённый символ (@#%!&)")
        else:
            print("Регистрация успешна")
else:
    print("Пароли не совпадают")
print("Заходите на наш сайт!")


text = input()
for i in text:
    print(text)
#
# for i in range(10):
#     print(i)
# print("Done")

print(3)