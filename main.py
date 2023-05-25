"""
You are given a list of strings representing a paragraph of text.
Your task is to write a Python function called word_frequency that
takes in this list as an argument and returns a dictionary where
the keys are unique words in the paragraph, and the values are the frequencies of those words.

Consider the following requirements:

-The function should treat words in a case-insensitive manner. For example, "apple" and "Apple" should be considered the same word.
-The function should strip leading and trailing whitespace from each word.
-The function should exclude any punctuation marks attached to words. For example, "apple." and "apple," should be considered the same word "apple".
-The function should exclude empty strings as words.
-The function should aim for an optimal time complexity.

"""

"""
    Translator solution
"""


import string

def word_frequency(paragraph):

    # Create a translator to remove punctuation marks
    translator = str.maketrans("", "", string.punctuation)
    word_freq = {}

    # Iterate over each sentence in the paragraph
    for sentence in paragraph:

        # Convert the sentence to lowercase, remove punctuation marks, and split into words
        words = sentence.lower().translate(translator).split()
        
        # Iterate over each word
        for word in words:
            
            # Update the word frequency in the dictionary
            word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq


"""
    Regular expression solution
"""

import re
from collections import defaultdict

def word_frequency2(paragraph):

    # Create a dictionary to store word frequencies
    frequency = defaultdict(int)
    
    # Iterate over each sentence in the paragraph
    for sentence in paragraph:
        # Find all words in the sentence and convert them to lowercase
        words = re.findall(r'\b\w+\b', sentence.lower())
        
        # Increment the frequency of each word
        for word in words:
            frequency[word] += 1
    
    # Convert the defaultdict to a regular dictionary and return it
    return dict(frequency)

paragraph = [
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
]

frequency = word_frequency(paragraph)

#frequency2 = word_frequency2(paragraph)

print(frequency)

#print(frequency2)
