import streamlit as st
import requests

# URL de l'API Rasa (assurez-vous que Rasa est en cours d'exécution à cette adresse)
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

# Titre de l'application
st.title("Chatbot Rasa avec Streamlit")

# Zone de saisie de l'utilisateur
user_message = st.text_input("Entrez votre message :", "")

# Fonction pour envoyer le message à Rasa et récupérer la réponse
def get_rasa_response(message):
    try:
        # Envoyer le message à l'API de Rasa
        response = requests.post(RASA_URL, json={"message": message})
        response.raise_for_status()  # Vérifie les erreurs HTTP
        return response.json()  # Récupérer la réponse au format JSON
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur de connexion à l'API Rasa : {e}")
        return [{"text": "Désolé, une erreur est survenue avec le chatbot."}]

# Bouton pour envoyer le message
if st.button("Envoyer"):
    if user_message.strip():
        # Appel à la fonction pour obtenir la réponse de Rasa
        rasa_response = get_rasa_response(user_message)
        
        # Affichage de la réponse du chatbot dans l'interface Streamlit
        for message in rasa_response:
            st.write("Bot :", message.get('text', ''))
    else:
        st.warning("Veuillez entrer un message.")

