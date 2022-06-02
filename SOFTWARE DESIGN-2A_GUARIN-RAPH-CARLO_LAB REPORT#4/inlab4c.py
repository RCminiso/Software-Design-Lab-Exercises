# function which accepts the given string as an argument and
# reverse the given string using recursion and return the reversed string
def reverseRecursion(given_string):
   # Calculate the length of the given string using the len() function.
    stringLen = len(given_string)
    # if len(str1) == 1 is used to check the length of the string, which is the fundamental condition of recursion. If                  the length of the string is 1,
    # the string is returned, otherwise, the function is called recursively.
    if stringLen == 1:
        return given_string
    else:
      # The slice operator will slice the string and concatenate it to the end of the
      # slice string if it anticipates the first character.
        return reverseRecursion(given_string[1:]) + given_string[0]

# Give the string from the user as static input and store it in a variable.
givenstring = 'btechgeeks'
# printing the original given string
print('The original given string =', givenstring)
# passing the given string as an argument to the recursive function
# 'reverseRecursion' which reverses the given string.

print('The modified given string{after reversing} = ',
      reverseRecursion(givenstring))
