# Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
# Using for loop
for magician in magicians:
    print(magician)

# Doing More Work Within a for Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a good trick!")
    print(f"I can't wait to see your next trick, {magician.title()}\n")

# Doing Something After a for Loop
for magician in magicians:
    print(f"{magician.title()}, that was a good trick!")
    print(f"I can't wait to see your next trick, {magician.title()}\n")
print("Thank you everyone. That was a great magic show")

# Making Numerical Lists
for value in range(1, 5): # using range() function
    print(value)
# or you can also use single argument
for value in range(5):  
    print(value)

# Using range() to Make a List of Numbers
numbers = list(range(1, 5))
print(numbers)

even_numbers = [list(range(2, 11, 2))] # A third argument was passed to print even numbers.
print(even_numbers)

odd_numbers = [list(range(1, 11, 2))] # A third argument was passed to print odd numbers.
print(odd_numbers)

# square numbers into a list
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# Some Statistics with a List of Numbers
cumm_digits = []
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

total = 0
for digit in digits:
    total = total + digit
    cumm_digits.append(total) # cummulative frequency(digits)
print(cumm_digits)

print(sum(digits)) # Sum total of all digits
print(max(digits)) # Maximum digit
print(min(digits)) # Minimum digit

# Using list comprehension
squares = [value ** 2 for value in range(1, 11)]
print(squares)


# Slicing list
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(digits[0:4]) # print first four elements.
print(digits[:4]) # print first four elements too.
print(digits[-4:]) # print last four elements.
print(digits[:]) # print all elements.



# TUPLES: An immutable list is called a tuple, we use parentheses (instead of square brackets) with the presence of comma. 
rect_dimensions = (34, 44) # tuple
print(rect_dimensions[0]) # it can be accessed like a list
print(rect_dimensions[1])

# Looping Through All Values in a Tuple (Same with list)
for dimension in rect_dimensions:
    print(dimension)

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
# change.
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu
buff_resturant = ('jollof', 'beans', 'yam', 'noodles', 'fries')
for food in buff_resturant:
    print(food)

# buff_resturant.append('swallow') #AttriuteError

buff_resturant = ('jollof', 'sharwarma', 'swallow', 'noodles', 'fries')
for food in buff_resturant:
    print(food)