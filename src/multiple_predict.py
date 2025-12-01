import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

model_diabetes = pickle.load(open("diabetes_model.sav", "rb"))  # here we have to replace "\" --> "/"

model_heart = pickle.load(open("heart_model.sav", "rb"))

model_parkinsons = pickle.load(open("parkinsons_model.sav", "rb"))


# create the side bar for navigation

with st.sidebar:

    selected = option_menu('Multiple Disease Predictor',
                           ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Disease Prediction'],
                           icons = ['activity','suit-heart-fill','person'],
                           default_index=0)   # this is where we start our web page when first loaded 
                                              # defaut_index=0 --> Diabetes page
                                              # default_index=1 --> Heart page

# Diabetes Prediction page

if (selected == 'Diabetes Prediction'):

    st.title('Diabetes Predictor')   # page title

    # getting inputs from users
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')    

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI Value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')

    with col2:
        Age = st.text_input('Age of the Person')


    # For prediction
    db_dignosis = ''

    # Creating button for prediction
    if st.button('Diabetes Test'):
        db_prediction = model_diabetes.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]) # all this list should be enclosed with another "[ ]", so this is just to tell the model that we are predicting for one datapoint
        
        if (db_prediction[0] == 1):
            db_dignosis = 'The Person has Diabetes'

        else:
            db_dignosis = 'The Person has not Diabetes'

    st.success(db_dignosis) # This will give end result

# heart disease page 

if (selected == 'Heart Disease Prediction'):

    st.title('Heart Disease Predictor')



# parkinsons page

if (selected == 'Parkinsons Disease Prediction'):

    st.title('Parkinsons Disease Predictor')




