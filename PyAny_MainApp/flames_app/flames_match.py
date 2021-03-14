# Import needed library
import numpy as np

def match_results(yourName,crushName):
    '''
    Function description here:
    Enter the names and find out how you two are destined to be.
    '''
    # split characters and turn into list
    yourNameChars = [char for char in yourName]

    crushNameChars = [char for char in crushName]

    try:
        yourNameChars.remove(' ')
        crushNameChars.remove(' ')
    except:
        pass
    
    print("Unique characters found:")
    print("From your name:",yourNameChars)
    print("From your crush's name:",crushNameChars)
    
    # Get unique letters and store in a variable uniqueChars
    uniqueChars = np.unique(yourNameChars + crushNameChars)

    # Count the number of unique characters
    uniqueCharsCount = len(uniqueChars)

    print("Unique Characters:",uniqueChars)
    print("Count:",uniqueCharsCount)
    
    # THE "DICTIONARY" OF DESTINY
    destinyKeys = ["F","L","A","M","E","S"]
    destiny = {"F":"to be just FRIENDS!",
               "L":"to be LOVERS!",
               "A":"it will end-up full of ANGER!",
               "M":"it end up in MARRIAGE!",
               "E": "to be ENGAGED!",
               "S":"as SOULMATES!"}
    
    if uniqueCharsCount % 6 == 0:
        print(f"Your destiny with your crush is...\n{destiny['S']}")
        return f"Your destiny with your crush is... {destiny['S']}"
    else:
        charLoc = (uniqueCharsCount % 6) - 1
        print(f"Your destiny with your crush is...\n{destiny[destinyKeys[charLoc]]}")
        return f"Your destiny with your crush is... {destiny[destinyKeys[charLoc]]}"