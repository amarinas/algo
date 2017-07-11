def r(s):
    ns = "" # New string to be returned
    a = s.split(' ') # Split string into list of words
    # Iterate through list of words
    for w in a:
        # If word is "is"
        if w == "is":
            # Add "is not" to the new string
            ns += "is not "
        else:
            # Add word to new string
            ns += w + " "
    return ns

s=raw_input()
print r(s)
