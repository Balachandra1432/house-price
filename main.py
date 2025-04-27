import pandas as pd
import pickle as pk
import streamlit as st
model=pk.load(open("house_price_model.pkl","rb"))
df=pd.read_csv("house_cleaned_data.xls")
df=df.sort_values(by="location")
st.header("House Price Prediction")

area=st.selectbox("select area",df["location"].unique())
sqft=st.number_input("enter total square feet")
bed=st.number_input("enter no.of bed rooms")
bath=st.number_input("enter no.of bath rooms")

if st.button("Predict Price"):
    value=pd.DataFrame([[area,sqft,bed,bath]],columns=["location","total_sqft","bath","BHK"])
    price=round(model.predict(value)[0]*100000,2)
    st.header(str(price)+" rupeess")