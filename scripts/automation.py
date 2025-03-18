# scraping_bot/scripts/automation.py
# Module pour automatiser des actions avec Selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def search_amazon(query, driver_path):
    """
    Utilise Selenium pour chercher un produit sur Amazon et retourne le premier prix.
    """
    # Configure les options de Chrome (headless = sans fenêtre visible)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Mode silencieux

    # Initialise le driver Chrome
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Va sur Amazon
    driver.get("https://www.amazon.fr")

    # Trouve la barre de recherche et entre la requête
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(query)
    search_box.submit()

    # Attend un peu pour que la page charge
    driver.implicitly_wait(2)

    # Cherche le premier prix
    price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
    driver.quit()  # Ferme le navigateur

    return price

# Test rapide
if __name__ == "__main__":
    from config import CHROMEDRIVER_PATH
    price = search_amazon("python book", CHROMEDRIVER_PATH)
    print(f"Prix trouvé : {price}€")