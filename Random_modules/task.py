import random

# random_numbers_from_0_to_1 = random.random() * 4
# print(random_numbers_from_0_to_1) 

# random_float = random.uniform(0,10) *10
# print(random_float)

# tail = random.choice(['heads', 'tails'])
# print(tail)
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print('Tails')
else:
    print('Heads')