import pygame
from pygame import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pandas as pd

#-------------------------------------------Tkinter--------------------------------------------------#
counter = 0
base = pd.read_csv("BDD.csv", sep=';')
chaine = base["Prenom"].tolist()
chaine_min = [chaine.lower() for chaine in chaine]
chaine2 = base["Nom"].tolist()
chaine_min2 = [chaine2.lower() for chaine2 in chaine2]
def connect():
    global Prenom, Nom, Sexe, Age, Pays, Argent, Rang, Autre, Photo
    if Entree.get() != '':
        x = Entree.get()
        x = x.capitalize()
        x2 = x.lower()
        find = "Empty"

        for i in range(len(chaine_min)):
            if chaine_min[i] in x2:
                find = chaine_min[i]
                find = find.capitalize()
                print(find)

        Prenom = base.loc[(base["Prenom"]==find) | (base["Nom"]==x), ["Prenom"]].to_string(index = False, header=False)
        Nom = base.loc[(base["Prenom"]==find) | (base["Nom"]==x), ["Nom"]].to_string(index = False, header=False)
        Sexe = base.loc[(base["Prenom"]==find) | (base["Nom"]==x), ["Sexe"]].to_string(index = False, header=False)
        Age = base.loc[(base["Prenom"]==find) | (base["Nom"]==x), ["Age"]].to_string(index = False, header=False)
        Pays = base.loc[(base["Prenom"]==find) | (base["Nom"]==x), ["Pays"]].to_string(index = False, header=False)
        Argent = base.loc[(base["Prenom"]==find) | (base["Nom"]==x), ["Argent"]].to_string(index = False, header=False)
        Rang = base.loc[(base["Prenom"]==find) | (base["Nom"]==x), ["Rang"]].to_string(index = False, header=False)
        Autre = base.loc[(base["Prenom"]==find) | (base["Nom"]==x), ["Desc"]].to_string(index = False, header=False)
        Photo = base.loc[(base["Prenom"]==find) | (base["Nom"]==x), ["Img"]].to_string(index = False, header=False)

        if 'Empty' in Prenom:
            messagebox.showwarning('Erreur', "Personne non trouvée") #message pop-up
        else:
            progbar = Toplevel(Fenetre)
            progresse = ttk.Progressbar(progbar, orient="horizontal", length=250, mode="determinate")

            ####### Centrer fenêtre #######

            page_height = 100
            page_width = 350
            screen_width_px = progbar.winfo_screenwidth()
            screen_height_px = progbar.winfo_screenheight()
            x_cordinate = int((screen_width_px / 2) - (page_width / 2))
            y_cordinate = int(((screen_height_px / 2) - (page_height / 2))-50) #le -50 relève un peut la fenêtre, je la trouvais trop basse
            progbar.geometry("{}x{}+{}+{}".format(page_width, page_height, x_cordinate, y_cordinate))

            ####### Centrer fenêtre #######

            progbar.config(bg="#ffa477")
            progresse.place(x=50, y=57.5)

            connectmsg = Label(progbar, text="Recherche en cours ...", bg="#ffa477")
            connectmsg.configure(font=("Engcomica", 15, "bold"))
            connectmsg.place(x=50, y=20)
            
            photo = PhotoImage(file="img/loupe.png")
            lab1 = Label(progbar, image=photo, bg="#ffa477")
            lab1.place(x=250, y=0)

            def update(delay=10):
                global counter
                progresse.step(0.6)
                counter += 1
                if counter < 167:
                    progresse.after(delay, update)
                else:
                    progbar.destroy()
                    counter = 0
                    Fenetre.destroy()
                    identity()

            update()
            progbar.mainloop()

    else:
        messagebox.showinfo('Recherche', "Veuillez saisir un champ") #message pop-up

def enterconnect(event): #fonction associer a la touche entré pour valider
    connect() #execute la fonction de connexion défini plus haut

