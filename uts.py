import numpy as np
import pickle
import streamlit as st
from PIL import Image

# Load the saved model
loaded_model = pickle.load(open('ML_NB_DRUG3.pkl','rb'))



def main():

    #Give a title
    img1 = Image.open('logo2.png')
    img1 = img1.resize((900, 300))
    st.image(img1)

    # To get the input data from the user
    age = st.number_input("Umur Anda",value=0)
    
    sex_display = ('Female', 'Male')
    sex_option = list(range(len(sex_display)))
    sex=st.selectbox('Gender Anda', sex_option, format_func=lambda x: sex_display[x])
   
    bp_display = ('Low', 'Normal','High')
    bp_option= list(range(len(bp_display)))
    bp=st.selectbox('Tekanan Darah Anda', bp_option, format_func=lambda x: bp_display[x])

    cholesterol_display = ('Normal','High',)
    cholesterol_option= list(range(len(cholesterol_display)))
    chol=st.selectbox('You selected:', cholesterol_option, format_func=lambda x: cholesterol_display[x])

    na_to_k = st.number_input("Masukan Rasio Sodium to Potasium dalam Darah",value=0)

    #Code for prediction
    drug = ''

    # Create a button for Prediciton

    if st.button("Drug Test Result"):
        features = [[age, sex, bp, chol, na_to_k]]
        prediction = loaded_model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.success(
                "DrugY"
            )
        elif ans == 1:
            st.success(
                "DrugX"
            )
        elif ans == 2:
            st.success(
                "DrugA"
            )
        elif ans == 3:
            st.success(
                "DrugB"
            )
        else:
            st.success(
                "DrugC"
            )

main()
