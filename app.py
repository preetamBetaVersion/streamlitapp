import streamlit as st
import pandas as pd

st.set_page_config(
     page_title="Portfolio app",
     page_icon="☘",
     layout="centered"
 )

st.title('Data Analysis portfolio app')
st.markdown('> In this project, we will try to answer a few questions related to diabetes using visualization tools to get meaningful insights.')
st.markdown("#", unsafe_allow_html=False)

# Creating the dataframe
df = pd.read_csv('diabetes.csv')

st.header('The diabetes dataset ')
st.dataframe(df)

@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='diabetes.csv',
     mime='text/csv',
 )
st.markdown('#', unsafe_allow_html=False)

# Mean calculator
st.subheader('Mean calculator (diabetic people)')
new_df = df.loc[df['outcome']==True]
age = new_df['age'].mean()
bloodpressure = new_df['bloodpressure'].mean()
bmi = new_df['bmi'].mean()
insulin = new_df['insulin'].mean()
glucose = new_df['glucose'].mean()

option = st.selectbox(
     'Select your option',
     ('','Age', 'Glucose','Blood pressure', 'BMI'))
def mean_cal(option):
    if option =='Age':
        st.info("{:.2f}".format(age))
    elif option == 'Blood pressure':
        st.info("{:.2f}".format(bloodpressure))
    elif option=='BMI':
        st.info("{:.2f}".format(bmi))
    elif option=='Glucose':
        st.info("{:.2f}".format(glucose))
    else:
        st.caption('Output display area')
mean_cal(option)
st.markdown('#', unsafe_allow_html=False)

# Bar chart
st.subheader('Bar chart representation of diabetic people against a selected parameter')

option = st.selectbox(
     'Select your option',
     ('','Age', 'Blood pressure', 'Glucose','BMI', 'Insulin'))

def show_chart(option):
    if option == 'Age':
        st.bar_chart(data=new_df['age'].head(20), width=0, height=0, use_container_width=True)
    elif option=='Blood pressure':
        st.bar_chart(data=new_df['bloodpressure'].head(20), width=0, height=0, use_container_width=True)
    elif option=='Glucose':
        st.bar_chart(data=new_df['glucose'].head(20), width=0, height=0, use_container_width=True)
    elif option=='BMI':
        st.bar_chart(data=new_df['bmi'].head(20), width=0, height=0, use_container_width=True)
    elif option == 'Insulin':
        st.bar_chart(data=new_df['insulin'].head(20), width=0, height=0, use_container_width=True)
    else:
        st.caption('')

show_chart(option)
st.markdown('#')

# Metric widget
st.subheader('Information based on age and it\'s deviation from mean value')

age = st.slider('Select age', 0, 130,25)
st.write("The value of age selected is ",age)


mean_df_with_selected_mean_age = new_df.loc[new_df['age']==age].mean()

bmi_percentage_change = (mean_df_with_selected_mean_age['bmi'] - bmi)/bmi
bmi_percentage_change = "{:.2%}".format(bmi_percentage_change)

glucose_percentage_change = (mean_df_with_selected_mean_age['glucose'] - glucose)/glucose
glucose_percentage_change = "{:.2%}".format(glucose_percentage_change)

insulin_percentage_change = (mean_df_with_selected_mean_age['insulin'] - insulin)/insulin
insulin_percentage_change = "{:.2%}".format(insulin_percentage_change)

col1, col2, col3 = st.columns(3)
col1.metric("BMI", "{:.2f}".format(mean_df_with_selected_mean_age['bmi']), bmi_percentage_change)
col2.metric("Glucose", "{:.2f}".format(mean_df_with_selected_mean_age['glucose']), glucose_percentage_change )
col3.metric("Insulin", "{:.2f}".format(mean_df_with_selected_mean_age['insulin']), insulin_percentage_change)


#Keynotes
st.markdown('#')
st.error('**Note**: Data can be misleading sometimes if there isn\'t enough of it. So it is important to carefully analyse and understand the data you are working with.')
st.markdown('#')
st.caption('Data is wonderful. It makes decision making easier and hence I ♥ it. Cheers!!!!')