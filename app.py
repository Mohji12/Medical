import streamlit as st
import pickle
import numpy as np


head = """
<h1 style='color: #90EE90; text-align: center; font-size: 40px ;border:1px solid red;'>Medical Cost Charges Prediction</h1>
"""
st.markdown(head,unsafe_allow_html=True)


pipe = pickle.load(open('pipe_gbr1.pkl','rb'))
Age = """
<h3 style = 'color:#63d8ab; font-size:30px'>Enter your Age</h3>
"""
Age1 = st.markdown(Age,unsafe_allow_html=True)
Ages = st.number_input("",step = 1,format="%d")
Sex = """
<h3 style = 'color:#63d8ab; font-size:30px'>Choose you Gender</h3>
"""
Age1 = st.markdown(Sex,unsafe_allow_html=True)
options1 = [0,1]
sex = st.selectbox ("0 for Male and 1 for Female",options1,placeholder="0 for Male and 1 for Female")

bmi = """
<h3 style = 'color:#63d8ab; font-size:30px'>Enter your BMI</h3>
"""
BMIdata = st.markdown(bmi,unsafe_allow_html=True)
bmi = st.number_input('bmi')
options2 = [0,1,2,3]
Children = """
<h3 style = 'color:#63d8ab; font-size:30px'>Select Number of Children</h3>
"""
child1 = st.markdown(Children,unsafe_allow_html=True)
children = st.selectbox('Number of children',options2,placeholder= 'Select the number of Children')
option3 = [0,1]
smoke = """
<h3 style = 'color:#63d8ab; font-size:30px'>Smoker</h3>
"""
smoke1 = st.markdown(smoke,unsafe_allow_html=True)
smoker = st.selectbox('0 for Non-Smoker and 1 for smoker',option3)

options4 = [1,2,3,4]
rin = """
<h3 style = 'color:#63d8ab; font-size:30px'>Select Your Region</h3>
"""
ren1 = st.markdown(rin,unsafe_allow_html=True)
region = st.selectbox('southwest:1, southeast:2, northwest:3, northeast:4',options4,placeholder='Enter your region code')

x = pipe.predict([[Ages,sex,bmi,children,smoker,region]])

price = """<h2 style = 'color:#c99f09'> Medical Cost for the patient is
</h2>"""
st.markdown(price,unsafe_allow_html=True)
price1 = np.round(x,2)
price_html = f"""
<p style='font-size: 24px; color:#49f757; text-align: center;'>{price1}</p>"""


st.markdown(price_html,unsafe_allow_html=True)

