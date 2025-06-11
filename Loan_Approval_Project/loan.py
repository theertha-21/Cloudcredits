import streamlit as st
import pickle
from PIL import Image

def main():
    st.title(":blue[LOAN PREDICTION]")
    img = Image.open('loan.jpeg')
    st.image(img, width=500)

    gender = st.selectbox("Gender", ["Select","Male", "Female"])
    married = st.selectbox("Married", ["Select","Yes", "No"])
    dependents = st.selectbox("Dependents", ["Select","0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Select","Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Select","Yes", "No"])
    applicant_income = st.text_input("Applicant Income", placeholder="e.g. 5000")
    co_applicant_income = st.text_input("Coapplicant Income", placeholder="e.g. 2000")
    loan_amount = st.text_input("Loan Amount", placeholder="e.g. 150")
    loan_amount_term = st.text_input("Loan Amount Term (in days)", placeholder="e.g. 360")
    credit_history = st.selectbox("Credit History", ["Select", "1", "0"])
    property_area = st.selectbox("Property Area", ["Select", "Urban", "Semiurban", "Rural"])

    pred = st.button('PREDICT')

    if pred:
        try:
            # Encode categorical values
            gender = 1 if gender == 'Male' else 0
            married = 1 if married == 'Yes' else 0
            education = 1 if education == 'Graduate' else 0
            self_employed = 1 if self_employed == 'Yes' else 0
            dependents = 3 if dependents == '3+' else int(dependents)
            credit_history = float(credit_history)
            property_area_map = {"Urban": 2, "Semiurban": 1, "Rural": 0}
            property_area = property_area_map[property_area]

            # Convert numeric inputs
            applicant_income = float(applicant_income)
            co_applicant_income = float(co_applicant_income)
            loan_amount = float(loan_amount)
            loan_amount_term = float(loan_amount_term)

            features = [gender, married, dependents, education, self_employed,
                        applicant_income, co_applicant_income, loan_amount,
                        loan_amount_term, credit_history, property_area]

            # Load model and scaler
            scaler = pickle.load(open("scaler_loan.sav", 'rb'))
            model = pickle.load(open("rfcmodel.sav", 'rb'))

            scaled_input = scaler.transform([features])
            result = model.predict(scaled_input)

            if result[0] == 1:
                st.success("✅ Loan Approved")
            else:
                st.error("❌ Loan Not Approved")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")

# Run the app
main()
