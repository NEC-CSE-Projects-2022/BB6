import streamlit as st

def main():
    st.title("Natural Language to SQL Query Generation System")

    st.markdown("""
    ### 🔍 Introduction
    This project converts **natural language questions (English text)** into **SQL queries**.
    It helps non-technical users interact with databases easily without knowing SQL syntax.

    ---

    ### 🎯 Problem Statement
    Most users do not know SQL, and writing SQL queries is difficult.
    This system allows users to ask questions in plain English and 
    automatically generates the correct SQL query for the database.

    ---

    ### 🎯 Objectives
    - Convert user English queries into SQL.
    - Support database schemas dynamically.
    - Execute generated SQL queries.
    - Display output clearly.
    - Validate model accuracy using LF & EX metrics.

    ---

    ### 🧠 System Workflow
    1. User types a natural language question.
    2. Text-to-SQL model generates the SQL query.
    3. SQL query is executed on the database.
    4. Results are shown to the user.
    5. Validation page shows accuracy metrics.

    ---

    ### 📌 Navigation
    Use the **left sidebar** to access:
    - Dataset Description
    - Text-to-SQL Interface
    - Validation & Results
    """)

if __name__ == "__main__":
    main()
