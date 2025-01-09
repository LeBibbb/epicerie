import tkinter as tk

#Abdelhai
# Dictionnaires des articles avec leurs prix
produits_laitiers = {
    "Lait (1L)": 1.00,
    "Beurre (250g)": 2.10,
    "Fromage (200g)": 3.50,
    "Yaourt (4x125g)": 2.00,
    "Crème fraîche (200ml)": 1.80
}

fruits = {
    "Pomme (kg)": 1.20,
    "Banane (kg)": 0.90,
    "Orange (kg)": 1.50,
    "Fraise (500g)": 3.00,
    "Raisin (kg)": 2.80
}

legumes = {
    "Tomate (kg)": 2.30,
    "Carotte (kg)": 1.20,
    "Pomme de terre (kg)": 0.85,
    "Poivron (kg)": 2.50,
    "Courgette (kg)": 2.00
}

produits_menagers = {
    "Liquide vaisselle (500ml)": 2.50,
    "Lessive (1L)": 6.00,
    "Éponge (paquet)": 1.50,
    "Nettoyant multi-surface (1L)": 3.00,
    "Sac-poubelle (10 unités)": 2.80
}

boissons = {
    "Eau (1.5L)": 0.60,
    "Café (250g)": 4.80,
    "Thé (boîte de 20 sachets)": 2.50,
    "Jus d'orange (1L)": 2.00,
    "Soda (canette)": 1.20
}


#ibrahim
# Dictionnaire vide pour le panier
panier = {}

# Création de la fenêtre principale
root = tk.Tk()
root.title("Épicerie")
root.geometry("700x600")  # Taille de la fenêtre mise à jour
root.resizable(False, False)  # Interdire le redimensionnement de la fenêtre
root.configure(bg="#f0f4f8")  # Couleur de fond moderne

# Titre de l'application
title_label = tk.Label(root, text="Épicerie", font=("Arial", 24, "bold"), bg="#f0f4f8", fg="#333")
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Fonction pour mettre à jour l'affichage du panier
def afficher_panier():
    listbox.delete(0, tk.END)  # Vide la liste avant de mettre à jour
    total = 0
    
    for article, details in panier.items():
        quantite = details['quantite']
        prix = details['prix']
        sous_total = quantite * prix
        listbox.insert(tk.END, f"{article} - {quantite} x {prix:.2f} € = {sous_total:.2f} €")
        total += sous_total
        
    listbox.insert(tk.END, f"\nTotal à payer : {total:.2f} €")

# Fonction pour ajouter un article au panier
def ajouter_au_panier(article):
    if article in panier:
        panier[article]['quantite'] += 1
    else:
        for articles in [produits_laitiers, fruits, legumes, produits_menagers, boissons]:
            if article in articles:
                panier[article] = {'quantite': 1, 'prix': articles[article]}
                break

    afficher_panier()  # Actualiser le panier
    afficher_articles(categorie_selection.get())  # Mettre à jour l'affichage des articles

# Fonction pour retirer un article du panier
def retirer_du_panier(article):
    if article in panier:
        panier[article]['quantite'] -= 1
        if panier[article]['quantite'] <= 0:
            del panier[article]
    afficher_panier()  # Actualiser le panier
    afficher_articles(categorie_selection.get())  # Mettre à jour l'affichage des articles

