# AI Company Intelligence Analyzer

## Overview

AI Company Intelligence Analyzer is a Python-based application that automatically extracts and analyzes business intelligence from company websites using Large Language Models (LLMs).

The application scrapes website content, processes it using Groq's Llama 3.3 70B model, and generates structured business insights including company profile, business model, revenue streams, competitive advantages, risks, and investment perspective.

---

## Features

* Website Content Extraction using BeautifulSoup
* AI-Powered Company Analysis using Groq LLM
* Structured JSON Output
* CSV Database Storage
* Automated Company Intelligence Generation
* Business Model Analysis
* Revenue Stream Identification
* Competitive Advantage Assessment
* Investment Perspective Generation

---

## Tech Stack

* Python
* Groq API
* OpenAI SDK
* BeautifulSoup
* Requests
* Pandas
* JSON
* CSV Storage

---

## Project Workflow

Company Website URL

↓

Website Scraping

↓

Content Cleaning

↓

Groq Llama 3.3 70B

↓

Structured JSON Extraction

↓

CSV Database Storage

---

## Example Output

```json
{
  "company_name": "Stripe",
  "industry": "Financial Technology",
  "business_model": "Payment Processing and Financial Services",
  "target_customers": "Businesses of all sizes",
  "revenue_streams": "Transaction fees and financial services"
}
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Nsb133124/ai-company-intelligence-analyzer.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
python summarizer.py
```

---

## Future Enhancements

* Streamlit Dashboard
* Excel Export
* Multi-Company Comparison
* Tableau Dashboard
* Power BI Integration
* Financial Ratio Analysis
* Company Scoring Framework

---

## Author

Nagaraj Badiger

Finance Specialist | Data Analytics | AI & ML Enthusiast
