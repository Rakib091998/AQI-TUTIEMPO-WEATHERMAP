
import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("AQI_XGBOOST_HYPER.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def Air_Quality_Index(T, TM,  Tm,  SLP, H, VV,  V, VM):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: T
        in: query
        type: number
        required: true
      - name: TM
        in: query
        type: number
        required: true
      - name: Tm
        in: query
        type: number
        required: true
      - name: SLP
        in: query
        type: number
        required: true
      - name: H
        in: query
        type: number
        required: true
      - name: VV
        in: query
        type: number
        required: true
      - name: V
        in: query
        type: number
        required: true
      - name: VM
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[T,TM,Tm,SLP,H,VV,V,VM]])
    print(prediction)
    return prediction



def main():
    st.title("AQI")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">AQI INDEX </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    T = st.text_input("T:Average Temperature(°C)",)
    TM = st.text_input("TM:Maximum temperature(°C)",)
    Tm = st.text_input("Tm:Minimum temperature(°C)",)
    SLP = st.text_input("SLP:Atmospheric pressure at sea level(hPa)",)
    H = st.text_input("H:Average relative humidity(%)",)
    VV = st.text_input("V V:Average visibility (Km)",)
    V = st.text_input("V:Average wind speed (Km/h)",)
    VM = st.text_input("VM:Maximum sustained wind speed(Km/h)",)
    result=""
    if st.button("Predict"):
        result=Air_Quality_Index(T, TM,  Tm,  SLP, H, VV,  V, VM)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("©Rakib")
 

if __name__=='__main__':
    main()