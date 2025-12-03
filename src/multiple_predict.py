import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

model_diabetes = pickle.load(open("src/diabetes_model.sav", "rb"))  # here we have to replace "\" --> "/"

model_heart = pickle.load(open("src/heart_model.sav", "rb"))

model_parkinsons = pickle.load(open("src/parkinsons_model.sav", "rb"))


# create the side bar for navigation

with st.sidebar:

    selected = option_menu('Multiple Disease Predictor',
                           ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                           icons = ['activity','suit-heart-fill'],
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

    # getting input from user
    col4, col5, col6 = st.columns(3)

    with col4:
        age = st.text_input('Age of Person')

    with col5:
        sex = st.text_input('Sex: Male = 1 or Female = 0')

    with col6:
        cp = st.text_input('Chest Pain Types')    

    with col4:
        trestbps = st.text_input('Resting Blood Pressure')

    with col5:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col6:
        fbs = st.text_input('Fasting Blood Sugar > 120mg/dl')
        
    with col4:
        restecg = st.text_input('Resting Electrocardiographic results')
    
    with col5:
        thalach = st.text_input('Maximum Heart Rate achieved')
    
    with col6:
        exang = st.text_input('Exercise Induced Angina')
    
    with col4:
        oldpeak = st.text_input('ST depression induced by exercise')
    
    with col5:
        slope = st.text_input('Slope of the peak exercise ST segment')
    
    with col6:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col4:
        thal = st.text_input('thal: 0 = normal; 1 = fixed detect; 2 = reversable defect')

    
    # for prediction
    heart_diagnosis = ''

    # create button for prediction
    if st.button('Heart Disease Test'):

        try:
            # Convert to numeric
            age = int(age)

            # Map sex
            if sex.lower() in ["male", "m"]:
                sex = 1
            else:
                sex = 0

            cp = int(cp)
            trestbps = float(trestbps)
            chol = float(chol)
            fbs = int(fbs)
            restecg = int(restecg)
            thalach = float(thalach)
            exang = int(exang)
            oldpeak = float(oldpeak)
            slope = int(slope)
            ca = int(ca)
            thal = int(thal)


            heart_pred = model_heart.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

            if (heart_pred[0] == 0):
               heart_diagnosis = 'Person has not Heart Disease'
        
            else:
               heart_diagnosis = 'Person has Heart Disease'
        
        except ValueError:
            heart_diagnosis = "❌ Error: Please enter only NUMBERS for all fields."
        
        st.success(heart_diagnosis)
    
    







