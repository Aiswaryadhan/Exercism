def rotate(text, key):
    result = []
    for c in text:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            result.append(chr((ord(c) - base + key) % 26 + base))
        else:
            result.append(c)
    return "".join(result)