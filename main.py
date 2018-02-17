"""Converts from English to morse code"""
print"Hello!"
print"Use /help for a better understanding of morse code translations."
print"Use /quit to quit."
morsedic = {
"A" : ".-",
"B" : "-...",
"C" : "-.-.",
"D" : "-..",
"E" : ".",
"F" : "..-.",
"G" : "--.",
"H" : "....",
"I" : "..",
"J" : ".---",
"K" : "-.-",
"L" : ".-..",
"M" : "--",
"N" : "-.",
"O" : "---",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--",
"Z" : "--.."
}

quit_accum = True
while quit_accum:
    try:
        word = raw_input("What would you like to translate to Morse code? ")
        if word == "/Quit" or word == "/quit":
            quit_accum = False
        elif word == "/Help" or word == "/help":
            print(morsedic)
        else: 
            wordlist = list(word)
            accum = ""
            for x in wordlist:
                cap = x.upper()
                accum += morsedic[cap]
            print(accum)
    except:
        print"That is not a valid input"
