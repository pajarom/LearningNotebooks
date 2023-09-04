fruits = ["Pineapple", "Banana", "Apple", "Melon"]
print(fruits)
fruits.append("Kiwi") # added new data
print(fruits)
fruits.insert(0, "Orange")
print(fruits)
fruits.insert(25, "Peach")
print(fruits)
print(len(fruits))
fruits.remove("Melon")
print(fruits)

print(fruits.pop(2)) # removing data
print(fruits)
fruits[2] = "Strawberry"
print(fruits)