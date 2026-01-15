import streamlit as st
import pandas as pd

st.set_page_config(page_title="Valorisation Gaz Congo - Cabinet", layout="wide")

st.title("📊 Analyse de Bancabilité : Objectif Gaz à 5 000 FCFA")
st.subheader("Données certifiées d'après le courrier FAAKI-CONGO (Déc. 2025)")

# --- Section des Paramètres (Basée sur le courrier du 22/12/25) ---
with st.sidebar:
    st.header("Paramètres d'Exploitation")
    # Volume de 5 000 tonnes cité dans le courrier
    volume_mensuel = st.slider("Volume mensuel cible (Tonnes)", 1000, 7000, 5000)

    st.header("Structure de Prix (FCFA/kg)")
    # Prix appliqué par Wing Wah selon le courrier [cite: 39]
    prix_wing_wah = st.number_input("Prix Sortie Wing Wah (Banga Kayo)", value=330.0)
    # Prix réglementaire de l'arrêté 2018 cité dans le courrier [cite: 39]
    prix_arrete_2018 = st.number_input("Prix d'Entrée (Arrêté 919/2018)", value=200.0)

    tva_actuelle = 48.93  # Valeur mémorisée du précédent arrêté

# --- Calculs ---
differentiel = prix_wing_wah - prix_arrete_2018  # Soit 130 FCFA/kg [cite: 39]
impact_mensuel = (volume_mensuel * 1000) * differentiel
impact_annuel = impact_mensuel * 12

economie_tva = (volume_mensuel * 1000) * tva_actuelle * 12

# --- Affichage des indicateurs ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Différentiel à compenser", f"{differentiel} FCFA/kg")
with col2:
    st.metric("Besoin de Financement Annuel", f"{impact_annuel:,.0f} FCFA")
with col3:
    st.metric("Gain via Abolition TVA", f"{economie_tva:,.0f} FCFA")

st.info(
    f"**Note stratégique :** Pour atteindre 5 000 t/mois (7 camions/jour), le besoin en fonds de roulement nécessite un délai de paiement de 30 jours, tel que requis par l'opérateur[cite: 89, 93].")

# --- Graphique ---
chart_data = pd.DataFrame({
    'Structure': ['Prix Social Cible', 'Réalité Wing Wah', 'Ancien Arrêté'],
    'FCFA/kg': [400, prix_wing_wah, prix_arrete_2018]
})
st.bar_chart(chart_data, x='Structure', y='FCFA/kg')
