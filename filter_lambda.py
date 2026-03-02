words_list = ["sky", "why", "apple", "try"]
vowels = set("aeiouy")
words = list(filter(lambda w: set(w) & vowels, words_list))
print(words)
