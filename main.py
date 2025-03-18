# scraping_bot/main.py
# Script principal qui orchestre le bot

import openpyxl
from scripts.scraper import scrape_books
from scripts.automation import search_amazon
from scripts.email_sender import send_email
from config import SCRAPING_URL, EXCEL_OUTPUT_PATH, CHROMEDRIVER_PATH, EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, SMTP_SERVER, SMTP_PORT

def main():
    """Exécute le bot : scraping, sauvegarde, et envoi par email."""
    # Étape 1 : Scraper les livres
    print("Début du scraping...")
    book_data = scrape_books(SCRAPING_URL)

    # Étape 2 : Sauvegarder dans Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Livres"
    sheet.append(["Titre", "Prix"])  # En-têtes
    for book in book_data:
        sheet.append(book)
    workbook.save(EXCEL_OUTPUT_PATH)
    print(f"Fichier Excel sauvegardé : {EXCEL_OUTPUT_PATH}")

    # Étape 3 : Scraper un prix sur Amazon avec Selenium
    amazon_price = search_amazon("python book", CHROMEDRIVER_PATH)
    print(f"Prix d’un livre Python sur Amazon : {amazon_price}€")

    # Étape 4 : Envoyer l’email
    subject = "Rapport des livres scrapés"
    body = f"Voici le rapport des livres + un prix Amazon : {amazon_price}€"
    send_email(
        EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, SMTP_SERVER, SMTP_PORT,
        subject, body, EXCEL_OUTPUT_PATH
    )

if __name__ == "__main__":
    main()