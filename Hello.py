# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="About Streamlit",
        page_icon="👋",
    )

    st.write("# Selamat Datang di Big Data Streamlit App! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit adalah sebuah framework open-source yang digunakan untuk membangun aplikasi web
        interaktif dengan framework Python.
        
        Aplikasi ini adalah Tugas Besar dari Rekruitas MBC Laboratory 2023 divisi Big Data.
        Semoga Aplikasi ini dapat membantu dan bermanfaat bagi teman-teman semua! 😎🙌
        
                
        ### Apa tujuan aplikasi ini?
        - Sebagai tugas besar dari Rekruitasi MBC Laboratory Big Data.
        - Mengaplikasikan Machine Learning untuk memprediksi kualitas udara berdasarkan parameter yang disesuaikan.
        - Memberikan informasi yang berguna tentang kualitas udara.
          
        ### Apa manfaat penggunaan aplikasi ini?
        - Dapat memprediksi kualitas udara berdasarkan parameter yang disesuaikan.
        - Memungkinkan pengguna untuk menjelajahi data dan informasi seputar kualitas udara.
        
        ## Source Link:
        
        **Google Colab**
        [![AirQualityML.ipynb](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1izcv1jkd0rEb4OBFnGXy2JX17dcvSdB6?usp=sharing)
        
        **Dataset**
        Kaggle: [Air Quality in Yogyakarta, Indonesia (2020)](https://github.com/streamlit/demo-uber-nyc-pickups)
        
        **Link**
        GitHub: [github.com/Aelzi/tubesbd](https://github.com/Aelzi/tubesbd)
      """
      )
    
    
    
    want_to_contribute = st.button("Coba Predict!")
    if want_to_contribute:
      switch_page("Predict")


if __name__ == "__main__":
    run()
