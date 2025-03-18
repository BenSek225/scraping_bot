# scraping_bot/scripts/scraper.py
# Module pour scraper les données avec BeautifulSoup

import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    """
    Scrape les titres et prix des livres depuis une URL donnée.
    Retourne une liste de listes : [[titre, prix], ...]
    """
    # Télécharge la page web
    response = requests.get(url)
    response.raise_for_status()  # Lève une erreur si la requête échoue (ex. 404)

    # Analyse le HTML avec BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Trouve tous les livres (balises <article class="product_pod">)
    books = soup.find_all("article", class_="product_pod")

    # Liste pour stocker les données
    book_data = []

    # Extrait titre et prix pour chaque livre
    for book in books:
        title = book.h3.a["title"]  # Titre dans l’attribut "title" de <a> dans <h3>
        price = book.find("p", class_="price_color").text  # Prix dans <p class="price_color">
        book_data.append([title, price])

    return book_data

# Test rapide si exécuté directement
if __name__ == "__main__":
    from config import SCRAPING_URL
    books = scrape_books(SCRAPING_URL)
    for book in books:
        print(f"Titre : {book[0]}, Prix : {book[1]}")