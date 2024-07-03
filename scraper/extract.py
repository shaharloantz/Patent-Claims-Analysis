import requests
from scraper.parser import parse_claims


def get_patent_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def extract_claims(url):
    page_content = get_patent_page(url)
    return parse_claims(page_content)


def get_claims_from_urls(urls):
    all_claims = []
    for url in urls:
        claims = extract_claims(url)
        all_claims.extend(claims)
    return all_claims
