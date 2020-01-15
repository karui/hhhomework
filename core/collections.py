# Есть список not_even_list, реализовать логику в функции even: создать новый список с четными элементами из списка not_even_list
not_even_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def even(some_not_even_list):
    return [ number for number in some_not_even_list if number % 2 == 0 ]
    return list(filter(lambda n: not n % 2, some_not_even_list))

# Следующий код с циклом, переписать с использованием спискового включения (list comprehension)
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
def get_ages(some_years_of_birth):
    return [ 2014 - year for year in some_years_of_birth ]

# Есть список numbers, реализовать логику в функции get_first_n_last: вернуть новый список состоящий из первого и последнего элемента переданного списка
numbers = [5, 10, 15, 20, 25]
def get_first_n_last(some_list):
    return [some_list[0], some_list[-1]] if some_list else []
    # return some_list[::len(some_list)-1]

# Написать функцию, которая принимает список и возвращает новый список, состоящий из элементов принятого, но без повторений
list_with_repetition = [1, 1, 3, 4, 2, 2, 2, 6]
def get_list_without_repetition(some_list):
    numberSet = set()
    return [ number for number in some_list if number not in numberSet and numberSet.add(number) is None ]

# Написать функцию, которая возвращает словарь, ключи которого из списка keys, а значения из списка values
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#00FF00', '#0000FF']
def map_keys_and_values(some_keys, some_values):
    return dict(zip(some_keys, some_values))
    return { key:value for key, value in zip(some_keys, some_values) }

# Написать функцию, которая принимает строку и возвращает словарь состоящий из ключей - символов из строки, значений - количество повторений этих символов в строке
s = 'some string'
def count_symbols(some_string):
    symbolDict = {}
    for symbol in some_string:
        symbolDict[symbol] = symbolDict.get(symbol,0) + 1
    return symbolDict

print(even(not_even_list))
print(get_ages(years_of_birth))
print(get_first_n_last(numbers))
print(get_list_without_repetition(list_with_repetition))
print(map_keys_and_values(keys, values))
print(count_symbols(s))

print(even([]))
print(get_ages([]))
print(get_first_n_last([]))
print(get_list_without_repetition([]))
print(map_keys_and_values([], []))
print(count_symbols(''))
