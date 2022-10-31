from gettext import textdomain
from pydoc import TextDoc


alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# textdoc = "Terrgvatf"
textdoc=input("Message to decrypt: ").upper()
shar = 13
newText=""
for x in textdoc:
    pizition= alfavit.find(x)
    namepoz = pizition+shar
    if x in alfavit:
        newText += alfavit[namepoz]
    else:
        newText += x
print(newText)