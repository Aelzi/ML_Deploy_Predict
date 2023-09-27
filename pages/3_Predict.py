import streamlit as st
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from imblearn.under_sampling import RandomUnderSampler

judul = st.write(" # Prediksi Kualitas Udara")

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




X = processed_data[["O3", "CO", "SO2", "PM10"]]
y = processed_data["Category"]

poly = PolynomialFeatures(2)
poly.fit(X)
poly_feats = pd.DataFrame(data=poly.transform(X), columns=poly.get_feature_names_out())
poly_feats = poly_feats.iloc[:, 1:]
print(poly_feats.shape)

poly_feats["Category"] = y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# pipe = Pipeline(steps=[
#     ('scaler', StandardScaler()),
# #     ('preprocessor', PolynomialFeatures(degree=2)),
#     ('estimator', DecisionTreeClassifier())
# ])

# param_grid = {
#     "estimator__criterion": ["gini", "entropy", "log_loss"],
#     "estimator__splitter": ["best", "random"],
#     "estimator__max_depth": [None, 4, 5],
# }
# search = GridSearchCV(pipe, param_grid, cv=5)
# search.fit(X, y)

# search.best_score_
# search.best_params_

# import numpy as np
# from imblearn.under_sampling import RandomUnderSampler
# from sklearn.datasets import make_classification

# Inisialisasi Random Under-sampler
# rus = RandomUnderSampler(sampling_strategy='auto', random_state=42)

# Melakukan undersampling
# X_res, y_res = rus.fit_resample(X, y)

# Menampilkan jumlah sampel setelah undersampling
# print("Jumlah sampel setelah undersampling:")
# print(np.bincount(y_res))

# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.metrics import accuracy_score

# gradient = GradientBoostingClassifier()

# XGBC = Pipeline ([
#     ('Model', gradient)
# ])

# XGBC.fit(X_res, y_res)
# y_train_gr = XGBC.predict(X_res)
# y_test_gr = XGBC.predict(X_test)

# train_acg = accuracy_score(y_res, y_train_gr)
# test_acg = accuracy_score(y_test, y_test_gr)
# print("Accuracy Gradient Boosting Classifier")
# print(f'train_accuracy: {train_acg}')
# print(f"accuracy: {test_acg}")

# clf = RandomForestClassifier()
# RFC = Pipeline ([
#     ('Model', clf)
# ])
# RFC.fit(X_res, y_res)
# y_train_rf = RFC.predict(X_res)
# y_test_rf = RFC.predict(X_test)

# train_acrf = accuracy_score(y_res, y_train_rf)
# test_acrf = accuracy_score(y_test, y_test_rf)
# print("Accuracy Random Forest Classifier")
# print(f'train_accuracy: {train_acrf}')
# print(f"accuracy: {test_acrf}")

# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LogisticRegression
# from imblearn.under_sampling import RandomUnderSampler

# Melakukan undersampling pada data pelatihan
undersampler = RandomUnderSampler(sampling_strategy='majority', random_state=42)
X_train_resampledww, y_train_resampledww = undersampler.fit_resample(X_train, y_train)
logistic_regression = LogisticRegression(max_iter=1000, random_state=42)
cv_scores = cross_val_score(logistic_regression, X_train_resampledww, y_train_resampledww, cv=5)
train_accuracy = cv_scores.mean()
logistic_regression.fit(X_train_resampledww, y_train_resampledww)
test_accuracy = logistic_regression.score(X_test, y_test)
print("Accuracy Logistic Regression")
print("Train Accuracy:", train_accuracy)
print("Test Accuracy:", test_accuracy)


# pipe =pickle.dump(XGBC, open('model.pkl', 'wb'))
# df = pickle.dump(processed_data, open('data.pkl', 'wb'))

# # print("BERHASIL")

# # Load the trained model and user input data
# pipe1 = joblib.load(open('../model.pkl', 'rb'))
# df1 = joblib.load(open('../data.pkl', 'rb'))
# # processed_data.to_csv('data.csv', index=False)



st.write("""

## Prediksi ini menggunakan metode:
# :blue[**Logistic Regression**] + :green[**Cross Validation**] + :red[**Oversampling**]

:blue[**Logistik Regresi**] adalah metode statistik yang membantu dalam mengklasifikasikan kualitas udara 
berdasarkan parameter-parameter seperti **ozon**, **karbon monoksida**, **sulfur dioksida**, dan **partikulat 
matter 10**. Ini membantu mengidentifikasi apakah udara tersebut baik atau buruk untuk kesehatan 
berdasarkan data parameter-parameter tersebut, memungkinkan pengambilan tindakan yang sesuai untuk 
menjaga kualitas udara yang lebih baik.

:green[**Cross Validation**] adalah teknik yang digunakan untuk mengukur seberapa baik model kita dalam memprediksi 
data yang belum pernah dilihat sebelumnya. Dalam konteks polusi udara, kita akan membagi data kita menjadi beberapa subset.

:red[**Oversampling**] adalah teknik yang digunakan untuk mengatasi ketidakseimbangan dalam dataset. Dalam konteks polusi udara, kita mungkin memiliki lebih banyak data pada 
tingkat polusi yang rendah daripada yang tinggi. Dengan oversampling, kita membuat salinan tambahan dari data yang tingkat polusinya tinggi sehingga dataset kita menjadi lebih seimbang.
""")

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
    prediction = logistic_regression.predict(user_input)

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

