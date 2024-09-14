import requests
import bs4
import json

cve_id = "CVE-2017-0144"

response = requests.get("https://nvd.nist.gov/vuln/detail/"+cve_id)

soup = bs4.BeautifulSoup(response.text,"html.parser")
desc = soup.find_all("p",{"data-testid":"vuln-description"})
print(type(desc))
