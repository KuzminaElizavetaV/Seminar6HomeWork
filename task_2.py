'''Задача 2. Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
    *Пример:*
    2+2 => 4;
    1+2*3 => 7;
    1-2*3 => -5;
- Добавьте возможность использования скобок, меняющих приоритет операций.
    *Пример:*
    1+2*3 => 7;
    (1+2)*3 => 9;'''

list_character = []
i = 0

def operation(math_operation, a, b):
    if math_operation == "/":
        return a / b
    elif math_operation == "*":
        return a * b
    elif math_operation == "-":
        return a - b
    elif math_operation == "+":
        return a + b

def calculate(znak, start=0, end=len(list_character), r_ind=0):
    global list_character, i
    res_i = list_character[start:end].index(znak) + r_ind
    res = operation(znak, list_character[res_i - 1], list_character[res_i + 1])
    list_character.pop(res_i + 1)
    list_character.pop(res_i)
    list_character.pop(res_i - 1)
    list_character.insert(res_i - 1, res)
    i += 2
str_inp = input("Введите выражение для расчета в 1 строку: ").strip()
num = ''
for ch in str_inp:
    if ch.isdigit():
        num += ch
    else:
        if len(num) > 0 and num.isdigit(): list_character.append(int(num))
        list_character.append(ch)
        num = ''

if len(num) > 0 and num.isdigit(): list_character.append(int(num))
list_character = list(filter((lambda el: el != " "), list_character))
while len(list_character) > 1:
    i = 0
    while "(" in list_character:
        r_index = (len(list_character) - 1) - list(reversed(list_character)).index("(")
        try:
            index = list_character.index(")")
        except:
            print("Выражение задано неверно!")
        list_character.pop(r_index)
        list_character.pop(index - 1)
        i = 0
        while "/" in list_character[r_index:index - 1 - i]:
            calculate("/", r_index, index - 1 - i, r_index)
        while "*" in list_character[r_index:index - 1 - i]:
            calculate("*", r_index, index - 1 - i, r_index)
        while "+" in list_character[r_index:index - 1 - i]:
            calculate("+", r_index, index - 1 - i, r_index)
        while "-" in list_character[r_index:index - 1 - i]:
            calculate("-", r_index, index - 1 - i, r_index)

    while "/" in list_character:
        calculate("/", 0, len(list_character), 0)
    while "*" in list_character:
        calculate("*", 0, len(list_character), 0)
    while "+" in list_character:
        calculate("+", 0, len(list_character), 0)
    while "-" in list_character:
        calculate("-", 0, len(list_character), 0)

print(f"{str_inp} = {list_character[0]}")
