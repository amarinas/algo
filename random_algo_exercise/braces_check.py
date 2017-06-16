# check the array to see if the secquence of type braces are valid

def braket(arr):
    newarr = [] #set a newarr a temporary placeholder to help determine if its valid
    if arr[0] == "]" or arr[0] == ")" or arr[0] == "}" or len(arr) % 2 == 1: # quick exit base case to see if the array is valid
        return False
    else:
        newarr.append(arr[0]) # appended the first value

    for i in range(1, len(arr)): # iterate through the array
        # print "newarr value is ", newarr
        if arr[i] == "]" or arr[i] == ")" or arr[i] == "}": # look for right braces
            if newarr[-1] == "[" and arr[i] == "]" or newarr[-1] == "(" and arr[i] == ")" or newarr[-1] == "{" and arr[i] == "}": # once found match with the last index in the newarr
                # print "newarr before pop ", newarr
                newarr.pop() # if it matched we remove from the newarr
                continue # continue so it will go back to the loop and not break

            else:
                # print "11111111111"
                return False
                # print "new after", newarr
        newarr.append(arr[i]) # if its not any of the right braces then just append

    if len(newarr) == 0: # check to see if newarr is empty when its empty then we know all braces are valid
        return True
    else:
        # print "22222222"
        # print newarr
        return False # braces are n                                    ot valid cause the newarr is not empty



print(braket(["[", "(", "{", "}", "]", ")"]))
print(braket(["[", "(", "{", "}", ")", "]"]))
print(braket([ "[", "]" ]))
