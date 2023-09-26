import streamlit as st
import pandas as pd
import pickle
import numpy as np
import joblib
import sklearn
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.linear_model import LogisticRegressionCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from imblearn.under_sampling import RandomUnderSampler
from sklearn.datasets import make_classification
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score






df=pd.read_csv("polusi_udara_jogja2020.csv")


processed_data = df.copy()
processed_data["Critical Component"] = LabelEncoder().fit_transform(processed_data["Critical Component"])

# map Label to ordinal encoding
label_map = {
    "Moderate": 1,
    "Good": 2,
    "Unhealthy": 3,
}
processed_data = processed_data.replace({"Category": label_map})

# processed_data.head()

processed_data = processed_data.drop(columns=["Max","NO2","Critical Component"])


st.dataframe(df, use_container_width=True)

X = processed_data[["O3", "CO", "SO2", "PM10"]]
y = processed_data["Category"]

poly = PolynomialFeatures(2)
poly.fit(X)
poly_feats = pd.DataFrame(data=poly.transform(X), columns=poly.get_feature_names_out())
poly_feats = poly_feats.iloc[:, 1:]
print(poly_feats.shape)

poly_feats["Category"] = y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

pipe = Pipeline(steps=[
    ('scaler', StandardScaler()),
#     ('preprocessor', PolynomialFeatures(degree=2)),
    ('estimator', DecisionTreeClassifier())
])

param_grid = {
    "estimator__criterion": ["gini", "entropy", "log_loss"],
    "estimator__splitter": ["best", "random"],
    "estimator__max_depth": [None, 4, 5],
}
search = GridSearchCV(pipe, param_grid, cv=5)
search.fit(X, y)

search.best_score_
search.best_params_

# import numpy as np
# from imblearn.under_sampling import RandomUnderSampler
# from sklearn.datasets import make_classification

# Inisialisasi Random Under-sampler
rus = RandomUnderSampler(sampling_strategy='auto', random_state=42)

# Melakukan undersampling
X_res, y_res = rus.fit_resample(X, y)

# Menampilkan jumlah sampel setelah undersampling
print("Jumlah sampel setelah undersampling:")
print(np.bincount(y_res))

# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.metrics import accuracy_score

gradient = GradientBoostingClassifier()

XGBC = Pipeline ([
    ('Model', gradient)
])

XGBC.fit(X_res, y_res)
y_train_gr = XGBC.predict(X_res)
y_test_gr = XGBC.predict(X_test)

train_acg = accuracy_score(y_res, y_train_gr)
test_acg = accuracy_score(y_test, y_test_gr)

print(f'train_accuracy: {train_acg}')
print(f"accuracy: {test_acg}")



# pipe =pickle.dump(XGBC, open('model.pkl', 'wb'))
# df = pickle.dump(processed_data, open('data.pkl', 'wb'))

# # print("BERHASIL")

# # Load the trained model and user input data
# pipe1 = joblib.load(open('../model.pkl', 'rb'))
# df1 = joblib.load(open('../data.pkl', 'rb'))
# # processed_data.to_csv('data.csv', index=False)


st.write("""
# Udara Jogja Prediction App

This app predicts the **Udara Jogja** type!
""")

st.sidebar.header('User Input Parameters')

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
    prediction = XGBC.predict(user_input)

    # Map the prediction to the corresponding category
    category_mapping = {1: 'Moderate', 2: 'Good', 3: 'Unhealthy'}
    category = category_mapping.get(prediction[0], 'Unknown')

    return category

# Get user input
Input = user_input_features()
ozone = Input['O3'].values[0]
carbon_monoksida = Input['CO'].values[0]
sulfur_dioksida = Input['SO2'].values[0]
particulate_matter = Input['PM10'].values[0]

# Predict the category
category = predict_category(ozone, carbon_monoksida, sulfur_dioksida, particulate_matter)

# Display the predicted category
st.write(f"Prediction: {category} Air Quality")
