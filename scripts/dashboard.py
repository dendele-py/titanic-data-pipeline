import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# -------------------------
# Page setup
# -------------------------
st.set_page_config(page_title="Titanic Dashboard", layout="wide")

st.title("🚢 Titanic Data Analytics Dashboard")
st.write("Interactive analysis using PostgreSQL + Streamlit")

# -------------------------
# DB connection
# -------------------------
engine = create_engine(
    "postgresql+psycopg2://postgres:Mitsubishi@localhost:5432/titanic_db"
)

# -------------------------
# Load full dataset
# -------------------------
df = pd.read_sql('SELECT * FROM titanic', engine)

# -------------------------
# Sidebar filters
# -------------------------
st.sidebar.header("Filters")

sex_filter = st.sidebar.multiselect(
    "Select Sex",
    options=df["Sex"].unique(),
    default=df["Sex"].unique()
)

class_filter = st.sidebar.multiselect(
    "Select Pclass",
    options=sorted(df["Pclass"].unique()),
    default=sorted(df["Pclass"].unique())
)

filtered_df = df[
    (df["Sex"].isin(sex_filter)) &
    (df["Pclass"].isin(class_filter))
]

# -------------------------
# KPIs
# -------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Passengers", len(filtered_df))
col2.metric("Survival Rate", f"{filtered_df['Survived'].mean():.2%}")
col3.metric("Average Fare", f"${filtered_df['Fare'].mean():.2f}")

# -------------------------
# Data table
# -------------------------
st.subheader("📊 Filtered Data")
st.dataframe(filtered_df)

# -------------------------
# Chart 1: Survival by Sex
# -------------------------
st.subheader("📈 Survival Rate by Sex")

chart_data = filtered_df.groupby("Sex")["Survived"].mean()
st.bar_chart(chart_data)

# -------------------------
# Chart 2: Survival by Class
# -------------------------
st.subheader("📊 Survival Rate by Class")

chart_data2 = filtered_df.groupby("Pclass")["Survived"].mean()
st.bar_chart(chart_data2)