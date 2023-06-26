import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')

streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗Omega 3 & bluebarry Oatmeal')
streamlit.text('🐔Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞Harrd-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


# Statistics
# Read a file from Amazon S3 Bucket
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Custom search
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error('Please select a fruit to get information.')
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      #streamlit.write('The user entered ', fruit_choice)
      #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
      #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      # write your own comment - what does this do?
      streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()
#Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list conatains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add ?','jackfruit')
insert_query = "INSERT INTO fruit_load_list (fruit_name) VALUES ('{}')".format(add_my_fruit)
streamlit.write("Thanks for adding : ", add_my_fruit)  # Print the SQL statement
my_cur.execute(insert_query)
