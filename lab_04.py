### Лабораторная работа № 4: Абстракция данных и списки"""

# ============================================================
# Вопрос 1. Индексация вложенных списков
# ============================================================
def _q_01():
    """
    Часть 1
    >>> x = [1, 3, [5, 7], 9]                                   # doctest: +SKIP
    >>> x[2][1]                                                 # doctest: +SKIP
    7
    >>> x = [[7]]                                               # doctest: +SKIP
    >>> x[0][0]                                                 # doctest: +SKIP
    7
    >>> x = [3, 2, 1, [9, 8, 7]]                                # doctest: +SKIP
    >>> x[3][2]                                                 # doctest: +SKIP
    7
    >>> x = [[3, [5, 7], 9]]                                    # doctest: +SKIP
    >>> x[0][1][1]                                              # doctest: +SKIP
    7

    Часть 2
    >>> lst = [3, 2, 7, [84, 83, 82]]                           # doctest: +SKIP
    >>> lst[4]                                                  # doctest: +SKIP
    IndexError: list index out of range
    >>> lst[3][0]                                               # doctest: +SKIP
    84
    """
    return 0   # заглушка


# ============================================================
# Вопрос 2. Генераторы списков
# ============================================================
def _q_02():
    """
    Часть 1
    >>> [x*x for x in range(5)]                                 # doctest: +SKIP
    [0, 1, 4, 9, 16]
    >>> [n for n in range(10) if n % 2 == 0]                    # doctest: +SKIP
    [0, 2, 4, 6, 8]
    >>> ones = [1 for i in ["привет", "как", "сам"]]            # doctest: +SKIP
    >>> ones + [str(i) for i in [6, 3, 8, 4]]                   # doctest: +SKIP
    [1, 1, 1, '6', '3', '8', '4']
    >>> [i+5 for i in [n for n in range(1,4)]]                  # doctest: +SKIP
    [6, 7, 8]

    Часть 2
    >>> [i**2 for i in range(10) if i < 3]                      # doctest: +SKIP
    [0, 1, 4]
    >>> lst = ['привет' for i in [1, 2, 3]]                     # doctest: +SKIP
    >>> print(lst)                                              # doctest: +SKIP
    ['привет', 'привет', 'привет']
    >>> lst + [i for i in ['1', '2', '3']]                      # doctest: +SKIP
    ['привет', 'привет', 'привет', '1', '2', '3']
    """
    return 0   # заглушка


# ============================================================
# Вопрос 3. Печать элементов с условием
# ============================================================
def if_this_not_that(i_list, this):
    """
    Определи функцию, которая принимает список целых `i_list` и целое число
    `this`. Каждый элемент в `i_list`, если элемент больше `this`, выводится в консоль; 
    в противном случае выводится слово `that`.

    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    for elem in i_list:
        if elem > this:
            print(elem)
        else:
            print('that')


# ============================================================
# Вопрос 4. Абстракция данных: город = [name, lat, lon]
# ============================================================
def make_city(name, lat, lon):
    """
    >>> city = make_city('Ярославль', 0, 1)
    >>> get_name(city)
    'Ярославль'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    return [name, lat, lon]


def get_name(city):
    """
    >>> city = make_city('Ярославль', 0, 1)
    >>> get_name(city)
    'Ярославль'
    """
    return city[0]


def get_lat(city):
    """
    >>> city = make_city('Ярославль', 0, 1)
    >>> get_lat(city)
    0
    """
    return city[1]


def get_lon(city):
    """
    >>> city = make_city('Ярославль', 0, 1)
    >>> get_lon(city)
    1
    """
    return city[2]


from math import sqrt


def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    lat_diff = get_lat(city1) - get_lat(city2)
    lon_diff = get_lon(city1) - get_lon(city2)
    return sqrt(lat_diff ** 2 + lon_diff ** 2)


