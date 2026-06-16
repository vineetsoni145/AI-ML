import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
nltk.download("stopwords")
from nltk.corpus import stopwords

word = set(stopwords.words("english"))
print(word)

data = "we are learning python and nlp "

token = word_tokenize(data)
print(token)

stw = []

for i in token:
    if i not in word:
        stw.append(i)

print(stw)