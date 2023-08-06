vowels = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}
words = []
res = "y"
while res == "y":
    word = input("Ingrese una palabra: ")
    while word.isalpha() == False:
        print("Eso no es una palabra")
        word = input("Ingrese una palabra: ")
    else:
        words.append(word.lower())
        res = (input("quieres ingresar mas palabras? y/n")).lower()
else:
    for word in words:
        for letter in word:
            if letter == "a":
                vowels["a"]=vowels["a"]+1
            if letter == "e":
                vowels["e"]=vowels["e"]+1
            if letter == "i":
                vowels["i"]=vowels["i"]+1
            if letter == "o":
                vowels["o"]=vowels["o"]+1
            if letter == "u":
                vowels["u"]=vowels["u"]+1
    print(vowels)               