# ============================================================
# Вопрос 5. Ближайший город
# ============================================================
def closer_city(lat, lon, city1, city2):
    """
    Возвращает название города city1 или города city2 в зависимости от того, 
    какой из них ближе к координате (lat, lon).

    >>> moscow = make_city('Москва', 55.75, 37.616667)
    >>> saint_petersburg = make_city('Питер', 59.9375, 30.308611)
    >>> closer_city(57.616667, 39.85, moscow, saint_petersburg)
    'Москва'
    >>> london = make_city('Лондон', 51.507222, -0.1275)
    >>> mumbai = make_city('Мумбаи', 18.975, 72.825833)
    >>> closer_city(57.616667, 39.85, london, mumbai)
    'Лондон'
    """
    target = make_city('target', lat, lon)
    dist1 = distance(target, city1)
    dist2 = distance(target, city2)
    if dist1 < dist2:
        return get_name(city1)
    else:
        return get_name(city2)


# ============================================================
# Вопрос 6. Альтернативная реализация (закомментирована)
# ============================================================
# make_city = lambda name, lat, lon: { 'name': name, 'lat': lat, 'lon': lon }
# get_name = lambda city: city['name']
# get_lat = lambda city: city['lat']
# get_lon = lambda city: city['lon']


# ============================================================
# Вопрос 7. Создание пустой доски
# ============================================================
def create_row(size):
    """
    Возвращает отдельную пустую строку поля заданного размера. Каждый пустой 
    элемент обозначается строкой '-'.

    >>> create_row(5)
    ['-', '-', '-', '-', '-']
    """
    return ['-'] * size


def create_board(rows, columns):
    """Возвращает игровое поле заданного размера.

    >>> create_board(3, 5)
    [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']]
    """
    return [create_row(columns) for _ in range(rows)]


# ============================================================
# Вопрос 8. Замена элемента с созданием нового списка
# ============================================================
def replace_elem(lst, index, elem):
    """Создаёт и возвращает новый список с теми же элементами, что и lst,
    за исключением элемента index, значение которого должно быть elem.

    >>> old = [1, 2, 3, 4, 5, 6, 7]
    >>> new = replace_elem(old, 2, 8)
    >>> new
    [1, 2, 8, 4, 5, 6, 7]
    >>> new is old         # проверяем, что replace_elem возвращает новый список
    False
    """
    assert index >= 0 and index < len(lst), 'Индекс за пределами размера списка'
    new_lst = lst[:]              # поверхностная копия через срез
    new_lst[index] = elem         # заменяем элемент в копии
    return new_lst


# ============================================================
# Вопрос 9. Получение и установка фишки
# ============================================================
def get_piece(board, row, column):
    """Возвращает состояние поля в позиции (row, column) на доске.

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> board = put_piece(board, rows, 0, 'X')[1]
    >>> board = put_piece(board, rows, 0, 'O')[1]
    >>> get_piece(board, 1, 0)
    'X'
    >>> get_piece(board, 1, 1)
    '-'
    """
    return board[row][column]


def put_piece(board, max_rows, column, player):
    """Размещает фишку игрока player в самом нижнем свободном поле заданного
    столбца. Возвращает тапл из двух элементов:

        1. Индекс строки, в которую встала фишка, или -1, если там нет мест.
        2. Новую доску.

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> row, new_board = put_piece(board, rows, 0, 'X')
    >>> row
    1
    >>> row, new_board = put_piece(new_board, rows, 0, 'O')
    >>> row
    0
    >>> row, new_board = put_piece(new_board, rows, 0, 'X')
    >>> row
    -1
    """
    # Идём снизу вверх: самая нижняя строка — с наибольшим индексом
    for row in range(max_rows - 1, -1, -1):
        # Нашли свободную ячейку в нужном столбце
        if get_piece(board, row, column) == '-':
            # Шаг 1: новая строка — копия board[row] с фишкой в column
            new_row = replace_elem(board[row], column, player)
            # Шаг 2: новая доска — копия board, где строка row заменена на new_row
            new_board = replace_elem(board, row, new_row)
            return row, new_board
    # Свободных мест нет
    return -1, board


