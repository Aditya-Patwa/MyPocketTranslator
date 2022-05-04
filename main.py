import streamlit as st
from PyDictionary import PyDictionary

dictionary = PyDictionary()

st.title("MyPocketTranslator")
# languages = []
# fromLang = st.selectbox(
#      'From',
#      ('en', 'fr', 'es', 'hi'))

# toLang = st.selectbox(
#      'To',
#      ('en', 'fr', 'es', 'hi'))

textInput = st.text_input('Word')
translation = dictionary.meaning(textInput)

st.header("Meanings")
for key, value in translation.items():
     words = ", ".join(value)
     st.markdown(f"""
     ##### {key}
     {words}
     """)

# st.header("Synonyms")
# synonym = dictionary.synonym(textInput)
# st.markdown(f"{synonym}")

# st.header("Antonyms")
# antonym = dictionary.antonym(textInput)
# st.markdown(f"{antonym}")
