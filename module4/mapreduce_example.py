""""MapReduce example for Module 4"""
from functools import reduce

my_list = [1, 2, 3, 4]


# Tradional SSV approach
ss_trad = sum([i**2 for i in my_list])


# MapReduce SSV approach
squared_values = map(lambda i: i**2, my_list)

# sqaure_values = [1, 4, 9, 16]

def add_numbers(x1, x2):
    return x1 + x2


ssv_mapreduce = reduce(add_numbers, squared_values)


print('Sum of Squared Values: (Traditional): {}'.format(ss_trad))
print('Sum of Squared Values: (MapReduce): {}'.format(ssv_mapreduce))