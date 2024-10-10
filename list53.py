
import string

input_string = 'Python'
words = ''.join(char for char in input_string if char not in string.punctuation).split()
hashtag = '#' + ''.join(word.capitalize() for word in words)

if len(hashtag) >= 140:
    hashtag = hashtag[:140]
print(hashtag)