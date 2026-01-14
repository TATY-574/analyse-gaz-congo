import streamlit as st
import pandas as pd

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Expertise Gaz Congo", layout="wide")

st.title("🇨🇬 Analyse Stratégique : Objectif Gaz à 5 000 FCFA")
st.markdown("---")

# 2. LES DONNÉES SOURCES (Issues de l'arrêté et du marché)
# Prix d'entrée selon l'arrêté : 200 FCFA/kg
prix_entree_arrete = 200.00

# Total des charges et taxes (Passage, Transport, Marges, TVA) : 310.12 FCFA/kg
# Calculé à partir de : 84.00 + 15.93 + 44.32 + 8.38 + 1.64 + 63.75 + 12.05 + 0.22 + 0.44 + 50.00 + 9.45 + 16.50 + 3.12 + 0.22 + 0.05 + 1.65
charges_structure = 310.12

# Réalité du terrain : Prix d'achat Wing Wah
prix_achat_wing_wah = 330.00

# Objectif final pour l'usager
objectif_bouteille = 5000.0
objectif_kg = 400.00 # Car 5000 / 12.5 kg = 400 FCFA/kg

# 3. CALCUL DES SCÉNARIOS
prix_total_arrete = prix_entree_arrete + charges_structure # 510.12 FCFA
prix_total_wing_wah = prix_achat_wing_wah + charges_structure # 640.12 FCFA

# 4. AFFICHAGE DU GRAPHIQUE
st.subheader("📊 Comparaison des Structures de Prix (FCFA/kg)")

# Création du DataFrame pour le graphique
df_data = pd.DataFrame({
    'Scénario': ['Structure Arrêté', 'Réalité Wing Wah', 'Objectif 5000F'],
    'Prix (FCFA/kg)': [prix_total_arrete, prix_total_wing_wah, objectif_kg]
})

# Palette de couleurs personnalisée : Bleu, Rouge, Vert
st.bar_chart(data=df_data, x='Scénario', y='Prix (FCFA/kg)', color='Scénario')

# 5. ANALYSE DÉTAILLÉE POUR LE CONSEILLER
st.markdown("### 🔍 Analyse des écarts")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("🔵 **Structure Arrêté**")
    st.metric("Prix au kg", f"{prix_total_arrete:.2f} F")
    st.write(f"Prix bouteille : **{(prix_total_arrete * 12.5):.0f} FCFA**")
    st.caption("Basé sur un VPC de 200 F/kg.")

with col2:
    st.error("🔴 **Réalité Wing Wah**")
    st.metric("Prix au kg", f"{prix_total_wing_wah:.2f} F")
    st.write(f"Prix bouteille : **{(prix_total_wing_wah * 12.5):.0f} FCFA**")
    st.caption("Prix d'achat réel à 330 F/kg.")

with col3:
    st.success("🟢 **Objectif Social**")
    st.metric("Prix au kg", f"{objectif_kg:.2f} F")
    st.write(f"Prix bouteille : **5 000 FCFA**")
    st.caption("Cible pour le consommateur.")

# 6. IMPACT BUDGÉTAIRE (Subvention nécessaire)
st.divider()
st.subheader("💰 Estimation de l'Effort de l'État")

effort_par_kg = prix_total_wing_wah - objectif_kg
effort_par_bouteille = effort_par_kg * 12.5

st.warning(f"Pour atteindre l'objectif de 5 000 FCFA, l'État doit subventionner **{effort_par_kg:.2f} FCFA/kg**.")

volume_mensuel = st.number_input("Volume mensuel estimé (Nombre de bouteilles)", value=50000, step=5000)
subvention_mensuelle = volume_mensuel * effort_par_bouteille

st.metric("Subvention Mensuelle Totale", f"{subvention_mensuelle:,.0f} FCFA")

st.markdown("""
**Recommandations pour le mémorandum :**
1. **Exonération de la TVA** : Gain immédiat de 48,93 FCFA/kg.
2. **Subvention Wing Wah** : Compensation de l'écart entre 330 FCFA et 200 FCFA.
""")