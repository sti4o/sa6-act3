
number = 12345

sum_of_digits = lambda num: sum(int(digit) for digit in str(num))

result = sum_of_digits(number)
print(result)