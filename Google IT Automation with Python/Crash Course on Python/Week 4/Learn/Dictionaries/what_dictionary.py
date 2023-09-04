file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(type(file_counts))
print(file_counts)

print("-----------------------------------------------------")

print(file_counts["txt"])

print("-----------------------------------------------------")

file_counts["cfg"] = 8
print(file_counts)

print("-----------------------------------------------------")

file_counts["csv"] = 17
print(file_counts)

print("-----------------------------------------------------")

del file_counts["cfg"]
print(file_counts)