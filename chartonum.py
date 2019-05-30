### Char to num converter, I made this because I am exploring some cryptography, and needed something like this.
### I am uploading this mainly to keep it saved, if you find it helpful for anything great, go ahead and enjoy!
### ---Joaquim Maurício

def chartonums(char):
    ordchars = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,]
    newchar = ""
    if ord(char) in ordchars:
        newchar = ord(char)
    else:
        print("Please use only the 26 characters of the english alphabet.")
    return(newchar)

def addtochar(char, change):
    ordchars = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,]
    newchar = ""
    if ord(char) in ordchars:
        newchar = ord(char)
    else:
        return "Please use only the 26 characters of the english alphabet."
    newvalue = newchar + change
    if newvalue in ordchars:
        return chr(newvalue)
    else:
        return "The amount that you added to the char made it overflow the alphabet."

def subfromchar(char, change):
    ordchars = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,]
    newchar = ""
    if ord(char) in ordchars:
        newchar = ord(char)
    else:
        return "Please use only the 26 characters of the english alphabet."
    newvalue = newchar - change
    if newvalue in ordchars:
        return chr(newvalue)
    else:
        return "The amount that you subtracter from the char made it overflow the alphabet."

