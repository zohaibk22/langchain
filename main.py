import langchain_helper as lch
import streamlit as st

st.title("Car Generator")

car_mod_type = st.sidebar.selectbox("What is your modification type?", ("Exterior", "performance", "Interior", "Suspension"))

if car_mod_type:
    car_make = st.sidebar.text_area (f"So you picked {car_mod_type}! For what car brand?", max_chars=100)

if car_make:
    car_model = st.sidebar.text_area(f"Wow! {car_make} is a great company. What model do you have?", max_chars=100)


if car_model:
    response = lch.generate_pet_name(car_mod_type, car_make, car_model)
    st.text(response['car_modifications'])