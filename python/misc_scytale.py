"""
Sample encoder/decoder for a Scytale cypher.

An ancient transposition cypher. Parchment is wrapped in a spiral around a rod of 
known diameter. The 'secret' message is written, then unwrapped into seeming gibberish. 
Only when wrapped around a rod of identical diameter does the message become clear again.

Encoding and decoding require the circumference of the rod, i.e. how many characters can 
fit on a single loop/line of the parchment around the rod. Here I call this the 'step' (as in,
an array slice step). The number of loops is string length divided by the step.

Requires Python3 for f string use.

ref: https://en.wikipedia.org/wiki/Scytale
"""

def encode(text, step):
    '''Transpose the text using the step'''
    cleaned_text = text.replace(" ", "") # clean whitespace first
    length = len(cleaned_text)
    passes = length // step

    remainder = length % step
    if remainder:
        # pad the string until the next clean division of length / step
        # as uneven division corrupts the transposition
        times_to_pad = step * (passes+1) - length
        for n in range(times_to_pad):
            cleaned_text += " "
        # text length has increased due to rounding up; passes must too
        passes += 1

    output = ''
    # for as many times as 'step' goes into length, iterate through 
    # the string, using the pass count as the step. offset by loop count
    for i in range(passes):
        output += cleaned_text[i::passes]

    return output
    
def decode(text, step):
    '''Decode a cipher text using the step'''

    output = ''
    # pass count is identical to step
    for i in range(step):
        output += text[i::step]
    # .rstrip() to remove any padded chars
    return output.rstrip()
    
step = 4
raw_text = "I am hurt very badly help"

print(f"Input: '{raw_text}'")

code = encode(raw_text, step)
print(f"Code: {code}") # Code: Iryyatbhmvaehedlurlp

decoded = decode(code, step)
print(f"Decoded: {decoded}") # Decoded: Iamhurtverybadlyhelp

step = 3
raw_text = "I am hurt very badly please send help as soon as possible, thanks very much"

print(f"Input: '{raw_text}'")

code = encode(raw_text, step)
print(f"Code: {code}") # Code: Ieiasbmelhneud,rhttehvlaepnrakyssbsvaoedorlnyyampsulpceohas ss 
# note the two whitespace characters, one of which is at the end

decoded = decode(code, step)
print(f"Decoded: {decoded}") # Decoded: Iamhurtverybadlypleasesendhelpassoonaspossible,thanksverymuch
# note the whitespace characters are now trimmed