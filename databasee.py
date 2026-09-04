from sqlalchemy import create_engine, text
import pandas as pd
engine = create_engine("sqlite:///expense.db", echo=False)

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS Expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expense_name TEXT NOT NULL,
            amount DECIMAL(10,2) NOT NULL,
            category TEXT NOT NULL,
            payment_method TEXT NOT NULL,
            expense_date DATE NOT NULL,
            notes TEXT
        )
    """))
    conn.commit()


def add_expense(expense_name, amount, category, payment_method, expense_date, notes):
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO Expenses
                (expense_name, amount, category, payment_method, expense_date, notes)
                VALUES
                (:expense_name, :amount, :category, :payment_method, :expense_date, :notes)
            """),
            {
                "expense_name": expense_name,
                "amount": amount,
                "category": category,
                "payment_method": payment_method,
                "expense_date": str(expense_date),
                "notes": notes
            }
        )
        conn.commit()
def edit_last():
  with engine.connect() as conn:
    conn.execute(text("""
        DELETE FROM Expenses
        WHERE id = (
            SELECT MAX(id)
            FROM Expenses
        )
    """))
    conn.commit()
def get_all_expenses():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM Expenses ORDER BY expense_date DESC")
        )
        return result.fetchall()
