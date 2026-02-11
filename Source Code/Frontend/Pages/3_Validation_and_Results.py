# pages/3_Validation_and_Results.py

import pandas as pd
import streamlit as st

from evaluation.evaluator import evaluate_model
from models.text2sql_engine import generate_sql
from backend.database import execute_query

st.set_page_config(page_title="Validation and Results", layout="wide")

# ------------------------------------------------------------------
# Upload Section
# ------------------------------------------------------------------
st.subheader("Upload English Queries File")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel file with English questions",
    type=["csv", "xlsx"]
)

uploaded_df = None

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        uploaded_df = pd.read_csv(uploaded_file)
    else:
        uploaded_df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")
    st.dataframe(uploaded_df, use_container_width=True)

# ------------------------------------------------------------------
# Page Title & Description
# ------------------------------------------------------------------
st.title("Validation and Results")

st.markdown(
    """
This page evaluates the **Text-to-SQL engine** using two approaches:

1. **Benchmark-based validation** using predefined question–SQL pairs.
2. **User-uploaded English queries**, where queries are converted to SQL
   and validated through database execution.
"""
)

st.divider()

# ------------------------------------------------------------------
# Benchmark Evaluation (Existing Feature)
# ------------------------------------------------------------------
st.subheader("Run Evaluation on Benchmark Dataset")

engine_mode = st.radio(
    "Select engine mode:",
    options=["model_based", "rule_based"],
    index=0,
    horizontal=True,
)

if st.button("Evaluate Text-to-SQL Engine", type="primary"):
    with st.spinner("Running evaluation on benchmark dataset..."):
        summary = evaluate_model(
            db_path="data/college.db",
            csv_path="evaluation/evaluation_cases.csv",
            mode=engine_mode,
        )

    st.success("Evaluation completed!")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Cases", summary["total"])
    col2.metric("LF Correct", summary["lf_correct"])
    col3.metric("EX Correct", summary["ex_correct"])
    col4.metric("LF Accuracy (%)", f"{summary['lf_accuracy']:.1f}")

    st.metric("EX Accuracy (%)", f"{summary['ex_accuracy']:.1f}")

    st.divider()

    st.subheader("Per-Case Evaluation Details")

    for item in summary["results"]:
        item["expected_rows"] = str(item["expected_rows"])
        item["generated_rows"] = str(item["generated_rows"])

    df = pd.DataFrame(summary["results"])

    df = df[
        [
            "question",
            "expected_sql",
            "generated_sql",
            "lf_correct",
            "ex_correct",
            "expected_rows",
            "generated_rows",
            "error",
        ]
    ]

    st.dataframe(df, use_container_width=True)

# ------------------------------------------------------------------
# Uploaded File Evaluation (NEW FEATURE)
# ------------------------------------------------------------------
if uploaded_df is not None and "question" in uploaded_df.columns:
    st.divider()
    st.subheader("Results for Uploaded English Queries")

    results = []

    for q in uploaded_df["question"]:
        try:
            sql = generate_sql(q, mode=engine_mode)
            df_result = execute_query(sql)

            if df_result is not None:
                status = "Success"
                result_text = df_result.to_string(index=False)
                error = None
            else:
                status = "Error"
                result_text = None
                error = "SQL execution failed"

        except Exception as e:
            status = "Error"
            sql = None
            result_text = None
            error = str(e)

        results.append({
            "question": q,
            "generated_sql": sql,
            "status": status,
            "result": result_text,
            "error": error
        })

    result_df = pd.DataFrame(results)
    st.dataframe(result_df, use_container_width=True)

elif uploaded_df is not None:
    st.error("Uploaded file must contain a column named 'question'")
