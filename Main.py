import streamlit as st

st.title('Calculator Segitiga'
)

"""ini adalah kalkulator untuk menghitung luas dan keliling segitu """

Alas = st.number_input("Alas" ,0)
Tinggi = st.number_input("Tinggi",0)

Luas = 0.5 * Alas*Tinggi 
Jawaban = Luas
print(Luas)
st.success(Luas)
st.button("Hasil")
if Jawaban:
    print(Luas)
    st.success("0")

