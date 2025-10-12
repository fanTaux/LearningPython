name = 'John Doe'
age = 21

my_integer_var = 10
print('Integer: ', my_integer_var)

my_float_var = 4.50
print('Float: ', my_float_var)

my_complex_var = 3 +4j
print('Complex: ', my_complex_var)

my_string_var = 'Hello World'
print('String: ', my_string_var)

my_boolean_var = True
print('Boolean: ', my_boolean_var)

my_set_var = {7, 5, 8}
print('Set: ', my_set_var)

my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary: ', my_dictionary_var)

my_tuple_var = (7, 5, 8)
print('Tuple: ', my_tuple_var)

my_range_var = range(5)
print('Range: ', my_range_var)

my_list = [22, 'Hello World', 3.14, True]
print('List: ', my_list)

my_none_var = None
print('None: ', my_none_var)

import time

# Membuat tuple dan set dengan 1 juta elemen
data_tuple = tuple(range(1_000_000))
data_set = set(range(1_000_000))

# Tes waktu akses
start = time.time()
999_999 in data_tuple
tuple_time = time.time() - start

start = time.time()
999_999 in data_set
set_time = time.time() - start

print(f"Waktu tuple: {tuple_time:.6f} detik")
print(f"Waktu set:   {set_time:.6f} detik")

import sys

data_tuple = tuple(range(10))
data_set = set(range(10))

print("Ukuran tuple:", sys.getsizeof(data_tuple), "bytes")
print("Ukuran set:", sys.getsizeof(data_set), "bytes")

print(type(my_boolean_var))

test_1_var = 'fanTa'
print(type(test_1_var))

nums = [1, 2, 3]
nums[0] = 4

print(nums)

user_name: str = 'John Doe'
user_age: int = 24

def greet(name: str, age: int) -> str:
    return f'Hello, {name}, age {age}'

print(greet(user_name, user_age))