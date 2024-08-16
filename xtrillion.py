import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import plotly.express as px
import requests
from credit_reports import create_country_report_tab
from report_utils import create_fund_report_tab

# Custom CSS for background and text colors (matching credit_reports.py)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1f1f1f;
        color: #ffffff;
        max-width: 2000px;
        margin: auto;
        padding-left: 4rem;
        padding-right: 4rem;
        display: flex;
        flex-direction: column;
        height: 100vh;
    }
    .reportColumn {
        width: 60% !important;
    }
    .chartColumn {
        width: 40% !important;
    }
    .data-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 12px;
        margin-top: 10px;
        margin-bottom: 30px;
    }
    .data-table th, .data-table td {
        border: 1px solid #ddd;
        padding: 4px;
        text-align: center;
    }
    .data-table th {
        background-color: #1f1f1f;
        color: white;
        width: 100px; /* Make year columns narrower */
    }
    .data-table td {
        color: black;
        background-color: white;
    }
    .reportText {
        word-wrap: break-word;
        white-space: normal;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Set up color palette (same as before)
color_palette = [
    "#FFA500",  # Bright Orange
    "#007FFF",  # Azure Blue
    "#DC143C",  # Cherry Red
    "#39FF14",  # Electric Lime Green
    "#00FFFF",  # Cyan
    "#DA70D6"   # Vivid Purple
]

# Define tabs for countries and funds
tabs = st.tabs(["Israel", "Qatar", "Mexico", "Saudi Arabia", "SKEWNBF", "SKESBF"])

# Country reports
with tabs[0]:
    create_country_report_tab("Israel", color_palette)

with tabs[1]:
    create_country_report_tab("Qatar", color_palette)

with tabs[2]:
    create_country_report_tab("Mexico", color_palette)

with tabs[3]:
    create_country_report_tab("Saudi Arabia", color_palette)

# Fund reports
with tabs[4]:
    create_fund_report_tab("Shin Kong Emerging Wealthy Nations Bond Fund", color_palette)

with tabs[5]:
    create_fund_report_tab("Shin Kong Environmental Sustainability Bond Fund", color_palette)
