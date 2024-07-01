# a set is an ordered collection of elements that can contain NO duplicates
# unordered - it has no indexes
# [] - list
# {k:v} - dictionary
# () - tuple
# {"Krillin"} - set - squiggly braces without k,v pairs

# Declaring a set
party_guests = {"Alice", "Bob", "Charlie"}
print(party_guests)
print(type(party_guests))

# Declaring an empty set
# {} <- reserved for dictionaries
# set()
empty_set = set()
print(empty_set)

# has no duplicates
ticket_numbers = {1, 2, 3, 4, 5, 5, 5, 5, 5}
print(ticket_numbers) # removes all by one 5

# removing duplicates from a list
ticket_numbers = [1, 2, 3, 3, 4, 4, 4, 5, 5, 6]
set_numbers = set(ticket_numbers)
print(set_numbers)
ticket_numbers = list(set_numbers)
print(ticket_numbers)

# set() - tuple or list to set
# tuple() - set or list to tuple
# list - set or tuple to list
tuple_guests = ("Alice", "Bob", "Charlies")
set_party = set(tuple_guests)
print(set_party)

# unique name party 
dict_guests = {
    "name1": "Alice",
    "name2": "Bob",
    "name3": "Alice"
}

print(dict_guests.values())
unique_name_party = set(dict_guests.values())
print(unique_name_party)

# sets are unordered so we cannot index into them
party_guests = {"Alice", "Bob", "Charlie"}
# print(party_guests[1]) TypeError - set object is not subscriptable

numbers = {10, 1, 4, 2, 3, 19, 17, 5}
sorted_nums = sorted(numbers)
print(sorted_nums)
numbers = set(sorted_nums)
print(numbers)

# Looping through sets
party_guests = {"Sydney", "Swathy", "Blake", "Jeremiah", "Stephen"}
for guest in party_guests:
    print(f"{guest} LOVES to party!")

# membership checks in sets
# if something in our_set:
#    do something

party_guests = {"Sydney", "Swathy", "Blake", "Jeremiah", "Stephen", "Jessica"}

if "Jessica" in party_guests:
    print("Jessica also LOVES to party")
else:
    print("Maybe Jessica loves to party, but she wasn't at this party.")

print(len(party_guests))

for thing, thing2 in enumerate(party_guests):
    print(thing, thing2)

# SET METHODS
# set.add()
# trying to apped to a set
party_guests = {"Sydney", "Swathy", "Blake", "Jeremiah", "Stephen", "Jessica"}
# party_guests.append("Anthony") set has not attribute appen
party_guests.add("Anthony")
print(party_guests)