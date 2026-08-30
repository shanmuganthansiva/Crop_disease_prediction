import streamlit as st
import pandas as pd
import joblib


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Crop Disease Prediction",
    page_icon="🌱",
    layout="centered"
)


# -----------------------------
# Load Saved Models
# -----------------------------
model = joblib.load("crop_disease_random_forest.pkl")
feature_encoders = joblib.load("crop_feature_encoders.pkl")
target_encoder = joblib.load("crop_target_encoder.pkl")


# -----------------------------
# Title
# -----------------------------
st.title("🌱 Crop Disease Prediction System")
st.write(
    "Enter the crop and environmental details below "
    "to predict the possible crop disease."
)

st.divider()


# -----------------------------
# User Inputs
# -----------------------------

crop = st.selectbox(
    "Select Crop",
    feature_encoders["Crop"].classes_
)

temperature = st.number_input(
    "Temperature (°C)",
    min_value=0.0,
    max_value=50.0,
    value=28.5
)

humidity = st.number_input(
    "Humidity (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

rainfall = st.number_input(
    "Rainfall (mm)",
    min_value=0.0,
    max_value=100.0,
    value=15.0
)

soil_moisture = st.number_input(
    "Soil Moisture (%)",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

soil_ph = st.number_input(
    "Soil pH",
    min_value=0.0,
    max_value=14.0,
    value=6.5
)

nitrogen = st.number_input(
    "Nitrogen (mg/kg)",
    min_value=0,
    max_value=200,
    value=80
)

phosphorus = st.number_input(
    "Phosphorus (mg/kg)",
    min_value=0,
    max_value=200,
    value=45
)

potassium = st.number_input(
    "Potassium (mg/kg)",
    min_value=0,
    max_value=200,
    value=60
)

leaf_color = st.selectbox(
    "Leaf Color",
    feature_encoders["Leaf_Color"].classes_
)

leaf_spot = st.selectbox(
    "Leaf Spot",
    feature_encoders["Leaf_Spot"].classes_
)

leaf_wilting = st.selectbox(
    "Leaf Wilting",
    feature_encoders["Leaf_Wilting"].classes_
)

leaf_yellowing = st.selectbox(
    "Leaf Yellowing",
    feature_encoders["Leaf_Yellowing"].classes_
)


# -----------------------------
# Prediction Button
# -----------------------------

if st.button("🔍 Predict Disease", use_container_width=True):

    # Create input DataFrame
    input_data = pd.DataFrame({
        "Crop": [crop],
        "Temperature_C": [temperature],
        "Humidity_Percent": [humidity],
        "Rainfall_mm": [rainfall],
        "Soil_Moisture_Percent": [soil_moisture],
        "Soil_pH": [soil_ph],
        "Nitrogen_mg_kg": [nitrogen],
        "Phosphorus_mg_kg": [phosphorus],
        "Potassium_mg_kg": [potassium],
        "Leaf_Color": [leaf_color],
        "Leaf_Spot": [leaf_spot],
        "Leaf_Wilting": [leaf_wilting],
        "Leaf_Yellowing": [leaf_yellowing]
    })

    # Encode categorical columns
    categorical_columns = [
        "Crop",
        "Leaf_Color",
        "Leaf_Spot",
        "Leaf_Wilting",
        "Leaf_Yellowing"
    ]

    for column in categorical_columns:
        input_data[column] = feature_encoders[column].transform(
            input_data[column]
        )

    # Prediction
    prediction = model.predict(input_data)

    predicted_disease = target_encoder.inverse_transform(
        prediction
    )[0]

    # Probability
    probabilities = model.predict_proba(input_data)[0]

    confidence = max(probabilities) * 100

    # -----------------------------
    # Display Result
    # -----------------------------

    st.divider()

    st.subheader("🌿 Prediction Result")

    st.success(
        f"Predicted Disease: **{predicted_disease}**"
    )

    st.info(
        f"Prediction Confidence: **{confidence:.2f}%**"
    )

    # Probability table
    probability_df = pd.DataFrame({
        "Disease": target_encoder.classes_,
        "Probability (%)": probabilities * 100
    })

    probability_df = probability_df.sort_values(
        by="Probability (%)",
        ascending=False
    )

    st.subheader("📊 Disease Probability")

    st.dataframe(
        probability_df.style.format({
            "Probability (%)": "{:.2f}%"
        }),
        use_container_width=True
    )