#  Count Vowels
string = "hello world"

vowel_count = {}
vowels = "aeiou"

for char in string:
    if char in vowels:
        vowel_count[char] = vowel_count.get(char, 0) + 1
        
print(vowel_count)        
