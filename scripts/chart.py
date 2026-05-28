import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# -------------------------
# Connect to PostgreSQL
# -------------------------
engine = create_engine(
    "postgresql+psycopg2://postgres:Mitsubishi@localhost:5432/titanic_db"
)

# -------------------------
# SQL query
# -------------------------
query = """
SELECT "Sex", AVG("Survived") AS survival_rate
FROM titanic
GROUP BY "Sex";
"""

# -------------------------
# Load into pandas
# -------------------------
df = pd.read_sql(query, engine)

print(df)

# -------------------------
# Plot chart
# -------------------------
df.plot(
    x="Sex",
    y="survival_rate",
    kind="bar"
)

plt.title("Titanic Survival Rate by Gender")
plt.ylabel("Survival Rate")
plt.xlabel("Sex")

plt.show()