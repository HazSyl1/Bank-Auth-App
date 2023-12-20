from flask import Flask, request
import pandas as pd
import numpy as np
import pickle 
import sklearn
import streamlit as st 
app=Flask(__name__)

classifier=pickle.load(open('Bank_Auth.pkl','rb'))

# @app.route('/')
def welcome():
    return "Welcome to the Home Page"

# @app.route('/predict')
def predict_note_auth(variance,skewness,curtosis,entropy):
    # variance=request.args.get('variance')
    # skewness=request.args.get('skewness')
    # curtosis = request.args.get('curtosis')
    # entropy = request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return prediction
    

# @app.route('/predict_file', methods=['POST'])
def predict_file():
    df_test=pd.read_csv(request.files.get('file'))
    prediction=classifier.predict(df_test)
    return "The predicted value for csv is:"+str(list(prediction))

    
def main():
    st.title("Bank Authenticator")
    html_temp="""
    <div style="background-color:red ;border-radius:90px;border-color:white; padding:10px">
    <h2 style="color:white ;text-align:centre"> Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance=st.text_input("Variance","Type Here")
    skewness=st.text_input("Skewness","Type Here")
    curtosis = st.text_input("Curtosis","Type Here")
    entropy = st.text_input("Entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_auth(variance,skewness,curtosis,entropy)
    st.success("The output is {}".format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit"
                )


if __name__ == '__main__':
    main()
    