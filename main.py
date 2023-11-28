import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place")

days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="The Number Of days you need forecast for")

option = st.selectbox("Select data to view", ('Temperature', 'Sky'))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict['main']['temp']/10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            path = {"Clear": "images/clear.png", "Cloud": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/rain.png"}
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [path[condition]for condition in sky_conditions ]
            st.image(image_paths, width=115)
    except KeyError:
        st.info("Please Enter a correct place")