def recherche():
    global Entree, Fenetre
    Fenetre=Tk() #création de la fenêtre principale

    ####### Centrer fenêtre #######

    page_height = 150
    page_width = 300
    screen_width_px = Fenetre.winfo_screenwidth()
    screen_height_px = Fenetre.winfo_screenheight()
    x_cordinate = int((screen_width_px / 2) - (page_width / 2)-8)
    y_cordinate = int(((screen_height_px / 2) - (page_height / 2)))
    Fenetre.geometry("{}x{}+{}+{}".format(page_width, page_height, x_cordinate, y_cordinate))

    ####### Centrer fenêtre #######

    Fenetre.resizable(width=False, height=False) #permet de ne pas pouvoir la redimensionner
    Fenetre.title("Wiki | Riche")
    Fenetre.bind("<Return>", enterconnect)

    imgback = PhotoImage(file="img/back.PNG")
    backimg = Label(Fenetre, image=imgback)

    mainmsg=Label(Fenetre,text="RECHERCHE") #message principal et couleur arrière plan de celui-ci
    mainmsg.configure(font=("Engcomica", 25, "bold"), bg="#ffa477") #taille et police d'écriture
    mainmsg.pack() #afficher le message en le placant

    backimg.place(x=-2, y=-2)

    Entree = Entry(Fenetre, width=20, justify='center', relief='flat', font=("Trebuchet MS", 13, "bold"))
    Entree.pack(pady=10)

    trait=Button(Fenetre, text="Rechercher", command=connect, cursor='hand2') #button de connxion qui exécute la fonction "connect"
    trait.configure(font=("Trebuchet MS", 15, "bold")) #config button
    trait.pack(pady="3")

    Fenetre.mainloop() #Fin de la fenetre principale

def add_table():
    global base, Prenom, Nom, chaine_min
    if Prenom_entry.get() != '' \
        and Nom_entry.get() != ''\
            and Sexe_entry.get() != ''\
                and Age_entry.get() != ''\
                    and Pays_entry.get() != ''\
                        and Argent_entry.get() != ''\
                            and Rang_entry.get() != ''\
                                and Desc_entry.get() != '':
        a,b,c,d,e,f,g,h = Prenom_entry.get(), Nom_entry.get(), Sexe_entry.get(), Age_entry.get(), Pays_entry.get(), Argent_entry.get(), Rang_entry.get(), Desc_entry.get()
        a = a.lower()
        b = b.lower()
        if a in chaine_min and b in chaine_min2:
            messagebox.showwarning('Erreur', "La personne est déjà enregistrer") #message pop-up
        else:
            a = a.capitalize()
            b = b.capitalize()
            base = base.append({'Prenom' : a,'Nom' : b,'Sexe' : c,'Age' : d,'Pays' : e,'Argent' : f,'Rang' : g, 'Desc' : h} , ignore_index=True)
            base.to_csv('BDD.csv', sep = ';', index = False)
            chaine = base["Prenom"].tolist()
            chaine_min = [chaine.lower() for chaine in chaine]
            messagebox.showinfo('Ajouter', "Le riche à été ajouté") #message pop-up
            Fenetre3.destroy()

    else:
        messagebox.showwarning('Erreur', "Champs manquants") #message pop-up

