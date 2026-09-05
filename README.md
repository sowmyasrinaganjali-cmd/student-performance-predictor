# 🎓 Student Performance AI

An AI-powered machine learning web application that predicts student academic performance based on academic and lifestyle factors.

## 🚀 Live Demo

[Open Student Performance AI](PASTE-YOUR-STREAMLIT-LINK-HERE)

## 📌 About the Project

Student Performance AI uses machine learning to estimate a student's potential final score using factors such as:

- 📚 Study Hours
- 📝 Previous Score
- 📅 Attendance
- 😴 Sleep Hours
- 📋 Assignments Completed
- 🙋 Participation

The application provides a predicted score, performance level, visual insights, and personalized recommendations.

## ✨ Features

- 🤖 Machine learning-based prediction
- 🎯 Predicted final score
- 📊 Performance visualization
- 💡 Personalized recommendations
- 🖥️ Interactive Streamlit interface
- ⚡ Fast predictions

## 🧠 Machine Learning

**Algorithm:** Linear Regression

**Evaluation Metrics:**
- Mean Absolute Error (MAE)
- R² Score

The trained model is saved using Joblib and loaded by the Streamlit application.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## 📂 Project Structure

```text
student-performance-predictor/
│
├── app.py
├── requirements.txt
│
├── data/
│   └── student_data.csv
│
└── model/
    └── student_performance_model.pkl
##  Run Locally

Clone the repository:

```bash
git clone https://github.com/sowmyasrinaganjali-cmd/student-performance-predictor.git

pip install -r requirements.txt

python -m streamlit run app.py

## Developer

**Sowmya**

B.Tech | AIML Student
