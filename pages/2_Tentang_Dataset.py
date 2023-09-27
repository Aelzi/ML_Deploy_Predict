import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Tentang Data Frame", page_icon="📊")

dataframe = pd.read_csv("polusi_udara_jogja2020.csv")

def data_frame_kotor():
    filtered_df = dataframe_explorer(dataframe, case=False)
    st.dataframe(filtered_df, use_container_width=True)


st.markdown("# Data Frame Kotor")
st.write(
    """ Di bawah menunjukkan Data Frame dari data polusi udara di Jogja tahun 2020 yang belum dibersihkan.
    """
)

data_frame_kotor()


dataframe = pd.read_csv("data.csv")

def data_frame_bersih():
    filtered_df = dataframe_explorer(dataframe, case=False)
    st.dataframe(filtered_df, use_container_width=True)



st.markdown("# Data Frame Bersih")
st.write(
    """ Di bawah menunjukkan Data Frame dari data polusi udara di Jogja tahun 2020 yang telah dibersihkan.
    Category nilai: 
    - **1**  untuk kategori :blue[**baik**]
    - **2**  untuk kategori :green[**sangat baik**]
    - **3**  untuk kategori :red[**buruk (tidak sehat)**]"""
)

data_frame_bersih()


want_to_contribute = st.button("Coba Predict!")
if want_to_contribute:
    switch_page("Predict")
    
    




