# -------------------------------------------------------
# code template for assignment-1
# -------------------------------------------------------

import time

def profanityFilter(aString, badWordList, substitute_string="#%@$!"):

    for word in badWordList: # search for index of bad word in string
        index =  aString.upper().find(word.upper())

        if index >= 0:
            aString = aString[0:index]+substitute_string+aString[index+len(substitute_string):len(aString)]
    
        odds = aString[::2] # check that bad words aren't divided by characters
        index = odds.upper().find(word.upper())
        if index >= 0:
            aString = aString[0:index*2]+substitute_string+aString[index*2+len(substitute_string)*2-1:len(aString)]
        

        evens = aString[1::2]# check other have of letters also
        index = evens.upper().find(word.upper())
        if index >= 0:
            aString = aString[0:index*2+1]+substitute_string+aString[index*2+len(substitute_string)*2:len(aString)]
        

    return aString

# -------------------------------------------------------

if __name__ == "__main__":

    theStartTime = time.time()

    #here we open a file that contains the list of badwords to be removed...
    with open('badwords.txt') as theBadWordFile:
        badWords = list(filter(None, (line.rstrip() for line in theBadWordFile)))

    #Here we send sample user input from a given file to your profanity filter...
    with open('userinput.txt') as theSampleInputFile, open('outputtext.txt', 'w') as theOutputFile:
        for theSampleInput in theSampleInputFile:
            theOutputFile.write(profanityFilter(theSampleInput, badWords) + '\n')

        theOutputFile.write('elapsed: ' + str( time.time() - theStartTime) + '\n')
