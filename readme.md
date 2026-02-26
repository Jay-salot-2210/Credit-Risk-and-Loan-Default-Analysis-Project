# 📊 Credit Risk & Loan Default Analysis

## 🔍 Project Overview

This project analyzes loan portfolio data to identify key drivers of loan default risk and evaluate the effectiveness of credit grading and risk segmentation models.

The objective is to:

- Assess overall portfolio risk  
- Identify factors contributing to loan defaults  
- Validate credit grade performance  
- Provide business insights for risk mitigation  

---

## 🚀 Live Interactive Dashboard

👉 **View the Tableau Dashboard Here:**  
🔗 https://public.tableau.com/app/profile/jay.salot/viz/CreditRiskandLoanDefaultAnalysis/Dashboard1

---

## 📈 Key Business Metrics

- **Total Loans:** 38,577  
- **Default Rate:** 14.59%  
- **Average Interest Rate:** 11.93%  
- **Total Defaults:** 5,627  

---

## 📊 Key Insights

### 1️⃣ Credit Grade Performance
- Default rate increases significantly from Grade A (~6%) to Grade G (~34%).
- Credit grading system effectively reflects risk levels.

### 2️⃣ Loan Term Risk
- 60-month loans show ~25% default rate.
- 36-month loans show ~11% default rate.
- Longer loan terms significantly increase portfolio risk exposure.

### 3️⃣ Risk Segmentation
- High-risk category default rate: ~26.6%
- Medium-risk: ~16.1%
- Low-risk: ~8.1%
- Risk categorization aligns with observed borrower behavior.

### 4️⃣ Key Default Drivers (Correlation Analysis)

Strongest positive predictors:
- Interest Rate  
- Loan Term (Months)  
- Revolving Utilization  
- Lower Credit Grades (E, F)

Strongest negative indicators:
- Grade A & B  
- Higher Annual Income  
- Credit Card Purpose Loans  

---

## 🛠 Tools & Technologies

- Python (EDA & Feature Engineering)
- Pandas & NumPy
- Tableau Public (Dashboard & Storytelling)
- Correlation & Risk Scoring Techniques

---

## 📂 Project Structure
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── data_exploration.ipynb
│
├── src/
│   ├── data_utils.py
│   └── features.py
│
└── dashboard/
    └── Tableau Dashboard (Published)

---

## 🎯 Business Recommendations

- Reduce exposure to long-term (60-month) high-risk loans.
- Apply stricter underwriting criteria for Grade E–G segments.
- Use interest rate and revolving utilization as early warning risk indicators.
- Strengthen monitoring of high-risk borrower segments.

---

## 👤 Author

**Jay Salot**  
Finance & Risk Analytics Enthusiast  

Tableau Public Profile:  
https://public.tableau.com/app/profile/jay.salot

---

## 📂 Project Structure
