import streamlit as st  
from streamlit import components

st.set_page_config(
    layout="wide")
lda = 'static/lda.html'
with open(lda, 'r', encoding='utf-8') as f:  
    html_string = f.read()

components.v1.html(html_string, width=1300, height=800)