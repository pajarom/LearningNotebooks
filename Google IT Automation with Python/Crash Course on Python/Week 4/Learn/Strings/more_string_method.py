print("Mountains".upper())
print("Mountains".lower())

answer = "YES"
if answer.lower() == "yes":
    print("User said yes")

print(" yes ".strip())
print(" yes ".lstrip())
print(" yes ".rstrip())

print("The number of times e occurs in this string is 4".count("e"))

print("Forest".endswith("for"))
print("Forest".endswith("rest"))
print("Forest".isnumeric())

print("1123".isnumeric())

print(int("12345") + int("54321"))

print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))

print("This is another example".split())