def sum_even_numbers(numbers: list) -> int:
    return sum([integer for integer in numbers if integer % 2 == 0])


number_list = [i for i in range(1, 10 + 1)]
print("even numbers sum:", sum_even_numbers(number_list))
