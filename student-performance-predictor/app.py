import streamlit as st
import os
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load(os.path.join(os.path.dirname(__file__), "model", "student_performance_model.pkl"))


model = load_model()


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* ============================================================
   GLOBAL DESIGN
============================================================ */

.stApp {
    background: #f7f8fc;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ============================================================
   DECORATIVE GRAPHICS
============================================================ */

.decor-circle {
    position: fixed;
    width: 180px;
    height: 180px;
    border-radius: 50%;
    background: linear-gradient(135deg, #7c5cff33, #00c9a733);
    top: 100px;
    right: -60px;
    z-index: 0;
    pointer-events: none;
}

.decor-circle-2 {
    position: fixed;
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background: linear-gradient(135deg, #ff4ecd33, #5b45e833);
    bottom: 100px;
    left: -40px;
    z-index: 0;
    pointer-events: none;
}

.graphic-line {
    height: 5px;
    width: 100%;
    border-radius: 20px;
    background: linear-gradient(
        90deg,
        #5b45e8,
        #8b5cf6,
        #e02b83,
        #12b981
    );
    margin: 20px 0 30px 0;
}


/* ============================================================
   HERO SECTION
============================================================ */

.hero {
    background: linear-gradient(
        135deg,
        #5b45e8,
        #7c5cff,
        #a855f7
    );
    padding: 42px 35px;
    border-radius: 28px;
    color: white;
    text-align: center;
    box-shadow: 0 18px 45px rgba(91, 69, 232, 0.22);
    margin-bottom: 25px;
}

.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    padding: 8px 16px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 15px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    margin: 5px 0 10px 0;
}

.hero-subtitle {
    font-size: 17px;
    opacity: 0.92;
    max-width: 720px;
    margin: auto;
}


/* ============================================================
   SECTION HEADINGS
============================================================ */

.section-title {
    font-size: 27px;
    font-weight: 800;
    color: #20203a;
    margin-top: 25px;
    margin-bottom: 6px;
}

.section-subtitle {
    color: #77778a;
    font-size: 15px;
    margin-bottom: 20px;
}


/* ============================================================
   INPUT CARD
============================================================ */

.input-card {
    background: white;
    padding: 28px;
    border-radius: 22px;
    border: 1px solid #e9eaf2;
    box-shadow: 0 10px 30px rgba(30, 30, 60, 0.06);
    margin-bottom: 25px;
}


/* ============================================================
   STREAMLIT INPUTS
============================================================ */

label {
    font-weight: 600 !important;
    color: #303044 !important;
}

div[data-baseweb="input"] {
    border-radius: 12px;
    border: 1px solid #e1e3ed;
    background: white;
}

div[data-baseweb="input"]:focus-within {
    border-color: #6c5ce7;
    box-shadow: 0 0 0 2px #6c5ce722;
}


/* ============================================================
   SLIDERS
============================================================ */

div[data-baseweb="slider"] {
    padding-top: 5px;
}


/* ============================================================
   PREDICT BUTTON
============================================================ */

.stButton > button {
    width: 100%;
    min-height: 52px;
    border-radius: 15px;
    border: none;
    font-size: 17px;
    font-weight: 750;
    background: linear-gradient(
        90deg,
        #5b45e8,
        #8b5cf6
    );
    color: white;
    box-shadow: 0 8px 20px rgba(91, 69, 232, 0.22);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 25px rgba(91, 69, 232, 0.30);
}


/* ============================================================
   RESULT CARDS
============================================================ */

.score-card {
    background: linear-gradient(
        135deg,
        #5b45e8,
        #8b5cf6
    );
    color: white;
    padding: 30px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0 12px 30px rgba(91, 69, 232, 0.22);
}

.score-label {
    font-size: 15px;
    opacity: 0.9;
}

.score-number {
    font-size: 54px;
    font-weight: 850;
    margin: 8px 0;
}

.score-description {
    font-size: 14px;
    opacity: 0.85;
}


.performance-card {
    background: white;
    padding: 30px;
    border-radius: 22px;
    border: 1px solid #e9eaf2;
    box-shadow: 0 10px 30px rgba(30, 30, 60, 0.06);
}

.card-title {
    font-size: 19px;
    font-weight: 750;
    color: #25253b;
    margin-bottom: 10px;
}

.performance-level {
    font-size: 31px;
    font-weight: 850;
    color: #5b45e8;
    margin: 10px 0;
}

.performance-message {
    color: #707084;
    font-size: 15px;
}


/* ============================================================
   PROGRESS CARD
============================================================ */

.progress-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #e9eaf2;
    box-shadow: 0 8px 25px rgba(30, 30, 60, 0.05);
    margin-top: 20px;
}

.progress-background {
    width: 100%;
    height: 14px;
    background: #ececf5;
    border-radius: 20px;
    overflow: hidden;
    margin-top: 12px;
}

.progress-fill {
    height: 100%;
    border-radius: 20px;
    background: linear-gradient(
        90deg,
        #5b45e8,
        #a855f7,
        #12b981
    );
}


/* ============================================================
   RECOMMENDATION CARDS
============================================================ */

.recommendation {
    background: white;
    padding: 20px;
    border-radius: 18px;
    border-left: 5px solid #6c5ce7;
    border-top: 1px solid #eeeeF5;
    border-right: 1px solid #eeeeF5;
    border-bottom: 1px solid #eeeeF5;
    margin-bottom: 12px;
    box-shadow: 0 6px 18px rgba(30,30,60,0.04);
}

.recommendation-title {
    font-weight: 750;
    color: #292941;
    margin-bottom: 5px;
}

.recommendation-text {
    color: #707084;
    font-size: 14px;
}


/* ============================================================
   INFO CARD
============================================================ */

.info-card {
    background: linear-gradient(
        135deg,
        #ffffff,
        #f6f3ff
    );
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #e8e2ff;
    margin-top: 20px;
}


/* ============================================================
   FOOTER
============================================================ */

.footer {
    text-align: center;
    padding: 35px 20px;
    margin-top: 50px;
    color: #77778a;
    font-size: 14px;
}

.footer-title {
    font-size: 17px;
    font-weight: 750;
    color: #4c4c60;
}


/* ============================================================
   MOBILE RESPONSIVE
============================================================ */

@media (max-width: 768px) {

    .hero {
        padding: 30px 20px;
    }

    .hero-title {
        font-size: 31px;
    }

    .hero-subtitle {
        font-size: 14px;
    }

    .score-number {
        font-size: 44px;
    }

    .section-title {
        font-size: 23px;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# DECORATIVE GRAPHICS
# ============================================================

st.markdown("""<div class="decor-circle"></div>
<div class="decor-circle-2"></div>
<div class="graphic-line"></div>""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""<div class="hero">
<div class="hero-badge">🤖 AI POWERED EDUCATION</div>
<div class="hero-title">🎓 Student Performance AI</div>
<div class="hero-subtitle">Intelligent machine learning system for predicting student academic performance</div>
</div>""", unsafe_allow_html=True)


# ============================================================
# INTRODUCTION
# ============================================================

st.markdown("""
<div class="section-title">📊 Student Information</div>
<div class="section-subtitle">
Enter your academic and lifestyle information to generate an AI-powered performance prediction.
</div>
""", unsafe_allow_html=True)


# ============================================================
# INPUT CARD
# ============================================================

st.markdown("""<div class="input-card">""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:

    study_hours = st.number_input(
        "📚 Study Hours",
        min_value=0.0,
        max_value=24.0,
        value=4.0,
        step=0.5
    )

    previous_score = st.number_input(
        "📝 Previous Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=1.0
    )


with col2:

    attendance = st.number_input(
        "📅 Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0,
        step=1.0
    )

    sleep_hours = st.number_input(
        "😴 Sleep Hours",
        min_value=0.0,
        max_value=24.0,
        value=7.0,
        step=0.5
    )


with col3:

    assignments_completed = st.number_input(
        "📖 Assignments Completed",
        min_value=0,
        max_value=100,
        value=15,
        step=1
    )

    participation = st.number_input(
        "🙋 Participation",
        min_value=0,
        max_value=10,
        value=6,
        step=1
    )

st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# PREDICT BUTTON
# ============================================================

predict = st.button(
    "🔮 Predict My Performance"
)


# ============================================================
# PREDICTION
# ============================================================

if predict:

    # --------------------------------------------------------
    # PREPARE INPUT DATA
    # --------------------------------------------------------

    input_data = pd.DataFrame({
        "study_hours": [study_hours],
        "previous_score": [previous_score],
        "attendance": [attendance],
        "sleep_hours": [sleep_hours],
        "assignments_completed": [assignments_completed],
        "participation": [participation]
    })


    # --------------------------------------------------------
    # MODEL PREDICTION
    # --------------------------------------------------------

    prediction = model.predict(input_data)[0]

    prediction = max(0, min(100, prediction))


    # --------------------------------------------------------
    # PERFORMANCE LEVEL
    # --------------------------------------------------------

    if prediction >= 90:

        performance_level = "Excellent"
        performance_message = "Outstanding performance! Keep up the excellent work! 🚀"

    elif prediction >= 75:

        performance_level = "Good"
        performance_message = "You're on a strong academic path! Keep improving! 🌟"

    elif prediction >= 60:

        performance_level = "Average"
        performance_message = "You're doing well, but a little more effort can take you higher! 💪"

    else:

        performance_level = "Needs Improvement"
        performance_message = "Focus on your study habits and build consistent learning routines! 📚"


    # ========================================================
    # RESULT HEADING
    # ========================================================

    st.markdown("""
    <div class="section-title">🎯 Your Prediction</div>
    <div class="section-subtitle">
    Here is the performance prediction generated by the machine learning model.
    </div>
    """, unsafe_allow_html=True)


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
            f"""<div class="performance-card">
<div class="card-title">⭐ Performance Level</div>
<div class="performance-level">{performance_level}</div>
<div class="performance-message">{performance_message}</div>
</div>""",
            unsafe_allow_html=True
        )


    # ========================================================
    # PROGRESS VISUALIZATION
    # ========================================================

    st.markdown(
        f"""<div class="progress-card">
<div class="card-title">📈 Performance Progress</div>
<div style="display:flex;justify-content:space-between;">
<span>Current prediction</span>
<span><b>{prediction:.1f}%</b></span>
</div>
<div class="progress-background">
<div class="progress-fill" style="width:{prediction}%"></div>
</div>
</div>""",
        unsafe_allow_html=True
    )


    # ========================================================
    # FACTOR ANALYSIS
    # ========================================================

    st.markdown("""
    <div class="section-title">📊 Your Learning Factors</div>
    <div class="section-subtitle">
    A quick visual overview of the information used by the AI model.
    </div>
    """, unsafe_allow_html=True)


    factor_data = pd.DataFrame({
        "Factor": [
            "Study Hours",
            "Previous Score",
            "Attendance",
            "Sleep Hours",
            "Assignments",
            "Participation"
        ],
        "Value": [
            study_hours,
            previous_score,
            attendance,
            sleep_hours,
            assignments_completed,
            participation
        ]
    })

    factor_data = factor_data.set_index("Factor")

    st.bar_chart(
        factor_data,
        height=350
    )


    # ========================================================
    # PERSONALIZED RECOMMENDATIONS
    # ========================================================

    st.markdown("""
    <div class="section-title">💡 Personalized Recommendations</div>
    <div class="section-subtitle">
    Small improvements in your daily habits can help improve your academic performance.
    </div>
    """, unsafe_allow_html=True)


    recommendations = []


    if study_hours < 3:

        recommendations.append(
            (
                "📚 Increase Study Time",
                "Try adding 1–2 focused study hours to your daily routine."
            )
        )

    elif study_hours < 6:

        recommendations.append(
            (
                "📚 Maintain Consistency",
                "Your study time is reasonable. Focus on consistency and quality."
            )
        )

    else:

        recommendations.append(
            (
                "📚 Strong Study Routine",
                "Great study commitment! Make sure you also include breaks."
            )
        )


    if attendance < 75:

        recommendations.append(
            (
                "📅 Improve Attendance",
                "Try to attend more classes. Regular attendance can strengthen your understanding."
            )
        )

    else:

        recommendations.append(
            (
                "📅 Good Attendance",
                "Your attendance is strong. Continue maintaining this consistency."
            )
        )


    if sleep_hours < 6:

        recommendations.append(
            (
                "😴 Improve Sleep",
                "Aim for a consistent sleep schedule and enough rest for better concentration."
            )
        )

    elif sleep_hours > 9:

        recommendations.append(
            (
                "😴 Balance Sleep",
                "Make sure your sleep schedule is consistent and balanced with your study routine."
            )
        )

    else:

        recommendations.append(
            (
                "😴 Healthy Sleep Range",
                "Your sleep duration looks reasonable. Keep a consistent sleep schedule."
            )
        )


    if assignments_completed < 10:

        recommendations.append(
            (
                "📖 Complete More Assignments",
                "Try finishing assignments regularly instead of waiting until the deadline."
            )
        )

    else:

        recommendations.append(
            (
                "📖 Assignment Progress",
                "Good assignment completion. Keep submitting your work consistently."
            )
        )


    if participation < 5:

        recommendations.append(
            (
                "🙋 Participate More",
                "Ask questions and participate in discussions to strengthen your learning."
            )
        )

    else:

        recommendations.append(
            (
                "🙋 Active Participation",
                "Good participation! Continue engaging with your classes."
            )
        )


    for title, text in recommendations:

        st.markdown(
            f"""<div class="recommendation">
<div class="recommendation-title">{title}</div>
<div class="recommendation-text">{text}</div>
</div>""",
            unsafe_allow_html=True
        )


    # ========================================================
    # AI INSIGHT
    # ========================================================

    st.markdown(
        f"""<div class="info-card">
<div class="card-title">🤖 AI Insight</div>
<p>
Based on the information provided, the machine learning model predicts
a final academic score of <b>{prediction:.1f}%</b>.
Your current performance level is classified as
<b>{performance_level}</b>.
</p>
<p>
Use this prediction as a learning guide rather than a guaranteed final result.
</p>
</div>""",
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""<div class="footer">
<div class="footer-title">🎓 Student Performance AI</div>
<br>
Built with ❤️ using Python • Pandas • Scikit-learn • Streamlit
<br><br>
Keep Learning • Keep Growing 🚀
</div>""", unsafe_allow_html=True)
