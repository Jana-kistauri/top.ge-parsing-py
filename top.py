import requests
from bs4 import BeautifulSoup

r = requests.get("https://top.ge")
c = r.text

soup = BeautifulSoup(c, "html.parser")

data = soup.find("tbody")

rows = data.find_all("tr")

for index, item in enumerate(rows, 1):

	print(f'{index}. {item.find_all("td")[2].find_all("a")[0].text}')
	print(item.find_all("td")[2].find_all("a")[1].text.strip())
	print(item.find_all("td")[4].text)
	print(item.find_all("td")[-3].text.strip())
	print("\n")