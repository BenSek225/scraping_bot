# scraping_bot/config.py
# Fichier de configuration pour centraliser les paramètres

# URL du site à scraper (site de test public)
SCRAPING_URL = "https://books.toscrape.com/"

# Chemin où sauvegarder les fichiers Excel
EXCEL_OUTPUT_PATH = "data/livres.xlsx"

# Chemin vers ChromeDriver
CHROMEDRIVER_PATH = "drivers/chromedriver.exe"

# Paramètres email
EMAIL_SENDER = "ton.email@gmail.com"  # Remplace par ton email
EMAIL_PASSWORD = "ton_mot_de_passe_app"  # Mot de passe d’application Gmail (voir plus bas)
EMAIL_RECEIVER = "destinataire@example.com"  # Où envoyer l’email
SMTP_SERVER = "smtp.gmail.com"  # Serveur Gmail
SMTP_PORT = 587  # Port pour TLS