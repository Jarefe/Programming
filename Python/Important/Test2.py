# 1) pass in string and search for words in dictionary
# 2) remove recognized text from sentence string
# 3) reinsert unrecognized text (names) back in fully capitalized
# 4) return unrecognized count and reconstructed text

DICTIONARY = ["looked", "just", "like", "her", "brother"]
SENTENCE = "jesslookedjustliketimherbrother"

import re

def respaceWithReconstruction(dictionary: list, sentence: str):
    unrecognized_count = 0
    edited_sentence = sentence  # found words will be removed from placeholder

    # use regex to search for each word in dictionary and store in list
    # (?: prevents function from returning list of tuples; instead returns list of strings
    search_pattern = [f'(?:{word})' for word in dictionary if word] # regex search pattern; ['(?:looked)', '(?:just)', '(?:like)', '(?:her)', '(?:brother)']
    search_pattern = re.compile('|'.join(search_pattern), re.IGNORECASE)
    found_words = re.findall(search_pattern, sentence)

    # list is sorted from longest to shortest to account for occurrences of substrings
    sorted_words = sorted(found_words, key=len, reverse=True)

    # loop through and remove each word from the sentence placeholder
    word_placeholder = []
    for word in sorted_words:
        word_placeholder.append(word)
        edited_sentence = edited_sentence.replace(word, ' ')
        sentence = sentence.replace(word, f'{word} ') # add space between words in original sentence

    # get rid of empty spaces and isolate remaining words
    remaining_words = [word for word in edited_sentence.split() if word.strip() != ""] # remove empty spaces in list to isolate names/unknown words

    # replace names (unknowns) in all caps and with space
    for name in remaining_words: # referring to unknown words as names since only proper nouns are not in dictionary
        unrecognized_count += len(name)
        sentence = sentence.replace(name, f'{name.upper()} ')

    # remove trailing whitespace
    sentence = sentence.strip()

    return unrecognized_count, sentence

count, reconstructed = respaceWithReconstruction(DICTIONARY, SENTENCE)
print("Unrecognized letters: " + str(count))
print("Reconstructed sentence: " + reconstructed)
