from tika import parser
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import spacy
from nltk.tokenize import word_tokenize, sent_tokenize
from textblob import TextBlob
from collections import Counter
from wordcloud import WordCloud



def extract_text(file_path):
    parsed = parser.from_file(file_path)
    return parsed["content"]


def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)


def clean_text(text):
    cleaned_text = str(text)
    cleaned_text = re.sub(r'\S+@\S+', '', cleaned_text)
    cleaned_text = re.sub(r'\S+\.com\S*', '', cleaned_text)
    cleaned_text = re.sub(r'http\S+', '', cleaned_text)
    cleaned_text = deEmojify(cleaned_text)
    cleaned_text = re.sub(r'\b\w+\.(png|jpg|jpeg)\b', '', text)
    cleaned_text = re.sub(r'\\.', '', cleaned_text)
    cleaned_text = re.sub(r' · ', '', cleaned_text)
    cleaned_text = re.sub(r'[^a-zA-Z]',' ',cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    cleaned_text = re.sub(r'\b([a-zA-Z])\1\b', "", cleaned_text)
    cleaned_text = re.sub(r'\b[a-zA-Z]\b', "", cleaned_text)
    cleaned_text = cleaned_text.lower()
    return cleaned_text.strip()


nlp = spacy.load("en_core_web_sm")
def lemmatization(text):
    doc = nlp(text)
    lemmatized_tokens = [token.lemma_.strip() for token in doc]
    return ' '.join(lemmatized_tokens)

nltk.download('punkt')
nltk.download('stopwords')
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text) # Tokenize the text
    filtered_text = [word.strip() for word in word_tokens if word.lower() not in stop_words]
    return ' '.join(filtered_text)

ner_categories =  ['PERSON','GPE','LOC','NORP', 'FAC','PRODUCT','EVENT','WORK_OF_ART','DATE','TIME','LANGUAGE','MONEY']   # https://dataknowsall.com/blog/ner.html
def remove_NER_categories(text):
    doc = nlp(text)
    cleaned_text = " ".join([token.text for token in doc if not token.ent_type_ in ner_categories])
    return cleaned_text

def remove_short_words(text):
    cleaned_text = re.sub(r'\b\w{1,2}\b', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text
