import json , csv , os
JSON_file="livres.json"
CSV_file= "livres.csv"

def charger_livres_json ():
    if os.path.exists(JSON_file):
        with open (JSON_file, "r", encording='utf-8') as f:
            return json.load(f)
        return []
    
def sauvegarder_livres_json(livres):
    with open(JSON_file, "w", encoding='utf-8') as f:
        json.dump(livres, f, ensure_ascii=False, indent=2)

def charger_livres_csv():
    if not os.path.exists(CSV_file):
        return []
    with open (CSV_file, newline='',encoding='utf-8') as f:  
        return list( csv.DictReader(f))
    
def sauvegarder_livres_csv (livres):
    if not livres:
        return
    with open (CSV_file, "w", newline="",encoding='utf_8') as f:
        writer = csv.DictWriter(f, fieldnames=livres.keys())
        writer.writeheader()
        writer.writerows(livres)

def generer_id(livres):
    if livres:
        return max(int(livre['id']) for livre in livres) + 1
     
    return 1
def ajouter_livre(livres , titre , auteur):
    livre={"id": str(generer_id(livres)), "titre": titre, "auteur": auteur}
    livres.append(livre)
    sauvegarder_livres_json(livres)
    sauvegarder_livres_csv(livres)

def supprimer_livre(livres, id_livre):
    livres[:] = [livre for livre in livres if livre['id'] != str(id_livre)]
    sauvegarder_livres_json(livres)
    sauvegarder_livres_csv(livres)

def modifier_livre(livres, id_livre, titre=None, auteur=None):
    for livre in livres:
        if livre['id'] == str(id_livre):
            if titre is not None:
                livre['titre'] = titre
            if auteur is not None:
                 livre['auteur'] = auteur
            break
def afficher_livres():
    for l in livres :
        print(f"ID: {l['id']}, Titre: {l['titre']}, Auteur: {l['auteur']}")
def initialiser_gestionnaire(format="json"):
    if format == "csv":
         livres = charger_livres_csv(livres)
    else:
        livres = charger_livres_json(livres)
    import atexit
    if format == "csv":
        atexit.register(sauvegarder_livres_csv, livres)
    else:
        atexit.register(sauvegarder_livres_json, livres)
    # Sauvegarder les modification
    sauvegarder_livres_json(livres)
    sauvegarder_livres_csv(livres)
# Exemple d'utilisation

livres = charger_livres_json()
ajouter_livre(livres, "Le Petit Prince", "Antoine de Saint-Exupéry")
supprimer_livre(livres, 1)
modifier_livre(livres, 2, titre="Le Petit Prince Modifié", auteur="Antoine de Saint-Exupéry Modifié")
afficher_livres()
