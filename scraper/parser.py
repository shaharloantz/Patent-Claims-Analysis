from bs4 import BeautifulSoup


def parse_claims(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    claims_section = soup.find("section", {"itemprop": "claims"})
    claims = []

    if claims_section:
        claims_list = claims_section.find_all("div", {"class": "claim-text"})
        for claim in claims_list:
            claims.append(claim.get_text(strip=True))
    else:
        print("Claims section not found.")

    return claims
