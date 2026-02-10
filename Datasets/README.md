## Dataset (WikiSQL)

- **Total queries:** 80,000+ natural language question–SQL pairs  
- **Tables:** 24,000+ single-table schemas extracted from Wikipedia  
- **Data type:** Text (natural language questions, SQL queries, table schemas)  
- **Task:** Natural Language to SQL (Text-to-SQL) generation  
- **Query scope:** Single-table SQL queries with SELECT and WHERE clauses  
- **Official source:** Kaggle (recommended)

---

### Download Links

- **Kaggle (official):**  
  https://www.kaggle.com/datasets/shahrukhkhan/wikisql

- **Project mirror (Google Drive):**  
  https://drive.google.com/drive/folders/1CntK0aiedkbU-HXVvuID_EqZqpv1iiUS?usp=drive_link

> **Important:** Do **not** commit the dataset files to this repository.  
> Download the dataset locally and place it under the `Datasets/` directory.

---

### Expected Dataset Structure

```text
Datasets/
  README.md
  train.json
  dev.json
  test.json
  train.tables.json
  dev.tables.json
  test.tables.json

