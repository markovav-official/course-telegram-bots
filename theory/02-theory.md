## **Теория**

### **Действия с переменными**

В `python` можно складывать, вычитать, умножать и делить числа:

```python
balance = balance + 500
balance = balance - 100
balance = balance * 2
balance = balance / 3
```

> Как вы видите, в этом примере в переменную `balance` мы кладем результат операции её самой и числа. Мы можем позволить себе такую конструкцию, так как сначала вычисляется значение выражения справа (`balance + 500`) и потом кладется в переменную `balance`. Это работает аналогично для других операциий и типов переменных.

В `python` можно применять функции к переменным.

Например, следующая программа выведет на экран имя пользователя в верхнем регистре:
```python
user_name = "Andrei"
print(user_name.upper())
```

Вывод:

```shell
ANDREI
```

### **Условный оператор `if`**

В `python` есть условный оператор `if`. Он позволяет выполнять различные действия в зависимости от истинности или ложности переданного ему логического выражения. Этим выражением может быть переменная типа `bool`, проверка на равенство двух переменных, проверка на принадлежность элемента к списку и т.д.

И также есть оператор `else`, который позволяет выполнить действия, если условие в `if` не выполнилось.

Например, следующая программа выведет на экран статус пользователя:
```python
is_active = True

if is_active:
    print("Пользователь активен")
else:
    print("Пользователь неактивен")
```

```shell
Пользователь активен
```
И, наоборот
```python
is_active = False

if is_active:
    print("Пользователь активен")
else:
    print("Пользователь неактивен")
```

```
Пользователь неактивен
```

> Сейчас и в дальнейшем, обращайте внимание на отступы в коде. Они очень важны в `python`. Отступы позволяют понять, какие конструкции вложены в другие. Например, в нашем примере, конструкция `print("Пользователь активен")` вложена в конструкцию `if is_active:`. Стандартный отступ в `python` - 4 пробела. Или один таб в современных редакторах кода (таком как `Visual Studio Code` которым мы пользуемся)
>
> Помимо этого, обратите внимание на двоеточие после условия `if is_active:` Оно означает что сейчас будет блок кода с отступом.

### **Цикл `for`**

В `python` есть цикл `for`. Он позволяет выполнять действия для каждого элемента списка.

Например, следующая программа выведет на экран всех друзей пользователя:

```python
friends = ["Timofey", "Grigorii", "Nikita", "Konstantin"]

for friend in friends:
    print(friend)
```

### **Вложенные конструкции**

В `python` можно вкладывать одни конструкции в другие. Например, в цикл `for` можно вложить условный оператор `if`.

Например, следующая программа выведет на экран всех друзей пользователя, если пользователь активен, иначе выведет сообщение о неактивности пользователя:

```python
is_active = True
friends = ["Timofey", "Grigorii", "Nikita", "Konstantin"]

if is_active:
    print("Друзья пользователя:")
    
    for friend in friends:
        print(friend)
else:
    print("Пользователь неактивен")
```

### **Функции**

В `python` есть функции. Они позволяют выполнять набор действий, которые можно вызывать из других мест программы.

Мы уже рассказывали вам про функцию `print`, которая выводит на экран переданные ей аргументы. Однако, в `python` есть и другие функции. Например, функция `len` возвращает длину списка или строки:

```python
friends = ["Timofey", "Grigorii", "Nikita", "Konstantin"]
print(len(friends))
```

Вывод:
```
4
```

> Функции можно вызывать внутри других функций. В нашем примере функция `print` вызывает функцию `len`, чтобы узнать длину списка `friends`.

Однако, можно использовать не только встроенные функции, но и создавать свои. Например, следующая программа выведет на экран имя пользователя в верхнем регистре:

```python
def my_print(user_name: str) -> None:
    print("Функция my_print")
    print(user_name.upper())

my_print("Andrei")
```

Вывод
```
Функция my_print
ANDREI
```

> В этом примере мы создали функцию `my_print`, которая принимает один аргумент типа `str` и ничего не возвращает `None` (указывать типы не обязательно, но желательно, для хорошей читаемости кода). Внутри нашей функции, мы вызываем функцию `upper` у переданной переменной `user_name` и выводим результат на экран.

## **Задания:**

### **Задание 1**
- Создайте файл `02-task-if-for.py`

- Создайте переменную `age` и присвойте ей значение `5`
- Создайте переменную `animal` и присвойте ей значение `"DOG"`
- Создайте переменную `is_hungry` и присвойте ей значение `False`
- Создайте список `actions` из строк `"eat"`, `"drink"` и `"sleep"`

- Выведите переменную `animal` нижним регистром при помощи функций `lower`
- Выведите переменную `age` умноженную на `2`
- Если переменная `is_hungry` равна `True`, то выведите `"Голоден"`, иначе выведите `"Сыт"` и все элементы списка `actions` при помощи цикла `for` и конструкции `if-else`

## **Ожидаемый результат:**

При запуске команды

```shell
python 02-task-if-for.py
```

Вывод:

```
dog
10
Сыт
eat
drink
sleep
```

### **Задание 2**

- Создайте файл `02-task-function.py`

- Создайте переменную `user_name` и присвойте ей значение `"Andrei"`
- Создайте переменную `user_age` и присвойте ей значение `18`
- Создайте функцию `print_user_name_and_age`, которая принимает два аргумента `name` и `age` и выводит на экран имя и возраст пользователя
- Вызовите функцию `print_user_name_and_age` с аргументами `user_name` и `user_age`

## **Ожидаемый результат:**

При запуске команды

```shell
python 02-task-function.py
```

Вывод:

```
Andrei
18
```