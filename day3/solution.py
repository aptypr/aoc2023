from collections import defaultdict
example = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

example2 = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*..s.
.664.598.1'''

def symbol_is_near(start_col, end_col, row, engine):
    def is_symbol(r,c):
        if r < 0 or r >= len(engine):
            return False
        if c < 0 or c >= len(engine[0]):
            return False
        return engine[r][c].isdigit() == False and engine[r][c] != '.'
    for c in range(start_col-1, end_col+2):
        if is_symbol(row-1,c):
            return True
        if is_symbol(row+1, c):
            return True
    if is_symbol(row, start_col-1) or is_symbol(row, end_col+1):
        return True
    return False



def calc_sum_of_part_numbers(engine):
    res = 0
    # бежим по строкам
    for row in range(len(engine)):
        # бежим по столбцам
        col = 0
        is_digit_mode = False
        number_str = ''
        digit_start_col = -1
        while col < len(engine[row]):
            c = engine[row][col]
            if not c.isdigit() and is_digit_mode:
                # если символ - не цифра, и режим определения числа, то если рядом есть символ,
                #  добавляем к результату это число, выходим из режима определения числа
                
                if symbol_is_near(digit_start_col, col-1, row, engine):
                    res += int(number_str)
                                    
                number_str = ''
                is_digit_mode = False
            elif not c.isdigit() and not is_digit_mode:
                # if c is not digit and not digit_mode противном случае переходим к следующему столбцу
                pass
            elif c.isdigit() and not is_digit_mode:
                # если символ - цифра и не режим определения числа, 
                # то переходим в режим определения чисел, добавляем цифру к числу
                digit_start_col = col
                is_digit_mode = True
                number_str += c
            elif c.isdigit() and is_digit_mode:
                
                # если символ - цифра и режим определения числа, добавляем цифру к числу
                number_str += c
            col += 1
        if is_digit_mode:
            if symbol_is_near(digit_start_col, len(engine[row])-1, row, engine):
                res += int(number_str)
                # print('near symbol ')
            number_str = ''
    
    return res

print(calc_sum_of_part_numbers(example2.splitlines()))


with open(r'C:\Users\1\Documents\code\advent_of_code_2023\day3\input.txt') as f:
    engine = f.read().splitlines()
    # print(engine)
    print(calc_sum_of_part_numbers(engine))

print('second part')

def closest_star(start_col, end_col, row, engine):
    def is_star(r,c):
        if r < 0 or r >= len(engine):
            return False
        if c < 0 or c >= len(engine[0]):
            return False
        return engine[r][c] == '*'
    for c in range(start_col-1, end_col+2):
        if is_star(row-1,c):
            return (row-1, c)
        if is_star(row+1, c):
            return (row +1, c)
    if is_star(row, start_col-1):
        return (row, start_col - 1)
    if is_star(row, end_col+1):
        return (row, end_col+1)
    return None

def calc_gears(engine):
    # res = 0
    number_near_stars = defaultdict(list)
    # бежим по строкам
    for row in range(len(engine)):
        # бежим по столбцам
        col = 0
        is_digit_mode = False
        number_str = ''
        digit_start_col = -1
        while col < len(engine[row]):
            c = engine[row][col]
            if not c.isdigit() and is_digit_mode:
                # если символ - не цифра, и режим определения числа, то если рядом есть символ,
                #  добавляем к результату это число, выходим из режима определения числа
                
                pos = closest_star(digit_start_col, col-1, row, engine)
                if pos:
                    number_near_stars[pos].append(int(number_str))
                    # print('near symbol ')
                # else:
                #     print('checking ', number_str)
                #     print('not near')
                    
                number_str = ''
                is_digit_mode = False
            elif not c.isdigit() and not is_digit_mode:
                # if c is not digit and not digit_mode противном случае переходим к следующему столбцу
                pass
            elif c.isdigit() and not is_digit_mode:
                # если символ - цифра и не режим определения числа, 
                # то переходим в режим определения чисел, добавляем цифру к числу
                digit_start_col = col
                is_digit_mode = True
                number_str += c
            elif c.isdigit() and is_digit_mode:
                
                # если символ - цифра и режим определения числа, добавляем цифру к числу
                number_str += c
            col += 1
        if is_digit_mode:
            pos = closest_star(digit_start_col, len(engine[row])-1, row, engine)
            if pos:
                number_near_stars[pos].append(int(number_str))
                # res += int(number_str)

                # print('near symbol ')
            number_str = ''
    res = 0
    for k, v in number_near_stars.items():
        if len(v) == 2:
            res += v[0] * v[1]
    return res

example3 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
print(calc_gears(example3.splitlines()))

with open(r'C:\Users\1\Documents\code\advent_of_code_2023\day3\input.txt') as f:
    engine = f.read().splitlines()
    # print(engine)
    print(calc_gears(engine))