import streamlit
import pandas as pd

streamlit.title('My Parents New Healthy Diner')

streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗Omega 3 & bluebarry Oatmeal')
streamlit.text('🐔Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞Harrd-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Statistics
# Read a file from Amazon S3 Bucket
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
