import os
import gdown
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="IT5006 Phase 1 – Chicago Crime Dashboard",
    layout="wide"
)

# -----------------------------
# Light UI styling 
# -----------------------------
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1, h2, h3 {
        color: #1f2937;
    }
    .stSlider > div, .stSelectbox > div {
        background-color: #f9fafb;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #e5e7eb;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Title
# -----------------------------
st.title("📊 IT5006 Phase 1 – Chicago Crime Dashboard")
st.caption(
    "Interactive dashboard for exploring temporal and spatial crime patterns in Chicago."
)

# -----------------------------
# Load data (Google Drive)
# -----------------------------
FILE_ID = "1YV39W4t48fKWGfxO1GoMqjXznb98agvy"
CSV_PATH = "chicago_crime_dashboard.csv"
GDRIVE_URL = f"https://drive.google.com/uc?id={FILE_ID}"

@st.cache_data(show_spinner=True)
def load_data():
    if not os.path.exists(CSV_PATH):
        gdown.download(GDRIVE_URL, CSV_PATH, quiet=False)
    return pd.read_csv(CSV_PATH, encoding="utf-8-sig")

with st.spinner("Loading data, please wait..."):
    df = load_data()

st.success("Data loaded successfully!")

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.title("🔎 Filters")

min_year = int(df["Year"].min())
max_year = int(df["Year"].max())

year_range = st.sidebar.slider(
    "📅 Select Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

crime_types = sorted(df["Primary Type"].dropna().unique())
selected_crime = st.sidebar.selectbox(
    "🚓 Select Crime Type",
    ["All"] + crime_types
)

# -----------------------------
# Apply filters
# -----------------------------
filtered_df = df[
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1])
]

if selected_crime != "All":
    filtered_df = filtered_df[
        filtered_df["Primary Type"] == selected_crime
    ]

# -----------------------------
# Dataset overview
# -----------------------------
st.header("📁 Dataset Overview")

col1, col2 = st.columns(2)
with col1:
    st.metric("Selected Rows", filtered_df.shape[0])
with col2:
    st.metric("Selected Columns", filtered_df.shape[1])

st.subheader("Sample Records")
st.dataframe(filtered_df.head(), use_container_width=True)

# -----------------------------
# Temporal analysis
# -----------------------------
st.header("📈 Temporal Analysis")
st.caption("Crime trends over time based on selected filters")

yearly_counts = (
    filtered_df.groupby("Year")
    .size()
    .reset_index(name="Crime Count")
    .sort_values("Year")
)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(
    yearly_counts["Year"],
    yearly_counts["Crime Count"],
    marker="o"
)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Crimes")
ax.set_title("Total Crimes per Year")

st.pyplot(fig, use_container_width=False)

# -----------------------------
# Spatial distribution
# -----------------------------
st.header("🗺️ Spatial Distribution")
st.caption("Each point represents a reported crime location")

MAP_SAMPLE_SIZE = 50000
map_df = (
    filtered_df[["Latitude", "Longitude"]]
    .rename(columns={"Latitude": "lat", "Longitude": "lon"})
    .dropna()
)

if len(map_df) > MAP_SAMPLE_SIZE:
    map_df = map_df.sample(MAP_SAMPLE_SIZE, random_state=42)

st.map(map_df, zoom=10)

# -----------------------------
# Top 5 Crime Types (only when All)
# -----------------------------
if selected_crime == "All":
    st.header("🏷️ Top 5 Crime Types")
    st.caption("Most frequent crime categories under current filters")

    top_crimes = (
        filtered_df["Primary Type"]
        .value_counts()
        .head(5)
    )

    fig2, ax2 = plt.subplots(figsize=(7, 4))
    ax2.bar(top_crimes.index, top_crimes.values)
    ax2.set_ylabel("Number of Crimes")
    ax2.set_title("Top 5 Crime Types")
    ax2.tick_params(axis="x", rotation=30)

    st.pyplot(fig2, use_container_width=False)

# -----------------------------
# Footer note
# -----------------------------
st.info(
    f"""
This interactive dashboard explores **temporal and spatial crime patterns**
in Chicago from **{year_range[0]} to {year_range[1]}**.

Users can filter by **crime type** and **year range** to dynamically update
all visualizations.  
The analysis is intended for **exploratory purposes only**.
"""
)
