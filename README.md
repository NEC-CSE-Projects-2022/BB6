
# Team Number – BB6 – Semantic-Augmented Prompt-Guided Sketch Filling for Text-to-SQL Generation

## Team Info
## 22471A05A6 — Kurivella Bala Venkata Mani Kanta  ( [LinkedIn](https://www.linkedin.com/in/kurivella-bala-venkata-manikanta-001421352) )
-Work Done: Project lead; responsible for model selection, training, evaluation, and overall system integration. Implemented deep learning pipelines for multiclass skin lesion classification and handled performance analysis.

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


---

## Dependencies Used
This project is developed using Python and executed on Google Colab for training and experimentation. PyTorch and the Hugging Face Transformers library are used to implement the T5 encoder–decoder model. NumPy and Pandas support data preprocessing, while SQLite and JSON are used for schema storage and SQL execution. Matplotlib, Torch, Tokenizers, and tqdm assist in training, visualization, and performance monitoring.



---

## EDA & Preprocessing
- Mounted Google Drive in Google Colab and imported required libraries for data loading and analysis.

- Loaded the WikiSQL dataset and reviewed the distribution of training, validation, and test samples.

- Verified the integrity of question–SQL pairs and ensured all queries had corresponding schema information.

- Analyzed natural language question lengths and SQL query complexity to understand data characteristics.

- Identified table schemas, column names, and data types used across the dataset.

- Normalized text by converting to lowercase and handling punctuation for consistent tokenization.

- Constructed structured prompts by combining user queries with table schema details.

- Generated SQL sketch templates with placeholders for SELECT, WHERE, operators, and values.
  Tokenized input prompts and target SQL queries using the T5 tokenizer.

- Applied padding and truncation to maintain uniform sequence lengths.

- Converted processed data into tensors suitable for model training.

- Completed data cleaning and preprocessing to ensure the dataset was ready for accurate and stable model training.

---

## Model Training Info
The model is developed using a prompt-guided sketch filling approach based on the T5 encoder–decoder architecture for Text-to-SQL generation. Training is carried out on Google Colab with GPU support using the WikiSQL dataset, which is divided into training, validation, and testing sets.

Before training, the dataset is carefully preprocessed by validating question–SQL pairs, cleaning text, embedding schema information, and constructing structured prompts and SQL sketches. This ensures high-quality input and stable learning.

After training, the model is evaluated using Execution Accuracy (EX) and Logical Form Accuracy (LF) to measure performance. The best-performing model checkpoints are saved and finalized, resulting in a trained Text-to-SQL model capable of generating and executing accurate SQL queries for real-world use.

---

## Model Testing / Evaluation
The model was evaluated after training to ensure reliable performance in practical Text-to-SQL scenarios. Validation was performed using Execution Accuracy (EX) and Logical Form Accuracy (LF) to assess the correctness of generated SQL queries.

The model was further tested on a separate test set to verify its ability to generalize across unseen database schemas and queries. After confirming stable performance, the best model checkpoints were selected and saved. Finally, the system was tested end-to-end by executing generated SQL queries on the database to ensure correct result retrieval.


---

## Results
The YOLO-HF model was successfully trained on 3,900 images and evaluated using standard metrics such as Precision, Recall, F1-score, and mAP. The results showed strong detection accuracy with fewer false alarms and missed detections, proving the model’s reliability for early fire and smoke identification.

Compared to the baseline YOLOv5s and other recent detection models, YOLO-HF delivered better overall performance while maintaining a lightweight design suitable for real-time use. Threshold tuning further reduced false positives without affecting detection sensitivity, making the system more stable in practical environments.

Validation plots such as the confusion matrix and Precision–Recall curve confirmed that the model can accurately localize fire and smoke across different conditions. Testing on unseen data demonstrated good generalization capability.

The trained model was then deployed into a real-time monitoring system that captures live video, detects fire instantly, and sends alerts through email with an attached image along with an automated call. The final system operates smoothly on a local setup, confirming its readiness for real-world safety applications.



---

## Limitations & Future Work
Limitations:
- The model is trained on the WikiSQL dataset, which is limited to single-table queries and may not fully represent complex real-world database scenarios.

- The system currently handles basic SQL structures and does not support advanced queries such as joins, nested queries, or group-by operations.

- Ambiguous or poorly phrased user questions can still lead to incorrect column or condition selection.

- Evaluation is primarily performed on benchmark data, so performance may vary on unseen, domain-specific databases.

Future Work:
- Extend the model to support complex SQL queries, including joins, aggregations, and nested subqueries.

- Train and evaluate the system on larger and more diverse Text-to-SQL datasets to improve generalization.

- Integrate external knowledge sources or schema linking techniques to better handle ambiguity in user queries.

- Explore execution-guided decoding and interactive user feedback to further improve accuracy and robustness.

- Deploy the system as a web or application-based interface for real-world database querying.



---

## Deployment Info
The trained Text-to-SQL model is saved as a finalized model checkpoint and deployed on a local system for natural language database querying. Users can input questions in plain English, and the system generates and executes the corresponding SQL queries in real time. The deployment enables seamless interaction with databases, allowing non-technical users to retrieve accurate results without writing SQL manually.

---
