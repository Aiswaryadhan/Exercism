def is_isogram(phrase):
    no_of_special_chars = phrase.count(" ") + phrase.count("-")
    unique_letters = set(phrase.lower().replace("-","").replace(" ",""))
    return (len(unique_letters)+no_of_special_chars)==len(phrase)
