def anagram(str1, str2):
    # Check if lengths are different
    if len(str1) != len(str2):
        return False
    
    # Convert both strings to lowercase, sort them, and compare
    s1 = ''.join(sorted(str1.lower()))
    s2 = ''.join(sorted(str2.lower()))
    print(s1)
    print(s2)
    
    return s1 == s2

# Get input from user
str1 = input("Enter the first word: ")
str2 = input("Enter the second word: ")

# Check if the strings are anagrams and print the result
if anagram(str1, str2):
    print("Anagram")
else:
    print("Not anagram")
