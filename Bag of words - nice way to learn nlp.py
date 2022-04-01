from nltk.corpus import stopwords
# nltk.download("stopwords")
from nltk.tokenize import word_tokenize
# nltk.download("punkt")
from nltk.stem.porter import PorterStemmer


import string
from collections import Counter


def bag_of_words(text):
    text = text.lower()
    words = word_tokenize(text)

    punct_white = set(string.punctuation + string.whitespace + "...")
    english_stop_words = set(stopwords.words("english"))

    words = [word for word in words if word not in english_stop_words and word not in punct_white]

    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    words = [word for word in words if len(word)>=3]

    bag = Counter(words)

    return bag


if __name__ == '__main__':
    with open("text.txt") as file:
        text = file.read()
    bag_of_words(text)
