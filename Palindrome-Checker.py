string = input("Enter a string: ")
new_string = list(string)

reversed(string)
reverse_string = "".join(new_string)

if string == reverse_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
