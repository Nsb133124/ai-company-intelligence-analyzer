<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

def fetch_website_contents(url):

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=15
        )

        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        return f"Could not fetch website. Error: {e}"

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "No title"

    for tag in soup([
        "script",
        "style",
        "nav",
        "footer",
        "header",
        "img",
        "input",
        "button",
        "form",
        "aside",
        "noscript",
        "svg"
    ]):
        tag.decompose()

    text = soup.get_text(
        separator="\n",
        strip=True
    )

    # Prevent huge prompts
    MAX_CHARS = 10000
    text = text[:MAX_CHARS]

    return f"""
Title: {title}

Page Contents:

{text}
"""
=======

>>>>>>> 5ac3a9ee14b66c36c83502ac4795be12fb8280eb
