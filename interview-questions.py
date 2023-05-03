
# Level of dificulty: Easy
# Problem A
# Write a Python function to check if a string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. 
def is_palindrome(word, reverse_word):
    if word == reverse_word[::-1]:
        print('it is')
    else:
        print('is not')

word = input('enter word: ')
reverse_word = input('enter new word to check if its a palindrome: ')
is_palindrome(word, reverse_word)

# Problem B 
# Find the maximun ocurring character in a given string
my_string = input('Enter string: ')
#Create an empty dictionary to que track of the count of each character in the string
char_counts = {}
for char in my_string:
    char_counts[char] = char_counts.get(char, 0) + 1
if char == 0:
    print('there is a most frequent character in my string')
else:
    print('There is not a most frequent character in the string')
max_char = max(char_counts, key=char_counts.get)
print(f'The most frequent character in "{my_string}" is "{max_char}"')
   
#give an example of Computing the sum of the digits of a given integer number in pyhon
number = 12345
sum_of_digits = 0

while number > 0:
    sum_of_digits += number % 10
    number //= 10

print("The sum of digits is:", sum_of_digits)



# Difficulty: Meduim
# Problem A
# Given a list of integers, write a function to find the largest sum of any contiguous subarray within the list.

def max_subarray_sum(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# Problem B
def longest_substring_without_repeating(s):
    max_len = 0
    start = 0
    char_map = {}

    for i in range(len(s)):
        if s[i] in char_map and start <= char_map[s[i]]:
            start = char_map[s[i]] + 1
        else:
            max_len = max(max_len, i - start + 1)
        char_map[s[i]] = i

    return max_len



