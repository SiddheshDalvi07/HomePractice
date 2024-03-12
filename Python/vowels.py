# def remove_vowels(input_string):
#     vowels = "aeiouAEIOU"
#     return ''.join(char for char in input_string if char not in vowels)

# input_string = input("Enter a string: ")
# print("String after removing vowels:", remove_vowels(input_string))


def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    modified_string = ''
    for char in input_string:
        if char not in vowels:
            modified_string += char
    return modified_string

input_string = input("Enter a string: ")
print("String after removing vowels:", remove_vowels(input_string))