word = input()
if word == " " or word == "":
    print("No word")
else:
    words = lambda word: False if word[-1] != "!" else True
    print(words(word))
