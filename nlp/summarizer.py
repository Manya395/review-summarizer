import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download("punkt")
nltk.download("stopwords")

def summarize(text, n=2):
    sentences = sent_tokenize(text)

    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())

    # Build frequency table
    freq = {}
    for word in words:
        if word.isalpha() and word not in stop_words:
            freq[word] = freq.get(word, 0) + 1

    # Score sentences
    sentence_scores = {}
    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        score = 0
        for word in sentence_words:
            if word in freq:
                score += freq[word]
        sentence_scores[sentence] = score

    # Pick top n sentences
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:n]

    return " ".join(summary_sentences)
