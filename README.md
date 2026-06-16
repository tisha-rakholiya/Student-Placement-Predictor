# 🎓 Student Placement Predictor

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)

**Predict your campus placement chances using ML — and get personalized tips to improve them!**

### 🌐 [Try the Live App →](https://student-placement-predictor-kl6au4vx7drdpsjowappue3.streamlit.app/)

</div>

---

## 📌 About the Project

Getting placed is every student's goal — but how do you know if you're on the right track? This project uses a **Random Forest Classifier** trained on real placement data to predict whether a student will get placed, along with **personalized improvement tips** based on their profile.

> 💡 Built for students who want data-driven insights on their placement readiness.

---

## ✨ Features

- 🎯 **Placement Prediction** — placed or not placed, with probability score
- 📊 **Feature Importance Chart** — see which factors matter most
- 💡 **Personalized Tips** — actionable suggestions to improve your chances
- 📈 **Score Comparison** — compare your profile against placed students
- 🖥️ **Interactive Web App** — clean Streamlit UI, no coding needed

---

## 🎯 Model Performance

| Metric | Score |
|--------|-------|
| 🤖 Algorithm | Random Forest Classifier |
| ✅ Accuracy | **79.07%** |
| 📦 Dataset | 215 students, 12 features |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Core language |
| 🤖 Scikit-learn | ML model (Random Forest) |
| 🎈 Streamlit | Web app interface |
| 🐼 Pandas | Data processing |
| 📊 Matplotlib | Charts & visualizations |

---

## 📁 Project Structure

```
Student-Placement-Predictor/
├── spp.py                          # Main Streamlit app
├── placement_model.ipynb           # Model training notebook
├── placement_model.pkl             # Saved ML model
├── features.pkl                    # Feature names
├── Placement_Data_Full_Class.csv   # Dataset
├── requirements.txt                # Dependencies
└── README.md
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/tisha-rakholiya/Student-Placement-Predictor
cd Student-Placement-Predictor
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app
```bash
streamlit run spp.py
```

### 4️⃣ Open in browser
```
http://localhost:8501
```

---

## 🔍 How It Works

```
📝 Student fills their academic profile
        ↓
🤖 Random Forest Model analyzes 12 features
        ↓
🎯 Placement prediction + probability score
        ↓
📊 Feature importance + score comparison chart
        ↓
💡 Personalized improvement tips
```

---

## 👩‍💻 Author

**Tisha Rakholiya**
BTech CSE (AI & Data Science) | ITM SLS Baroda University | Surat, Gujarat

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/tisha-rakholiya)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github)](https://github.com/tisha-rakholiya)

---

<div align="center">
⭐ If this helped you, please give it a star!
</div>
