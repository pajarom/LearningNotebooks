# message = "A kong string with a silly typo"
# print(message[2])
# new_message = message[0:2] + "l" + message[3:]
# print(new_message)

# pets = "Cats & Dogs"
# print(pets.index("&"))

# print("Dragon" in pets)
# print("Cats" in pets)

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email