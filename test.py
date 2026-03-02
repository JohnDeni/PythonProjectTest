word = input()
words = lambda word: False if word[-1] != "!" else True
print(words(word))