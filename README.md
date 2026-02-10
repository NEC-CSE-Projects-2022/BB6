
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
- Enhanced the base sketch-filling approach by integrating prompt-guided SQL generation using the T5 encoder–decoder architecture, improving semantic understanding and query accuracy.

- Designed structured prompts that explicitly combine user queries with database schema information, strengthening schema–query alignment compared to the original model.

- Implemented a semantic-augmented sketch filling framework that reduces ambiguity and prevents invalid SQL generation by filling predefined query templates instead of generating full SQL statements.

- Conducted systematic preprocessing, training, validation, and testing on the WikiSQL dataset to ensure stable performance and reliable execution accuracy in practical scenarios.

- Converted the research-oriented model into a fully functional Text-to-SQL system capable of generating and executing SQL queries end to end.

- Focused on execution accuracy–driven evaluation, ensuring that generated queries return correct results rather than relying only on exact string matching.

- Optimized the implementation so the system can run efficiently on standard local machines without requiring high-end computational infrastructure.

- Emphasized practical usability by transforming a research-based Text-to-SQL model into a ready-to-use natural language database querying solution for non-technical users.

---

## About the Project
Give a simple explanation of:
What the project does:
This project converts natural language questions into executable SQL queries using a prompt-guided sketch filling approach based on the T5 transformer model. Instead of generating complete SQL statements directly, the system fills predefined SQL templates by understanding the user query and the corresponding database schema, ensuring accurate and syntactically valid query generation.

Why it is useful:
Querying databases usually requires knowledge of SQL, which can be difficult for non-technical users. This project makes database access easier by allowing users to retrieve information using plain English queries. By reducing semantic ambiguity and preventing invalid SQL generation, the system improves reliability and supports practical, real-world database interaction.

General project workflow (Input → Processing → Model → Output):
A natural language question is provided as input → the query is combined with database schema information to form a structured prompt → the prompt-guided T5 model processes the input and fills predefined SQL sketch placeholders → a complete SQL query is generated and executed on the database → the final query result is returned to the user.

---

## Dataset Used
👉 **[Dataset Name](https://drive.google.com/drive/folders/1CntK0aiedkbU-HXVvuID_EqZqpv1iiUS?usp=drive_link)**
Dataset Details:
This project uses the WikiSQL dataset, which contains over 80,000 natural language questions paired with corresponding SQL queries and table schemas. The dataset is divided into three subsets: a training set for model learning, a validation set for tuning and performance improvement, and a test set for final evaluation.

The dataset is a standard benchmark for Text-to-SQL research and is publicly available at:
https://github.com/salesforce/WikiSQL
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
