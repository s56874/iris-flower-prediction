# import required libraries 
import pandas as pd 
import streamlit as st 

# Page configuration
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":smiley:",
    layout="wide"
)

st.title("IRIS Flower Prediction App")
st.write("Flower Prediction App")


# Load the trained model
model = pd.read_pickle("model/iris_model.pkl")

# User input for flower features
sepal_length = st.number_input(
    "sepal_Length (cm)",
    max_value=10.0,
    min_value=0.0,
    step=0.1
)

sepal_width = st.number_input(
    "sepal_Width (cm)",
    max_value=10.0,
    min_value=0.0,
    step=0.1
)

petal_length = st.number_input(
    "petal_Length (cm)",
    max_value=10.0,
    min_value=0.0,
    step=0.1
)

petal_width = st.number_input(
    "petal_Width (cm)",
    max_value=10.0,
    min_value=0.0,
    step=0.1
)

# Create a DataFrame from user input

df = pd.DataFrame({
    "sepal_length": [sepal_length],
    "sepal_width": [sepal_width],
    "petal_length": [petal_length],
    "petal_width": [petal_width]
})

# Predict the Flower species based on user input
if st.button("Predict Flower"):
    df = pd.DataFrame({
        "sepal_length": [sepal_length],
        "sepal_width": [sepal_width],
        "petal_length": [petal_length],
        "petal_width": [petal_width]
    })
    # Make prediction using the trained model
    prediction = model.predict(df)
    # Display the prediction result
    st.success(f"Prediction: {prediction[0]}")