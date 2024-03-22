'''
CS 5001 Final Project
Name: app
Author: Yuhao Lu
Date: 2023-12-04
This file includes the main app of the project.
'''

# app.py
import streamlit as st
import datetime
from models.AstronomyPicture import ApodData

# User input: Choose a date to view the astronomy picture
d = st.date_input("Choose a date to watch that day's astronomy!", datetime.date(2023, 2, 14))
st.write('The day you choose is:', d)
new_date = d.strftime("%Y-%m-%d")

# Display header for the Astronomy Picture section
st.header('Astronomy Picture:')


# Initialize the ApodData object with the NASA API key
api_key = "your_nasa_api_key"
my_astronomy_picture = ApodData(api_key)

# Fetch APOD data for the selected date
my_astronomy_picture.fetch_apod_data(new_date)

# Display button to show the astronomy picture when clicked
if st.button('Click here to see a astronomy picture'):
    st.image(my_astronomy_picture.image, caption='Astronomy Picture of the Day', use_column_width=True)

# Save the astronomy picture to a local file
file_path = my_astronomy_picture.save_image(new_date)

# Download button
with open(file_path, "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="astronomy_picture.jpg",
            mime="image/png"
          )
