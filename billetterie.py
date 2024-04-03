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
zone_tarifaire = None
nb_billets_adulte = 0
nb_billets_enfant = 0
has_reduit = False
distance_totale = 0
prix_adulte = 0
prix_enfant = 0
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
has_reduit = str(input("Votre réponse : "))

if has_reduit == "oui":
    print("\n--- Combien souhaitez-vous de billets à tarif réduit ?")
    nb_billets_enfant = int(input("Billets à tarif réduit : "))


# Calculs de l'itinéraire

print("\n--- Quelle est le numéro de votre station de départ ?")
station_depart = int(input("Départ : ")) -1
print("\n--- Quelle est le numéro de votre station d'arrivée ?")
station_arrivee = int(input("Arrivée : ")) -1


# Choix de la bonne zone tarifaire

if (station_depart < station_arrivee):
    for i in range(station_depart, station_arrivee) :
        distance_totale = distance_totale + stations_distances[i]
else : 
    for i in range (station_arrivee, station_depart) :
        distance_totale = distance_totale + stations_distances[i]
    

if distance_totale <= 3 :
    zone_tarifaire = 1
elif 3 < distance_totale <= 7 :
    zone_tarifaire = 2
elif 7 < distance_totale <= 11 :
    zone_tarifaire = 3    
elif 11 < distance_totale <= 15 :
    zone_tarifaire = 4


# Calcul du coût total

if zone_tarifaire == 1 :
    prix_adulte = 210
    if has_reduit == True :
        prix_enfant = 110
elif zone_tarifaire == 2 :
    prix_adulte = 260
    if has_reduit == True :
        prix_enfant = 130
elif zone_tarifaire == 3 :
    prix_adulte = 300
    if has_reduit == True :
        prix_enfant = 150
elif zone_tarifaire == 4 :
    prix_adulte = 340
    if has_reduit == True :
        prix_enfant = 170

prix_total = (prix_adulte * nb_billets_adulte) + (prix_enfant * nb_billets_enfant)

# Affichage des détails du voyage et du tarif

print ("\n --- Votre station de départ : " + stations_names[station_depart])
print ("\n --- Votre station d'arrivée : " + stations_names[station_arrivee])
print ("\n --- Votre zone tarifaire : ", zone_tarifaire)
print ("\n --- Votre nombre de billets à tarif plein : ", nb_billets_adulte)
print ("\n --- Votre nombre de billets à tarif réduit : ", nb_billets_enfant)
print ("\n --- Prix à payer : ", prix_total, " yens")

# Affichage de la voie du train à emprunter

if (station_depart < station_arrivee) :
    print ("\n --- Veuillez prendre la voie 1 pour terminus Fukuokakuko (Airport).")
else : print ("\n --- Veuillez prendre la voie 2 pour terminus Meinohama.")
print ("\n --- Excellent voyage !")