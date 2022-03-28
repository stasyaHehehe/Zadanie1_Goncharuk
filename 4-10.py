name = input("Введите имя: ")
age = input("Введите возраст: ")
print("Привет,", name, ", тебе действительно", age, "? А ты неплохо выглядишь для такого-то возраста!")


age = int(input("Введите возраст:"))
if age < 18:
    print("На второй год ещё не оставляли?")
else:
    print("Как дела с суставами? Кажется, я слышу скрип")


name = "Анастасия"
print(name[1: -1])
print(name[::-1])
print(name[-3::])
print(name[0:5])


name = "Анастасия"
print(len(name))

age = int("18")
s = 0
t = 1
while age > 0:
    n = age % 10
    s = s + n
    t = t * n
    age = age // 10
print(s, t)


name = "АНАСТАСИЯ"
name2 = str.capitalize(name)
name3 = str.casefold(name)
print(name2, name3)


while True:
   name = input("Введите ваше имя: ")
   if not name.isalpha() ==True:
       print("Введено некоректно!")
   else:
        print ("Спасибо!")
        break

while True:
    age= input("Введите возраст: ")
    if not age.isnumeric():
        print("Вы ввели не число. ")
    elif not 0 <= int(age) <= 150:
        print("Вам не может быть столько лет. ")
    else:
        print("Спасибо!")
        break


z = 7
while True:
    z = (input("Сколько будет 2x+5=2(x=6) ?"))
if not z.isnumeric():
    print("Вы ввели не числовое значение!")
elif not int(z) != 7
    print("Правильный ответ. Молодец!")
else:
    print("Стоит попробовать еще раз...")
    break
