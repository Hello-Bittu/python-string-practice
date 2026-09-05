# Q6.2. Take a string as user input and check whether
# it is a palindrome.

str1 = "madam"

if(str1 == str1[::-1]):
    print("This string is a palindrome.")
else:
    print("This string is not a palindrome.")