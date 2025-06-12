import os
import csv
import json
livres=[]
next_id=1
def charger_csv(fichierr):
    global livres , next_id
    if os.path.exists(fichierr):
        with open(fichierr, mode='r', newline= '') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row ['id'] = int(row['id'])
                livres.append(row)
        if livres:
            next_id = max(livre['id'] for livre in livres) + 1
def sauvegarder_csv(fichierr):
    with open(fichierr, mode='w', newline='') as f:
        fieldnames = ['id', 'titre', 'auteur', 'annee', 'isbn', 'emprunte']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for livre in livres:
            writer.writerow(livre)