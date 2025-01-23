def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty list after removing non-numeric elements
    total = sum(numeric_numbers)
    count = len(numeric_numbers)
    average = total / count
    return average

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [10,20,30,40,50]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [10,20,30,40,50,'a']
result = calculate_average(my_list)
print(f"The average is: {result}") #This will now work correctly