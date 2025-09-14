# Importing required modules
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

# Ensure NLTK resources are available
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab")

# Sample text
text = """
Natural Language Processing (NLP) is a field of Artificial Intelligence that focuses on the interaction between computers and humans through natural language. 
The goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful. 
Common NLP applications include language translation, sentiment analysis, speech recognition, and text summarization.
"""

# Step 1: Parse the text
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Step 2: Initialize summarizer
summarizer = LsaSummarizer()

# Step 3: Generate summary (let's take 2 sentences)
summary = summarizer(parser.document, 2)

# Step 4: Print the result
for sentence in summary:
    print(sentence)
