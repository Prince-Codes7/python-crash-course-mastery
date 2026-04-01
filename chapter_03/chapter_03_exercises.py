# 1. Names: Store the names of a few of your friends in a list called names. Print
#each person’s name by accessing each element in the list, one at a time.

names = ['Jamal', 'Favour', 'Ayomide', 'Harlex', 'Samuel']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())

# 2.  Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message should be the same, 
# but each message should be personalized with the person’s name

print("\nHello " + names[0].title() + " I'm learning Python.")
print("Hello " + names[1].title() + " I'm learning Python.")
print("Hello " + names[2].title() + " I'm learning Python.")
print("Hello " + names[3].title() + " I'm learning Python.")
print("Hello " + names[4].title() + " I'm learning Python.")

# 3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”

motorcycle = ["Toyota", "Benz", "Lexus",]
print("\nI don't want to have " + motorcycle[0] + ".")
print("I might want to have " + motorcycle[1] + ".")
print("I will definitely have " + motorcycle[2] + ".")

# 4.  Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner

guest_list = ['Jamal', 'Favour', 'Samuel', 'Ayomide']
print(f"\nI'm inviting you {guest_list[0]} to my dinner party on Saturday. \nBring your laptop along don't forget for we have what to push. :)")
print(f"\nI'm inviting you {guest_list[1]} my dinner party on Saturday. \nPlease bring your laptop remember you will teach me and also check my projects.  :)")
print(f"\nI'm inviting you {guest_list[2]} my dinner party on Saturday. \nPlease bring resources :)")
print(f"\nI'm inviting you {guest_list[3]} my dinner party on Saturday. \nBring your friends along also. :)")

#  5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of
# your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in
# your list

print(f"\n{guest_list[3]} can't make it.")
guest_list[3] = 'Harlex'
# Second set of invitation.
print(f"\nI'm inviting you {guest_list[0]} to my dinner party on Saturday. \nBring your laptop along don't forget for we have what to push. :)")
print(f"\nI'm inviting you {guest_list[1]} my dinner party on Saturday. \nPlease bring your laptop remember you will teach me and also check my projects.  :)")
print(f"\nI'm inviting you {guest_list[2]} my dinner party on Saturday. \nPlease bring resources :)")
print(f"\nI'm inviting you {guest_list[3]} my dinner party on Saturday. \nBring your friends along also. :)")

# 6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

print(f"Hello all invitees I found a bigger table and I'll like to invite more people.")
guest_list.insert(0, 'Dbond')
guest_list.insert(3, 'Abiola')
guest_list.insert(-1, 'EmmyDee')
print(guest_list)
# New set of invitation
print(f"\nI'm inviting you {guest_list[0]} to my dinner party on Saturday. \nPlease bring foodstuffs:)")
print(f"\nI'm inviting you {guest_list[1]} to my dinner party on Saturday. \nBring your laptop along don't forget for we have what to push. :)")
print(f"\nI'm inviting you {guest_list[2]} to my dinner party on Saturday. \nPlease bring your laptop remember you will teach me and also check my projects.  :)")
print(f"\nI'm inviting you {guest_list[3]} to my dinner party on Saturday. \nPlease bring drinks along :)")
print(f"\nI'm inviting you {guest_list[4]} to my dinner party on Saturday. \nPlease bring resources :)")
print(f"\nI'm inviting you {guest_list[5]} to my dinner party on Saturday. \nPlease bring small chops along. :)")
print(f"\nI'm inviting you {guest_list[6]} to my dinner party on Saturday. \nBring your friends along also. :)")


# 7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print a
# message to that person letting them know you’re sorry you can’t invite them
# to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end of
# your program.

print(f"\nI'm sorry to inform you all I can't invite you all due to limited space")
# Guests no longer invited
dbond_popped = guest_list.pop(0) # removed 'Dbond'
print(f"I'm sorry {dbond_popped} you're no longer invited as there are limited space")

abiola_popped = guest_list.pop(2) # removed 'Abiola'
print(f"I'm sorry {abiola_popped} you're no longer invited as there are limited space")

emmydee_popped = guest_list.pop(3) # removed 'EmmyDee'
print(f"I'm sorry {emmydee_popped} you're no longer invited as there are limited space")

samuel_popped = guest_list.pop(2) # removed 'Samuel'
print(f"I'm sorry {samuel_popped} you're no longer invited as there are limited space")

harlex_popped = guest_list.pop(2) # removed 'Harlex'
print(f"I'm sorry {harlex_popped} you're no longer invited as there are limited space")

# Guests still invited
print(f"\nThis is to inform you {guest_list[0]} that you're still invited to the dinner")
print(f"This is to inform you {guest_list[1]} that you're still invited to the dinner")

# Deleting the lists
del guest_list[0] # Deleting the 'Jamal'
del guest_list[0] # Deleting the 'Favour'

print(guest_list)


# 8. Seeing the World: Think of at least five places in the world you’d like
# to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly;
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.

places_to_visit = ['usa', 'germany', 'japan', 'canada', 'brazil']

print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)
print("\n")

print(sorted(places_to_visit, reverse = True))
print(places_to_visit)

places_to_visit.reverse() # change the order of your list
print(places_to_visit)
places_to_visit.reverse() # back to its original order
print(places_to_visit)
print("\n")

places_to_visit.sort() # order has been changed in alphabetical order
print(places_to_visit)

places_to_visit.sort(reverse = True) # order has been changed in reverse-alphabetical order
print(places_to_visit)

#  9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (pages 41–42), use len() to print a message indicating the number
# of people you’re inviting to dinner.
names = ['Jamal', 'Favour', 'Ayomide', 'Harlex', 'Samuel']
print(f"I'm inviting {len(names)} guests to my dinner")

# 10. Every Function: Think of things you could store in a list. For example, you
# could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items and
# then uses each function introduced in this chapter at least once.
print("\n")
languages = ['igbo', 'yoruba', 'efik', 'hausa', 'ibibio']
print(languages)
print("One more language I'll like to add: 'igala' ")
#languages.insert(len(languages), 'igala')
# or
languages.append('igala')
print(languages)
print("\n")

popped_languages = languages.pop(4)
print(languages)
print(f"I can't speak {popped_languages.title()}")
print("\n")

print(f"I haven't seen anyone that can speak the {len(languages)} languages")
print("The languages in alphabetical order are: ")
print(sorted(languages))
print("The languages in reverse alphabetical order are: ")
print(sorted(languages, reverse = True))
print("\n")

print("The original languages apart from the one I can't speak in the reverse order are: ")
languages.reverse()
print(languages)
print("The original languages apart from the one I can't speak in the original order are: ")
languages.reverse()
print(languages)
print("\n")

print(f"Surprisingly I can only speak one out the {len(languages)} of them. \nThe only one I can speak is {languages[0]}. ")
