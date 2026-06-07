import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from scraper import fetch_website_contents
from save_to_csv import save_company

# Load environment variables
load_dotenv()

# Groq Client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

SYSTEM_PROMPT = """
You are a senior business analyst.

Analyze the company website and return ONLY valid JSON.

{
    "company_name":"",
    "industry":"",
    "business_model":"",
    "target_customers":"",
    "products_services":"",
    "revenue_streams":"",
    "competitive_advantages":"",
    "risks":"",
    "investment_perspective":"",
    "executive_summary":""
}

Return valid JSON only.
Do not use markdown.
Do not add explanations before or after the JSON.
"""

def summarize(url):
    try:
        website_content = fetch_website_contents(url)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": website_content
                }
            ],
            temperature=0.2
        )

        result = response.choices[0].message.content

        # Convert JSON string to Python dictionary
        company_data = json.loads(result)

        return company_data

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":

    url = input("Enter Website URL: ").strip()

    result = summarize(url)

    if "error" not in result:
        print("DEBUG: Calling save_company()")
        save_company(result)

    print("\n" + "=" * 60)
    print("COMPANY INTELLIGENCE REPORT")
    print("=" * 60)

    print("\nData Type:")
    print(type(result))

    print("\nFull Result:")
    print(result)

    if "error" not in result:
        print("\nCompany Name:", result["company_name"])
        print("Industry:", result["industry"])
