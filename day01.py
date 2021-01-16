input_data = [int(line) for line in open('input01').read().strip('\n').splitlines()]

def part01(target, data):
    val_exp = set()
    for val in data:
        val_n = target - val
        if val_n in val_exp:
            return val_n * val
        else:
            val_exp.add(val)

def part02(target, data):
    idx = 0
    while True:
        val_f = data[idx]
        idx += 1
        match_two = part01(target - val_f, data[idx:])
        if match_two is not None:
            return val_f * match_two
            
    
if __name__ == '__main__':
    print(part01(2020, input_data))
    print(part02(2020, input_data))