import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
st.title("Data minning Diabetes")

col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Input nilai Pregnancies')
    Glucose = st.text_input('Input nilai Glucose')
    BloodPressure = st.text_input('Input nilai BloodPressure')
    SkinThickness = st.text_input('Input nilai SkinThickness')

with col2:
    Insulin = st.text_input('Input nilai Insulin')
    BMI = st.text_input('Input nilai BMI')
    DiabetesPedigreeFunction = st.text_input('Input nilai DiabetesPedigreeFunction')
    Age = st.text_input('Input nilai Age')

diab_diagnosis = ''

if st.button("test Prediksi diabetes"):
    diab_prediction = diabetes_model.predict([[
        Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
        ]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = "Pasien terkena diabetes"
    else:
        diab_diagnosis = "Passien terkena diabetes"

    st.success(diab_diagnosis)