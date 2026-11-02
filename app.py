import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="عقارات الغردقة")

data = {
'المساحة': [90, 100, 120, 150, 80, 110, 130, 200, 70, 95],
'عدد_الغرف': [2, 3, 3, 4, 2, 3, 3, 5, 1, 2],
'عمر_العقار': [10, 5, 2, 1, 15, 7, 3, 0, 20, 8],
'السعر': [900000, 1200000, 1500000, 2100000, 700000, 1300000, 1600000, 3000000, 500000, 950000]
}

df = pd.DataFrame(data)
X = df[['المساحة', 'عدد_الغرف', 'عمر_العقار']]
y = df['السعر']

model = RandomForestRegressor()
model.fit(X, y)

st.title("🏠 حاسبة سعر الشقة في الغردقة")
مساحة = st.number_input("المساحة", 50, 500, 100)
غرف = st.number_input("عدد الغرف", 1, 10, 3)
عمر = st.number_input("عمر العقار", 0, 30, 5)

if st.button("احسب السعر"):
    سعر = model.predict([[مساحة, غرف, عمر]])
    st.success(f"السعر: {سعر[0]:,.0f} جنيه")
