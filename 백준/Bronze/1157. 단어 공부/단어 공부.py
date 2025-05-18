import string

text = input().upper()

alphabets = {}

for char in text:
    if char in string.ascii_uppercase: 
        alphabets[char] = alphabets.get(char, 0) + 1

maximum = max(alphabets.values())

candidates = [char for char, count in alphabets.items() if count == maximum]

if len(candidates) == 1:
    print(candidates[0])
else:
    print('?')
