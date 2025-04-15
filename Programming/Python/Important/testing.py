import re

def respaceWithReconstruction(dictionary: list, sentence: str):
    unrecognized_count = 0
    edited_sentence = sentence  # found words will be removed from placeholder

    # Use regex to search for each word in dictionary
    search_pattern = [f'(?:{word})' for word in dictionary if word] # regex search pattern; ['(?:looked)', '(?:just)', '(?:like)', '(?:her)', '(?:brother)']
    search_pattern = re.compile('|'.join(search_pattern))
    found_words = re.findall(search_pattern, sentence)

    # found list is sorted from longest to shortest to account for occurrences of substrings
    sorted_words = sorted(found_words, key=len, reverse=True)

    # loop through and remove each word from the sentence placeholder
    for word in sorted_words:
        edited_sentence = edited_sentence.replace(word, ' ')

    remaining_words = [word for word in edited_sentence.split() if word.strip() != ""] # remove empty spaces in list to isolate names/unknown words
    for name in remaining_words: # referring to unknown words as names since only proper nouns are not in dictionary
        unrecognized_count += len(name)
        sentence = sentence.replace(name, name.upper())

    return unrecognized_count, sentence


DICTIONARY = ["looked", "just", "like", "her", "brother"]
SENTENCE = "jesslookedjustliketimherbrother"



count, reconstructed = respaceWithReconstruction(DICTIONARY, SENTENCE)
print("Unrecognized letters: " + str(count))
print("Reconstructed sentence: " + reconstructed)