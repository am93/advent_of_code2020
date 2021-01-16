input_data = [line.split(' ') for line in open('input02').read().strip('\n').splitlines()]

def extract_data(line):
    limits = [int(l) for l in line[0].split('-')]
    char = line[1].strip(':')
    password = line[2]
    return (limits, char, password)
    

def part01(data):
    valid_pass = 0
    for line in data:
        (limits, char, password) = extract_data(line)
        char_count = password.count(char)
        if limits[0] <= char_count and char_count <= limits[1]:
            valid_pass += 1
    return valid_pass

def part02(data):
    valid_pass = 0
    for line in data:
        (limits, char, password) = extract_data(line)
        char_count = sum([1 for idx in limits if password[idx-1] == char])
        if char_count == 1:
            valid_pass += 1
    return valid_pass
    

if __name__ == '__main__':
    print(part01(input_data))
    print(part02(input_data))