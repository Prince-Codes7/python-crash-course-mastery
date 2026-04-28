# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza,
# instead of printing just the name of the pizza. For each pizza, you should
# have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!

# 1
favorite_pizzas = ['pepperoni', 'margherita', 'sicilian', 'grandma', 'new_york-style']
for favorite_pizza in favorite_pizzas:
    print(f"{favorite_pizza} pizza.")
print("\n")

# 2
favorite_pizzas = ['pepperoni', 'margherita', 'sicilian', 'grandma', 'new_york-style']
for favorite_pizza in favorite_pizzas:
    print(f"I like {favorite_pizza} pizza!")
print("\n")

# 3
print("I really like how nutritious pizza tastes. \nIt tastes better with a chilled soft drink especially yoghurt.")
print("I really enjoy pizzas")
print("wait :) with yoghurt! 😊😊😊")
print("\n")



# 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A
# dog would make a great pet.
# • Add a line at the end of your program, stating what these animals have in
# common. You could print a sentence, such as Any of these animals would
# make a great pet!

# 1
animals = ['lion', 'tiger', 'cheetah']
for animal in animals: 
    print(animal)
print("\n")

# 2
animals = ['lion', 'tiger', 'cheetah']
for animal in animals: 
    print(f"A {animal.title()} is a good hunter")
print("\n")

# 3
print("These animals share the following common characteristics: ")
print("1. They are all members of the Felidae family (cats).\n")
print("2. They are all carnivores, feeding on other animals.\n")


# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.
for value in range(1, 21):
    print(value)



# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing CTRL-C or by closing the output window.)
millions_list = list(range(1, 1000001))
#for million in millions_list:
#    print(million)


# 4-5. Summing a Million: Make a list of the numbers from one to one million, and
# then use min() and max() to make sure your list actually starts at one and ends
# at one million. Also, use the sum() function to see how quickly Python can add
# a million numbers.
millions_list = list(range(1, 1000001))
print(max(millions_list))
print(min(millions_list))
print(sum(millions_list))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.
odd_numbers = list(range(1, 21, 2))
for odd_number in odd_numbers:
    print(odd_number)


# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to
# print the numbers in your list.
threes = list(range(3, 31, 3))
for three in threes:
    print(three)


# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube
cubes = [value ** 3 for value in range(1, 11)]
for cube in cubes:
    print(cube)


# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first
# 10 cubes.
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Then use a
# slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice to
# print the last three items in the list
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
print("The first three items in the cubes list are: ")
print(cubes[:3])

print("The three middle items in the list are:")
print(cubes[4:7])

print("The last three items in the list are:")
print(cubes[-3:])


# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the
# following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My
# friend’s favorite pizzas are:, and then use a for loop to print the second list.
# Make sure each new pizza is stored in the appropriate list.
favorite_pizzas = ['pepperoni', 'margherita', 'sicilian', 'grandma', 'new_york-style']
friend_pizzas = favorite_pizzas[:]
print(friend_pizzas)
favorite_pizzas.append('choco')
friend_pizzas.append('vanilla')

print("My favorite pizzas are: ")
for favorite_pizza in favorite_pizzas:
    print(favorite_pizza)

print("My friend’s favorite pizzas are: ")
for friend_pizza in friend_pizzas:
    print(friend_pizza)