def ajouter():
    global Prenom_entry, Nom_entry, Sexe_entry, Age_entry, Pays_entry, Argent_entry, Rang_entry, Desc_entry, Fenetre3
    Fenetre3=Tk() #création de la fenêtre principale

    Fenetre3.overrideredirect(1)

    Fenetre3.resizable(width=False, height=False) #permet de ne pas pouvoir la redimensionner
    Fenetre3.title("Wiki | Riche")

    ####### Centrer fenêtre #######

    page_height = 688
    page_width = 688
    screen_width_px = Fenetre3.winfo_screenwidth()
    screen_height_px = Fenetre3.winfo_screenheight()
    x_cordinate = int((screen_width_px / 2) - (page_width / 2))
    y_cordinate = int(((screen_height_px / 2) - (page_height / 2))-50) #le -50 relève un peut la fenêtre, je la trouvais trop basse
    Fenetre3.geometry("{}x{}+{}+{}".format(page_width, page_height, x_cordinate, y_cordinate))

    ####### Centrer fenêtre #######

    imgcard = PhotoImage(file="img/inputID.PNG")
    backcard = Label(Fenetre3, image=imgcard)
    backcard.place(x=-2, y=-2)

    imgclose = PhotoImage(file="img/close.PNG")
    closebutton = Button(Fenetre3, image=imgclose, command=Fenetre3.destroy, borderwidth=0, highlightthickness=0, cursor='hand2')
    closebutton.place(x=608, y=28)

    imgsubmit = PhotoImage(file="img/valid.PNG")
    submitbutton = Button(Fenetre3, image=imgsubmit, command=add_table, borderwidth=0, highlightthickness=0, cursor='hand2')
    submitbutton.place(x=255, y=598)

    Prenom_entry = Entry(Fenetre3, width=30, justify='left', relief='flat', font=("Trebuchet MS", 12, "bold"), bg="#353535", fg="white")
    Prenom_entry.place(x=190, y=233)

    Nom_entry = Entry(Fenetre3, width=30, justify='left', relief='flat', font=("Trebuchet MS", 12, "bold"), bg="#353535", fg="white")
    Nom_entry.place(x=190, y=279)

    Sexe_entry = Entry(Fenetre3, width=30, justify='left', relief='flat', font=("Trebuchet MS", 12, "bold"), bg="#353535", fg="white")
    Sexe_entry.place(x=190, y=325)

    Age_entry = Entry(Fenetre3, width=30, justify='left', relief='flat', font=("Trebuchet MS", 12, "bold"), bg="#353535", fg="white")
    Age_entry.place(x=190, y=368)

    Pays_entry = Entry(Fenetre3, width=30, justify='left', relief='flat', font=("Trebuchet MS", 12, "bold"), bg="#353535", fg="white")
    Pays_entry.place(x=190, y=414)

    Argent_entry = Entry(Fenetre3, width=30, justify='left', relief='flat', font=("Trebuchet MS", 12, "bold"), bg="#353535", fg="white")
    Argent_entry.place(x=190, y=460)

    Rang_entry = Entry(Fenetre3, width=30, justify='left', relief='flat', font=("Trebuchet MS", 12, "bold"), bg="#353535", fg="white")
    Rang_entry.place(x=190, y=508)

    Desc_entry = Entry(Fenetre3, width=30, justify='left', relief='flat', font=("Trebuchet MS", 12, "bold"), bg="#353535", fg="white")
    Desc_entry.place(x=190, y=554)

    Fenetre3.mainloop() #Fin de la fenetre principale

def identity():
    Fenetre2=Tk() #création de la fenêtre principale

    Fenetre2.resizable(width=False, height=False) #permet de ne pas pouvoir la redimensionner
    Fenetre2.title("Wiki | Riche")

    ####### Centrer fenêtre #######

    page_height = 470
    page_width = 800
    screen_width_px = Fenetre2.winfo_screenwidth()
    screen_height_px = Fenetre2.winfo_screenheight()
    x_cordinate = int((screen_width_px / 2) - (page_width / 2))
    y_cordinate = int(((screen_height_px / 2) - (page_height / 2))-50) #le -50 relève un peut la fenêtre, je la trouvais trop basse
    Fenetre2.geometry("{}x{}+{}+{}".format(page_width, page_height, x_cordinate, y_cordinate))

    ####### Centrer fenêtre #######

    imgcard = PhotoImage(file="img/carteID.PNG")
    backcard = Label(Fenetre2, image=imgcard)
    backcard.place(x=-2, y=-2)

    imgwomen = PhotoImage(file="img/women.PNG")
    backwomen = Label(Fenetre2, image=imgwomen)
    if "F" in Sexe:
        backwomen.place(x=62, y=75)

    prenomID=Label(Fenetre2,text=Prenom)
    prenomID.configure(font=("Comic Sans MS", 18, "bold"), bg="#fffef9")
    prenomID.place(x=440, y=75)

    nomID=Label(Fenetre2,text=Nom)
    nomID.configure(font=("Comic Sans MS", 18, "bold"), bg="#fffef9")
    nomID.place(x=635, y=75)

    sexeID=Label(Fenetre2,text=Sexe)
    sexeID.configure(font=("Comic Sans MS", 18, "bold"), bg="#fffef9")
    sexeID.place(x=410, y=160)

    ageID=Label(Fenetre2,text=Age)
    ageID.configure(font=("Comic Sans MS", 18, "bold"), bg="#fffef9")
    ageID.place(x=527, y=160)

    paysID=Label(Fenetre2,text=Pays)
    paysID.configure(font=("Comic Sans MS", 12, "bold"), bg="#fffef9")
    paysID.place(x=668, y=168)

    argentID=Label(Fenetre2,text=Argent)
    argentID.configure(font=("Comic Sans MS", 15, "bold"), bg="#fffef9")
    argentID.place(x=450, y=248)

    rangID=Label(Fenetre2,text=Rang)
    rangID.configure(font=("Comic Sans MS", 18, "bold"), bg="#fffef9")
    rangID.place(x=703, y=247)

    autreID=Label(Fenetre2,text=Autre)
    autreID.configure(font=("Comic Sans MS", 15, "bold"), bg="#fffef9")
    autreID.place(x=438, y=335)

    if not 'NaN' in Photo:
        imgID = PhotoImage(file=Photo)
        photoID = Label(Fenetre2, image=imgID)
        photoID.place(x=62, y=76)

    Fenetre2.mainloop() #Fin de la fenetre principale


