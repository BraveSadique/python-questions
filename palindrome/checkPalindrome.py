def is_palindrome(input_string):
    # Remove spaces and convert to lowercase
    cleaned_string = input_string.replace(" ", "").lower()
    
    # Compare the original string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Input string to check for palindrome
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
