import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place")

days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="The Number Of days you need forecast for")

option = st.selectbox("Select data to view", ('Temperature', 'Sky'))

st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    temperature = [10, 11, 15]
    date = ["2020 - 26 - 10", "2020 - 27 - 10", "2020 - 28 - 10"]
    temperature = [days * i for i in temperature]
    return date, temperature


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
