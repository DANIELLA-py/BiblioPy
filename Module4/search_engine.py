import time
livres = [
    {"titre":"introduction à l'algorithmique","auteur":"thomas H.cormen","ISBN":"978-2744072956"},
    {"titre":"les reseaux informatiques","auteur":"Andrew s.tanenbaum","ISBN":"978-2744075551"},
    {"titre":"Intelligence artificiellle","auteur":"stuart Russell,peter Norvig","ISBN":"978-2340091445"},
    {"titre":"cloud computing:concepts,technology & architecture","auteur":"Thomas Erl","ISBN":"978-0133387520"},
    {"titre":"python pour les data scientists","auteur":"Jake Vanderplas","ISBN":"978-1491912058"},
    {"titre":"Deep learning ","auteur":"Ian Goodfellow,Yoshua Bengio,Aaron Courville","ISBN":"978-0262035613"},
    {"titre":"l'ingénierie des exigences","auteur":"Didier Garlan","ISBN":"978-2100795826"},
]
def recherche_sequentielle(liste,cle,valeur):
    for item in liste:
        if item[cle].lower()==valeur.lower():
            return item 
    return None
def recherche_dichotomique(liste,cle,valeur):
    liste_triee = sorted(liste,key=lambda x:x[cle].lower())
    gauche,droite = 0,len(liste_triee) - 1
    while gauche <= droite:
        milieu = (gauche + droite)//2
        courant = liste_triee[milieu][cle].lower()
        if courant == valeur.lower():
            return liste_triee[milieu]
        elif courant < valeur.lower():
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return None
def recherche_par_titre(titre,methode="sequentielle"):
    if methode =="sequentielle":
        return recherche_sequentielle( livres,"titre",titre)
    else:
        return recherche_dichotomique( livres,"titre",titre)
def rechercher_par_auteur(auteur,methode="sequentielle"):
    if methode =="sequentielle":
        return recherche_sequentielle(livres,"auteur",auteur)
    else:
        return recherche_dichotomique(livres,"auteur",auteur)
def recherche_par_ISBN(ISBN):
        return recherche_sequentielle(livres,"ISBN",ISBN)
def comparaison_performances(cle,valeur):
    print(f"comparaison de performances pour la recherche de '{valeur}' dans '{cle}'")
    debut = time.time()
    result_seq = recherche_sequentielle(livres,cle,valeur)
    temps_seq = time.time() - debut
    print(f"recherche sequentielle:{temps_seq:6f}s - resultat: {result_seq}")
    debut = time.time()
    result_dicho = recherche_dichotomique(livres,cle,valeur)
    temps_dicho =time.time() - debut
    print(f"recherche dichotomique:{temps_dicho:6f}s - resultat:{result_dicho}")
    print(f"\n compléxité theorique:")
    print(" - sequentielle:0(n)")
    print("- dichotomique:0(log n)(si tri prealable)")
def recherche_multi_critere(titre=None,auteur=None):
    resultats  = []
    for livre in livres:
        if titre and titre.lower()!= livre["titre"].lower():
           continue
        if auteur and auteur.lower() != livre["auteur"].lower():
            continue
        resultats.append(livre)
    return resultats 
print("\n🔍 Test de recherche par titre")
resultat_titre = recherche_par_titre("Deep learning")
print(f"Résultat : {resultat_titre}")

print("\n🔍 Test de recherche par auteur")
resultat_auteur = rechercher_par_auteur("Ian Goodfellow, Yoshua Bengio, Aaron Courville")
print(f"Résultat : {resultat_auteur}")

print("\n🔍 Test de recherche par ISBN")
resultat_ISBN = recherche_par_ISBN("978-0262035613")
print(f"Résultat : {resultat_ISBN}")

print("\n🔍 Test de recherche multi-critère")
resultat_multi = recherche_multi_critere(titre="Deep learning", auteur="Ian Goodfellow, Yoshua Bengio, Aaron Courville")
print(f"Résultat : {resultat_multi}")

# 🔥 Comparaison des performances
comparaison_performances("titre", "Deep learning")
    
    
    