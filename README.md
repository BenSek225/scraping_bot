# Bot de Scraping Web & Automatisation

Ce projet est un bot Python qui automatise la récupération de données sur le web, leur stockage dans un fichier Excel, et leur envoi par email. Il utilise des outils comme **BeautifulSoup**, **Selenium**, **OpenPyXL**, et **smtplib** pour scraper des sites statiques et dynamiques, générer des rapports, et partager les résultats automatiquement.

---

## 🎯 Fonctionnalités actuelles

Le bot exécute ces tâches en une seule commande (`python main.py`) :

1. **Scraping statique avec BeautifulSoup** :
   - **Quoi** : Récupère les **titres** et **prix** des livres sur [books.toscrape.com](https://books.toscrape.com/).
   - **Comment** : Utilise `requests` pour télécharger la page HTML, puis `BeautifulSoup` pour extraire les données via des sélecteurs HTML (ex. `<article class="product_pod">`).
   - **Exemple** : "A Light in the Attic, £51.77".
   - **Fichier** : `scripts/scraper.py`.

2. **Sauvegarde dans Excel avec OpenPyXL** :
   - **Quoi** : Crée un fichier `data/livres.xlsx` avec deux colonnes : "Titre" et "Prix".
   - **Comment** : `openpyxl` génère un classeur, ajoute une ligne d’en-tête, puis insère chaque livre extrait.
   - **Résultat** : Un tableau clair dans `data/`.
   - **Fichier** : `main.py`.

3. **Scraping dynamique avec Selenium** :
   - **Quoi** : Recherche "python book" sur Amazon.fr et extrait le prix du premier résultat (ex. "41€").
   - **Comment** : Ouvre Chrome en mode silencieux (headless) via `selenium`, simule une recherche dans la barre de recherche (ID `twotabsearchtextbox`), et récupère le prix (classe `a-price-whole`).
   - **Fichier** : `scripts/automation.py`.

4. **Envoi d’email avec smtplib** :
   - **Quoi** : Envoie `livres.xlsx` par email avec un message incluant le prix Amazon.
   - **Comment** : Utilise `smtplib` pour se connecter à Gmail (via SMTP), et `email.mime` pour joindre le fichier et formater le message.
   - **Fichier** : `scripts/email_sender.py`.

### Exemple de logs après exécution :
```
Début du scraping...
Fichier Excel sauvegardé : data/livres.xlsx
Prix d’un livre Python sur Amazon : 41€
Email envoyé avec succès !
```

---

## 🛠️ Structure du projet
```
📂 scraping_bot
├── 📂 venv               # Environnement virtuel
├── 📂 data               # Fichiers Excel générés (ex. livres.xlsx)
├── 📂 drivers            # ChromeDriver pour Selenium
├── 📂 scripts            # Modules spécifiques
│   ├── 📄 scraper.py     # Scraping statique avec BeautifulSoup
│   ├── 📄 automation.py  # Automatisation dynamique avec Selenium
│   └── 📄 email_sender.py # Envoi d’emails avec smtplib
├── 📄 main.py            # Script principal qui orchestre tout
├── 📄 config.py          # Configuration (URLs, emails, chemins)
├── 📄 requirements.txt   # Dépendances
├── 📄 README.md          # Ce fichier
```

---

## 📋 Prérequis

- **Python 3.12** : [python.org/downloads](https://www.python.org/downloads/), coche "Add Python to PATH" lors de l’installation.
- **Google Chrome** : Installé sur ton PC (vérifie la version via Menu > Aide > À propos).
- **ChromeDriver** :
  - Compatible avec ta version de Chrome (ex. 134.x).
  - Télécharge depuis [googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/) :
    1. Va dans "Stable" ou "Known Good Versions".
    2. Trouve la version correspondant à Chrome (ex. 134.x).
    3. Télécharge `chromedriver-win32.zip`, extrais `chromedriver.exe`, et place-le dans `drivers/`.
- **Compte Gmail** : Crée un mot de passe d’application via "Gérer votre compte Google" > "Sécurité" > "Mot de passe d’application".

---

## 🚀 Installation

1. **Crée la structure** :
   ```powershell
   cd C:\Users\ASUS\Desktop\
   mkdir scraping_bot
   cd scraping_bot
   mkdir venv data drivers scripts
   ```

2. **Crée et active l’environnement virtuel** :
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Installe les dépendances** :
   - Édite `requirements.txt` :
     ```
     requests==2.32.3
     beautifulsoup4==4.12.3
     selenium==4.25.0
     openpyxl==3.1.5
     ```
   - Puis :
     ```powershell
     pip install -r requirements.txt
     ```

4. **Configure `config.py`** :
   - Mets à jour :
     - `EMAIL_SENDER` : Ton adresse Gmail.
     - `EMAIL_PASSWORD` : Ton mot de passe d’application.
     - `EMAIL_RECEIVER` : L’adresse de destination.
     - `CHROMEDRIVER_PATH` : `"drivers/chromedriver.exe"`.

5. **Ajoute ChromeDriver** :
   - Place `chromedriver.exe` dans `drivers/` (voir Prérequis).

---

## ▶️ Utilisation

- Lance le bot :
  ```powershell
  python main.py
  ```
- Résultats :
  - `data/livres.xlsx` contient les données scrapées.
  - Un email arrive avec le fichier et le prix Amazon.

---

## 🌟 Options d’amélioration

1. **Scraper plus de pages** :
   - **Ajout** : Boucle dans `scraper.py` pour scraper plusieurs pages :
     ```python
     def scrape_books(url, max_pages=3):
         book_data = []
         for page in range(1, max_pages + 1):
             page_url = f"{url}catalogue/page-{page}.html"  # Pages paginées
             response = requests.get(page_url)
             soup = BeautifulSoup(response.text, "html.parser")
             books = soup.find_all("article", class_="product_pod")
             for book in books:
                 title = book.h3.a["title"]
                 price = book.find("p", class_="price_color").text
                 book_data.append([title, price])
         return book_data
     ```
   - **Effet** : Plus de livres dans `livres.xlsx`.

2. **Planification automatique** :
   - **Ajout** : Utilise `schedule` (`pip install schedule`) :
     ```python
     import schedule
     import time
     def job():
         main()
     schedule.every().day.at("08:00").do(job)
     while True:
         schedule.run_pending()
         time.sleep(60)
     ```
   - **Effet** : Exécution quotidienne automatique.

3. **Surveiller les prix** :
   - **Ajout** : Boucle dans `automation.py` pour plusieurs produits :
     ```python
     def monitor_prices(products, driver_path):
         prices = {}
         driver = webdriver.Chrome(service=Service(driver_path), options=Options())
         for product in products:
             driver.get("https://www.amazon.fr")
             search_box = driver.find_element(By.ID, "twotabsearchtextbox")
             search_box.send_keys(product)
             search_box.submit()
             driver.implicitly_wait(2)
             price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
             prices[product] = price
         driver.quit()
         return prices
     ```
   - **Effet** : Suivi multi-produits.

4. **Interface graphique** :
   - **Ajout** : Utilise `tkinter` pour une fenêtre de saisie.
   - **Effet** : Contrôle convivial sans terminal.

5. **Plus de sites** :
   - **Ajout** : Nouvelles fonctions dans `scraper.py` ou `automation.py` avec des sélecteurs adaptés.
   - **Effet** : Scraping multi-sources.

---

## 🚀 Potentiel avec modifications

- **Tracker de prix** : Alerte si un prix baisse sous un seuil.
- **Agrégateur** : Compile données de multiples sites (ex. avis, stats).
- **Assistant e-commerce** : Remplit des formulaires d’achat.
- **Rapports avancés** : Ajoute des graphiques avec `matplotlib`.

---

## 🛠️ Dépannage

- **ChromeDriver incompatible** :
  - Vérifie ta version Chrome (Menu > Aide > À propos) et télécharge le ChromeDriver correspondant.
- **Email ne part pas** :
  - Vérifie `EMAIL_PASSWORD` (doit être un mot de passe d’application).
- **Amazon bloque Selenium** :
  - Désactive `--headless` dans `automation.py` :
    ```python
    chrome_options = Options()  # Sans add_argument("--headless")
    ```

---

## 🎉 Conclusion

Ce bot est une introduction solide à l’automatisation et au scraping web. Il montre comment combiner des outils Python pour des tâches pratiques. Avec les améliorations proposées, il peut devenir un assistant personnalisé ou un outil professionnel. Explore, modifie, et fais-en ce que tu veux !
