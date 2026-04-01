# CHAPTER 3 - INTRODUCING LISTS
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# ACCESING ELEMENTS IN A LIST
# We use indexes to access elements in list
print(bicycles[0])      # trek
print(bicycles[1])      # cannondale
print(bicycles[-1])     # specialized (last item) or print(bicycles[3])

print("The first bicycle element is " + bicycles[0].title() + ".")


# Modifying, Adding, and Removing Elements in a List.

#__________________________________________________________________________________________________
# Modifying Elements in a List. (use index and re-assign)
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles[0] = 'ducati'
print(motocycles)

# Adding Elements in a List. (use append() method)
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles.append('ducati')
print(motocycles)

#___________________________________________________________________________________________________
# Inserting Elements in a List. (use insert(index, value))
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles.insert(0, 'ducati')
print(motocycles)

#______________________________________________________________________________________________________
# Removing Elements in a List.
# We have 3 methods:
# 1. del statement
# 2. pop() method
# 3. removing method by value( remove() )

# 1. using del statement
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

del motocycles[0] # deletes 'honda'
print(motocycles) 


# 2. Using pop() method
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

popped_motocycles = motocycles.pop() # removes last item and assign it to popped_motocycles
print(motocycles)
print(popped_motocycles)

# We can also pop from any position in a list
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

popped_motocycles = motocycles.pop(1) # removes the second item and assign it to popped_motocycles
print(motocycles)
print(popped_motocycles)

#______________________________________________________________________________________
# 3. removing method by value( remove() )
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles.remove('honda') # remove 'honda' from the list
print(motocycles)

# ______________________________________________________________________________________

# ORGANISING A LIST
# ______________________________________________________________________________________
# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # alphabetical order
print("\n")
print(cars)

cars.sort(reverse = True) # alphabetical order in the reverse
print(cars)

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars)) # Temporarily sorts alphabetically
print(sorted(cars, reverse = True))
print(cars)

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
print(len(cars))