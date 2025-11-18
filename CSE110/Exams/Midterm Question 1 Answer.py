string = input()
digit_string = '0123456789'
vowel_string = 'aeiou'
digit_count = 0
vowel_count = 0
consonant_count = 0

for char in string:
    if 97 <= ord(char) <= 122:
        if char in vowel_string:
            vowel_count += 1
        else:
            consonant_count += 1
    elif char in digit_string:
        digit_count += 1

print("Number of Vowels:", vowel_count)
print("Number of Consonant:", consonant_count)
print("Number of Digits:", digit_count)
