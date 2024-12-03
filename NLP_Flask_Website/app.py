from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

import spacy
import pandas as pd
from  textblob import TextBlob

app = Flask(__name__)

# Load the Spacy model
nlp = spacy.load("en_core_web_sm")

def lemmatize(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not (token.is_stop or token.is_punct)]

    return " ".join(tokens)


# Load your data (replace with your actual data loading)
url = "https://raw.githubusercontent.com/alexisperrier/intro2nlp/master/data/brown_corpus_extract_humor_science_fiction.csv"
df = pd.read_csv(url)


# Preprocess your data
new_df = df.copy()
new_df['processed_text'] = new_df.text.apply(lambda txt: lemmatize(txt))

# Transform the topic from string to integer using mapping
topic_mapping = {'humor': 0, 'science_fiction': 1}
new_df['topic'] = [topic_mapping[topic] for topic in df['topic']]

# Define your target variable
y = new_df.topic.astype(int)

# Vectorize your text data
cv = CountVectorizer()
X = cv.fit_transform(new_df.processed_text)

# Create a MultinomialNB classifier
clf = MultinomialNB(alpha=0.1, fit_prior=False, force_alpha=True)  # Use your best hyperparameters

# Fit the classifier to your data
clf.fit(X, y)

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        # Get the text input from the user
        text = request.form["text"]
        analysis_type = request.form["analysis_type"]  # Get the selected analysis type

        if analysis_type == "classifier":
            # Preprocess the text
            processed_text = lemmatize(text)
            # Vectorize the text
            text_vector = cv.transform([processed_text])

            # Perform sentiment analysis
            sentiment_prediction = clf.predict(text_vector)[0]
            sentiment = "Humor" if sentiment_prediction == 0 else "Science Fiction"

            return render_template("index.html", sentiment=sentiment, text=text, analysis_type=analysis_type)

        elif analysis_type == "textblob":
            # TextBlob analysis
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            return render_template("index.html", polarity=polarity, subjectivity=subjectivity, text=text, analysis_type=analysis_type)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)