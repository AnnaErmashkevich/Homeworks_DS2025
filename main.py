numbers = list(range(1,21))
print(numbers)
div_by_2and3 = [num for num in numbers if num % 2 == 0 and num % 3 == 0]
print(div_by_2and3)