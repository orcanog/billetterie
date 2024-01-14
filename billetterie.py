"""
Cours "Introduction 1" - Exercice "Billetterie"
"""

# Variables
stations = {
    "Meinohama": 1.5,
    "Muromi": 0.8,
    "Fujisaki": 1.1,
    "Nishijin": 1.2,
    "Tojinmachi": 0.8,
    "Ohorikoen (Ohori Park)": 1.1,
    "Akasaka": 0.8,
    "Tenjin": 0.8,
    "Nakasu-Kawabata": 1.0,
    "Gion": 0.7,
    "Hakata": 1.2,
    "Higashi-Hie": 2.1,
    "Fukuokakuko (Airport)": 0.0,
}

stations_names = list(stations.keys())
stations_distances = list(stations.values())
station_depart = None
distance_depart = 0
distance_arrivee = 0
station_arrivee = None
nb_billets_adulte = 0
nb_billets_enfant = 0
has_reduit = False
distance_totale = 0
prix_total = 0

# Introduction
print("           /////// ")
print("         ///       ")
print("  //////////////   ")
print("      ///          ")
print("///////            ")
print("\nBienvenue sur la billetterie du métro municipal de Fukuoka.")

# Questions à l'utilisateur
print("\n--- Combien souhaitez-vous de billets à tarif plein ?")
nb_billets_adulte = int(input("Billets : "))

print("\n--- Souhaitez-vous des billets à tarif réduit ? oui / non")
has_reduit = bool(input("Votre réponse : "))
if has_reduit == "oui":
    has_reduit = True
elif has_reduit == "non":
    has_reduit = False

print("\n--- Combien souhaitez-vous de billets à tarif réduit ?")
nb_billets_enfant = int(input("Billets à tarif réduit : "))

# Calculs de l'itinéraire
print("\n--- Quelle est votre station de départ ?")
station_depart = stations_names[str(input("Départ : "))]
print("\n--- Quelle est votre station d'arrivée ?")
station_arrivee = stations_names[str(input("Arrivée : "))]

# Choix de la bonne zone tarifaire

for i in range(station_depart, station_arrivee):
    distance_totale = distance_totale + stations_distances[i]

# Calcul du coût total

# Affichage des détails du voyage et du tarif

# Affichage de la voie du train à emprunter