# Fonction pour afficher les articles selon la catégorie sélectionnée
def afficher_articles(categorie):
    # Vider le cadre des articles
    for widget in articles_frame.winfo_children():
        widget.destroy()
    
    # Sélectionner les articles selon la catégorie
    articles = {
        "Produits Laitiers": produits_laitiers,
        "Fruits": fruits,
        "Légumes": legumes,
        "Produits Ménagers": produits_menagers,
        "Boissons": boissons
    }[categorie]

    # Ajouter les articles à la colonne des articles
    for i, (article, prix) in enumerate(articles.items()):
        # Création d'une ligne pour l'article, la quantité, et les boutons
        article_frame = tk.Frame(articles_frame, bg="#f0f4f8")
        article_frame.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        # Label pour afficher l'article (avec une largeur fixe)
        article_label = tk.Label(article_frame, text=f"{article:<30}", bg="#f0f4f8", fg="#333", font=("Arial", 12), width=30, anchor='w')
        article_label.pack(side=tk.LEFT)

        # Label pour afficher le prix (aligné à gauche)
        prix_label = tk.Label(article_frame, text=f"{prix:.2f} €", bg="#f0f4f8", fg="#333", font=("Arial", 12))
        prix_label.pack(side=tk.LEFT, padx=(5, 0))  # Ajoute un peu d'espace à gauche du prix

        # Obtenir la quantité actuelle de l'article
        quantite = panier.get(article, {'quantite': 0})['quantite']
        
        # Label pour afficher la quantité, affiché uniquement si > 0
        if quantite > 0:
            quantite_label = tk.Label(article_frame, text=f"{quantite}", bg="#f0f4f8", fg="#333", font=("Arial", 12))
            quantite_label.pack(side=tk.LEFT, padx=(5, 0))  # Espace à gauche du label de quantité

        # Ajouter bouton pour augmenter la quantité, collé à droite
        ajouter_button = tk.Button(article_frame, text="Ajouter", command=lambda a=article: ajouter_au_panier(a), bg="#4CAF50", fg="white", font=("Arial", 10), activebackground="#66bb6a", bd=0, padx=5, pady=5)
        ajouter_button.pack(side=tk.RIGHT, padx=5)

        # Ajouter bouton pour diminuer la quantité, collé à droite
        retirer_button = tk.Button(article_frame, text="Retirer", command=lambda a=article: retirer_du_panier(a), bg="#e74c3c", fg="white", font=("Arial", 10), activebackground="#c0392b", bd=0, padx=5, pady=5)
        retirer_button.pack(side=tk.RIGHT, padx=5)

# Fonction pour gérer le changement de catégorie
def changer_categorie(categorie):
    categorie_selection.set(categorie)
    afficher_articles(categorie)

# Création de la colonne de gauche pour les catégories
categories = ["Produits Laitiers", "Fruits", "Légumes", "Produits Ménagers", "Boissons"]
categorie_selection = tk.StringVar(value=categories[0])  # Valeur par défaut

for i, categorie in enumerate(categories):
    button = tk.Button(root, text=categorie, command=lambda c=categorie: changer_categorie(c), bg="#007bff", fg="white", font=("Arial", 12), activebackground="#0056b3", bd=0, padx=10, pady=5)
    button.grid(row=i + 2, column=0, padx=10, pady=5, sticky='ew')

# Création de la colonne de droite pour les articles
articles_frame = tk.Frame(root, bg="#f0f4f8")
articles_frame.grid(row=1, column=1, rowspan=len(categories) + 1, padx=10, pady=10, sticky='nsew')

# Fixer les largeurs de colonnes
root.grid_columnconfigure(0, minsize=150)  # Colonne des catégories
root.grid_columnconfigure(1, minsize=350)  # Colonne des articles

# Zone de texte pour afficher le panier (remplacée par Listbox)
panier_frame = tk.Frame(root, bg="#f0f4f8", bd=2, relief="groove")
panier_frame.grid(row=len(categories) + 3, column=0, columnspan=3, padx=10, pady=10)

panier_label = tk.Label(panier_frame, text="Votre Panier", font=("Arial", 16, "bold"), bg="#f0f4f8", fg="#333")
panier_label.pack(pady=5)

listbox = tk.Listbox(panier_frame, height=10, width=50, font=("Arial", 12), bg="#ffffff", fg="#333", bd=0, selectbackground="#e0e0e0")
listbox.pack(padx=10, pady=5)

# Afficher les articles de la catégorie par défaut au démarrage
afficher_articles(categorie_selection.get())

# Démarrer la boucle principale de l'application
root.mainloop()


