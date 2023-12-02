test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def get_id(line):
    return int(line[line.index(' '): line.index(':')])

    
def split(line) -> list[str]:
    """
    Возвращает массив игр вида ['N1 blue, N2 green', ...]
    """
    # находим :, сдвигаем влево, и убираем лишний пробел слева
    return [s.strip() for s in line[line.index(':')+1:].lstrip().split(';')]


def get_colors(set_):
    a = set_.split(', ')
    blue = 0
    red = 0
    green = 0
    for p in a:
        if p.endswith(' blue'):
            blue = int(p[:p.index(' ')])
        if p.endswith(' red'):
            red = int(p[:p.index(' ')])
        if p.endswith(' green'):
            green = int(p[:p.index(' ')])
    return [red, green, blue]


def game_is_possible(line, max_values):
    # разбить на под игры
    games = split(line)
    # в каждой подигре определить сколько шаров какого цвета использовалось, обновить макс значения
    max_colors = [0,0,0]
    for game in games:
        colors = get_colors(game)
        for i in range(3):
            if colors[i] > max_colors[i]:
                max_colors[i] = colors[i]
    # вернуть макс значения для каждого цвета <= max_blue, max_red, max_green, 

    for i in range(3):
        if max_colors[i] > max_values[i]:
            return False
    return True


def game_power(line):
    # разбить на под игры
    games = split(line)
    # в каждой подигре определить сколько шаров какого цвета использовалось, обновить макс значения
    max_colors = [0,0,0]
    for game in games:
        colors = get_colors(game)
        for i in range(3):
            if colors[i] > max_colors[i]:
                max_colors[i] = colors[i]
    return max_colors[0] * max_colors[1] * max_colors[2]

def calc_func(lines, max_values):
    ids_sum = 0
    for line in lines:
        if game_is_possible(line, max_values):
            ids_sum += get_id(line)
    return ids_sum


def calc_power(lines):
    power = 0
    for line in lines:
        power += game_power(line)
    return power

def func1():
    max_blue = 14
    max_red = 12
    max_green = 13
    with open('input.txt') as f:
        ids_sum = 0
        lines = f.readlines()
        ids_sum = calc_func(lines, [max_red, max_green, max_blue])
    return ids_sum

def func2():
    """Решение второй части"""
    with open('input.txt') as f:
        power_sum = 0
        lines = f.readlines()
        power_sum = calc_power(lines)
    return power_sum


