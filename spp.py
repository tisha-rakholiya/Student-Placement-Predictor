import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load model
with open('placement_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Placement Predictor", page_icon="🎓", layout="wide")

st.markdown("""
<style>
    .stButton>button {
        background-color: #2ecc71;
        color: white;
        font-size: 18px;
        padding: 10px 30px;
        border-radius: 10px;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#2ecc71;'>🎓 Student Placement Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Built with Machine Learning | Random Forest | By Tisha Rakholiya</p>", unsafe_allow_html=True)
st.markdown("---")

st.sidebar.title("📋 About")
st.sidebar.info("""
**Student Placement Predictor**
- Dataset: 215 students
- Model: Random Forest
- Accuracy: 79.07%
- Features: 12 academic factors
""")
st.sidebar.markdown("**👩‍💻 Developer:** Tisha Rakholiya")
st.sidebar.markdown("**🎓 BTech CSE (AI & DS)**")

st.markdown("### 📝 Enter Your Details")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**🏫 Academic**")
    ssc_p = st.slider("10th Percentage", 40.0, 100.0, 70.0)
    hsc_p = st.slider("12th Percentage", 40.0, 100.0, 70.0)
    degree_p = st.slider("Degree Percentage", 40.0, 100.0, 70.0)
    mba_p = st.slider("MBA Percentage", 40.0, 100.0, 60.0)

with col2:
    st.markdown("**📋 Personal**")
    gender = st.selectbox("Gender", ["Male", "Female"])
    workex = st.selectbox("Work Experience", ["No", "Yes"])
    ssc_b = st.selectbox("10th Board", ["Central", "Others"])
    hsc_b = st.selectbox("12th Board", ["Central", "Others"])

with col3:
    st.markdown("**🎯 Specialisation**")
    hsc_s = st.selectbox("12th Stream", ["Commerce", "Science", "Arts"])
    degree_t = st.selectbox("Degree Type", ["Sci&Tech", "Comm&Mgmt", "Others"])
    specialisation = st.selectbox("MBA Specialisation", ["Mkt&HR", "Mkt&Fin"])
    etest_p = st.slider("Employability Test %", 40.0, 100.0, 70.0)

st.markdown("---")

if st.button("🔮 Predict My Placement"):
    gender_e = 1 if gender == "Male" else 0
    workex_e = 1 if workex == "Yes" else 0
    ssc_b_e = 0 if ssc_b == "Central" else 1
    hsc_b_e = 0 if hsc_b == "Central" else 1
    hsc_s_e = {"Commerce": 1, "Science": 2, "Arts": 0}[hsc_s]
    degree_t_e = {"Comm&Mgmt": 0, "Others": 1, "Sci&Tech": 2}[degree_t]
    specialisation_e = 0 if specialisation == "Mkt&Fin" else 1

    features = np.array([[gender_e, ssc_p, ssc_b_e, hsc_p, hsc_b_e,
                          hsc_s_e, degree_p, degree_t_e, workex_e,
                          etest_p, specialisation_e, mba_p]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0]
    placed_prob = probability[1] * 100

    col_r1, col_r2 = st.columns(2)

    with col_r1:
        if prediction == 1:
            st.success(f"✅ PLACED! Probability: {placed_prob:.1f}%")
            st.balloons()
        else:
            st.error(f"❌ NOT PLACED. Probability: {placed_prob:.1f}%")

        # Progress bar
        st.markdown("### 📊 Placement Probability")
        st.progress(int(placed_prob))
        st.markdown(f"**{placed_prob:.1f}%** chance of placement")

        # Improvement Tips
        st.markdown("### 💡 Tips")
        if etest_p < 70:
            st.warning("📈 Employability Test 70%+ lao!")
        else:
            st.success("✅ E-Test — Good!")
        if degree_p < 65:
            st.warning("🎯 Degree % 65+ karo!")
        else:
            st.success("✅ Degree % — Good!")
        if workex == "No":
            st.warning("💼 Internship lo!")
        else:
            st.success("✅ Work Experience — Good!")
        if mba_p < 60:
            st.warning("📚 MBA % improve karo!")
        else:
            st.success("✅ MBA % — Good!")

    with col_r2:
        # Feature Importance
        st.markdown("### 🔍 Key Factors")
        feature_names = ['Gender', 'SSC%', 'SSC Board', 'HSC%', 'HSC Board',
                         'HSC Stream', 'Degree%', 'Degree Type', 'Work Ex',
                         'E-Test%', 'Specialisation', 'MBA%']
        importance = model.feature_importances_
        sorted_idx = np.argsort(importance)
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.barh([feature_names[i] for i in sorted_idx],
                importance[sorted_idx], color='#2ecc71')
        ax.set_title('Feature Importance', color='white')
        ax.set_facecolor('#0e1117')
        fig.patch.set_facecolor('#0e1117')
        ax.tick_params(colors='white')
        st.pyplot(fig)

        # Comparison Chart
        st.markdown("### 📈 Your Score vs Good Score")
        categories = ['10th%', '12th%', 'Degree%', 'E-Test%', 'MBA%']
        your_scores = [ssc_p, hsc_p, degree_p, etest_p, mba_p]
        good_scores = [70, 70, 65, 70, 60]
        x = np.arange(len(categories))
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        ax2.bar(x - 0.2, your_scores, 0.4, label='Your Score', color='#3498db')
        ax2.bar(x + 0.2, good_scores, 0.4, label='Good Score', color='#2ecc71')
        ax2.set_xticks(x)
        ax2.set_xticklabels(categories)
        ax2.legend(facecolor='#0e1117', labelcolor='white')
        ax2.set_facecolor('#0e1117')
        fig2.patch.set_facecolor('#0e1117')
        ax2.tick_params(colors='white')
        st.pyplot(fig2)