from datetime import datetime
class Livre:
     def __init__(self, titre, auteur):
         self.titre = titre
         self.auteur = auteur
         self.emprunteur = None
         self.date_emprunt = None

     def emprunter(self, nom_emprunteur):
         """Marque le livre comme emprunté avec la date d'emprunt."""
         if self.emprunteur:
             print(f"Le livre '{self.titre}' est déjà emprunté par {self.emprunteur}.")
         else:
             self.emprunteur = nom_emprunteur
             self.date_emprunt = datetime.now().strftime("%Y-%m-%d")
             print(f"Le livre '{self.titre}' a été emprunté par {self.emprunteur} le {self.date_emprunt}.")
 
     def retourner(self):
         """Marque le livre comme retourné et le rend disponible."""
         if self.emprunteur:
             print(f"Le livre '{self.titre}' a été retourné par {self.emprunteur}.")
             self.emprunteur = None
             self.date_emprunt = None
         else:
             print(f"Le livre '{self.titre}' est déjà disponible.")
 
     def statut(self):
         """Affiche le statut actuel du livre."""
         if self.emprunteur:
             print(f"Le livre '{self.titre}' est emprunté par {self.emprunteur} depuis le {self.date_emprunt}.")
         else:
             print(f"Le livre '{self.titre}' est disponible.")

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        """Ajoute un livre à la bibliothèque."""
        self.livres.append(livre)

    def lister_livres_empruntes(self):
        """Affiche tous les livres actuellement empruntés."""
        empruntes = [livre for livre in self.livres if livre.emprunteur]
        if empruntes:
            print("\nLivres empruntés :")
            for livre in empruntes:
                print(f"- {livre.titre}, emprunté par {livre.emprunteur} depuis le {livre.date_emprunt}.")
        else:
            print("\nAucun livre n'est actuellement emprunté.")

    def lister_livres_disponibles(self):
        """Affiche tous les livres disponibles."""
        disponibles = [livre for livre in self.livres if livre.emprunteur is None]
        if disponibles:
            print("\nLivres disponibles :")
            for livre in disponibles:
                print(f"- {livre.titre} de {livre.auteur}")
        else:
            print("\nTous les livres sont empruntés.")