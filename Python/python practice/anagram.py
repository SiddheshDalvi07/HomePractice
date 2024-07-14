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


#without function 

def anagrams(string1, string2):
    
    string1 = string1.lower()
    string2 = string2.lower()

    if len(string1) != len(string2):
        return False
    
    count1 = {}
    count2 = {}

    for char in string1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1

    for char in string2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1

    return count1 == count2


string1 = "listen"
string2 = "silent"

if anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
