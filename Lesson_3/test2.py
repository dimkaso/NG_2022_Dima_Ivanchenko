string = str(input("Enter string pless: "))

# option sentence sort STR
print('1.Do you want to sort a string?\n2.Do you want to count the number of elements?\n3.Do you want to display only vowels?\n4.Do you want consonants?\n5.Do you want to break the word and output and output from the end?\n6.Want to display a word by number?\n7.Print the line again?\n8.Do you want to leave the program?\n ')



while True: 
    Option_sentence=input('Select number: ')
    if Option_sentence == '1':
        sorted_=sorted(string)
        sortedS=''.join(sorted_)
        print(sortedS)

    if Option_sentence == '2':
        print(len(string))

    if Option_sentence == '3':
        count=0 
        vowels= set("ayeiou")
        for x in string:
            if x in vowels:
                count += 1
        print(count)

    if Option_sentence == '4':
        count=0 
        consonants= set("qwrtpsdfghjklzxcvbnm")
        for x in string:
            if x in consonants:
                count += 1
        print(count)

    if Option_sentence == '5':
        print(string.split()[::-1])

    if Option_sentence == '6':
        nomber_str= int(input('What line number do you want?: '))
        compartments=string.split()
        print(compartments[nomber_str])

    if Option_sentence == '7':
        print(string)

    if Option_sentence == '8':
            break

    