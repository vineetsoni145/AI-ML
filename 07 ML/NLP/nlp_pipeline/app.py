from flask import Flask, render_template, request
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
nltk.download("stopwords")
from nltk.corpus import stopwords
nltk.download("wordnet")
from nltk.stem import PorterStemmer, WordNetLemmatizer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    tokens = ""
    filtered = ""
    stemmed = ""
    lemmatized = ""

    if request.method == "POST":
        sentence = request.form["sentence"]
        tokens = word_tokenize(sentence)

        stop_words = set(stopwords.words("english"))
        filtered_words = []

        for word in tokens:
            if word.lower() not in stop_words:
                filtered_words.append(word)
        filtered = filtered_words

        ps = PorterStemmer()
        stemmed_words = []

        for word in filtered_words:
            stemmed_words.append(ps.stem(word))
        stemmed = stemmed_words
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = []

        for word in filtered_words:
            lemmatized_words.append(lemmatizer.lemmatize(word))
        lemmatized = lemmatized_words

    else:
        tokens = "Will be displayed soon"
        filtered = "Will be displayed soon"
        stemmed = "Will be displayed soon"
        lemmatized = "Will be displayed soon"

    return render_template("index.html",tokens=tokens,filtered=filtered,stemmed=stemmed,lemmatized=lemmatized)

if __name__ == "__main__":
    app.run(debug=True)