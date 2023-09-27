import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.altex import bar_chart


st.set_page_config(page_title="Tentang Data Frame", page_icon="📊")

st.markdown("# Tentang Dataset")
st.markdown('''Dataset ini berisi pengukuran polusi udara, seperti Particulate Matter (PM10), Sulfur Dioxide (SO2), Carbon Monoxide (CO), Ozone (O3), 
        dan Natrium Dioxide (NO2). Pengukuran tersebut telah dikonversi ke Indeks Standar Pencemaran Udara (ISPU) atau Pollutant Standards Index (PSI).
        Berikut informasi mengenai kolom-kolom yang ada pada dataset ini:''')
        
st.markdown(''' 

        - :blue[Date]: Tanggal pengukuran.
        - :blue[PM10]: Pengukuran Particulate Matter (PM10).
        - :blue[SO2]: Pengukuran Sulfur Dioxide (SO2).
        - :blue[CO]: Pengukuran Carbon Monoxide (CO).
        - :blue[O3]: Pengukuran Ozone (O3).
        - :blue[NO2]: Pengukuran Natrium Dioxide (NO2).
        - :blue[Critical Component]: Komponen atau komponen yang memiliki nilai pengukuran tertinggi.
        - :blue[Category]: Kategori polusi udara, baik atau tidak baik''')

dataframe = pd.read_csv("polusi_udara_jogja2020.csv")
def data_frame_kotor():
    
    filtered_df = dataframe_explorer(dataframe, case=False)
    st.dataframe(filtered_df, use_container_width=True)


st.markdown("## :red[Data Frame Kotor]")
st.write(
    """ Di bawah menunjukkan Data Frame dari data polusi udara di Jogja tahun 2020 yang belum dibersihkan.
    """
)

data_frame_kotor()

# category_counts = dataframe['Category'].value_counts().reset_index()
# category_counts.columns = ['Category', 'Count']

# st.write("Total Kategori:")
# st.write(category_counts)

# chart = alt.Chart(category_counts).mark_bar().encode(
#     x=alt.X('Category', axis=alt.Axis(labelAngle=0)),
#     y='Count',
#     color='Category'
# ).properties(
#     title="Grafik Total Kategori"
# )

# st.altair_chart(chart, use_container_width=True)




dataframe = pd.read_csv("data.csv")

def data_frame_bersih():  
    filtered_df = dataframe_explorer(dataframe, case=False)
    st.dataframe(filtered_df, use_container_width=True)
    


st.markdown("## :green[Data Frame Bersih]")
st.write(
    """ Di bawah menunjukkan Data Frame dari data polusi udara di Jogja tahun 2020 yang telah dibersihkan.
    Category nilai: 
    - **1**  untuk kategori :blue[**baik**]
    - **2**  untuk kategori :green[**sangat baik**]
    - **3**  untuk kategori :red[**buruk (tidak sehat)**]"""
)

data_frame_bersih()


# category_counts = dataframe['Category'].value_counts().reset_index()
# category_counts.columns = ['Category', 'Count']

# st.write("Total Kategori:")
# st.write(category_counts)

# chart = alt.Chart(category_counts).mark_bar().encode(
#     x=alt.X('Category', axis=alt.Axis(labelAngle=0)),
#     y='Count',
#     color='Category'
# ).properties(
#     title="Grafik Total Kategori"
# )

# st.altair_chart(chart, use_container_width=True)


want_to_contribute = st.button("Coba Predict!")
if want_to_contribute:
    switch_page("Predict")
    
    




