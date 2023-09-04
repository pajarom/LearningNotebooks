[1]
def confirm_length(word):

    # Complete the condition statement using a string operation. 
    if len(word) > 0:
        # Complete the return statement using a string operation.
        return len(word) 
    else:
        return 0


print(confirm_length("a")) # Should print 1
print(confirm_length("This is a long string")) # Should print 21
print(confirm_length("Monday")) # Should print 6
print(confirm_length("")) # Should print 0

[2]
def string_words(string):
    # Complete the return statement using both a string operation and 
    # a string method in a single line.
    return len(string.split())


print(string_words("Hello, World")) # Should print 2
print(string_words("Python is awesome")) # Should print 3
print(string_words("Keep going")) # Should print 2
print(string_words("Have a nice day")) # Should print 4

[3]
def combine_lists(list1, list2):


  combined_list = ___ # Initialize an empty list variable
  Reverse_list = list1[::-1] # Reverse the order of "list1"
  ___ # Combine the two lists 
  combined_list = list2 + Reverse_list
  return combined_list  
  
Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]


print(combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']

[4]
def increments(start, end):
    return [ n + 2 for n in range(start, end+1) ] # Create the required list comprehension.


print(increments(2, 3)) # Should print [4, 5]
print(increments(1, 5)) # Should print [3, 4, 5, 6, 7]
print(increments(0, 10)) # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

[5]
def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.    
    for animals, population in animal_dict.items(): 
        # Use a string method to format the required string.
        result += "{} \n".format(animals)
    return result


print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger

[6]
def setup_guests(guest_list):
    # loop over the guest list and add each guest to the dictionary with
    # an initial value of 0
    result = {} # Initialize a new dictionary 
    for guest in guest_list: # Iterate over the elements in the list 
        result[guest] = 0 # Add each list element to the dictionary as a key with 
            # the starting value of 0
    return result

guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]

print(setup_guests(guests))
# Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}

[7]
def count_letters(text):
  # Initialize a new dictionary.
  dictionary = {} 
  # Complete the for loop to iterate through each "text" character and 
  # use a string method to ensure all letters are lowercase.
  for character in text:   
    character = character.lower()
    # Complete the if-statement using a string method to check if the
    # character is a letter.
    if character.isalpha():
      # Complete the if-statement using a logical operator to check if 
      # the letter is not already in the dictionary.
      if character not in dictionary:
           # Use a dictionary operation to add the letter as a key
           # and set the initial count value to zero.
           dictionary[character] = 0
      # Use a dictionary operation to increment the letter count value 
      # for the existing key.
      dictionary[character] += 1 
       # Increment the letter counter. 
    
  return dictionary

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

[8]
car_make = "Lamborghini"
print(car_make[3:-5])
print(car_make[-4:])
print(car_make[:7])

[9]
colors = ["red", "white", "blue"]
colors.insert(2, "yellow")

[10]
teacher_names = {"Math": "Aniyah Cook", "Science": "Ines Bisset", "Engineering": "Wayne Branon"}
teacher_names.values()