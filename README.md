# 💸 SpendSense

> **Powered by Kanakku**

SpendSense is a simple personal expense-tracking web application built with **Python, Streamlit, and SQLite**. It allows users to record daily expenses, categorize spending, select payment methods, add notes, and view their expense history through a clean and simple interface.

## ✨ Features

* 💸 Add and save personal expenses
* 🛒 Enter the name/description of an expense
* 💰 Record expense amount in Indian Rupees (₹)
* 📂 Categorize expenses
* 💳 Select payment method
* 📅 Select the expense date
* 📝 Add optional notes
* 🧾 View complete expense history
* 🗑️ Delete the most recently added expense
* 💾 Persistent local storage using SQLite
* 🎨 Clean and responsive Streamlit interface

## 🛠️ Tech Stack

| Technology     | Purpose                               |
| -------------- | ------------------------------------- |
| **Python**     | Application logic                     |
| **Streamlit**  | Web application UI                    |
| **SQLite**     | Local database                        |
| **SQLAlchemy** | Database connection and SQL execution |
| **Pandas**     | Data handling                         |
| **HTML/CSS**   | UI customization                      |

## 📂 Project Structure

```text
SpendSense/
│
├── app.py
├── databasee.py
├── expense.db
└── README.md
```

### Files

**main.py**

Contains the Streamlit application interface and handles:

* Expense input
* Form validation
* Saving expenses
* Expense preview
* Deleting the latest expense
* Displaying expense history

**`databasee.py`**

Contains the database layer and handles:

* SQLite database connection
* Table creation
* Adding expenses
* Retrieving expenses
* Deleting the latest expense

**`expense.db`**

SQLite database file used to persist expense records locally.

> `expense.db` is generated when the application initializes the database if it does not already exist.

## 🗄️ Database Design

SpendSense uses an SQLite database containing an `Expenses` table.

### Expenses Table

| Column           | Type          | Description                     |
| ---------------- | ------------- | ------------------------------- |
| `id`             | INTEGER       | Unique expense ID               |
| `expense_name`   | TEXT          | Name/description of the expense |
| `amount`         | DECIMAL(10,2) | Expense amount                  |
| `category`       | TEXT          | Expense category                |
| `payment_method` | TEXT          | Method used for payment         |
| `expense_date`   | DATE          | Date of the expense             |
| `notes`          | TEXT          | Additional information          |

The `id` column is automatically generated using:

```sql
INTEGER PRIMARY KEY AUTOINCREMENT
```

## 📂 Expense Categories

SpendSense currently supports the following categories:

* Food & Dining
* Groceries
* Public Transport
* Travel
* Train
* Stationery
* Exam Fees
* Housing
* Utilities
* Education
* Healthcare
* Clothing
* Footwear
* Accessories
* Personal Care
* Entertainment
* Software & Subscriptions
* Haircut
* Others

## 💳 Payment Methods

Users can select one of four payment methods:

* Cash
* UPI
* Debit Card
* Credit Card

## ⚙️ How It Works

The application follows a simple flow:

```text
User
 │
 ▼
Streamlit Interface
 │
 ├── Enter Expense Details
 │
 ├── Validate Input
 │
 ▼
databasee.py
 │
 ▼
SQLAlchemy
 │
 ▼
SQLite Database
 │
 ▼
expense.db
```

### Saving an Expense

When the user clicks **Save Expense**:

1. The application collects the expense details.
2. Basic validation is performed.
3. `add_expense()` is called.
4. SQLAlchemy executes an `INSERT` query.
5. The expense is stored in SQLite.
6. A success message is displayed.

### Viewing Expenses

When the application loads the expense history:

1. A database connection is created.
2. `get_all_expenses()` executes a `SELECT` query.
3. Expenses are ordered by date.
4. The records are displayed in the Streamlit interface.

### Deleting the Last Expense

When **Delete Last Expense** is selected:

1. `edit_last()` identifies the record with the highest `id`.
2. The corresponding record is deleted.
3. The user is asked to re-enter the details if necessary.

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd SpendSense
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install streamlit sqlalchemy pandas
```

## ▶️ Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

Streamlit will start the application locally and provide a URL in the terminal.

Open the provided URL in your browser.

## 🧪 Example

A user can enter:

```text
Spend On: Lunch
Amount: ₹150
Category: Food & Dining
Payment Method: UPI
Date: 2026-09-04
Notes: Lunch at college
```

After clicking **Save Expense**, the expense is inserted into the SQLite database and becomes available in the **Expense History** section.

## 🔐 Data Storage

SpendSense currently uses a **local SQLite database**.

This means:

* No external database server is required.
* Expenses are stored locally.
* The application can work without an internet connection once dependencies are installed.
* The database file is created locally as `expense.db`.

## 🧠 SQL Operations Used

The project provides practical implementation of basic SQL operations through SQLAlchemy.

### INSERT

Used to add a new expense:

```sql
INSERT INTO Expenses
(expense_name, amount, category, payment_method, expense_date, notes)
VALUES (...)
```

### SELECT

Used to retrieve expense history:

```sql
SELECT *
FROM Expenses
ORDER BY expense_date DESC
```

### DELETE

Used to remove the most recently added expense:

```sql
DELETE FROM Expenses
WHERE id = (
    SELECT MAX(id)
    FROM Expenses
)
```

## 🎯 Project Purpose

SpendSense was built as a practical project to understand how a Python application can interact with a relational database.

It combines:

**Python + Streamlit + SQL + SQLAlchemy + SQLite**

into a small, functional personal finance application.

## 🔮 Future Improvements

Possible improvements for future versions include:

* 📊 Expense analytics and charts
* 📈 Monthly spending trends
* 💰 Budget management
* 🏷️ Custom categories
* 🔎 Search and filtering
* ✏️ Edit existing expenses
* 📅 Monthly and yearly reports
* 📥 Export expenses to CSV/Excel
* 📊 Category-wise spending analysis
* 🔐 User authentication
* ☁️ Cloud database support
* 📱 Improved mobile experience

## 👨‍💻 Author

**Muthu**

Built with Python, SQL, and Streamlit.

---

## 📜 License

This project is intended for learning and personal project purposes.
