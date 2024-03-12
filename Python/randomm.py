


import random


random_integers = [random.randint(1, 100) for _ in range(10)]


odd_list = [num for num in random_integers if num % 2 != 0]
even_list = [num for num in random_integers if num % 2 == 0]


print("Random integers:", random_integers)
print("Odd integers:", odd_list)
print("Even integers:", even_list)
