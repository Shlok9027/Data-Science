import streamlit as st
import pandas as pd

import joblib
 

model = joblib.load(r'C:\Users\shrey\SHLOK Python Code\MACHINE_LEARNING\Heart_Diesease_predictor\KNN_heart_disease_predictor_model.pkl')

scaler = joblib.load(r'C:\Users\shrey\SHLOK Python Code\MACHINE_LEARNING\Heart_Diesease_predictor\scaler.pkl')

expected_columns = joblib.load(r'C:\Users\shrey\SHLOK Python Code\MACHINE_LEARNING\Heart_Diesease_predictor\columns.pkl')

st.title("Heart Disease Prediction App by Shlok💖")

st.markdown('Provide the following details to predict the likelihood of heart disease:')


age = st.slider('Age', 18,100,40)
sex = st.selectbox('Gender',['M', 'F'])

chest_pain_type = st.selectbox('Chest Pain Type', ['ATA', 'NAP', 'TA', 'ASY'])

resting_bp = st.number_input('Resting Blood Pressure (mm Hg)', 90,200,120)

cholesterol = st.number_input('Cholesterol (mg/dl)', 100,600,200)


fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])


resting_ecg = st.selectbox('Resting ECG' , ['Normal', 'ST', 'LVH'])


max_hr = st.slider('Max Heart Rate', 60,220,150)


exercise_angina = st.selectbox('Exercise Induced Angina', ['Y', 'N'])

oldpeak = st.number_input('Oldpeak (ST depression)', 0.0,6.0,1.0)

 
st_slope = st.selectbox('ST Slope', ['Up', 'Flat', 'Down'])




if st.button('Predict'):
    raw_data = {
        'age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' +sex :1,
        'ChestPainType_' + chest_pain_type :1,
        'RestingECG_' + resting_ecg :1,
        'ExerciseAngina_' + exercise_angina :1,
        'ST_Slope_' + st_slope :1

    }


    input_data = pd.DataFrame([raw_data])

    for col in expected_columns:
        if col not in input_data.columns:
            input_data[col] = 0


    input_data = input_data[expected_columns]


    scaled_data = scaler.transform(input_data)

    prediction = model.predict(scaled_data)[0]



    if prediction == 1:
        st.error('⚠️ High Rish of Heart Diease... Please consult a doctor immediately!')
    else:
        st.success('✅ Low Risk of Heart Disease. Keep up the healthy lifestyle!')