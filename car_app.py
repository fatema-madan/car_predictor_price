import streamlit as st
import joblib
import pandas as pd


@st.cache_resource
def load_model():
    return joblib.load("model.pkl")


@st.cache_data
def load_unique_values():
    df = pd.read_csv("data.csv")

    cols = [
        "Make",
        "Model",
        "Engine Fuel Type",
        "Transmission Type",
        "Driven_Wheels",
        "Market Category",
        "Vehicle Size",
        "Vehicle Style"
    ]

    return {
        c: sorted(df[c].dropna().astype(str).unique().tolist())
        for c in cols
    }


model = load_model()
options = load_unique_values()


st.title("Car MSRP Predictor")


year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2026,
    value=2017
)

engine_hp = st.number_input(
    "Engine HP",
    min_value=0.0,
    value=200.0
)

engine_cylinders = st.number_input(
    "Engine Cylinders",
    min_value=0.0,
    value=4.0
)

doors = st.number_input(
    "Number of Doors",
    min_value=0.0,
    value=4.0
)

highway_mpg = st.number_input(
    "Highway MPG",
    min_value=0,
    value=30
)

city_mpg = st.number_input(
    "City MPG",
    min_value=0,
    value=22
)

popularity = st.number_input(
    "Popularity",
    min_value=0,
    value=1000
)


make = st.selectbox(
    "Make",
    options["Make"]
)

car_model = st.selectbox(
    "Model",
    options["Model"]
)

fuel_type = st.selectbox(
    "Engine Fuel Type",
    options["Engine Fuel Type"]
)

transmission = st.selectbox(
    "Transmission Type",
    options["Transmission Type"]
)

drive = st.selectbox(
    "Driven Wheels",
    options["Driven_Wheels"]
)

market_category = st.selectbox(
    "Market Category",
    options["Market Category"]
)

vehicle_size = st.selectbox(
    "Vehicle Size",
    options["Vehicle Size"]
)

vehicle_style = st.selectbox(
    "Vehicle Style",
    options["Vehicle Style"]
)


if st.button("Predict MSRP"):

    row = pd.DataFrame([{
        "Year": year,
        "Engine HP": engine_hp,
        "Engine Cylinders": engine_cylinders,
        "Number of Doors": doors,
        "highway MPG": highway_mpg,
        "city mpg": city_mpg,
        "Popularity": popularity,
        "Make": make,
        "Model": car_model,
        "Engine Fuel Type": fuel_type,
        "Transmission Type": transmission,
        "Driven_Wheels": drive,
        "Market Category": market_category,
        "Vehicle Size": vehicle_size,
        "Vehicle Style": vehicle_style
    }])

    prediction = model.predict(row)[0]

    st.success(
        f"Predicted MSRP: ${prediction:,.0f}"
    )