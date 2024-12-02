# Reindeer fission/fusion reactor

# How many reports are safe
# Safe - all asc/desc (not equal), no jump > 3

data = []
with open('day2input.txt','r') as input:
    for line in input:
        row = [int(x) for x in line.strip().split(' ')]
        data.append(row)

def direction(a):
    if (a[1] - a[0]) > 0:
        return 1
    else:
        return -1

def checker(a):
    dir = direction(a)
    #if len(report)
    # below removed as it remove from list a, rather than creating a new list
    # for x, y in zip(a, a[1:]):
    for x, y in zip(a, a[1:]):
        if not 1 <= ((y - x) * dir) <= 3:
            return 0
    return 1

def remover_checker(a):
    counter = 0
    for x in a:
        b = a[:counter] + a[counter+1:]
        if checker(b) == 1:
            return 1
        counter += 1
    return 0

safe_report = []
dampened_report = []

for report in data:    
    if checker(report) == 1:
        safe_report.append(report)
        dampened_report.append(report)
        continue
    elif remover_checker(report) == 1:
        dampened_report.append(report)
            
print(len(safe_report))
print(len(dampened_report))
