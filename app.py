import streamlit as st
import pandas as pd
import json
from summarizer import summarize

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="AI Company Intelligence & Investment Analyzer",
    page_icon="📊",
    layout="wide"
)

# ----------------------------------
# Sidebar
# ----------------------------------
st.sidebar.title("About")

st.sidebar.info(
    """
    AI Company Intelligence & Investment Analyzer

    Built with:
    - Python
    - Groq LLM
    - BeautifulSoup
    - Streamlit
    - Pandas

    Features:
    - Website Scraping
    - AI Company Analysis
    - Investment Scoring
    - Structured JSON Output
    - CSV Export
    - JSON Export
    """
)

# ----------------------------------
# Main Header
# ----------------------------------
st.title("📊 AI Company Intelligence & Investment Analyzer")

st.markdown("""
Analyze company websites using AI and automatically generate:

✅ Company Profile  
✅ Industry Analysis  
✅ Business Model  
✅ Target Customers  
✅ Revenue Streams  
✅ Competitive Advantages  
✅ Risks  
✅ Investment Perspective  
✅ Executive Summary  
✅ Investment Score
""")

# ----------------------------------
# URL Input
# ----------------------------------
url = st.text_input(
    "Enter Company Website",
    placeholder="stripe.com"
)

# ----------------------------------
# Analyze Button
# ----------------------------------
if st.button("🚀 Analyze Company"):

    if not url:
        st.warning("Please enter a company website.")
        st.stop()

    with st.spinner("Analyzing company..."):
        result = summarize(url)

    if "error" in result:
        st.error(result["error"])

    else:

        st.success("✅ Analysis Completed Successfully")

        # ----------------------------------
        # AI Investment Score
        # ----------------------------------
        score = 75

        if "high growth" in result["investment_perspective"].lower():
            score += 10

        if "competition" in result["risks"].lower():
            score -= 5

        if "ai" in result["competitive_advantages"].lower():
            score += 5

        st.metric(
            "📈 Investment Attractiveness Score",
            f"{score}/100"
        )

        # ----------------------------------
        # Download Files
        # ----------------------------------
        df = pd.DataFrame([result])

        csv_data = df.to_csv(index=False).encode("utf-8")

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                label="📥 Download CSV Report",
                data=csv_data,
                file_name=f"{result['company_name']}_analysis.csv",
                mime="text/csv"
            )

        with col2:
            st.download_button(
                label="📥 Download JSON Report",
                data=json.dumps(result, indent=4),
                file_name=f"{result['company_name']}_analysis.json",
                mime="application/json"
            )

        st.divider()

        # ----------------------------------
        # Company Overview
        # ----------------------------------
        st.subheader("🏢 Company Overview")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Company Name",
                result["company_name"]
            )

            st.write("### Industry")
            st.write(result["industry"])

            st.write("### Business Model")
            st.write(result["business_model"])

        with col2:

            st.write("### Target Customers")
            st.write(result["target_customers"])

            st.write("### Revenue Streams")
            st.write(result["revenue_streams"])

        st.divider()

        # ----------------------------------
        # Products & Services
        # ----------------------------------
        st.subheader("🛠 Products & Services")
        st.write(result["products_services"])

        # ----------------------------------
        # Competitive Advantages
        # ----------------------------------
        st.subheader("🏆 Competitive Advantages")
        st.write(result["competitive_advantages"])

        # ----------------------------------
        # Risks
        # ----------------------------------
        st.subheader("⚠ Risks")
        st.write(result["risks"])

        # ----------------------------------
        # Investment Perspective
        # ----------------------------------
        st.subheader("📈 Investment Perspective")
        st.write(result["investment_perspective"])

        # ----------------------------------
        # Executive Summary
        # ----------------------------------
        st.subheader("📋 Executive Summary")
        st.write(result["executive_summary"])

        st.divider()

        # ----------------------------------
        # Raw JSON
        # ----------------------------------
        with st.expander("🔍 View Raw JSON Output"):
            st.json(result)