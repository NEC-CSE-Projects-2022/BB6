"""
Text-to-SQL Engine with two modes:
- rule_based   : basic logical mapping (offline)
- model_based  : Groq AI + smart fallback (recommended)
"""

import re
from typing import Optional, Dict, List

import config
from groq import Groq

ENGINE_MODES = ("rule_based", "model_based")

# ======================================================================= #
# 1. LOAD MODEL (placeholder for future training)
# ======================================================================= #

def load_model(mode: str = "model_based"):
    """Currently we don't load any heavy local model."""
    return None  # no heavy local model yet

# ======================================================================= #
# 2. Groq API Client
# ======================================================================= #

_groq_client: Optional[Groq] = None


def _get_groq_client() -> Optional[Groq]:
    """
    Create (or reuse) a Groq client using the API key from config.py.
    If anything fails, return None so that we can safely fall back.
    """
    global _groq_client
    try:
        if _groq_client is None:
            api_key = getattr(config, "GROQ_API_KEY", None)
            if not api_key:
                print("[LLM] GROQ_API_KEY missing in config.py → fallback to offline logic.")
                return None
            _groq_client = Groq(api_key=api_key)
        return _groq_client
    except Exception as e:
        print(f"[LLM] Failed to initialize Groq client → {e}")
        return None


def _call_llm(prompt: str) -> str:
    """
    Call GROQ LLM (Text-to-SQL). If anything fails, return "" safely.
    """
    client = _get_groq_client()
    if client is None:
        return ""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are an expert Text-to-SQL generator."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
        )
        content = response.choices[0].message.content
        return content.strip() if content else ""
    except Exception as e:
        print(f"[LLM] Error while calling Groq → {e}")
        return ""

# ======================================================================= #
# Helper to clean LLM output
# ======================================================================= #

def _clean_sql_output(text: Optional[str]) -> str:
    """
    Clean raw LLM text and extract a usable SQL query.
    """
    if not text:
        return ""
    sql = text.strip()

    # Remove markdown ``` and ```sql fences
    if sql.startswith("```"):
        sql = sql.replace("```sql", "").replace("```", "").strip()

    # Take only part starting from SELECT
    idx = sql.lower().find("select")
    if idx != -1:
        sql = sql[idx:]

    # Ensure ending semicolon
    if not sql.endswith(";"):
        sql += ";"

    return sql.strip()

# ======================================================================= #
# RULE BASED ENGINE (always offline, simple backup)
# ======================================================================= #

def _generate_sql_rule_based(question: str, schema_info=None) -> str:
    q = question.lower()

    # CGPA filter
    if "cgpa" in q and ("greater" in q or "above" in q or "more than" in q):
        return "SELECT name, cgpa FROM students WHERE cgpa > 8.0;"

    # All students
    if "all students" in q or "list students" in q or "show students" in q:
        return "SELECT id, name, department, cgpa FROM students;"

    # All courses
    if "courses" in q:
        return "SELECT id, course_name, credits FROM courses;"

    # Students with their courses
    if "enroll" in q or "student course" in q or "students with courses" in q:
        return (
            "SELECT s.name AS student_name, c.course_name, e.grade "
            "FROM students s "
            "JOIN enrollments e ON s.id = e.student_id "
            "JOIN courses c ON c.id = e.course_id;"
        )

    # Default fallback
    return "SELECT id, name, department, cgpa FROM students;"

# ======================================================================= #
# MODEL BASED ENGINE (Groq → Smart Logic → Rule Backup)
# ======================================================================= #

def _schema_to_string(schema: Dict[str, List[str]]) -> str:
    return "\n".join([f"{table}({', '.join(cols)})" for table, cols in schema.items()])


def _generate_sql_model_based(question: str, schema_info=None, model=None) -> str:
    """
    1. Build prompt with schema + question.
    2. Try Groq LLM.
    3. If LLM fails or returns bad SQL → smart local logic.
    """

    # ---------- 1. Build prompt for LLM ----------
    schema_text = _schema_to_string(schema_info or {})
    prompt = f"""
You are a Text-to-SQL generator.

### Schema ###
{schema_text}

### Question ###
{question}

### Output Rules ###
- Output only SQL query.
- No explanation.
- Use correct table/column names.
- End with a semicolon.
""".strip()

    # ---------- 2. Try Groq first ----------
    llm_raw = _call_llm(prompt)
    llm_sql = _clean_sql_output(llm_raw)

    if llm_sql.lower().startswith("select"):
        return llm_sql

    # ---------- 3. Smart pattern fallback ----------
    q = question.lower()
    has_students = "student" in q or "students" in q
    has_courses = "course" in q or "courses" in q

    # detect CGPA (first number)
    cgpa = None
    if "cgpa" in q:
        m = re.search(r"(\d+(\.\d+)?)", q)
        if m:
            cgpa = m.group(1)

    # detect department
    depts = ["cse", "it", "ece", "eee", "mech", "civil"]
    dept = next((d.upper() for d in depts if d in q), None)

    # students with courses
    if has_students and has_courses:
        return (
            "SELECT s.name, c.course_name, e.grade "
            "FROM students s "
            "JOIN enrollments e ON s.id = e.student_id "
            "JOIN courses c ON c.id = e.course_id;"
        )

    # CGPA + department (case-insensitive department)
    if cgpa and dept:
        return (
            "SELECT name, department, cgpa "
            "FROM students "
            f"WHERE cgpa > {cgpa} AND LOWER(department) = LOWER('{dept}');"
        )

    # Only CGPA
    if cgpa:
        return (
            "SELECT name, cgpa "
            "FROM students "
            f"WHERE cgpa > {cgpa};"
        )

    # Only department (case-insensitive)
    if dept:
        return (
            "SELECT name, department, cgpa "
            "FROM students "
            f"WHERE LOWER(department) = LOWER('{dept}');"
        )

    # Only students
    if has_students:
        return "SELECT id, name, department, cgpa FROM students;"

    # Only courses
    if has_courses:
        return "SELECT id, course_name, credits FROM courses;"

    # Final fallback
    return "SELECT id, name, department, cgpa FROM students;"

# ======================================================================= #
# PUBLIC FUNCTION (USED BY STREAMLIT)
# ======================================================================= #

def generate_sql(
    question: str,
    schema_info=None,
    mode: str = "model_based",
    model=None,
) -> str:
    """
    Main entry used by the Streamlit UI.
    """
    mode = (mode or "model_based").lower().strip()

    if mode == "model_based":
        try:
            return _generate_sql_model_based(question, schema_info, model)
        except Exception as e:
            print(f"[model_based error] {e}")
            return _generate_sql_rule_based(question, schema_info)

    # rule_based
    return _generate_sql_rule_based(question, schema_info)
