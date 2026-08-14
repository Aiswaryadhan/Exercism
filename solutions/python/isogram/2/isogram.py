def is_isogram(phrase):
    unique_letters = phrase.lower().replace("-","").replace(" ","")
    return len(unique_letters)==len(set(unique_letters))
