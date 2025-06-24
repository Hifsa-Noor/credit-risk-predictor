# 💼 Credit Risk Predictor

This is a machine learning web app built with **Gradio** that predicts whether a loan applicant is at **high risk** or **low risk** of credit default. It uses financial features like income, debt ratio, and credit history to make predictions.

---

## 🚀 Demo

[![Gradio App](https://img.shields.io/badge/Gradio-Live_App-blue?logo=gradio)](https://huggingface.co/spaces/hifsa-noor/Credit_Risk_Predictor)

---

## 📊 Features Used

- **Age**
- **Income**
- **Employment Length**
- **Loan Amount**
- **Interest Rate**
- **Loan Percent Income**
- **Credit History Length**

---

## 🧠 Model Details

- Model: `RandomForestClassifier` or `XGBoost`
- Data balanced using **SMOTE** to avoid bias
- Inputs scaled using **StandardScaler**
- Metrics on test set:
  - Accuracy: ~91%
  - Precision: 92%
  - Recall: 88%
  - F1 Score: 90%

---

## 🛠️ How to Run Locally

### 1. Clone the repo:
```bash
git clone https://github.com/your-username/credit-risk-predictor.git
cd credit-risk-predictor

