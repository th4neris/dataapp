import requests
url = "https://github.com/search?q=mental+health+ai&type=repositories"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,ar-MA;q=0.6,ar;q=0.5,ru-RU;q=0.4,ru;q=0.3,es-US;q=0.2,es;q=0.1",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}
response = requests.get(url, headers=headers)
with open("response.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print(response)