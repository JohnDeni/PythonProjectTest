
word = input()
if not word.strip():
     raise ValueError("Error! The field cannot be empty.")
else:
    ends_with_exclamation = lambda x: word.endswith("!")
    print(ends_with_exclamation(word))
