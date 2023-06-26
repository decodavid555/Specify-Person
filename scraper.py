import requests
from bs4 import BeautifulSoup
from google.cloud import translate_v2 as translate
 
from googletrans import Translator

# defining the urls of the news websites
urls = [
    "https://thehill.com/",
    "https://jacobin.com/",
     "https://www.cnn.com",
    "https://www.bbc.com",
    "https://www.nytimes.com",
    "https://www.aljazeera.com",
    "www.nationalreview.com",
    "www.politico.com/",
    "https://www.axios.com/",
    "https://www.theguardian.com/",
    "https://www.cbsnews.com/",
    "www.rtl.fr/",
    "www.valeursactuelles.com",
    "www.ladn.eu",
    "https://lincorrect.org/",
    "https://fr.news.yahoo.com/",
    "www.leprogres.fr",
    "www.purepeople.com",
    "www.lejdd.fr/",
    "www.gala.fr",
    "https://lesalonbeige.fr/",
    "https://marionmarechal.info/",
]

# Define the keywords to filter the articles
keywords = ["Marion Marechal", "Princess Kako of Akishino", "Alexandria Ocasio Cortez"]

# Replace with your service account key file path
service_account_key_path = "/path/to/your/service_account_key.json"
# Define the Google Translate API key
api_key = ""
# Initialize the Translator object
translator = Translator(service_urls=['translate.google.com'], credentials=api_key)
# Translate a text from French to English
text = "Bonjour, comment ça va?"
translated_text = translator.translate(text, src='fr', dest='en')
print(translated_text.text)

# Loop through the URLs and fetch the HTML content
for url in urls:
    print(f"Scraping URL: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the article titles and URLs
    articles = []
    for title in soup.find_all("h2"):
        if any(keyword in title.text for keyword in keywords):
            article = {}
            article["title"] = title.text.strip()
            article["url"] = title.find("a").get("href")
            articles.append(article)

    # Print the articles
for article in articles:
    print(article["title"])
    print(article["url"])

    # Translate the articles
    for article in articles:
        # Fetch the HTML content of the article
        response = requests.get(article["url"])
        soup = BeautifulSoup(response.content, "html.parser")
        # Extract the article text
        article_text = ""
        for paragraph in soup.find_all("p"):
            article_text += paragraph.text + "\n"
        # Translate the article text
        translation = translator.translate(article_text, src='auto', dest='en')
        article["text"] = translation.text

        print(article["text"])
    # Store the articles in a database or a file
