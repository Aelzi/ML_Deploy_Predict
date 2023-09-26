import streamlit as st
import pandas as pd
import pickle
import numpy as np
import joblib


df=pd.read_csv("polusi_udara_jogja2020.csv")
st.dataframe(df, use_container_width=True)


# print("BERHASIL")

# # Load the trained model and user input data
# pipe = joblib.load(open('../model.pkl', 'rb'))
# df = joblib.load(open('../data.pkl', 'rb'))

# st.write("""
# # Udara Jogja Prediction App

# This app predicts the **Udara Jogja** type!
# """)

# st.sidebar.header('User Input Parameters')

# # User input features
# def user_input_features():
#     ozone = st.sidebar.slider('Ozone (O3)', 0, 81, 50)
#     carbon_monoksida = st.sidebar.slider('Carbon Monoksida (CO)', 0, 164, 50)
#     sulfur_dioksida = st.sidebar.slider('Sulfur Dioksida (SO2)', 0, 6, 3)
#     particulate_matter = st.sidebar.slider('Particulate Matter 10 (PM10)', 3, 60, 40)
#     data = {'O3': ozone,
#             'CO': carbon_monoksida,
#             'SO2': sulfur_dioksida,
#             'PM10': particulate_matter}
#     features = pd.DataFrame(data, index=[0])
#     return features

# # Function to make predictions
# def predict_category(ozone, carbon_monoksida, sulfur_dioksida, particulate_matter):
#     # Create a DataFrame with the user input
#     user_input = pd.DataFrame({'O3': [ozone],
#                             'CO': [carbon_monoksida],
#                             'SO2': [sulfur_dioksida],
#                             'PM10': [particulate_matter]})

#     # Use the loaded model to make predictions
#     prediction = pipe.predict(user_input)

#     # Map the prediction to the corresponding category
#     category_mapping = {1: 'Moderate', 2: 'Good', 3: 'Unhealthy'}
#     category = category_mapping.get(prediction[0], 'Unknown')

#     return category

# # Get user input
# Input = user_input_features()
# ozone = Input['O3'].values[0]
# carbon_monoksida = Input['CO'].values[0]
# sulfur_dioksida = Input['SO2'].values[0]
# particulate_matter = Input['PM10'].values[0]

# # Predict the category
# category = predict_category(ozone, carbon_monoksida, sulfur_dioksida, particulate_matter)

# # Display the predicted category
# st.write(f"Prediction: {category} Air Quality")
