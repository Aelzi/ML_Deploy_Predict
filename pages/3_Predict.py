import streamlit as st
import pandas as pd
import numpy as np
import pickle
from pathlib import Path



judul = st.write(" # Prediksi Kualitas Udara")


pkl_path = Path(__file__).parents[1]/ 'model/model.pkl'
with open(pkl_path, 'rb') as file:
    model=pickle.load(file)
    

st.sidebar.header('Parameter Input:')

# User input features
def user_input_features():
    ozone = st.sidebar.slider('Ozone (O3)', 0, 81, 50)
    carbon_monoksida = st.sidebar.slider('Carbon Monoksida (CO)', 0, 164, 50)
    sulfur_dioksida = st.sidebar.slider('Sulfur Dioksida (SO2)', 0, 6, 3)
    particulate_matter = st.sidebar.slider('Particulate Matter 10 (PM10)', 3, 60, 40)
    data = {'O3': ozone,
            'CO': carbon_monoksida,
            'SO2': sulfur_dioksida,
            'PM10': particulate_matter}
    features = pd.DataFrame(data, index=[0])
    return features


# Function to make predictions
def predict_category(ozone, carbon_monoksida, sulfur_dioksida, particulate_matter):
    # Create a DataFrame with the user input
    user_input = pd.DataFrame({'O3': [ozone],
                            'CO': [carbon_monoksida],
                            'SO2': [sulfur_dioksida],
                            'PM10': [particulate_matter]})

    # Use the loaded model to make predictions
    prediction = model.predict(user_input)

    # Map the prediction to the corresponding category
    category_mapping = {1: 'baik', 2: 'sangat Baik', 3: 'tidak sehat'}
    category = category_mapping.get(prediction[0], 'Unknown')

    return category

# Get user input
Input = user_input_features()
st.subheader('Parameter Input: ')
if Input['O3'].values[0] == 0 and Input['CO'].values[0] == 0 and Input['SO2'].values[0] == 0 and Input['PM10'].values[0] == 3:
    st.write('''Inputan tidak valid ❌
                
                Mohon masukkan data yang tepat!''')
else:
    st.write(Input)
    ozone = Input['O3'].values[0]
    carbon_monoksida = Input['CO'].values[0]
    sulfur_dioksida = Input['SO2'].values[0]
    particulate_matter = Input['PM10'].values[0]
    

# Predict the category
category = predict_category(ozone, carbon_monoksida, sulfur_dioksida, particulate_matter)\
# st.write(f"Prediction: {category} Air Quality")

# st.subheader('Probabilitas Prediksi:')
# prediction_proba=logistic_regression.predict_proba(Input)
# st.write(prediction_proba)


# Display the predicted category

st.write('''### Hasil prediksi: ''')
if category == 'baik':
    st.markdown(''' # Kualitas udara :blue[baik]''')
    st.markdown(''' 
                - Orang-orang dengan sensitivitas tinggi mungkin perlu mengurangi waktu di luar ruangan atau berolahraga intensif.
                - Pastikan ventilasi dalam ruangan baik untuk mengurangi paparan polusi udara dalam ruangan.
                - Pantau pemberitahuan dan peringatan kualitas udara setempat untuk informasi terkini.''')
    
elif category== 'sangat Baik':
    st.markdown(" # Kualitas udara :green[sangat baik]\n ")
    st.markdown(''' 
                - Aman untuk beraktivitas di luar ruangan. Cobalah untuk menikmati udara segar dan berolahraga di luar.
                - Anda dapat menggunakan kendaraan bermotor seperti biasa.
                - Tetap menjaga kebersihan dan lingkungan agar tetap bersih.''')
    st.markdown('&mdash;\:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:')
else:
    st.markdown(""" # Kualitas udara :red[tidak sehat]\n""")
    st.markdown('''
                - Hindari aktivitas di luar ruangan, terutama berolahraga. Coba untuk tetap berada di dalam ruangan.
                - Jika Anda harus keluar, gunakan masker penutup wajah yang sesuai untuk melindungi diri Anda.
                - Pastikan ventilasi dalam ruangan baik dan hindari merokok atau menggunakan alat bakar dalam ruangan.''')


st.info("""
 
### Prediksi ini menggunakan metode:
### :blue[**Logistic Regression**] + :green[**Cross Validation**] + :red[**Oversampling**]
 
""")
