programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
    }

# Retrieving data from dictionary.
print(programming_dictionary["Bug"])

# Adding new item ot dictionary
programming_dictionary["Loop2"] = "Hello"

# programing_dictionary = {}
# programing_dictionary["Bug"] = "Moth in a computer"

for thing in programming_dictionary:
    print(thing)