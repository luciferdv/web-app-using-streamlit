import streamlit as st
import pickle 

st.title('crop prediction system')
model=pickle.load(open('model.pkl','rb'))

col1,col2=st.columns(2)
n=col1.number_input('enter nitrogen')
p=col2.number_input('enter posphorous')
k=col1.number_input('enter potassium')
t=col2.number_input('enter temperature')
h=col1.number_input('enter humidity')
ph=col2.number_input('enter ph')
r=col1.number_input('enter rainfall')

if st.button('predict'):
    data=[[n,p,k,t,h,ph,r]]
    result=model.predict(data)[0]
    st.success(result)