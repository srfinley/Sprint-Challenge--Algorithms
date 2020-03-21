'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    if len(word) < 2:
        return 0
    
    check = word[0:2]
    remainder = word[1:]
    if check == 'th':
        rest = count_th(remainder)
        return 1 + rest
    
    return count_th(remainder)
