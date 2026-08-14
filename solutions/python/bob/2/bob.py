def response(hey_bob):
    response = hey_bob.strip()
    if not response:
        return "Fine. Be that way!"
    if response.endswith("?"):
        if response.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if response.isupper():
        return "Whoa, chill out!"
    return "Whatever."
    
    
