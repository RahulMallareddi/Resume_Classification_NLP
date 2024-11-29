import streamlit as st
import re
import pandas as pd
from utils import CleaningFunctions
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer


tfidf = pickle.load(open('artifacts/tfidf_vectorizer.pkl', 'rb'))
rf_clf = pickle.load(open('artifacts/rf_clf.pkl', 'rb')) 

rol_dict = {0: 'Peoplesoft', 1: 'React Developer', 2: 'SQL Developer', 3: 'workday'}
file_type_df = pd.DataFrame([], columns=['Uploaded File',  'Predicted Profile'])
filename = []
predicted = []

st.markdown("<h1 style='text-align: center; color: white;'>Resume Classification To Required Job Role</h1>", unsafe_allow_html=True)

if "uploaded_files" not in st.session_state: 
  st.session_state["uploaded_files"] = []

with st.form("my-form", clear_on_submit=True):
  uploaded_files = st.file_uploader("Upload a resume", accept_multiple_files=True)
  submitted = st.form_submit_button("UPLOAD!")

if uploaded_files: 
  st.session_state["uploaded_files"] = uploaded_files

for doc_file in uploaded_files:
  if doc_file is not None:
    filename.append(doc_file.name)
    text = CleaningFunctions.extract_text(doc_file)
    processed_text = CleaningFunctions.remove_short_words(CleaningFunctions.remove_NER_categories(CleaningFunctions.remove_stopwords(CleaningFunctions.lemmatization(CleaningFunctions.clean_text(text)))))
    result = rf_clf.predict(tfidf.transform([processed_text]))[0]
    predicted.append(rol_dict[result])        

col1, col2 = st.columns([1,1])

with col1:
    if st.button("Classify"):
       if len(predicted) > 0:
        file_type_df['Uploaded File'] = filename
        file_type_df['Predicted Profile'] = predicted
        st.table(file_type_df.style.format())

with col2:
    if st.button("Clear"):
      filename = []
      predicted = []
      file_type_df = pd.DataFrame()
      st.session_state["uploaded_files"] = []

