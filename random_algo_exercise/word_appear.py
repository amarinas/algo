# Return the number of times that the string "code" appears anywhere in the given string,
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.
# countCode("aaacodebbb") - 1
# countCode("codexxcode") - 2
# countCode("cozexxcope") - 2

def word_appear(str):
    count = 0
    oldstr = str.split("")
    for i in range(len(oldstr)):
        if oldstr[i] == "c":
            temp = oldstr.slice(i, i+4)
            count += 1

    return count


print(word_appear("codexxcode"))
