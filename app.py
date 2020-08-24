# Core Pkgs
import streamlit as st 
import os

import nltk
nltk.download('punkt')

# NLP Pkgs
from textblob import TextBlob 
import spacy
from gensim.summarization import summarize

# Sumy Summary Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Function for Sumy Summarization
def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result

# Function to Analyse Tokens and Lemma
@st.cache
def text_analyzer(my_text):
	nlp = spacy.load('en_core_web_sm')
	docx = nlp(my_text)
	# tokens = [ token.text for token in docx]
	allData = [('"Token":{},\n"Lemma":{}'.format(token.text,token.lemma_))for token in docx ]
	return allData

# Function For Extracting Entities
@st.cache
def entity_analyzer(my_text):
	nlp = spacy.load('en_core_web_sm')
	docx = nlp(my_text)
	tokens = [ token.text for token in docx]
	entities = [(entity.text,entity.label_)for entity in docx.ents]
	allData = ['"Token":{},\n"Entities":{}'.format(tokens,entities)]
	return allData

def main():
	""" NLP Based App with Streamlit """
    # Title
st.title("NLPiffy with Streamlit")
st.subheader("Natural Language Processing On the Go..")
st.markdown("""
#### Description
+ This is a Natural Language Processing(NLP) Based App useful for basic NLP task
Tokenization, NER, Sentiment, Summarization
""")

analysis_option = st.selectbox("Select your Analysis", ["Lemmatization", "Extract Entities", "Sentiment Analysis", 
                        "Summarization"])

message = st.text_area("Enter Text","Type Here ..")

if analysis_option == "Lemmatization":
    nlp_result = text_analyzer(message)
elif analysis_option == "Extract Entities":
    nlp_result = entity_analyzer(message)
elif analysis_option == "Sentiment Analysis":
    blob = TextBlob(message)
    nlp_result = blob.sentiment
elif analysis_option == "Summarization":
    summary_options = st.selectbox("Choose Summarizer",['sumy','gensim'])
    if summary_options == 'sumy':
        st.text("Using Sumy Summarizer ..")
        nlp_result = sumy_summarizer(message)
    elif summary_options == 'gensim':
        st.text("Using Gensim Summarizer ..")
        nlp_result = summarize(message)
    else:
        st.warning("Using Default Summarizer")
        st.text("Using Gensim Summarizer ..")
        nlp_result = summarize(message)

#if st.button("Analyze"):
st.success(nlp_result)

st.sidebar.subheader("About App")
st.sidebar.text("NLPiffy App with Streamlit")


if __name__ == '__main__':
	main()