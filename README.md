# 🌱 Crop Disease Prediction System

## Live Demo

**Application Link:**
https://cropdiseasepredictiongit-dguw8u4rlgfs5fmxmsntle.streamlit.app/

---

## Project Overview

The Crop Disease Prediction System is a Machine Learning web application that predicts potential crop diseases based on crop characteristics, environmental conditions, soil properties, and leaf symptoms.

The application helps farmers, agricultural researchers, and agronomists identify crop diseases early and take preventive measures to improve crop health and productivity.

The system is built using:

* Python
* Scikit-Learn
* Pandas
* Streamlit

The application provides disease predictions along with confidence scores and probability distributions for all possible diseases.

---

## Features

✅ User-friendly web interface

✅ Real-time disease prediction

✅ Disease confidence score

✅ Probability comparison for all diseases

✅ Environmental and soil parameter analysis

✅ Machine Learning powered prediction model

---

## Input Parameters

The model uses the following features for prediction:

### Crop Information

* Crop Type

### Environmental Factors

* Temperature (°C)
* Humidity (%)
* Rainfall (mm)

### Soil Factors

* Soil Moisture (%)
* Soil pH
* Nitrogen (mg/kg)
* Phosphorus (mg/kg)
* Potassium (mg/kg)

### Leaf Symptoms

* Leaf Color
* Leaf Spot
* Leaf Wilting
* Leaf Yellowing

These inputs are collected through an interactive Streamlit interface.

---

## Machine Learning Workflow

1. User enters crop and environmental details.
2. Categorical features are encoded using saved encoders.
3. Input data is processed and passed to the trained Random Forest model.
4. The model predicts the most likely crop disease.
5. Prediction confidence is calculated.
6. Disease probability distribution is displayed to the user.

---

## Project Structure

```text
CropDiseasePrediction/
│
├── app.py
├── crop_disease_random_forest.pkl
├── crop_feature_encoders.pkl
├── crop_target_encoder.pkl
├── requirements.txt
├── test.ipynb
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd CropDiseasePrediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages include: Streamlit, Pandas, Joblib, and Scikit-Learn.

---

## Run the Application

```bash
streamlit run app.py
```

---

## Application Interface

The application provides:

* Crop selection
* Environmental parameter inputs
* Soil condition inputs
* Leaf symptom selection
* Disease prediction button
* Confidence score display
* Disease probability table

The Streamlit application is configured as a Crop Disease Prediction System and loads the trained model and encoders during startup.

---

## Sample Output

```text
Predicted Disease: Leaf Blight

Prediction Confidence: 92.45%

Disease Probability:
--------------------------------
Leaf Blight       92.45%
Rust               4.12%
Mildew             2.03%
Others             1.40%
```

---

## Future Enhancements

* Disease treatment recommendations
* Image-based disease detection
* Weather API integration
* Mobile application support
* Multi-language interface
* Cloud deployment with monitoring

---

## Author

Shanmuganathan S

Artificial Intelligence & Machine Learning Project

---

## License

This project is intended for educational and research purposes.
# Crop_disease_prediction
