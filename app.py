import pickle
import streamlit as st
import numpy as np

# Membaca model
pokemon_model = pickle.load(open('Pokemon_model.sav','rb'))

# Judul web
st.title('Prediksi Pokemon')

# Input data dengan contoh angka valid untuk pengujian
Total = st.text_input('Total')
HP = st.text_input('HP')
Attack = st.text_input('Attack')
Defense = st.text_input('Defense')
SP_Attack = st.text_input('SP_Attack')
Sp_Defense = st.text_input('Sp_Defense')
Speed = st.text_input('Speed')
Generation = st.text_input('Generation')

prediksi_pokemon = ''

# Membuat tombol untuk prediksi
if st.button('Prediksi'):
    try:
        # Konversi input menjadi numerik
        inputs = np.array([[float(Total), float(HP), float(Attack), float(Defense),
                  float(SP_Attack), float(Sp_Defense), float(Speed), float(Generation)]])
        # Lakukan prediksi
        pokemon_prediksi = pokemon_model.predict(inputs)
        
        if pokemon_prediksi[0] == 1:
            prediksi_pokemon = 'Pokemon Lagendary'
            st.success(prediksi_pokemon)
        else:
            prediksi_pokemon = '<span style="color:red">Bukan Pokemon Lagendary</span>'
            st.markdown(prediksi_pokemon, unsafe_allow_html=True)
    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
