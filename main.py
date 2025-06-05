import csv
FILENAME= "catalague.csv"
FIELDS=[" Titre", "Auteur","ISBN","Annee","Statut"]
def charger_catalogue():
  try:
    with open(FILENAME,newline=",encording='utf-8') as f:
              return list(csv.DictReader(f))
  except FileNotFoundError:
    return[]
def sauvegarder_catalogue(catalogue):
  with open(FILENAME,'w',newline=",encording='utf-8') as f:
            writer= csv.DictWriter(f,fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(catalogue)
def ajouter_livre():
  livre={champ: input (f"{champ}: ") for champ in FIEDLS}
  catalogue = charge_catalogue()
  catalogue.append(livre)
  sauvegarder_catalogue(catalogue)
  print("livre ajouter  avec succes !")
def supprimer_livre():
  isbn = input("ISBN du livre à supprimer : ")
  catalogue = charger_catalogue()
  catalogue = [ l for l in catalogue if l ["ISBN"] != isbn]
  sauvegarder_catalogue(catalogue)
  print ("livre a été supprimer avec succes! ")
def modifier_livre():
  isbn = input("ISBN du livre à modiffier:")
  catalogue = charger_catalogue()
  for livre in catalogue:
    if livre ["ISBN"] == isbn:
      for champ in FIELDS:
        nv= input(f"{champ} [{livre[champ]}] :")
            if nv: livre[champ] = nv:
      break
sauvegarder_catalogue(catalogue)
print("livre modifier !")
                  livre [champ] = nv
   break
                 
