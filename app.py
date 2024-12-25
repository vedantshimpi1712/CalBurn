import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model and dataset
models = pickle.load(open('model.pkl', 'rb'))
x_train = pd.read_csv('x_train.csv')


# Prediction function
def pred(Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp):
    features = np.array([[Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp]])
    prediction = models.predict(features).reshape(1, -1)
    return prediction[0]


# Custom styles for the app
st.markdown("""
    <style>
        .big-font {
            font-size: 30px;
            color: #ff6347;
            font-weight: bold;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 15px;
            border-radius: 10px;
            width: 250px;
        }
        .container {
            background-color: #f7f7f7;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .result-card {
            background-color: #f0f8ff;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title at the top of the page
st.markdown('<p class="big-font">Calories Burnt Prediction</p>', unsafe_allow_html=True)

# Side Bar Inputs
st.sidebar.title("User Input")
Gender = st.sidebar.selectbox('Gender', ['Male', 'Female'], help="Select your gender")
Age = st.sidebar.slider('Age', min_value=int(x_train['Age'].min()), max_value=int(x_train['Age'].max()), value=25,
                        help="Select your age")
Height = st.sidebar.slider('Height (cm)', min_value=int(x_train['Height'].min()),
                           max_value=int(x_train['Height'].max()), value=170, help="Select your height in cm")
Weight = st.sidebar.slider('Weight (kg)', min_value=int(x_train['Weight'].min()),
                           max_value=int(x_train['Weight'].max()), value=70, help="Select your weight in kg")
Duration = st.sidebar.slider('Duration (minutes)', min_value=int(x_train['Duration'].min()),
                             max_value=int(x_train['Duration'].max()), value=30,
                             help="Select the duration of activity in minutes")
Heart_rate = st.sidebar.slider('Heart Rate (bpm)', min_value=int(x_train['Heart_Rate'].min()),
                               max_value=int(x_train['Heart_Rate'].max()), value=120,
                               help="Select your heart rate in beats per minute")
Body_temp = st.sidebar.slider('Body Temperature (°C)', min_value=int(x_train['Body_Temp'].min()),
                              max_value=int(x_train['Body_Temp'].max()), value=36,
                              help="Select your body temperature in Celsius")

# Map gender input to numerical value for model prediction
gender_map = {'Male': 0, 'Female': 1}
Gender_numeric = gender_map[Gender]

# Prediction button
if st.button('Predict'):
    with st.spinner('Calculating...'):
        result = pred(Gender_numeric, Age, Height, Weight, Duration, Heart_rate, Body_temp)

    # Show the result dynamically
    st.success("Prediction Complete!")

    # Extract the result as a scalar
    result_value = result[0]  # Assuming result is a numpy array with a single value

    # Show the result with proper formatting
    st.markdown(f"""
        <div class="result-card">
            <h3 style="color: #333;">You have burned approximately:</h3>
            <h2 style="color: #ff6347; font-size: 36px;">{result_value:.2f} kcal</h2>
        </div>
    """, unsafe_allow_html=True)

# Expanded Explanation Section with Math Formula and Styling
st.markdown("""
    <div class="container" style="background-color: #f7f7f7; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h3 style="color: #333; font-size: 24px;">How the prediction works:</h3>
        <p style="color: #555; font-size: 16px;">This app predicts the number of calories burned based on several factors related to your physical activity.</p>
        <p style="color: #555; font-size: 16px;">The primary factors that affect the number of calories burned are:</p>
        <ul style="color: #555; font-size: 16px;">
            <li><strong>Gender:</strong> Gender can impact metabolic rate and overall energy expenditure during physical activities.</li>
            <li><strong>Age:</strong> As you age, your metabolic rate may decrease, affecting the number of calories burned.</li>
            <li><strong>Height:</strong> Taller individuals often burn more calories because of a larger body mass.</li>
            <li><strong>Weight:</strong> Heavier individuals generally burn more calories, as it requires more energy to move a larger body mass.</li>
            <li><strong>Duration:</strong> The longer the duration of your physical activity, the more calories you burn.</li>
            <li><strong>Heart Rate:</strong> A higher heart rate usually indicates more intense exercise, leading to more calories burned.</li>
            <li><strong>Body Temperature:</strong> Higher body temperatures can suggest more strenuous activity, possibly increasing calorie expenditure.</li>
        </ul>
        <p style="color: #555; font-size: 16px;"><strong>Formula to estimate calories burned:</strong></p>
        <p style="color: #555; font-size: 16px;">Calories burned during an activity can be calculated using the following formula:</p>
        <p style="font-size: 18px; text-align: center; color: #0073e6;">
            Calories Burned=MET×Body Weight(kg)×Duration(hours)
        </p>
        <p style="color: #555; font-size: 16px;">Where:</p>
        <ul style="color: #555; font-size: 16px;">
            <li><strong>MET (Metabolic Equivalent of Task):</strong> Represents the energy cost of physical activity. For example, running has a higher MET value than walking.</li>
            <li><strong>Body Weight:</strong> Heavier people burn more calories at the same intensity.</li>
            <li><strong>Duration:</strong> The longer the activity, the more calories are burned.</li>
        </ul>
        <p style="color: #555; font-size: 16px;">This formula provides a reasonable estimate based on common activity data. The MET value varies by activity type:</p>
        <ul style="color: #555; font-size: 16px;">
            <li>Walking: MET = 3.8</li>
            <li>Running: MET = 7.0 to 12.0 (depending on intensity)</li>
            <li>Cycling: MET = 4.0 to 8.0</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

