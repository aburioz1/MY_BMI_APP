#importing the library
import streamlit as st
from PIL import Image
#title of the app
st.title("BUCHI's BMI CALCULATOR")
image = Image.open('pexels-mister-mister-3490348.jpg')
st.image(image, width= 350)
#taking weight in kg
weight = st.number_input('enter your weight in kg ')
name = st.text_input('type your name')
#specify the unit for measurement for height
unit = st.radio('select unit of height', ('cm','m', 'ft'))
if (unit == 'cm'):
    height = st.number_input('cm')
    try:
        bmi = weight/((height/100)**2)
    except:
        st.text('enter your height')
elif (unit == 'm'):
    height = st.number_input('m')
    try:
        bmi = weight / (height ** 2)
    except:
        st.text('enter your height')
else:
    height = st.number_input('ft')
    try:
        bmi = weight / ((height / 3.28) ** 2)
    except:
        st.text('enter your height')
if (st.button('calculate bmi')):
    # print the bmi index
    st.text('bmi index = {}'.format(bmi))

#interpretation of the bmi index
    if(bmi<16):
        st.error('ahhh you are extremely underweight!!! {}, see a dietian'.format(name))
    elif(bmi >= 16 and bmi < 18.5):
        st.warning('hmmm you are underweight o {}, see a dietian'.format(name))
    elif(bmi >=18.5 and bmi < 25):
        st.success('yay!! You are healthy {} , Keep it up'.format(name))
    elif (bmi >=25 and bmi < 30 ):
        st.warning('opps , {} you are overweight'.format(name))
    else:
       st.error('mehn {}, this is obesity'.format(name))

