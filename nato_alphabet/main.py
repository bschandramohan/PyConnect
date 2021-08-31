import pandas

nato_words_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_words_dict = {item.letter: item.code for (index, item) in nato_words_df.iterrows()}

source = "SireeshaChandra".upper()
print([nato_words_dict[letter] for letter in source])
