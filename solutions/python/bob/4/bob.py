def response(hey_bob):
    question = hey_bob.strip()
    if not question:
        return "Fine. Be that way!"
    if question.endswith("?"):
        if question.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if question.isupper():
        return "Whoa, chill out!"
    return "Whatever."