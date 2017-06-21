
def check_braces(expression):
    open_braces = ['(', '[', '{']
    closed_braces = [')', ']', '}']
    q = []


    for char in expression:

        if char in open_braces: # Push the stack
            q.append(char)

        else: # It's a closed brace.

            if len(q) == 0: # First bracket closed/extra closed brackets

                return 0



            if closed_braces.index(char) != open_braces.index(q.pop()):

                return 0

            else:
                return 1





expressions = [ ")(){}", "[]({})", "([])", "{()[]}", "([)]" ]



for expression in expressions:

    print check_braces(expression)
