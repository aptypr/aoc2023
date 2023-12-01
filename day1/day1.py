def func1():
    with open('input.txt') as f:
        res = 0
        for line in f.readlines():
            digits = []
            for c in line:
                if c.isdigit():
                    if len(digits) < 2:
                        digits.append(int(c))
                    else:
                        digits[-1] = int(c)
            if len(digits) == 1:            
                res += 11 * digits[0]
            else:
                res += 10*digits[0] + digits[-1]
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
                    if len(digits) < 2:
                        digits.append(int(c))
                    else:
                        digits[-1] = int(c)
                else:
                    for candidate in subs_to_digits.keys():
                        try:
                            if line[i:i + len(candidate)] == candidate:
                                if len(digits) < 2:
                                    digits.append(subs_to_digits[candidate])
                                else:
                                    digits[-1] = subs_to_digits[candidate]
                        except:
                            pass

            # print(digits)
            if len(digits) == 1:            
                res += 11 * digits[0]
            else:
                res += 10*digits[0] + digits[-1]
        print(res)

func2()