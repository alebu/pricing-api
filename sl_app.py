import streamlit as st
import json 
import requests

st.title("Call Options Price Calculator")

calculation_method = st.selectbox(
    "What method do you want to use?",
    ['Closed Form']
)

S = st.number_input("Spot Price", value = 100)
K = st.number_input("Strike Price", value = 100)
T = st.slider("Time to expiry (fraction of a year)", min_value = 0., max_value = 1., step = 0.01, value = 1.)
r = st.slider("Risk-free interest rate", min_value = 0., max_value = .2,  step = 0.01, value = 0.05)
sigma = st.slider("Volatility", min_value = 0., max_value = 1.,  step = 0.01, value = 0.2)

inputs = {"S":S, "K":K, "T":T, "t":0, "r":r, "sigma":sigma}

if st.button('Calculate'):
    print(json.dumps(inputs))
    res = requests.post(url = "http://127.0.0.1:8000/calculate", data = json.dumps(inputs))
    st.subheader(f"Call Option Price: {res.text}💰")