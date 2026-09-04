
import streamlit as st
import pandas as pd
import joblib

# ============================================================
# LOAD MACHINE LEARNING MODEL
# ============================================================

model = joblib.load("model/student_performance_model.pkl")


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>/




    /* ---------------- GLOBAL ---------------- */

    .stApp {
        background: #f7f8fc;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* ---------------- HERO ---------------- */

    .hero {
        background: linear-gradient(
            120deg,
            #315bea 0%,
            #6546d9 50%,
            #7b3fb0 100%
        );

        border-radius: 24px;
        padding: 42px 50px;
        margin-bottom: 28px;

        color: white;

        box-shadow:
            0 15px 40px rgba(70, 70, 150, 0.18);
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        margin: 0;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        font-size: 18px;
        margin-top: 12px;
        opacity: 0.92;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.16);
        padding: 8px 16px;
        border-radius: 30px;
        margin-bottom: 15px;
        font-size: 14px;
    }


    /* ---------------- CARDS ---------------- */

    .card {
        background: white;
        border-radius: 20px;
        padding: 28px;

        box-shadow:
            0 8px 30px rgba(30, 40, 80, 0.07);

        border: 1px solid #eef0f6;

        margin-bottom: 20px;
    }

    .card-title {
        font-size: 23px;
        font-weight: 750;
        color: #17213b;
        margin-bottom: 5px;
    }

    .card-subtitle {
        color: #69738c;
        font-size: 14px;
        margin-bottom: 20px;
    }


    /* ---------------- SCORE CARD ---------------- */

    .score-card {
        background: linear-gradient(
            135deg,
            #12b981,
            #11aeca
        );

        border-radius: 20px;
        padding: 28px;

        color: white;

        min-height: 180px;

        box-shadow:
            0 12px 30px rgba(17, 174, 202, 0.18);
    }

    .score-label {
        font-size: 15px;
        opacity: 0.9;
    }

    .score-number {
        font-size: 55px;
        font-weight: 800;
        margin: 8px 0;
    }

    .score-description {
        font-size: 14px;
        opacity: 0.9;
    }


    /* ---------------- PERFORMANCE CARD ---------------- */

    .performance-card {
        background: white;
        border-radius: 20px;
        padding: 28px;

        min-height: 180px;

        border: 1px solid #eef0f6;

        box-shadow:
            0 8px 30px rgba(30, 40, 80, 0.07);
    }

    .good {
        color: #11a875;
        font-size: 30px;
        font-weight: 800;
    }

    .excellent {
        color: #f39c12;
        font-size: 30px;
        font-weight: 800;
    }

    .average {
        color: #e67e22;
        font-size: 30px;
        font-weight: 800;
    }

    .poor {
        color: #e74c3c;
        font-size: 30px;
        font-weight: 800;
    }


    /* ---------------- RECOMMENDATIONS ---------------- */

    .recommendation {
        background: #fbfcff;

        border: 1px solid #e3e8f5;

        border-left: 4px solid #5b6ff5;

        border-radius: 12px;

        padding: 15px 18px;

        margin-bottom: 12px;

        color: #35405d;

        font-size: 15px;
    }


    /* ---------------- SECTION TITLES ---------------- */

    .section-title {
        font-size: 26px;
        font-weight: 800;
        color: #17213b;

        margin-top: 10px;
        margin-bottom: 18px;
    }


    /* ---------------- BUTTON ---------------- */

    .stButton > button {

        background: linear-gradient(
            90deg,
            #5b45e8,
            #e02b83
        );

        color: white;

        border: none;

        border-radius: 12px;

        height: 52px;

        font-size: 17px;

        font-weight: 700;

        width: 100%;

        transition: 0.2s;
    }

    .stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0 8px 20px rgba(91, 69, 232, 0.25);
    }


    /* ---------------- INPUTS ---------------- */

    div[data-baseweb="input"] {

        border-radius: 10px;
    }


    /* ---------------- FOOTER ---------------- */

    .footer {

        text-align: center;

        color: #788198;

        padding: 25px;

        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


 

# ============================================================
# HERO
# ============================================================

st.markdown("""<div class="hero">
<div class="hero-badge">🤖 AI POWERED EDUCATION</div>
<h1 class="hero-title">🎓 Student Performance AI</h1>
<div class="hero-subtitle">Intelligent machine learning system for predicting student academic performance</div>
</div>""", unsafe_allow_html=True)


# ============================================================
# STUDENT INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">📋 Student Information</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">

<div class="card-title">
Enter Student Details
</div>

<div class="card-subtitle">
Provide the student's academic and lifestyle information.
Our machine learning model will estimate the final score.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INPUTS
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:

    study_hours = st.number_input(
        "📚 Study Hours per Day",
        min_value=0.0,
        max_value=24.0,
        value=6.0,
        step=0.5
    )

    previous_score = st.number_input(
        "📝 Previous Exam Score",
        min_value=0,
        max_value=100,
        value=70
    )


with col2:

    attendance = st.number_input(
        "📅 Attendance (%)",
        min_value=0,
        max_value=100,
        value=80
    )

    sleep_hours = st.number_input(
        "😴 Sleep Hours per Day",
        min_value=0.0,
        max_value=24.0,
        value=7.0,
        step=0.5
    )


with col3:

    assignments_completed = st.number_input(
        "📖 Assignments Completed",
        min_value=0,
        max_value=10,
        value=7
    )

    participation = st.number_input(
        "🙋 Class Participation",
        min_value=0,
        max_value=10,
        value=7
    )


st.write("")


# ============================================================
# PREDICT BUTTON
# ============================================================

predict = st.button(
    "🚀 Predict Student Performance"
)


# ============================================================
# MACHINE LEARNING PREDICTION
# ============================================================
if predict:

    input_data = pd.DataFrame({
        "study_hours": [study_hours],
        "previous_score": [previous_score],
        "attendance": [attendance],
        "sleep_hours": [sleep_hours],
        "assignments_completed": [assignments_completed],
        "participation": [participation]
    })
    prediction = model.predict(input_data)[0]

    prediction = max(0, min(100, prediction))

    # ========================================================
    # PERFORMANCE LEVEL
    # ========================================================

    if prediction >= 90:
        performance_level = "Excellent"
        performance_message = "Outstanding performance! Keep it up! 🚀"

    elif prediction >= 75:
        performance_level = "Good"
        performance_message = "You're on a strong academic path! 🌟"

    elif prediction >= 60:
        performance_level = "Average"
        performance_message = "You're doing okay. A little more effort can help! 💪"

    else:
        performance_level = "Needs Improvement"
        performance_message = "Focus on your study habits and keep improving! 📚"


    # ========================================================
    # SCORE + PERFORMANCE
    # ========================================================

    score_col, performance_col = st.columns(2)

    with score_col:

        st.markdown(
            f"""<div class="score-card">
<div class="score-label">Predicted Final Score</div>
<div class="score-number">{prediction:.1f}%</div>
<div class="score-description">🤖 AI-generated prediction</div>
</div>""",
            unsafe_allow_html=True
        )

    with performance_col:

        st.markdown(
            f"""<div class="card">
<div class="card-title">Performance Level</div>
<div class="good">{performance_level} 🌟</div>
<p>{performance_message}</p>
</div>""",
            unsafe_allow_html=True
        )
  
    # ========================================================
    # SCORE PROGRESS
    # ========================================================

    st.write("")

    st.markdown("### 📊 Overall Performance")

    st.progress(int(prediction))


    # ========================================================
    # TWO COLUMN DASHBOARD
    # ========================================================

    chart_col, recommendation_col = st.columns(2)


    # ========================================================
    # PERFORMANCE FACTORS
    # ========================================================

    with chart_col:

        st.markdown("""
        <div class="card">

        <div class="card-title">
        📈 Performance Factors
        </div>

        <div class="card-subtitle">
        Visualization of the student's key academic factors
        </div>

        </div>
        """, unsafe_allow_html=True)


        factors = pd.DataFrame({

            "Factor": [

                "Previous Score",
                "Attendance",
                "Study Hours",
                "Sleep Hours",
                "Assignments",
                "Participation"

            ],

            "Value": [

                previous_score,

                attendance,

                min(study_hours / 8 * 100, 100),

                min(sleep_hours / 8 * 100, 100),

                assignments_completed / 10 * 100,

                participation / 10 * 100

            ]

        })


        factors = factors.set_index("Factor")


        st.bar_chart(
            factors,
            y="Value",
            height=350
        )


        st.caption(
            "ℹ️ Study, sleep, assignments and participation "
            "are normalized to a 0–100 scale for visualization."
        )


    # ========================================================
    # RECOMMENDATIONS
    # ========================================================

    with recommendation_col:

        st.markdown("""
        <div class="card">

        <div class="card-title">
        💡 Personalized Recommendations
        </div>

        <div class="card-subtitle">
        Suggestions based on the student's current inputs
        </div>

        </div>
        """, unsafe_allow_html=True)


        recommendations = []


        if study_hours < 6:

            recommendations.append(
                "📚 Increase your study time to at least 6 hours per day."
            )


        if previous_score < 70:

            recommendations.append(
                "📝 Review previous exam mistakes and strengthen weak topics."
            )


        if attendance < 85:

            recommendations.append(
                "📅 Try to maintain attendance above 85%."
            )


        if sleep_hours < 7:

            recommendations.append(
                "😴 Aim for at least 7 hours of sleep each night."
            )


        if assignments_completed < 8:

            recommendations.append(
                "📖 Try to complete more assignments consistently."
            )


        if participation < 7:

            recommendations.append(
                "🙋 Participate more actively during classes."
            )


        if not recommendations:

            recommendations.append(
                "🌟 Great habits! Keep maintaining your current routine."
            )


        for recommendation in recommendations:

            st.markdown(
                f"""
                <div class="recommendation">
                    {recommendation}
                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""<div class="footer">🎓 <b>Student Performance AI</b><br><br>Built with ❤️ using Python • Pandas • Scikit-learn • Streamlit<br><br>Keep Learning • Keep Growing 🚀</div>""", unsafe_allow_html=True)