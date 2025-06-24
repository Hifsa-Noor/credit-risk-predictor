import gradio as gr
import joblib
import numpy as np

# Load the saved model and scaler
model = joblib.load("credit_risk_model.pkl")
scaler = joblib.load("scaler.pkl")

# Prediction function
def predict_credit_risk(age, income, emp_length, loan_amount, interest_rate, percent_income, credit_hist_length):
    try:
        input_data = np.array([[float(age), float(income), float(emp_length), float(loan_amount),
                                float(interest_rate), float(percent_income), float(credit_hist_length)]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]
        return "High Risk" if prediction == 1 else "Low Risk"
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Interface
interface = gr.Interface(
    fn=predict_credit_risk,
    inputs=[
        gr.Number(label="Person Age"),
        gr.Number(label="Person Income"),
        gr.Number(label="Employment Length (years)"),
        gr.Number(label="Loan Amount"),
        gr.Number(label="Interest Rate"),
        gr.Number(label="Loan Percent Income"),
        gr.Number(label="Credit History Length")
    ],
    outputs=gr.Text(label="Prediction"),
    title="Credit Risk Predictor",
    description="Enter the applicant's information to predict if they are high or low credit risk."
)

interface.launch()
