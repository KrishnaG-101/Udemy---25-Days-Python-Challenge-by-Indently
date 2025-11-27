# Since in the password checker we are only allowing passwords more than 8 characters of length.
# We will update the common passwords file to only contain common passwords which are longer than 8 characters.
# This file creates a copy of common_passwords.txt which will only contain password longer than 8 characters.

with open("common_passwords.txt", "r", encoding="utf-8") as main_file:
    common_passwords_long : list[str] = [line for line in main_file if len(line) > 8]
    
# checking if this is correct
print(common_passwords_long)
print(len(common_passwords_long))
# on checking found that >= 8 will also count \n so making it > 8 in the condition only.

with open("common_passwords_long.txt", "x", encoding="utf-8") as copy_file:
    copy_file.write("".join(common_passwords_long))

# It worked and the file got created.