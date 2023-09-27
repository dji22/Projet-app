import tkinter as tk
from tkinter import messagebox

# Fonction pour ajouter un patient
def ajouter_patient():
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    age = age_entry.get()

    # Vérification des champs vides
    if not nom or not prenom or not age:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return

    # Affichage des informations du patient
    info_text.config(state=tk.NORMAL)
    info_text.insert(tk.END, f"Nom: {nom}\n")
    info_text.insert(tk.END, f"Prénom: {prenom}\n")
    info_text.insert(tk.END, f"Âge: {age}\n")
    info_text.insert(tk.END, "-" * 20 + "\n")
    info_text.config(state=tk.DISABLED)

    # Effacement des champs d'entrée
    nom_entry.delete(0, tk.END)
    prenom_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

# Configuration de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Gestion des patients")

# Labels et champs d'entrée
nom_label = tk.Label(fenetre, text="Nom:")
prenom_label = tk.Label(fenetre, text="Prénom:")
age_label = tk.Label(fenetre, text="Âge:")

nom_entry = tk.Entry(fenetre)
prenom_entry = tk.Entry(fenetre)
age_entry = tk.Entry(fenetre)

ajouter_bouton = tk.Button(fenetre, text="Ajouter Patient", command=ajouter_patient)

# Zone de texte pour afficher les informations des patients
info_text = tk.Text(fenetre, height=10, width=30)
info_text.config(state=tk.DISABLED)

# Placement des éléments dans la fenêtre
nom_label.grid(row=0, column=0)
prenom_label.grid(row=1, column=0)
age_label.grid(row=2, column=0)

nom_entry.grid(row=0, column=1)
prenom_entry.grid(row=1, column=1)
age_entry.grid(row=2, column=1)

ajouter_bouton.grid(row=3, column=0, columnspan=2)
info_text.grid(row=4, column=0, columnspan=2)

fenetre.mainloop()

