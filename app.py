import base64
import streamlit as st
import pandas as pd
import pdfplumber
import re
from fpdf import FPDF
from dotenv import load_dotenv
import os
import openai
import matplotlib.pyplot as plt
import nltk
from nltk.util import ngrams
from collections import Counter
from wordcloud import WordCloud
import requests
from bs4 import BeautifulSoup

# Ensure you have the NLTK data downloaded
nltk.download('punkt')

# Load environment variables from a .env file if present
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define weights for specific phrases
phrase_weights = {
    # (Your phrase weights here)
}

# Load lexicon CSV file
lexicon_path = 'Loughran-McDonald_MasterDictionary_1993-2023.csv'
lexicon_df = pd.read_csv(lexicon_path)
lexicon_words = set(lexicon_df['Word'].str.lower())

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# (The rest of your functions)

# Function to encode an image to base64
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Encode your background images
img_main = get_img_as_base64("Background3.png")

# Custom CSS for background images and styling
def add_custom_css():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{img_main}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .css-1d391kg {{
            background-color: rgba(255, 255, 255, 0.85);
            border-radius: 10px;
            padding: 20px;
        }}
        .stButton > button {{
            background-color: #1f77b4;
            color: white;
            border-radius: 10px;
            height: 50px;
            width: 100%;
            font-size: 18px;
            border: none;
        }}
        .stButton > button:hover {{
            background-color: #0056a1;
        }}
        .stTextInput > div > div > input {{
            font-size: 18px;
            padding: 10px;
            background-color: #ffffff;
            border-radius: 10px;
            border: 2px solid #000000;
        }}
        .stFileUploader > div > div > div > button {{
            font-size: 18px;
            border-radius: 10px;
            background-color: #1f77b4;
            color: white;
            border: none;
        }}
        .stFileUploader > div > div > div > button:hover {{
            background-color: #0056a1;
        }}
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {{
            color: #000000;
        }}
        .css-1aumxhk, .css-1avcm0n, .css-1kyxreq, .css-1d391kg, .css-1offfwp, .css-pkbazv {{
            background-color: rgba(255, 255, 255, 0.85) !important;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_custom_css()

# Define the PDF class here so it's available throughout the script
class PDF(FPDF):
    def body(self, body):
        self.set_font('Arial', '', 14)
        # Handling utf-8 encoded strings
        body = body.encode('latin-1', 'replace').decode('latin-1')
        self.multi_cell(0, 10, body)
        self.ln()

# Streamlit app main function
def main():
    st.title("Financial Sentiment Analyzer ✔")

    st.markdown("## Analyze PDFs, Text, and News Articles for Financial Data")

    # Add a refresh button
    if st.button("Refresh"):
        st.experimental_rerun()

    # (Rest of your main function code)

if __name__ == "__main__":
    main()
