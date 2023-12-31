def square_even_numbers(numbers: list) -> list:
    sq_even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            sq_even_numbers.append(num ** 2)
    return sq_even_numbers

input_list = [1, 2, 3, 4, 5, 6]
output_result = square_even_numbers(input_list)
print(output_result)
