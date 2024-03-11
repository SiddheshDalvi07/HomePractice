string = input("enter the  word: ")
len  = len(string)
isPalindrome = True

for i in range(0, (len//2)):
    if string[i] != string[len-1-i]:
        isPalindrome = False
        break       #to stop checking further as we know that it's not a palindrome.
    
if isPalindrome == True:
    print ("The given word is a Palindrome")
else:
    print ("The given word is not a Palindrome")



# def is_palindrome(word):
#     length = len(word)
#     is_palindrome = True

#     for i in range(0, (length // 2)):
#         if word[i] != word[length - 1 - i]:
#             is_palindrome = False
#             break  # to stop checking further as we know that it's not a palindrome.

#     return is_palindrome

# word = input("Enter the word: ")
# if is_palindrome(word):
#     print("The given word is a Palindrome.")
# else:
#     print("The given word is not a Palindrome.")