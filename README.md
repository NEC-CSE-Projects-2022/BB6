
# Team Number – BB6 – Semantic-Augmented Prompt-Guided Sketch Filling for Text-to-SQL Generation

## Team Info
- 22471A05XX — **Name** ( [LinkedIn](https://linkedin.com/in/xxxxxxxxxx) )
_Work Done: xxxxxxxxxx_

- 22471A05XX — **Name** ( [LinkedIn](https://linkedin.com/in/xxxxxxxxxx) )
_Work Done: xxxxxxxxxx_

- 22471A05XX — **Name** ( [LinkedIn](https://linkedin.com/in/xxxxxxxxxx) )
_Work Done: xxxxxxxxxx_

- 22471A05XX — **Name** ( [LinkedIn](https://linkedin.com/in/xxxxxxxxxx) )
_Work Done: xxxxxxxxxx_

---

## Abstract
Enabling users to query relational databases using natural language is essential for improving accessibility; however, traditional Text-to-SQL systems often struggle with semantic ambiguity and the generation of syntactically invalid queries, particularly for non-technical users. This work presents a prompt-guided sketch filling framework for automated natural language to SQL conversion, evaluated on the WikiSQL benchmark dataset. The proposed approach utilizes a T5 encoder–decoder architecture that generates SQL queries by completing predefined query sketches instead of producing full queries directly. By incorporating structured prompts, database schema information, and schema-aware attention mechanisms, the model effectively aligns user intent with relational structures while ensuring syntactic correctness. The system addresses key challenges such as ambiguous query interpretation and invalid SQL generation, achieving reliable performance suitable for practical database interaction. Experimental evaluation demonstrates that the proposed method attains an execution accuracy of 85.1%, outperforming the SQLNet baseline by 6.7%, highlighting its effectiveness for real-world natural language database querying applications.

---

## Paper Reference (Inspiration)
👉 Generate Text-to-SQL Queries Based on Sketch Filling – Yinpei Fu, Songtao Ye, and Hongjie Fan ([Paper Link](https://doi.org/10.1109/ACCESS.2024.3476927))




---

## Our Improvement Over Existing Paper
Enhanced the base sketch-filling approach by integrating prompt-guided SQL generation using the T5 encoder–decoder architecture, improving semantic understanding and query accuracy.

Designed structured prompts that explicitly combine user queries with database schema information, strengthening schema–query alignment compared to the original model.

Implemented a semantic-augmented sketch filling framework that reduces ambiguity and prevents invalid SQL generation by filling predefined query templates instead of generating full SQL statements.

Conducted systematic preprocessing, training, validation, and testing on the WikiSQL dataset to ensure stable performance and reliable execution accuracy in practical scenarios.

Converted the research-oriented model into a fully functional Text-to-SQL system capable of generating and executing SQL queries end to end.

Focused on execution accuracy–driven evaluation, ensuring that generated queries return correct results rather than relying only on exact string matching.

Optimized the implementation so the system can run efficiently on standard local machines without requiring high-end computational infrastructure.

Emphasized practical usability by transforming a research-based Text-to-SQL model into a ready-to-use natural language database querying solution for non-technical users.

---

## About the Project
Give a simple explanation of:
- What your project does
- Why it is useful
- General project workflow (input → processing → model → output)

---

## Dataset Used
👉 **[Dataset Name](Dataset URL)**

**Dataset Details:**
xxxxxxxxxx

---

## Dependencies Used
xxxxxxxxxx, xxxxxxxxxx, xxxxxxxxxx ...

---

## EDA & Preprocessing
xxxxxxxxxx

---

## Model Training Info
xxxxxxxxxx

---

## Model Testing / Evaluation
xxxxxxxxxx

---

## Results
xxxxxxxxxx

---

## Limitations & Future Work
xxxxxxxxxx

---

## Deployment Info
xxxxxxxxxx

---
