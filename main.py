import streamlit as st
from datetime import date
from databasee import add_expense
from databasee import get_all_expenses
from databasee import engine
from databasee import edit_last
import pandas as pd
st.set_page_config(
    page_title="SpendSense",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<h1 style="
font-family:'Poppins',sans-serif;
font-size:48px;
font-weight:700;
color:#2E7D32;
margin-bottom:0;">
SpendSense
</h1>

<p style="
font-family:'Inter',sans-serif;
font-size:18px;
color:gray;
margin-top:-5px;">   
Powered by Kanakku
</p>
""", unsafe_allow_html=True)
st.subheader("💸 Way to track to your money")
st.divider()
st.markdown("## 🛒 What did you spend on?")
expense_name=st.text_input("",placeholder="Example: Lunch, Petrol, Netflix,etc.")
st.markdown("## 💰 Amount (₹)")
amount=st.number_input("",value=None,min_value=0.0,step=100.0,format="%.2f")
st.markdown("## 📂 Category")
categories = [
    "Food & Dining",
    "Groceries",
    "Public Transport",
    "Travel",
    "Train",
    "Stationery",
    "Exam Fees",
    "Housing",
    "Utilities",
    "Education",
    "Healthcare",
    "Clothing",
    "Footwear",
    "Accessories",
    "Personal Care",
    "Entertainment",
    "Software & Subscriptions",
    "Haircut",
    "Others"
]
category=st.selectbox("",categories)
st.markdown("## 💳 Payment Method")
payment_methods = st.radio("", ["Cash", "UPI", "Debit Card", "Credit Card"],horizontal=True)
st.markdown("## 📅 Date")
expense_date=st.date_input("",value=date.today(),max_value=date.today())
st.markdown("## 📝 Notes")
notes=st.text_area("",placeholder="Add any additional notes or details about the expense.")
#save button
save=st.button("💾 Save Expense")
if save:
    if (expense_name=="") &  (amount<=0):
        st.warning("Please enter expense name and amount.")
    else:
        add_expense(expense_name, amount, category, payment_methods, expense_date, notes)
        st.success("Expense saved successfully!")
st.divider()
st.header("Expense Preview")
st.write("Spend On:", expense_name)
st.write("Amount:", amount)
st.write("Category:", category)
st.write("Payment Method:", payment_methods)
st.write("Expense Date:", expense_date)
edit=st.button("🗑️ Delete Last Expense")
if edit:
    with engine.connect() as conn:
        conn.execute(edit_last())
    st.warning("Last added expense will be deleted. Please re-enter the details.")
st.divider()
st.header("🧾Expense History:")
with engine.connect() as conn:
    result = get_all_expenses()
    if result:
        st.table(result)
    else:
        st.write("No expenses found.")
st.divider()
