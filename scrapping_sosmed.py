# Cek status koneksi dan isi mentah website menggunakan requests
import requests

res = requests.get('https://www.detik.com/terpopuler')
print(res.status_code)
print(res.content)

# Membaca isi website menggunakan urllib bawaan python
from urllib.request import urlopen
html = urlopen('https://www.detik.com/terpopuler')
content = html.read()
print(content)

# Mengambil judul halaman website menggunakan BeautifulSoup
import requests
from bs4 import BeautifulSoup

url = "https://www.detik.com/terpopuler"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title

print(title)

# Melakukan proses scraping data dan menyimpannya ke file CSV menggunakan pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.detik.com/terpopuler"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("li")

data = []

for item in titles:
    data.append(item.get_text(strip=True))

print(data)

df = pd.DataFrame(data, columns=["title"])
df.to_csv("detik.csv", index=False)
