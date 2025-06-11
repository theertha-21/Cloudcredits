# 🏦 Loan Approval Prediction Using Machine Learning

This project aims to build a machine learning model to predict whether a loan application will be approved, based on various applicant details. It also includes a user-friendly web interface using Streamlit for live predictions.

---

## 🎯 Objective

To:
- Analyze loan applicant data
- Build a prediction model using machine learning
- Visualize key trends and insights
- Create an interactive **Streamlit web app** for real-time prediction

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `LoanApprovalPrediction.csv` | Dataset used for training and analysis |
| `LoanApproval.ipynb` | Main notebook with EDA, model building, and evaluation |
| `loan.py` | Streamlit code for the interactive loan prediction app |
| `rfcmodel.sav` | Trained Random Forest model |
| `scaler_loan.sav` | Standard scaler used for input transformation |
| `loan.jpeg` | Optional image banner for the app |
| `README.md` | Project documentation (this file) |

---

## 📊 Dataset Description

- Features include:
  - Gender, Married, Dependents
  - Education, Self_Employed
  - ApplicantIncome, CoapplicantIncome
  - LoanAmount, Loan_Amount_Term
  - Credit_History, Property_Area
  - Loan_Status (Target: Y/N)

---

## 🔎 Data Analysis Summary

- **Exploratory Data Analysis (EDA)** included:
  - Loan approval distribution
  - Approval breakdown by gender, education, credit history
  - Correlation heatmap
- **Insights:**
  - Credit History has the strongest impact on loan approval.
  - Gender and education have weaker correlations.

---

## 🤖 Machine Learning Models Used

| Model                    | Description                               |
|--------------------------|-------------------------------------------|
| K-Nearest Neighbors (KNN)| Distance-based model with k=3             |
| Support Vector Classifier (SVC) | Margin-based classifier              |
| Random Forest Classifier | Ensemble model with 7 trees (entropy-based) |
| Gaussian Naive Bayes     | Probabilistic classifier assuming feature independence |
| Decision Tree Classifier | Tree-based model using entropy criterion  |

📌 **Random Forest performed the best** and was used in the final deployment.

---

## 🌐 Streamlit Web App: Loan Prediction

A user-friendly Streamlit app allows users to enter loan details and get instant predictions.

### 🔧 Features
- Input form with dropdowns/textboxes
- Image banner
- Uses `.sav` files to load pre-trained model and scaler
- Predicts and displays result: ✅ Approved or ❌ Not Approved

