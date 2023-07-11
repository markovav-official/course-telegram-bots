## **Теория**

### **Переменные**

В языке `python` как и во многих других языках программирования существуют переменные. Простым языком, **переменная - это именованная коробочка, в которую можно положить какое-то значение**. Переменные могут быть разных типов, например:

Строка `str`: 
```python
user_name = "Andrei"
```

Целое число `int`: 
```python
balance = 1000
```

Логическое значение `bool`:
```python
is_active = True
```

Список `list`:
```python
friends = ["Timofey", "Grigorii", "Nikita", "Konstantin"]
```

> В примере выше, то, что написано слева от знака `=` - это имя переменной, а то, что написано справа - это значение, которое мы кладем в переменную.

В `python` не нужно указывать тип переменной при ее объявлении, он определяется автоматически. Также в `python` не нужно указывать точку с запятой в конце строки.

### **Вывод на экран**

Для вывода на экран используется функция `print`. В скобках после функции `print` указывается то, что нужно вывести на экран. Например:

```python
print("Hello, world!")
```

Выведет на экран:

```
Hello, world!
```

> `print` - это функция, а `"Hello, world!"` - это аргумент, который мы передаем в функцию `print`. Аргументы в функции указываются в скобках через запятую. Мы еще встретимся с функциями в дальнейшем.

### **Запуск программы**

Давайте запустим программу на `python`. Чтобы запустить программу, введите в терминале команду:
```shell
python 01-python-variables.py
```
либо нажмите на кнопку *"Запуск файла Python"* в правом верхнем углу окна с кодом

В терминале вы должны увидеть следующий результат:
```shell
Andrei
1000
True
['Timofey', 'Grigorii', 'Nikita', 'Konstantin']
```

## **Задание**

- Создайте файл `01-task.py`

- Создайте переменную `animal` и присвойте ей значение `"cat"`
- Создайте переменную `age` и присвойте ей значение `3`
- Создайте переменную `is_hungry` и присвойте ей значение `True`
- Создайте список `actions` из строк `"eat"`, `"drink"` и `"sleep"`

- Выведите все переменные на экран при помощи функции `print`

## **Ожидаемый результат**

При запуске команды

```shell
python 01-task.py
```

Вывод:

```
cat
3
True
['eat', 'drink', 'sleep']
```