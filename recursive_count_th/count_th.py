'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC

    # base case, if the word is less than 2 then "th" can't be in it
    if len(word) < 2:
        return 0
    else:
        # if the first two elements have "th" recursive call it which will look through the word again on all but the first element and add 1 for count
        if word[:2] == "th":
            return count_th(word[1:]) + 1
        # if the first two elements don't have "th" recursive call it on all but first element
        else:
            return count_th(word[1:])
