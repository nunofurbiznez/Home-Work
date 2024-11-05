# 1. List of Favorite Fruits
fruits = ['apple', 'banana', 'mango', 'orange', 'grape']
print(fruits)

# 2. Get Colors from List
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors[0])
print(colors[2]) 
print(colors[-1])    

# 3. Change a Number in List
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25 
numbers.append(60) 
print(numbers)

# 4. Slice First 3 Names
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = names[:3]
print(subset)

# 5. Loop to Print Squared Numbers
numbers = list(range(1, 11))
print("Squares of numbers 1-10:")
for number in numbers:
    print(number ** 2)

# 6. Add Items to Shopping List
shopping_cart = []
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
shopping_cart.extend(['butter', 'cheese'])
print(shopping_cart)

# 7. Find Max and Min
numbers = [45, 22, 88, 56, 92, 33]
print("Max number: ", max(numbers))
print("Min number: ", min(numbers))

# 8. Count 'a' in List
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
print("Count of 'a': ", letters.count('a'))

# 9. Squares of Even Numbers from 0 to 10
squares_of_even = [x ** 2 for x in range(11) if x % 2 == 0]
print(squares_of_even)

# 10. Remove Duplicates
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_nums = list(set(nums))
print(unique_nums)
