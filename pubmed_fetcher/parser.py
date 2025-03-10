from lxml import etree
from typing import List, Dict

COMPANY_KEYWORDS = ["pharma", "biotech", "inc", "ltd", "corp"]

def parse_papers(xml_data: str) -> List[Dict]:
    """Extract details from PubMed XML response."""
    tree = etree.fromstring(xml_data.encode())
    papers = []
    
    for article in tree.xpath("//PubmedArticle"):
        pubmed_id = article.xpath(".//PMID/text()")[0]
        title = article.xpath(".//ArticleTitle/text()")[0]
        pub_date = article.xpath(".//PubDate/Year/text()")
        publication_date = pub_date[0] if pub_date else "Unknown"

        authors = article.xpath(".//Author")
        non_academic_authors = []
        company_affiliations = []
        corresponding_email = "N/A"

        for author in authors:
            affiliation = "".join(author.xpath(".//Affiliation/text()"))
            if any(keyword in affiliation.lower() for keyword in COMPANY_KEYWORDS):
                non_academic_authors.append(" ".join(author.xpath(".//ForeName/text()") + author.xpath(".//LastName/text()")))
                company_affiliations.append(affiliation)

            email = author.xpath(".//ElectronicAddress/text()")
            if email:
                corresponding_email = email[0]

        papers.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": publication_date,
            "Non-academic Author(s)": ", ".join(non_academic_authors) or "N/A",
            "Company Affiliation(s)": ", ".join(company_affiliations) or "N/A",
            "Corresponding Author Email": corresponding_email
        })

    return papers
