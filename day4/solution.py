example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def calc_points(cards: str):
    cards = cards.splitlines()
    res = 0
    for card in cards:
        card_num, numbers = card.split(':')
        winning_numbers_str, my_numbers_str = numbers.split('|')

        winning_numbers = [int(e.strip()) for e in winning_numbers_str.split(' ') if e.strip() != '']
        my_numbers = [int(e.strip()) for e in my_numbers_str.split(' ') if e.strip() != '']
        local_res = 0
        for my_number in my_numbers:
            if my_number in winning_numbers:
                if local_res == 0:
                    local_res = 1
                else:
                    local_res *= 2
        res += local_res
    return res

print(calc_points(example))

print('result')
with open('day4\input.txt') as f:
    print(calc_points(f.read()))

print('second part')
from collections import defaultdict

def calc_scratchcards(cards: str):
    cards1 = cards.splitlines()
    total = 0
    i = 1
    cards = dict()
    for card in cards1:
        card_num, numbers = card.split(':')
        if i in cards:
            cards[i] += 1
        else:
            cards[i] = 1  # original
        # total += 1
        
        winning_numbers_str, my_numbers_str = numbers.split('|')

        winning_numbers = [int(e.strip()) for e in winning_numbers_str.split(' ') if e.strip() != '']
        my_numbers = [int(e.strip()) for e in my_numbers_str.split(' ') if e.strip() != '']
        matching_numbers = 0
        for my_number in my_numbers:
            if my_number in winning_numbers:
                matching_numbers += 1
        for k in range(cards[i]):
            for j in range(matching_numbers):
                if i+j+1 in cards:
                    cards[i+j+1] += 1
                else:
                    cards[i+j+1] = 1
        i+=1
    # print(cards)
    for v in cards.values():
        total += v
    return total
print('test result')
print(calc_scratchcards(example))

with open('day4\input.txt') as f:
    print(calc_scratchcards(f.read()))