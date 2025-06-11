import os
import json
import csv
bibliotheque=[]

def read_json(file_name):
    with open (file_name, newline='', encoding='utf-8') as f:
        return )json.load(f)
def read_csv(file_name):
    with open(file_name, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))
def load_data():
    if os.path.exists ('data.csv'):
        print("lecture des fichier CSV...")
        return read_csv ('data.csv')
    elif os.path.exists('data.json'):
        print("lecture du fichier JSON...")
        return read_json('data.json')
    else:
        print ("Aucun fichier de données trouvé")
        return[]
if__name__=="__main__":
data = load_data()
print("Données chargées : " data)
def charges_livres_json(nom_fichier):
    