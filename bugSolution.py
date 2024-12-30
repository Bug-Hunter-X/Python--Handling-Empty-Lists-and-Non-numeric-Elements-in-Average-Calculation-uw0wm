def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    return sum(numeric_numbers) / len(numeric_numbers)

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list) 
print(f"The average is: {average_empty}")

my_list_with_strings = [10, 20, 'a', 40, 50]
average_strings = calculate_average(my_list_with_strings) 
print(f"The average is: {average_strings}")

my_list_with_strings2 = ['a', 'b', 'c']
average_strings2 = calculate_average(my_list_with_strings2) 
print(f"The average is: {average_strings2}") 