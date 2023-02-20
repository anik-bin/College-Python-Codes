import nltk

from nltk.tokenize import sent_tokenize

core = "Hello my name is aniket bindhani and I live in bhubaneswar, I am going out today"

sent = sent_tokenize(core)
print(sent)