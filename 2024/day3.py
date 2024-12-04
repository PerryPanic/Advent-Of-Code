import math as m, re

# Need as one string, rather than list
# corrupted_code = list(open('2024\day3input.txt'))
# New lines were screwing everything up
# corrupted_code = ''.join(list(open('2024\day3input.txt')))

corrupted_code = ''.join(list(open('2024\day3input.txt'))).replace('\n', '')

# Need Lazy match with ?
uncorrupted_code = re.sub(r'(don\'t\(\)).*?(do\(\))','',corrupted_code)

def multiply_pair(code):
    multiple_sum = 0
    for mul in re.finditer(r'mul\(\d+,\d+\)', code):
        pair = [int(x) for x in mul.group()[4:-1].split(',')]
        multiple_sum += m.prod(pair)
    return multiple_sum
    
print(multiply_pair(corrupted_code), multiply_pair(uncorrupted_code))