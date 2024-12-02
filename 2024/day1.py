# Two lists

# Match up the two lists of location IDs
# Pair up numbers in order from smallest
# Take absolute difference

list1 = []
list2 = []

with open('day1input.txt','r') as lists:
    for line in lists:
        row = [int(x) for x in line.strip().split('   ')]
        list1.append(row[0])
        list2.append(row[1])

list1.sort()
list2.sort()

x = 0
list_difference = 0

for x, y in zip(list1, list2):
    list_difference += abs(x - y)

print(list_difference)

# Location IDs appear in both lists
# How often is ID in left list in right list?
# Similarity Score - sum of x in list 1 times occurrences in list 2

similarity_score = 0
for x in list1:
    similarity_score += x * (list2.count(x))

print(similarity_score)

# Version 2
# map and lambda taken from Reddit
print(sum(map(lambda a, b: abs(a-b), list1, list2)))
print(sum(map(lambda a: a*list2.count(a), list1)))