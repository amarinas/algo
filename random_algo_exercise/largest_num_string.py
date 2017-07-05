# Find the sentence containing the largest number
# of words in some given text. The text is specified
# as a string S consisting of N characters: letters,
# spaces, dots (.), question marks (?) and exclamation
# marks (!).

def solutions(S):
    sentences= []
    string= ""

    for char in S:
        if char == "." or char == "!" or char == "?":

            sentences.append(string)
            # print sentences
            string = ""
        else:
            string = string + char

    words_len = 0
    for i in sentences:
        words = i.split()
        if len(words) > words_len:
            words_len = len(words)
    return words_len




S1 = "We test coders. Give us a try?"
print(solutions(S1))
S2 = "Forget CVs..Save time . x x"
print "Largest number of words:", solutions(S2)
