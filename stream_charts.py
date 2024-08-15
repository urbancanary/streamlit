import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(layout="wide")

# Custom color palette
color_palette = [
    "#FFA500",  # Bright Orange
    "#007FFF",  # Azure Blue
    "#DC143C",  # Cherry Red
    "#39FF14",  # Electric Lime Green
    "#00FFFF",  # Cyan
    "#DA70D6"   # Vivid Purple
]

# Function to fetch fund data from the API
def fetch_fund_data(fund_name):
    url = "https://my-combined-app-vpljqiia2a-uc.a.run.app/process_json"
    payload = {
        "sample_key": f'{{"db_path": "consolidated.db", "table": "fund_holdings", "filters": {{"fund_name": "{fund_name}"}}, "fields": "*", "page": 1, "page_size": 100}}'
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        st.error(f"Failed to fetch data for {fund_name}. Status code: {response.status_code}")
        return None

# Function to create pie charts and filter the data table
def create_pie_charts_and_table(fund_data):
    if fund_data is not None:
        # Add "Cash" for missing NFA ratings and create the NFA pie chart
        fund_data['nfa_star_rating'] = fund_data['nfa_star_rating'].fillna('Cash')
        fig_nfa = px.pie(fund_data, names='nfa_star_rating', values='weighting', title="NFA Star Rating Distribution",
                         color_discrete_sequence=color_palette, hole=0.4)
        fig_nfa.update_traces(textinfo='percent+label')
        fig_nfa.update_layout(paper_bgcolor='#1f1f1f', plot_bgcolor='#1f1f1f', font=dict(color='white'), height=500, width=500, 
                              transition_duration=500)

        # Add "Cash" for missing ESG ratings and create the ESG pie chart
        fund_data['esg_country_star_rating'] = fund_data['esg_country_star_rating'].fillna('Cash')
        fig_esg = px.pie(fund_data, names='esg_country_star_rating', values='weighting', title="ESG Country Star Rating Distribution",
                         color_discrete_sequence=color_palette, hole=0.4)
        fig_esg.update_traces(textinfo='percent+label')
        fig_esg.update_layout(paper_bgcolor='#1f1f1f', plot_bgcolor='#1f1f1f', font=dict(color='white'), height=500, width=500, 
                              transition_duration=500)

        # Create a chart for ESG ratings with a rating of 6 or more
        fund_data['esg_6_or_more'] = fund_data['esg_country_star_rating'].apply(
            lambda x: 'ESG >= 6' if isinstance(x, (int, float)) and x >= 6 else 'ESG < 6 or Cash'
        )
        fig_esg_6 = px.pie(fund_data, names='esg_6_or_more', values='weighting', title="ESG Ratings 6 or More",
                           color_discrete_sequence=color_palette, hole=0.4)
        fig_esg_6.update_traces(textinfo='percent+label')
        fig_esg_6.update_layout(paper_bgcolor='#1f1f1f', plot_bgcolor='#1f1f1f', font=dict(color='white'), height=500, width=500, 
                                transition_duration=500)

        # Create a Region pie chart
        fig_region = px.pie(fund_data, names='region', values='weighting', title="Region Distribution",
                            color_discrete_sequence=color_palette, hole=0.4)
        fig_region.update_traces(textinfo='percent+label')
        fig_region.update_layout(paper_bgcolor='#1f1f1f', plot_bgcolor='#1f1f1f', font=dict(color='white'), height=500, width=500, 
                                 transition_duration=500)

        # Create two rows for the charts
        col1, col2 = st.columns([1, 1])
        with col1:
            st.plotly_chart(fig_region, use_container_width=True)
        with col2:
            st.plotly_chart(fig_nfa, use_container_width=True)

        col3, col4 = st.columns([1, 1])
        with col3:
            st.plotly_chart(fig_esg, use_container_width=True)
        with col4:
            st.plotly_chart(fig_esg_6, use_container_width=True)

        # Add "All" to the dropdown and filter table by clicking on the pie chart region
        regions = ["All"] + fund_data['region'].unique().tolist()
        selected_region = st.selectbox("Filter by Region", options=regions)

        if selected_region != "All":
            filtered_data = fund_data[fund_data['region'] == selected_region]
        else:
            filtered_data = fund_data

        st.write(filtered_data)

# Main section
st.title("Shin Kong Emerging Wealthy Nations Bond Fund Overview")
fund_name = "Shin Kong Emerging Wealthy Nations Bond Fund"
fund_data = fetch_fund_data(fund_name)

if fund_data is not None:
    create_pie_charts_and_table(fund_data)
else:
    st.error("No data available for the selected fund.")










