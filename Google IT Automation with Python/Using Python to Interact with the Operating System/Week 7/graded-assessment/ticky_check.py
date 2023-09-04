#!/usr/bin/env python3
import re
import operator
import csv
import os

# Initialize the dictionary
error = {}
per_user = {}

# Open the log file
with open("syslog.log", "r") as file:
    for line in file.readlines():
        # Extract the username
        username = re.search(r"\((.*)\)", line).group(1)
        # Extract the error type
        error_type = re.search(r"ERROR|INFO", line).group(0)
        # Extract the error message
        error_message = re.search(r"ERROR|INFO (.*) ", line).group(1)

        # Count the error type
        if error_type == "ERROR":
            if error_message not in error:
                error[error_message] = 0
            error[error_message] += 1

        # Count the user
        if username not in per_user:
            per_user[username] = {}
            per_user[username]["INFO"] = 0
            per_user[username]["ERROR"] = 0
        per_user[username][error_type] += 1

# Sort the dictionary
error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
per_user = sorted(per_user.items())
print(per_user)
print(error)

# Write the error message to error_message.csv
with open("error_message.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Error", "Count"])
    writer.writerows(error)

# Write the user statistics to user_statistics.csv
with open("user_statistics.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "INFO", "ERROR"])
    for item in per_user:
        writer.writerow([item[0], item[1]["INFO"], item[1]["ERROR"]])