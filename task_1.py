'''Задача 1. Создайте программу для игры в "Крестики-нолики".'''

def print_field(field):
    for i in range(len(field)):
        print(' | '.join(field[i]))


def check_input_pos(text): #проверка ввода позиции в пределах заданного поля
    check_input = False
    while not check_input:
        try:
            position = list(map(int, input(text).split(',')))
            check_input = True
            if position[0] > 3 or position[1] > 3 or position[0] < 1 or position[1] < 1:
                print("Значения должны быть в диапазоне от 1 до 3")
                check_input = False
        except:
            print("Некорректный ввод")
    return position


def check_win(field, go_elem): #проверка на выигрыш по строкам, столбцам и диагоналям
    for el in field:
        if el.count(go_elem) == 3:
            return True
    col_in_row = [[field[j][i]
                   for j in range(len(field))] for i in range(len(field[0]))]
    for el in col_in_row:
        if el.count(go_elem) == 3:
            return True
    find_elem = 0
    for i in range(3):
        if field[i][i] == go_elem: find_elem += 1
    if find_elem == 3: return True
    if field[2][0] == go_elem and field[1][1] == go_elem and field[0][2] == go_elem:
        return True

field = [['-' for j in range(3)] for i in range(3)]
print_field(field)

for i in range(9):
    go_elem = "0" if i % 2 != 0 else "X"
    while True:
        play = check_input_pos(f"Куда ходит {go_elem}, введите номер строки и столбца, разделяя их запятой, например 1,1: ")
        if field[play[0]-1][play[1]-1] == '-':
            field[play[0]-1][play[1]-1] = go_elem
            print_field(field)
            break
        else:
            print("Это место уже занято! Повторите ход")
            print_field(field)
    if i >= 2:
        if check_win(field, go_elem):
            print("Ваша победа!!!")
            break