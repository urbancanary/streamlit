import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# Custom color palette
color_palette = [
    "#FFA500",  # Bright Orange
    "#007FFF",  # Azure Blue
    "#DC143C",  # Cherry Red
    "#39FF14",  # Electric Lime Green
    "#00FFFF",  # Cyan
    "#DA70D6"   # Vivid Purple
]

# Apply custom CSS for consistent styling across the app
def apply_custom_css():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #1f1f1f;
        }
        .reportColumn, .chartColumn {
            background-color: #1f1f1f;
            color: #f5f5f5;
        }
        .reportColumn h3, .reportColumn p, .reportColumn th, .reportColumn td {
            color: #f5f5f5;
        }
        .data-table th {
            color: white;
            background-color: #000000;  /* Black background for table header */
        }
        .data-table td {
            color: #1f1f1f;
            background-color: #f5f5f5;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to fetch country data from the API and create a country report tab
def create_country_report_tab(entity_name, color_palette, db_name="credit_research.db", table_name="FullReport"):
    apply_custom_css()
    st.write(f"### {entity_name} Report")
    url = "https://my-combined-app-vpljqiia2a-uc.a.run.app/process_json"
    payload = {
        "sample_key": f'{{"db_path": "{db_name}", "table": "{table_name}", "filters": {{"Country": "{entity_name}"}}, "fields": "*", "page": 1, "page_size": 10}}'
    }

    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            report = data[0]

            col1, col2 = st.columns([6, 4])

            with col1:
                st.markdown('<div class="reportColumn">', unsafe_allow_html=True)
                st.markdown(f'<h1 class="reportText">{report.get("Title", "Credit Research Report")}</h1>', unsafe_allow_html=True)
                st.markdown('<h2 class="reportText">Country Information</h2>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText"><strong>Country:</strong> {report.get("Country", "N/A")}</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText"><strong>Ownership:</strong> {report.get("Ownership", "N/A")}</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText"><strong>NFA Rating:</strong> {report.get("NFARating", "N/A")}</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText"><strong>ESG Rating:</strong> {report.get("ESGRating", "N/A")}</p>', unsafe_allow_html=True)
                st.markdown('<h2 class="reportText">Overview</h2>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText">{report.get("Overview", "No overview available.")}</p>', unsafe_allow_html=True)
                st.markdown('<h2 class="reportText">Politics</h2>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText">{report.get("PoliticalNews", "No political news available.")}</p>', unsafe_allow_html=True)
                st.markdown('<h2 class="reportText">Strengths</h2>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText">{report.get("Strengths", "No strengths information available.")}</p>', unsafe_allow_html=True)
                st.markdown('<h2 class="reportText">Weaknesses</h2>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText">{report.get("Weaknesses", "No weaknesses information available.")}</p>', unsafe_allow_html=True)
                st.markdown('<h2 class="reportText">Opportunities</h2>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText">{report.get("Opportunities", "No opportunities information available.")}</p>', unsafe_allow_html=True)
                st.markdown('<h2 class="reportText">Threats</h2>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText">{report.get("Threats", "No threats information available.")}</p>', unsafe_allow_html=True)
                st.markdown('<h2 class="reportText">Recent News</h2>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText">{report.get("RecentNews", "No recent news available.")}</p>', unsafe_allow_html=True)
                st.markdown('<h2 class="reportText">Ratings and Comments from Credit Rating Agencies</h2>', unsafe_allow_html=True)
                st.markdown('<h3 class="reportText">Moody\'s:</h3>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText">{report.get("MoodysRating", "N/A")}</p>', unsafe_allow_html=True)
                st.markdown('<h3 class="reportText">S&P Global Ratings:</h3>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText">{report.get("SPGlobalRating", "N/A")}</p>', unsafe_allow_html=True)
                st.markdown('<h3 class="reportText">Fitch Ratings:</h3>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText">{report.get("FitchRating", "N/A")}</p>', unsafe_allow_html=True)
                st.markdown('<h2 class="reportText">Conclusion</h2>', unsafe_allow_html=True)
                st.markdown(f'<p class="reportText">{report.get("Conclusion", "No conclusion available.")}</p>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="chartColumn">', unsafe_allow_html=True)
                st.header("Economic Data (2024 Onwards)")

                charts_data = [
                    ("GDP Growth (%)", [report.get(f'GDPGrowthRateYear{i}', 0) for i in range(1, 7)], color_palette[0]),
                    ("Inflation Rate (%)", [report.get(f'InflationYear{i}', 0) for i in range(1, 7)], color_palette[1]),
                    ("Unemployment Rate (%)", [report.get(f'UnemploymentRateYear{i}', 0) for i in range(1, 7)], color_palette[2]),
                    ("Population (millions)", [report.get(f'PopulationYear{i}', 0) for i in range(1, 7)], color_palette[3]),
                    ("Government Budget Balance (% of GDP)", [report.get(f'GovernmentFinancesYear{i}', 0) for i in range(1, 7)], color_palette[4]),
                    ("Current Account Balance (% of GDP)", [report.get(f'CurrentAccountBalanceYear{i}', 0) for i in range(1, 7)], color_palette[5])
                ]

                years = [2024, 2025, 2026, 2027, 2028, 2029]

                for metric, values, color in charts_data:
                    df = pd.DataFrame({
                        "Year": years,
                        metric: values
                    })

                    st.plotly_chart(plot_chart(df, metric, metric, color), use_container_width=True)
                    st.markdown(create_data_table(df, metric), unsafe_allow_html=True)

                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error(f"No data found for {entity_name}.")
    else:
        st.error(f"Failed to fetch data for {entity_name}. Status code: {response.status_code}")

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

def filter_dataframe(df: pd.DataFrame, identifier: str = "", filter_columns: list = None) -> pd.DataFrame:
    if filter_columns is None:
        filter_columns = []

    filtered_df = df.copy()

    for idx, col in enumerate(filter_columns):
        if col not in df.columns:
            continue

        unique_values = sorted(df[col].dropna().astype(str).unique())

        if pd.api.types.is_numeric_dtype(df[col]):
            numeric_values = df[col].dropna()
            default_value = [float(numeric_values.min()), float(numeric_values.max())]
            selected_values = st.slider(
                f"Filter {col} ({identifier})",
                min_value=default_value[0],
                max_value=default_value[1],
                value=default_value,
                step=(default_value[1] - default_value[0]) / 100,
                key=f"filter_{col}_{identifier}_{idx}"
            )
            filtered_df = filtered_df[
                (filtered_df[col] >= selected_values[0]) &
                (filtered_df[col] <= selected_values[1])
            ]
        else:
            selected_values = st.multiselect(
                f"Filter {col} ({identifier})",
                options=unique_values,
                default=unique_values,
                key=f"filter_{col}_{identifier}_{idx}"
            )
            filtered_df = filtered_df[filtered_df[col].astype(str).isin(selected_values)]

    return filtered_df


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

        # Apply the filters to the table data
        filtered_data = filter_dataframe(fund_data)

        # Display the filtered DataFrame
        st.write(filtered_data)

# Function to create the fund report tab
def create_fund_report_tab(fund_name, color_palette):
    apply_custom_css()
    st.write(f"### {fund_name} Fund Report")
    fund_data = fetch_fund_data(fund_name)
    
    if fund_data is not None:
        create_pie_charts_and_table(fund_data)
    else:
        st.error(f"No data found for {fund_name}.")

# Function to plot charts (for both country and fund reports)
def plot_chart(df, y_column, title, color):
    fig = px.bar(df, x='Year', y=y_column,
                 title=title,
                 color_discrete_sequence=[color],
                 height=375)
    fig.update_layout(
        plot_bgcolor='#1f1f1f', 
        paper_bgcolor='#1f1f1f',
        font=dict(color='white'),
        margin=dict(l=20, r=20, t=60, b=40)
    )
    return fig

# Function to create data tables
def create_data_table(df, y_column):
    table_html = "<table class='data-table'>"
    table_html += "<tr><th style='width: 80px;'>Year</th>" + "".join([f"<th>{year}</th>" for year in df['Year']]) + "</tr>"
    table_html += f"<tr><td>{y_column}</td>"
    for value in df[y_column]:
        if value is not None:
            table_html += f"<td>{value:.2f}</td>"  # Format as a float with 2 decimal places
        else:
            table_html += "<td>N/A</td>"  # Use "N/A" for None values
    table_html += "</tr></table>"
    return table_html

# The code is now organized into separate functions, and duplications have been removed.
# You can call create_country_report_tab() or create_fund_report_tab() in your main app to generate the reports.
