# Q2.1. Given text = "Python Programming":
# Print the first 6 characters of the string.
# Print the last 6 character of the string.
# Print every second character of the string


text = "Python Programming"
print(text[0:6])
print(text[-6:]) # This goes to -6 to length of the string ie. [-6:18] 

print(text[::2]) # Skip the character 2 -1 = 1.
print(len(text))
