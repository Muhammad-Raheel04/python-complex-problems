# Given a string 
# sentence = "The quick brown fox jumps
# over the lazy dog", use a set comprehension 
# to extract all unique vowels (a, e, i, o, u)
# present in the sentence. Ignore case.

sentence = "The quick brown fox jumps ovEr the lazy dog"
vowelLetters=["a","e","i","o","u"]

vowels={s for s in sentence if s.lower() in vowelLetters}
print(vowels)


