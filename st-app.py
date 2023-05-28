""" Expense tracking application designed to manage a monthly budget,
categorise outgoings and generate visualisations from the input data
"""

import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def main():
    """ Main Streamlit function to organise and display the webapp
    """
    st.title("Monthly Outgoings Dashboard")

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            amount REAL
        )
    ''')

    st.sidebar.header("Add Expense")
    category = st.sidebar.selectbox("Category", get_category_list(conn))
    if category == "Custom Category":
        custom_category = st.sidebar.text_input("Custom Category")
    amount = st.sidebar.number_input(
        "Amount",
        value=0.0,
        step=0.01,
        format="%.2f"
        )

    if st.sidebar.button("Add"):
        if custom_category:
            category = custom_category.strip()
            if category not in get_category_list(conn):
                add_category(cursor, category, conn)
        cursor.execute(
            "INSERT INTO expenses (category, amount) VALUES (?, ?)",
            (category, amount)
            )
        conn.commit()
        st.sidebar.success("Expense added successfully.")

    st.sidebar.header("Remove Expense")
    expenses = pd.read_sql_query("SELECT * FROM expenses", conn)
    if not expenses.empty:
        selected_expense = st.sidebar.radio(
            "Selected Expense",
            expenses["id"])
        if st.sidebar.button("Remove"):
            remove_expense(cursor, selected_expense, conn)
            expenses = pd.read_sql_query("SELECT * FROM expenses", conn)

    category_expenses = expenses.groupby("category")["amount"].sum()

    # Create a pie chart for the monthly expenses
    fig, axis = plt.subplots()
    axis.pie(
        category_expenses,
        labels=category_expenses.index,
        autopct=lambda pct: func(pct, category_expenses),
        startangle=90
        )
    axis.axis("equal")
    st.pyplot(fig)

    with st.expander("Expenses Raw Dataframe"):
        st.header("Monthly Expenses")
        if not expenses.empty:
            st.dataframe(expenses)
        else:
            st.info("No expenses recorded.")


def get_category_list(conn):
    """Displays all existing categories in database

    Args:
        conn (sqlite3.Connection): Database connection

    Returns:
        list: Category list
    """
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT category FROM expenses")
    stored_categories = [row[0] for row in cursor.fetchall()]
    return ["Custom Category"] + stored_categories


def add_category(cursor, category, conn):
    """Add a custom category to the database

    Args:
        cursor (sqlite3.Cursor): Database cursor
        category (str): Expense category
        conn (sqlite3.Connection): Database connection
    """
    cursor.execute(
        "SELECT category FROM expenses WHERE category=?",
        (category,)
        )
    existing_category = cursor.fetchone()
    if not existing_category:
        conn.commit()


def remove_expense(cursor, selected_expense, conn):
    """Remove an expense from the database

    Args:
        cursor (sqlite3.Cursor): Database cursor
        selected_expense (str): Current selected expense
        conn (sqlite3.Connection): Database connection
    """
    cursor.execute("DELETE FROM expenses WHERE id=?", (selected_expense,))
    conn.commit()
    st.sidebar.success("Expense removed successfully.")


def func(pct, allvals):
    """Calculate expense percentage of total
    """
    absolute = int(pct / 100. * sum(allvals))
    return f"{pct:.1f}%\n{absolute:d}"


if __name__ == "__main__":
    main()
