import requests
from bs4 import BeautifulSoup

# Lista de pagini web de căutat (exemplu)
urls = [
    "https://example.com",
    "https://anotherexample.com"
]

query = "Gras Videochat"
found_videos = []

def search_videos(url, query):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            if query.lower() in link.text.lower():
                found_videos.append((url, link['href']))
    except Exception as e:
        print(f"Error searching {url}: {e}")

for url in urls:
    search_videos(url, query)

# Generare raport
with open("report.txt", "w") as f:
    if found_videos:
        f.write("Videoclipuri găsite:\n")
        for url, video in found_videos:
            f.write(f"{url}: {video}\n")
    else:
        f.write("Nu au fost găsite videoclipuri.")

print("Raportul a fost generat.")
