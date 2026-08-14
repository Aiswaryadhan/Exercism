def response(hey_bob):
    if hey_bob.endswith("?"):
        if hey_bob.isupper:
            return "Sure."
        return "Calm down, I know what I'm doing!"
    
    if hey_bob.isupper():
        return "Whoa, chill out!"

    if not hey_bob.strip():
        return "Fine. Be that way!"

    return "Whatever."
    
    
