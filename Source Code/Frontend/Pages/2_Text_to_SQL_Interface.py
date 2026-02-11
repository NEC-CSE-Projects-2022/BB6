import streamlit as st
import pandas as pd

from models.text2sql_engine import load_model, generate_sql
from backend.database import get_schema, execute_query


def main():
    st.title("Text to SQL Interface")

    st.markdown("""
    This page allows you to enter a **natural language question** in English.
    The system will generate an SQL query and execute it on the database.
    """)

    st.markdown("---")

    # Load schema from DB
    schema = get_schema()

    # Initialize engine mode in session (default: model_based)
    if "engine_mode" not in st.session_state:
        st.session_state["engine_mode"] = "model_based"

    # Optionally let user switch modes (useful in review)
    st.subheader("Engine Mode")
    selected_mode = st.radio(
        "Select Text-to-SQL Engine Mode:",
        options=["model_based", "rule_based"],
        index=0,
        horizontal=True,
    )
    st.session_state["engine_mode"] = selected_mode

    # Load model according to mode (for now both return None)
    if "text2sql_model" not in st.session_state or st.session_state.get("model_mode") != selected_mode:
        st.session_state["text2sql_model"] = load_model(mode=selected_mode)
        st.session_state["model_mode"] = selected_mode

    model = st.session_state["text2sql_model"]

    # Show schema to the user
    st.subheader("Database Schema")
    if schema:
        for table_name, columns in schema.items():
            st.markdown(f"**{table_name}**: {', '.join(columns)}")
    else:
        st.warning("Could not load schema information. Please check the database connection.")

    st.markdown("---")

    # Input question
    st.subheader("Ask a Question in English")
    question = st.text_input(
        "Enter your question:",
        placeholder="e.g., List all students with CGPA greater than 8",
    )

    generate_clicked = st.button("Generate SQL and Execute")

    if generate_clicked:
        if not question.strip():
            st.warning("Please enter a question before generating SQL.")
            return

        # Generate SQL using selected engine mode
        sql_query = generate_sql(
            question=question,
            schema_info=schema,
            mode=selected_mode,
            model=model,
        )

        st.success(f"Generated SQL Query ({selected_mode}):")
        st.code(sql_query, language="sql")

        # Execute SQL
        st.subheader("Query Execution Result")
        result_df = execute_query(sql_query)

        if result_df is None:
            st.error("Failed to execute the query. Please check SQL or database.")
        elif isinstance(result_df, pd.DataFrame) and result_df.empty:
            st.info("Query executed successfully, but no rows were returned.")
        else:
            st.dataframe(result_df, use_container_width=True)


if __name__ == "__main__":
    main()
