def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list) 
print(f"The average is: {average_empty}")

my_list_with_strings = [10, 20, 'a', 40, 50]
average_strings = calculate_average(my_list_with_strings) #This will cause an error
print(f"The average is: {average_strings}")