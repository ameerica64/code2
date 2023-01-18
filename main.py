import streamlit as st
import pandas as pd

data = {'Series_1':[1,3,4,5,7] ,'Series':[10,30,40,100,250]}

df = pd.DataFrame(data)

st.title('our first app')
st.subheader('Automate with streamlit')
st.write('''first app enjoy it!''')

st.write(df)
st.line_chart(df)
st.area_chart(df)


