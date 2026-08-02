# 🛍️ Customer Lifetime Value Prediction & Customer Segmentation

## 📌 Overview

Customer Lifetime Value (CLV) is a key business metric that estimates the total revenue a customer is expected to generate throughout their relationship with a business. Predicting CLV helps organizations identify valuable customers, improve customer retention, and optimize marketing strategies.

This project combines **Machine Learning** and **Customer Segmentation** to predict a customer's lifetime value and classify them into meaningful customer segments. An interactive **Streamlit** application has also been developed to make predictions in real time.

This project was developed as part of the **IIT Jammu Data Science Internship Capstone Project**.

---

## 🚀 Features

* Predict Customer Lifetime Value (CLV) using Machine Learning.
* Segment customers using K-Means Clustering.
* Interactive Streamlit web application.
* Simple and user-friendly interface.
* Business recommendations based on predicted CLV.
* Real-time customer segmentation.

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib
* Matplotlib
* Seaborn

---

## 📂 Dataset

**Dataset:** Online Retail II Dataset

The dataset contains historical retail transactions including:

* Customer ID
* Invoice Number
* Purchase Date
* Quantity
* Unit Price
* Total Purchase Amount

After preprocessing, customer-level features were generated for machine learning.

---

## 📊 Feature Engineering

The following features were created:

* **Recency** – Days since the customer's last purchase.
* **Frequency** – Total number of purchases.
* **Monetary Value** – Total amount spent by the customer.
* **Customer Tenure** – Duration of the customer's relationship with the business.
* **Purchase Frequency** – Average purchase frequency over time.

---

## 🤖 Machine Learning Models

### Customer Lifetime Value Prediction

**Algorithm Used**

* Linear Regression

**Input Features**

* Recency
* Frequency
* Customer Tenure
* Purchase Frequency

**Output**

* Predicted Customer Lifetime Value (CLV)

---

### Customer Segmentation

**Algorithm Used**

* K-Means Clustering

Customers are classified into five segments:

* VIP Customers
* Premium Customers
* Loyal Customers
* Regular Customers
* At-Risk Customers

---

## 📈 Project Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Customer Segmentation using K-Means
6. Customer Lifetime Value Prediction using Linear Regression
7. Model Evaluation
8. Streamlit Application Development

---

## 💻 Streamlit Application

The application enables users to:

* Enter customer details
* Predict Customer Lifetime Value
* Identify customer segment
* Receive business insights based on prediction results

---

## 📷 Application Screenshots

<img width="1920" height="1080" alt="Screenshot (104)" src="https://github.com/user-attachments/assets/6bef0bef-2834-420a-835e-1dd669fedabd" />
<img width="1920" height="1080" alt="Screenshot (105)" src="https://github.com/user-attachments/assets/17fdadf1-ffbc-47e0-8836-42145333be9d" />
<img width="1920" height="1080" alt="Screenshot (106)" src="https://github.com/user-attachments/assets/7ad0c524-907d-4b05-b0ae-e9e0b01c4b4e" />
<img width="1920" height="1080" alt="Screenshot (107)" src="https://github.com/user-attachments/assets/fdac50b3-a330-48e8-8885-55c8eb9b2100" />





---

## 📁 Project Structure

```text
Customer-Lifetime-Value-Prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── sample_dataset.csv
│
├── models/
│   ├── clv_model.pkl
│   ├── kmeans_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── Customer_Lifetime_Value.ipynb
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Hansika1225/Customer-Lifetime-Value-Prediction.git
```

Navigate to the project directory:

```bash
cd Customer-Lifetime-Value-Prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app/app.py
```

---

## 📌 Future Improvements

* Deploy the application on Streamlit Community Cloud.
* Improve prediction accuracy using ensemble models such as Random Forest and XGBoost.
* Add interactive dashboards and visualizations.
* Integrate with cloud databases for real-time predictions.
* Build an API for business integration.

---

## 👩‍💻 Author

**Hansika Arora**

Computer Science Engineering Student

Developed as part of the **IIT Jammu Data Science Internship (Summer 2026)**.

---

## 📄 License

This project is licensed under the MIT License.
