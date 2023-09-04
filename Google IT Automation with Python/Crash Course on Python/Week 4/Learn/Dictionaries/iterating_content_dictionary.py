file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)

print("-----------------------------------------------------")

for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))

print("-----------------------------------------------------")

print(file_counts.keys())

print("-----------------------------------------------------")

print(file_counts.values())

print("-----------------------------------------------------")

for value in file_counts.values():
    print(value)

print("-----------------------------------------------------")

def count_letter(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result
print(count_letter("tenant"))
print(count_letter("a long string with a long letters"))

print("-----------------------------------------------------")
