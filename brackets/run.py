# setup
def is_valid_bracket(inp_str):

    # array of relevant values
    validity = []

    # break down inp_str to just the chars we care about
    for char in inp_str:
        typeof = is_open(char)
        if typeof == True:
            validity.append(char)
        elif typeof == False:
            validity.append(char)

    # break down input
    disolve(validity)

    # if there is anything left after disolve(), the input is invalid
    if len(validity) > 0:
        return 'invalid'
    else:
        return 'valid'

# recursive fn, it will erase any values next to eachother that are valid
def disolve(validity):

    no_disolve = True

    # look for first valid pair to disolve
    for i in range(1, len(validity)):
        if is_open(validity[i]) == False:
            if validity[i-1] == get_opposite(validity[i]):
                validity.pop(i)
                validity.pop(i-1)
                no_disolve = False
                break

    # if nothing left to do, return
    if no_disolve:
        return
    else:
        disolve(validity)

# if char is open bracket return True
# if char is closed bracket return False
# else if normal character, return None
def is_open(char):
    if char == '(' or char == '[' or char == '{':
        return True
    elif char == ')' or char == ']' or char == '}':
        return False
    else:
        return None

# if bracket, will return the 'sister-bracket'
def get_opposite(char):
    if char == '(':
        return ')'
    if char == ')':
        return '('
    if char == '{':
        return '}'
    if char == '}':
        return '{'
    if char == '[':
        return ']'
    if char == ']':
        return '['

