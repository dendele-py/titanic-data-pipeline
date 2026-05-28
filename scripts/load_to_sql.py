import pandas as pd
from sqlalchemy import create_engine

# Load Titanic CSV
df = pd.read_csv("../data/titanic.csv")

# Clean data
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Connect to PostgreSQL
engine = create_engine(
    "postgresql+psycopg2://postgres:Mitsubishi@localhost:5432/titanic_db"
)

# Upload to PostgreSQL
df.to_sql(
    "titanic",
    engine,
    if_exists="replace",
    index=False
)

print("Titanic data uploaded successfully!")