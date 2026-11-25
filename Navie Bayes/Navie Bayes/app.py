
import streamlit as st
import joblib
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download required NLTK data
nltk.download('stopwords', quiet=True)

# Load stopwords and stemmer
stop_words = set(stopwords.words('english'))
stop_words = stop_words - {'not', 'no', 'nor'}
stemmer = PorterStemmer()

# Load trained model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('count_vectorizer.pkl')


# Text preprocessing function
def preprocess_text(text):
    text = text.lower()

    text = re.sub(r"\bdidn't\b", "did not", text)
    text = re.sub(r"\bwasn't\b", "was not", text)
    text = re.sub(r"\bisn't\b", "is not", text)
    text = re.sub(r"\baren't\b", "are not", text)
    text = re.sub(r"\bwon't\b", "will not", text)
    text = re.sub(r"\bcan't\b", "can not", text)
    text = re.sub(r"\bwouldn't\b", "would not", text)
    text = re.sub(r"\bcouldn't\b", "could not", text)
    text = re.sub(r"\bshouldn't\b", "should not", text)

    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    words = text.split()

    words = [
        stemmer.stem(word)
        for word in words
        if word not in stop_words
    ]

    return ' '.join(words)


# Streamlit page configuration
st.set_page_config(
    page_title="Restaurant Review Sentiment Analysis",
    page_icon="🍽️",
    layout="centered"
)

# Application interface
st.title("🍽️ Restaurant Review Sentiment Analysis")

st.write(
    "Enter a restaurant review below to predict "
    "whether the sentiment is Positive or Negative."
)

review = st.text_area("Enter your restaurant review:")

if st.button("Analyze Sentiment"):

    if review.strip():

        cleaned_review = preprocess_text(review)

        review_features = vectorizer.transform([cleaned_review])

        prediction = model.predict(review_features)

        if prediction[0] == 1:
            st.success("😊 Positive Review")
        else:
            st.error("😞 Negative Review")

    else:
        st.warning("Please enter a review first.")
