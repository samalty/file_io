# The re library is for regular expressions, and the collections library counts the occurrence of words

import re
import collections

# Next, we read everything into a string called text, using the read method
# Then we use the regular expressions findall() method, which ensures that all occurrences of the pattern are found. Our pattern here is \w+. The w denotes anything that isn't a whitespace, and the + denotes one or more. 
# So for every occurrence of one or more characters that are not whitespace, we view is as a word.
# Next we use the counter method from our collections library, and instruct it to find the 10 most common words

text = open('book.txt').read().lower()
words = re.findall('\w+', text)
print(collections.Counter(words).most_common(10))