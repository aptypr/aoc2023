def update_digits(digits, n):
    if len(digits) < 2:
        digits.append(n)
    else:
        digits[-1] = n

def digits_to_num(digits):
    if len(digits) == 1:            
        return 11 * digits[0]
    else:
        return 10*digits[0] + digits[-1]



def func1():
    with open('input.txt') as f:
        res = 0
        for line in f.readlines():
            digits = []
            for c in line:
                if c.isdigit():
                    update_digits(digits, int(c))
            res += digits_to_num(digits)
        print(res)

subs_to_digits = {'one': 1,
                  'two': 2,
                  'three': 3,
                  'four': 4,
                  'five': 5,
                  'six': 6,
                  'seven': 7,
                  'eight': 8,
                  'nine': 9}


def func2():
    with open('input.txt') as f:
        res = 0
        for line in f.readlines():
            digits = []
            for i in range(len(line)):
                # check if line[i] is digit:
                c = line[i]
                if c.isdigit():
                    update_digits(digits, int(c))
                else:
                    for candidate in subs_to_digits.keys():
                        try:
                            if line[i:i + len(candidate)] == candidate:
                                update_digits(digits, subs_to_digits[candidate])
                        except:
                            pass
            res += digits_to_num(digits)
        print(res)

func2()