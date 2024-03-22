'''
CS 5001 Final Project
Name: gallery_page
Author: Yuhao Lu
Date: 2023-12-04
This file includes the Mars photos gallery page of the app.
'''

# pages/gallery_page.py
import streamlit as st
from models.MarsPhotos import MarsPhoto

# Dropdown to select a camera
option = st.selectbox(
    'Which camera you want to choose?',
    ('FHAZ', 'RHAZ', 'MAST', 'CHEMCAM', 'MAHLI', 'MARDI', 'NAVCAM'))
st.write('You selected:', option)

# Initialize MarsPhoto class with the provided API ke
MarsPhoto = MarsPhoto()
# Fetch photos for the selected sol (Martian day) and camera
MarsPhoto.fetch_photos(sol=700, camera=option)

# Header for Mars Photos
st.header('Mars Photos:')

# Display images using Streamlit
st.image(MarsPhoto.images, caption=None, use_column_width=True)
