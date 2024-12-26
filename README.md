# CalBurn - Calorie Burn Prediction App

CalBurn is a simple and dynamic web application that predicts the number of calories burned based on user input. This app uses a machine learning model to provide accurate predictions and offers an intuitive interface for users. 💪

  ✨ Features
- 🚻 Input key physical parameters like Gender, Age, Height, Weight, Duration, Heart Rate, and Body Temperature.
- 🤖 Machine learning-powered calorie burn prediction.
- 🎨 Dynamic and responsive user interface built with Streamlit.
- 📊 Clear visual representation of results with stylish design.

  🛠️ How It Works
1. 📝 Enter your personal and workout-related data into the app:
   - Gender: Male or Female
   - Age: Your current age
   - Height: In centimeters
   - Weight: In kilograms
   - Duration: Duration of activity in minutes
   - Heart Rate: Average heart rate during activity in bpm
   - Body Temperature: Body temperature during activity in °C
   
2. The app uses the following formula to estimate the calories burned:
   
   Calories Burned = f(\text{Gender, Age, Height, Weight, Duration, Heart Rate, Body Temperature})
   
   The prediction is based on a pre-trained machine learning model. 📉

3. 🔘 Click the Predict button to see the result.

4. 🖥️ The app displays the calories burned along with an explanation of the parameters used.


    📂 Project Files
   
    -app.py: Main Streamlit app file.
   
    -model.pkl: Pre-trained machine learning model for prediction.
   
    -x_train.csv: Training data used for building the model.
    
    🖥️ Technologies Used
   
      -Streamlit: For building the web interface.
   
      -Python: Backend development and machine learning.
   
      -NumPy & Pandas: For data manipulation and handling.
   
      -Pickle: For model serialization.

📸 Screenshots
![Screenshot (119)](https://github.com/user-attachments/assets/ca2c2073-5272-4296-b18e-e4c01d006f91)

🙌 Contributions
Feel free to fork this repository and make improvements. Contributions are welcome! 🤝

Developed with ❤️ by Vedant Shimpi.
