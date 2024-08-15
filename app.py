import re
import pandas as pd
import streamlit as st
from geopy.distance import geodesic
import requests
import random
import math
from PIL import Image
import streamlit as st

def main():
    st.title('Hello, Heroku!')
    st.write('This is a simple Streamlit app deployed on Heroku.')
    image = Image.open('survey.jpg')
    col1, col2 = st.beta_columns(2)
    col1.image(image,
            caption='Designed by slidesgo / Freepik',
            use_column_width=True)

if __name__ == "__main__":
    main()
