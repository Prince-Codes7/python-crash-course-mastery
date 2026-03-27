# Strings
name = "Booyah"
print(name)
print('This is also a string. ')

# Changing Case in Strings
name = "booyah pablo"
print(name.title()) # Booyah Pablo
print(name.upper()) # BOOYAH PABLO
print(name.lower()) # booyah pablo

# Combining or Concatenating Strings
first_name = 'booyah'
last_name = 'pablo'
full_name = first_name + " " + last_name
print( "Hi " + full_name.title() + "!")

# Adding Whitespace to Strings with Tabs or Newlines
print("\tPython") # tabs
print("Languages: \nPython\nC\nJavascript") # new lines

# Stripping Whitespace
favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())