#-------------------------------------------Tkinter--------------------------------------------------#



#-------------------------------------------PyGame---------------------------------------------------#

pygame.init()

pygame.display.set_caption("Wiki | Riche - Personne Fortuné")
taille = largeur, hauteur = 700, 400  # taille de la fenêtre
fenetre = pygame.display.set_mode(taille)  # def la taille avec la ligne juste au dessus

nbcurseur = 1

background_menu = pygame.image.load("img/menu.png").convert()
rect_backmenu = background_menu.get_rect()

add_button = pygame.image.load("img/button1.png").convert_alpha()
rect_add_button = add_button.get_rect()
rect_add_button.x, rect_add_button.y = 236, 268  # place l'image sur l'écran

search_button = pygame.image.load("img/button2.png").convert_alpha()
rect_search_button = search_button.get_rect()
rect_search_button.x, rect_search_button.y = 236, 181  # place l'image sur l'écran

def pointer():
    global nbcurseur
    """
        procédure qui place une image de curseur sur celui de base en temps réel
    """
    if nbcurseur == 1:
        nbcurseur = "img/curseur1.png"
    elif nbcurseur == 2:
        nbcurseur = "img/curseur2.png"
    curseur = pygame.image.load(
        nbcurseur).convert_alpha()  # "convert_alpha()" permet d'importer l'image avec sa transparence (png)
    curseur_rect = curseur.get_rect()
    x, y = pygame.mouse.get_pos()  # prend la position de la souris en temps réel
    curseur_rect.x, curseur_rect.y = x, y  # applique les postions de la lignes au dessus au nouveaux curseur
    fenetre.blit(curseur, curseur_rect)  # affiche le nouveau curseur
    pygame.display.flip()  # raffraichit l'écran

def main_menu():
    global nbcurseur
    menu = 1
    pygame.mouse.set_visible(False)  # cacher la souris de base pour mettre la nouvelle (personnalisé)
    while menu:
        pointer()
        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                menu = 0 #termine la boucle menu
            if event.type == KEYDOWN:  # si une touche pressé
                if event.key == K_ESCAPE:  # si touche echap pressé
                    menu = 0  # On arrête la boucle
            if event.type == pygame.MOUSEBUTTONDOWN:  # si click souris pressé
                if rect_search_button.collidepoint(event.pos):
                    recherche()
                if rect_add_button.collidepoint(event.pos):
                    ajouter()
        if rect_search_button.collidepoint(pygame.mouse.get_pos()) or rect_add_button.collidepoint(pygame.mouse.get_pos()):
            #si curseur survole le button play, quitter ou menu principale
            nbcurseur = 2  # affiche le curseur 2, la main
        else:  # sinon, laisse le curseur 1
            nbcurseur = 1
        fenetre.blit(background_menu, rect_backmenu)
        fenetre.blit(search_button, rect_search_button)
        fenetre.blit(add_button, rect_add_button)

main_menu()

pygame.quit()

#-------------------------------------------PyGame---------------------------------------------------#