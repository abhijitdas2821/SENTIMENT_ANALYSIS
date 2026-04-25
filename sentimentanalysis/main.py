import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analysis App")

st.write("Enter text to analyze sentiment:")

user_input = st.text_area("Your Text")

def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive 😊", polarity
    elif polarity < 0:
        return "Negative 😞", polarity
    else:
        return "Neutral 😐", polarity

if st.button("Analyze"):
    if user_input:
        result, score = get_sentiment(user_input)
        st.subheader("Result:")
        st.write(result)
        st.write(f"Sentiment Score: {score}")
    else:
        st.warning("Please enter some text.")