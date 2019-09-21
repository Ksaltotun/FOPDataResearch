import random
chance = 2000000
peoples_num = 7500000000
count = 0
for i in range(peoples_num):
    if i % 10000000 == 0:
        print('10 million')
    if random.randint(0, chance) == 666:
        count += 1
print(count)

