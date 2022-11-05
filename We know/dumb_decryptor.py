
English = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
text=input("Message to decrypt: ").upper()
shar = 13
Text=""
for x in text:
    pizition= English .find(x)
    namepoz = pizition+shar
    if x in English:
        Text += English[namepoz]
    else:
        Text += x
print("\n" , Text)