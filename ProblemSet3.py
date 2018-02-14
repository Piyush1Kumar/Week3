
def isWordGuessed(secretWord, lettersGuessed):

""" 
secretWord : word that the user is guessing
lettersGuessed : letters that have been guessed so far
returns true if all the letters guessed are present in secretWord
"""

    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):

"""
returns : string, comprised of letters and underscores indicating what letters
          in secretWord have been guessed so far.
"""

    ans = ''
    for x in secretWord:
        if x in lettersGuessed:
            ans = ans + x
        else:
            ans = ans + '_'
    return ans

def getAvailableletters(lettersGuessed):

""" returns : a string of letters that have not been guessed by the user so far.
"""

    ans = ''
    for x in 'abcdefghijklmnopqrstuvwxyz':
        if x not in lettersGuessed:
            ans = ans + x
    return ans