# ============================================================
# Вопрос 10. Ход игрока
# ============================================================
def make_move(board, max_rows, max_cols, col, player):
    """Размещает фишку игрока в столбец col доски в случае возможного хода.
    Возвращает тапл из двух значений:

        1. Если ход возможен, возвращается индекс строки, в которую попала фишка.
           Иначе возвращает -1.
        2. Обновлённая доска

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> row, board = make_move(board, rows, columns, 0, 'X')
    >>> row
    1
    >>> get_piece(board, 1, 0)
    'X'
    >>> row, board = make_move(board, rows, columns, 0, 'O')
    >>> row
    0
    >>> row, board = make_move(board, rows, columns, 0, 'X')
    >>> row
    -1
    >>> row, board = make_move(board, rows, columns, -4, '0')
    >>> row
    -1
    """
    # Проверка границ столбца
    if col < 0 or col >= max_cols:
        return -1, board
    return put_piece(board, max_rows, col, player)


# ============================================================
# Вопрос 11. Печать доски
# ============================================================
def print_board(board, max_rows, max_cols):
    """
    Распечатывает доску. Строка 0 сверху, столбец 0 слева.

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> print_board(board, rows, columns)
    - -
    - -
    >>> new_board = make_move(board, rows, columns, 0, 'X')[1]
    >>> print_board(new_board, rows, columns)
    - -
    X -
    """
    for row in range(max_rows):
        row_str = ''
        for col in range(max_cols):
            row_str += get_piece(board, row, col)
            if col < max_cols - 1:
                row_str += ' '
        print(row_str)


# ============================================================
# Вопрос 12. Проверка победы в строке/столбце
# ============================================================
def check_win_row(board, max_rows, max_cols, num_connect, row, player):
    """ 
    Возвращает True, если игрок player победил в заданной строке, иначе False.

    >>> rows, columns, num_connect = 4, 4, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'O')
    False
    >>> board = make_move(board, rows, columns, 2, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'X')
    False
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'X')
    True
    >>> check_win_row(board, rows, columns, 4, 3, 'X')
    False
    >>> check_win_row(board, rows, columns, num_connect, 3, 'O')
    False
    """
    adjacent = 0
    for col in range(max_cols):
        if get_piece(board, row, col) == player:
            adjacent += 1
            if adjacent >= num_connect:
                return True
        else:
            adjacent = 0
    return False


def check_win_column(board, max_rows, max_cols, num_connect, col, player):
    """
    Возвращает True, если игрок player победил в заданном столбце, иначе False.

    >>> rows, columns, num_connect = 5, 5, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 0, 'X')
    False
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 1, 'O')
    False
    >>> board = make_move(board, rows, columns, 2, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 1, 'O')
    True
    >>> check_win_column(board, rows, columns, 4, 1, 'O')
    False
    >>> check_win_column(board, rows, columns, num_connect, 1, 'X')
    False
    """
    adjacent = 0
    for row in range(max_rows):
        if get_piece(board, row, col) == player:
            adjacent += 1
            if adjacent >= num_connect:
                return True
        else:
            adjacent = 0
    return False


# ============================================================
# Вопрос 13. Общая проверка победы
# ============================================================
def check_win(board, max_rows, max_cols, num_connect, row, col, player):
    """
    Возвращает True, если игрок player победил любым образом в заданных строке, 
    столбце или диагонали (row, col), иначе False.

    >>> rows, columns, num_connect = 2, 2, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'O')
    False
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    True

    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 1, 0, 'X')
    True
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    False

    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    False
    >>> check_win(board, rows, columns, num_connect, 1, 0, 'X')
    True
    """
    diagonal_win = check_win_diagonal(board, max_rows, max_cols, num_connect,
                                      row, col, player)
    return (check_win_row(board, max_rows, max_cols, num_connect, row, player) or
            check_win_column(board, max_rows, max_cols, num_connect, col, player) or
            diagonal_win)


##########################################################
### Функции для решения задач, которые не надо трогать ###
##########################################################

