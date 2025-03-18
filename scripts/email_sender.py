# scraping_bot/scripts/email_sender.py
# Module pour envoyer un email avec une pièce jointe

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(sender, password, receiver, smtp_server, smtp_port, subject, body, attachment_path):
    """
    Envoie un email avec un fichier joint.
    """
    # Crée le message email
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Ajoute le corps du texte
    msg.attach(MIMEText(body, "plain"))

    # Ajoute le fichier Excel en pièce jointe
    with open(attachment_path, "rb") as f:
        attachment = MIMEApplication(f.read(), _subtype="xlsx")
        attachment.add_header("Content-Disposition", "attachment", filename=attachment_path.split("/")[-1])
        msg.attach(attachment)

    # Connexion au serveur SMTP et envoi
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Active TLS pour la sécurité
        server.login(sender, password)  # Connexion
        server.send_message(msg)  # Envoi

    print("Email envoyé avec succès !")

# Test rapide
if __name__ == "__main__":
    from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, SMTP_SERVER, SMTP_PORT
    send_email(
        EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, SMTP_SERVER, SMTP_PORT,
        "Test Rapport", "Voici un test.", "data/livres.xlsx"
    )