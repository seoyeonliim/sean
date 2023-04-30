<<<<<<< HEAD
import streamlit as st
from streamlit_chat import message
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

@st.cache(allow_output_mutation=True)
def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_csv('furniture.csv')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()

st.header('가구인테리어 챗봇')

if 'generated' not in st.session_state:
    st.session_state['generated']=[]
    
if 'past' not in st.session_state:
    st.session_state['past'] = []
    
with st.form('form', clear_on_submit = True):
    user_input = st.text_input('당신: ', '')
    submitted = st.form_submit_button('전송')
=======
import streamlit as st
from streamlit_chat import message
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

@st.cache(allow_output_mutation=True)
def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_csv('furniture.csv')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()

st.header('가구인테리어 챗봇')

if 'generated' not in st.session_state:
    st.session_state['generated']=[]
    
if 'past' not in st.session_state:
    st.session_state['past'] = []
    
with st.form('form', clear_on_submit = True):
    user_input = st.text_input('당신: ', '')
    submitted = st.form_submit_button('전송')
>>>>>>> 3cb187ca6377fb9ee0feac519b5cdb018b68a5f1
