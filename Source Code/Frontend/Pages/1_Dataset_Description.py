import streamlit as st

def main():
    st.title("Dataset Description")

    st.markdown("""
    ### 📘 Overview
    In this project, we work with a **Text-to-SQL style dataset**.
    Each record in the dataset contains:
    - A natural language question (English)
    - The corresponding SQL query
    - The database schema on which the query is executed
    """)

    st.markdown("---")

    st.markdown("""
    ### 🗄️ Demo Database Schema

    We use a **college-style relational database** with the following tables:

    **1. `students`**
    - `id` (INTEGER, Primary Key)  
    - `name` (TEXT)  
    - `department` (TEXT)  
    - `cgpa` (REAL)  

    **2. `courses`**
    - `id` (INTEGER, Primary Key)  
    - `course_name` (TEXT)  
    - `credits` (INTEGER)  

    **3. `enrollments`**
    - `student_id` (INTEGER, Foreign Key → students.id)  
    - `course_id` (INTEGER, Foreign Key → courses.id)  
    - `grade` (TEXT)  
    """)

    st.markdown("---")

    st.markdown("""
    ### 🧾 Example Question–SQL Pairs

    **Example 1**  
    - Question: *"List all students with CGPA greater than 8."*  
    - SQL:  
    ```sql
    SELECT name, cgpa 
    FROM students 
    WHERE cgpa > 8.0;
    ```

    **Example 2**  
    - Question: *"Show all course names and their credits."*  
    - SQL:  
    ```sql
    SELECT course_name, credits 
    FROM courses;
    ```

    **Example 3**  
    - Question: *"Display each student with the courses they are enrolled in."*  
    - SQL:  
    ```sql
    SELECT s.name, c.course_name 
    FROM students s
    JOIN enrollments e ON s.id = e.student_id
    JOIN courses c ON c.id = e.course_id;
    ```
    """)

if __name__ == "__main__":
    main()
