import string
def is_pangram(sentence):
    lower_sentence = sentence.lower()
    return all(char in lower_sentence for char in string.ascii_lowercase)
