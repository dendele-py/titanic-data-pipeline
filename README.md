\# 🚢 Titanic Data Pipeline Project



\## 📌 Overview

This project demonstrates a complete data engineering workflow using Python and PostgreSQL.



It takes the Titanic dataset and processes it through a full pipeline:



\*\*CSV → Pandas → Data Cleaning → PostgreSQL → SQL Analysis → Visualization\*\*



\---



\## 🧰 Tools Used

\- Python

\- Pandas

\- SQLAlchemy

\- PostgreSQL

\- Matplotlib

\- Git \& GitHub



\---



\## ⚙️ Project Workflow



\### 1. Data Ingestion

\- Loaded Titanic dataset from CSV using Pandas



\### 2. Data Cleaning

\- Filled missing values in Age column with median

\- Filled missing Embarked values with mode

\- Removed Cabin column due to excessive missing data



\### 3. Database Storage

\- Stored cleaned dataset in PostgreSQL database (`titanic\_db`)



\### 4. SQL Analysis

Example query:

```sql

SELECT "Sex", AVG("Survived") AS survival\_rate

FROM titanic

GROUP BY "Sex";

