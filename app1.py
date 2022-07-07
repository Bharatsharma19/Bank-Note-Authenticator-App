import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome"

def predict_note_authentication(variance,skewness,curtosis,entropy):
 
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction



def main():
    st.title("Developed by Bharat Sharma")
    html_temp = """
    <div style="background-color:blue;color:white;padding:10px;display:flex;text-align:center;">
    <h2 style="color:white;text-align:center;">Bank Authenticator App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance")
    skewness = st.text_input("skewness")
    curtosis = st.text_input("curtosis")
    entropy = st.text_input("entropy")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Bharat Sharma")
        st.text("Software Developer")

if __name__=='__main__':
    main()
