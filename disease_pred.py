# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:47:31 2022

@author: Acer
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

autism_model = pickle.load(open('autism_model.sav','rb')) 



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',                          
                          ['Autism Prediction'
                          ,'About us','Contact'],
                          icons = ['caret-right-square-fill','house','cast'],
                          default_index=0)
    
if (selected == 'Autism Prediction'):
    
    st.title('Autism Disease Prediction Using ML')
    
    
    A1_Score = st.text_input('Whether the child look at you when you call his/her name?(Yes-1/No-0)')
    A2_Score = st.text_input('How easy it is for you to get eye contact with the child?(Yes-1/No-0)')
    A3_Score = st.text_input('Does your child point to indicate that he/she wants something?(Yes-1/No-0)')
    A4_Score = st.text_input('Does your child point to share interest with you?(Yes-1/No-0)')
    A5_Score = st.text_input('Does your child pretend?(Yes-1/No-0)')
    A6_Score = st.text_input('Does your child follow when you are looking?(Yes-1/No-0)')
    A7_Score = st.text_input('If you or someone else in the family is visibly upset,does your child show signs of warning to comfort them?(Yes-1/No-0)')
    A8_Score = st.text_input('Does your child talk back when you talk?(Yes-1/No-0)')
    A9_Score = st.text_input('Does your child use simple gestures?(Yes-1/No-0)')
    A10_Score = st.text_input('Does your child stare at nothing with no apparent purpose?(Yes-1/No-0)')
    age = st.text_input('Age')
    jundice=st.text_input('Whether the child was born with jaundice?(Yes-1/No-0)')
    
    
    autism_diagnosis = ''
    
    if st.button("AUTISM TEST RESULT"):
        autism_prediction = autism_model.predict([[A1_Score,A2_Score,A3_Score,A4_Score,A5_Score,A6_Score,A7_Score,A8_Score,A9_Score,A10_Score,age,jundice]])
        
        if (autism_prediction[0] == 1):
            autism_diagnosis = "The Person has the risk of Autism"
        else:
            autism_diagnosis = "The Person does not have Autism Disease"
            st.success( autism_diagnosis)
            "For further consultant kindly use:"
            "1. ABA Therapy Centre for AUTISM link:" "http://www.youcanautism.com/"
            "2. Third Eye - A learning center for Autism Link:" "http://www.thirdeyecenter.org/"
            "3. Vatsalyam Centre For Autism Link:" "http://www.vatsalyam.in/"
            "4. Sparks Vidyalaya Link:" "http://sparksautismschool.com/"

         
        
if (selected == 'About us'):
    st.title('About us')
    st.text('This application is designed to predict whether a person has the AUTISM DISODER or not.')
    st.text('It works by the principle of applying machine learning techniques. When the user')
    st.text('gives the inputs regarding the person, it gets tested by the machine learning model.')
    st.text('The proposed model is based on the Support Vector Machine.The input data gets tested')
    st.text(' and predicts the result.')
if (selected == 'Contact'):
    st.title('FURTHER CONTACT DETAILS')
    st.text('For further details contact us at mkinfotechology2022@gmail.com')
    st.text('Developed by mkinfotech')

    
