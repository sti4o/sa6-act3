def find_maximum(numbers, compare):
    max_number = numbers[0]

    for number in numbers:
        max_number = compare(max_number, number)

    return max_number


numbers_list = [3, 65, 34, 75, 28, 99, 4]

greater = lambda a, b: a if a > b else b


maximum_number = find_maximum(numbers_list, greater)
print(maximum_number)