def check_win_diagonal(board, max_rows, max_cols, num_connect, row, col, player):
    """ 
    Возвращает True, если победная диагональ заданного игрока проходит через поле
    (row, column), иначе False.
    """
    # Верхнее левое начало потенциальной диагонали
    adjacent = 0
    row_top_left, col_top_left = row, col
    while row_top_left > 0 and col_top_left > 0:
        row_top_left -= 1
        col_top_left -= 1

    # Идём вниз-вправо
    while row_top_left < max_rows and col_top_left < max_cols:
        piece = get_piece(board, row_top_left, col_top_left)
        if piece == player:
            adjacent += 1
        else:
            adjacent = 0
        if adjacent >= num_connect:
            return True
        row_top_left += 1
        col_top_left += 1

    # Верхнее правое начало потенциальной диагонали
    adjacent = 0
    row_top_right, col_top_right = row, col
    while row_top_right > 0 and col_top_right < max_cols - 1:
        row_top_right -= 1
        col_top_right += 1

    # Идём вниз-влево
    while row_top_right < max_rows and col_top_right >= 0:
        piece = get_piece(board, row_top_right, col_top_right)
        if piece == player:
            adjacent += 1
        else:
            adjacent = 0
        if adjacent >= num_connect:
            return True
        row_top_right += 1
        col_top_right -= 1

    return False


###################################################################################
### Читать и понимать, что написано ниже, не нужно. Там только игровая механика. ###
###################################################################################

import sys


def other(player):
    """ Возвращает другого игрока. """
    if player == 'X':
        return 'O'
    return 'X'


def play(board, max_rows, max_cols, num_connect):
    max_turns = max_rows * max_cols
    print("\nИгрок 'X' начинает")
    who = 'X'
    turns = 0

    while True:
        turns += 1
        if turns > max_turns:
            print("\nНет ходов. Ничья!")
            sys.exit()

        while True:
            try:
                col_index = int(input('\nКакой столбец, игрок {}? '.format(who)))
            except ValueError as _:
                print('Неверный ввод. Попробуй ещё.')
                continue

            row_index, board = make_move(board, max_rows, max_cols, col_index, who)

            if row_index != -1:
                break

            print("Упс, сюда сунуть фишку никак")

        print_board(board, max_rows, max_cols)

        if check_win(board, max_rows, max_cols, num_connect, row_index, col_index, who):
            print("\nИгрок {} победил!".format(who))
            sys.exit()

        who = other(who)


def start_game():
    # Получаем все условия игры от пользователя.
    while True:
        while True:
            try:
                num_connect = int(input('Размер соединения (то есть 4 для «Четыре в ряд»)? '))
            except ValueError as _:
                print('Неверный ввод. Попробуй ещё.')
                continue
            break

        while True:
            try:
                 max_rows = int(input('Сколько строк? '))
            except ValueError as _:
                print('Неверный ввод. Попробуй ещё.')
                continue
            break

        while True:
            try:
                max_cols = int(input('Сколько столбцов? '))
            except ValueError as _:
                print('Неверный ввод. Попробуй ещё.')
                continue
            break

        if max_rows >= num_connect or max_cols >= num_connect:
            break
        print("Неверный размер для минимального соединения {0}. Попробуй ещё.".format(num_connect))

    board = create_board(max_rows, max_cols)
    play(board, max_rows, max_cols, num_connect)


if __name__ == '__main__':
    import doctest, sys
    finder = doctest.DocTestFinder()
    runner = doctest.DocTestRunner(doctest.OutputChecker(), optionflags=doctest.FAIL_FAST)
    doctest.OutputChecker.output_difference = lambda a, b, c, d: ""
    m = sys.modules.get('__main__')
    for test in finder.find(m, m.__name__):
        if test.name == '__main__': continue
        if test.name.split('.')[1][:2] != '_q': continue
        for example in test.examples: example.options[doctest.SKIP] = False
        if  runner.run(test).failed != 0: break
