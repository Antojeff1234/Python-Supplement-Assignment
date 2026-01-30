# Problem 16: Find the second largest number in a list
# Find and fix the error

numbers = [45, 89, 12, 78, 34]
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
second_largest = unique_numbers[1]  
print(f"Second largest: {second_largest}")
