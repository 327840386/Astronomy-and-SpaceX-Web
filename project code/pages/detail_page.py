'''
CS 5001 Final Project
Name: detail_page
Author: Yuhao Lu
Date: 2023-12-04
This file includes the Rocket detail page of the app.
'''

import streamlit as st
from models.Rocket import Rockets

# Input for rocket_id
rocket_id = st.text_input('rocket_id', '5e9d0d95eda69974db09d1ed')
st.write('The current rocket id is', rocket_id)

# Header for Rocket detail
st.header('Rocket detail:')

# Initialize Rockets class
my_rocket = Rockets()

# Fetch rocket data
my_rocket_data = my_rocket.fetch_rocket_data(rocket_id)

# Button to trigger fetching and displaying rocket details
if st.button('Click here to see rocket details'):
    # Display information in a more organized format
    st.subheader('Rocket Information')

    # Display name, description, and other key details
    st.markdown(f'**Name:** {my_rocket_data.get("name")}')
    st.markdown(f'**Description:** {my_rocket_data.get("description")}')

    # Display numerical details using a table
    st.subheader('Numeric Details')
    numeric_details = {
        'Cost per Launch': f'{my_rocket_data.get("cost_per_launch")} USD',
        'Height': my_rocket_data.get('height'),
        'Mass': my_rocket_data.get('mass'),
        'Diameter': my_rocket_data.get('diameter'),
        'Stages': my_rocket_data.get('stages'),
        'Success Rate (%)': my_rocket_data.get('success_rate_pct'),
    }
    st.table(numeric_details)

    # Display images
    st.subheader('Rocket Images')
    for image in my_rocket_data.get('flickr_images', []):
        st.image(image, caption='Rocket Image', use_column_width=True)

    # Display additional information in columns
    st.subheader('Additional Information')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'**First Flight:** {my_rocket_data.get("first_flight")}')
        st.markdown(f'**Country:** {my_rocket_data.get("country")}')
        st.markdown(f'**Company:** {my_rocket_data.get("company")}')
    with col2:
        st.markdown(f'**Type:** {my_rocket_data.get("type")}')
        st.markdown(f'**Wikipedia:** [{my_rocket_data.get("wikipedia")}](\
            {my_rocket_data.get("wikipedia")})')
        st.markdown(f'**Rocket ID:** {my_rocket_data.get("id")}')
