#########################################
# groupe 4 MPCI TD07 
# Iness MOUSSAOUI
# Myriem EL ALAOUI
# Tommy RAMAROSON
# https://github.com/uvsq22007167/PROJET_SNAKE
#########################################

############################################# IMPORTATION DES MODULES #############################################################
import tkinter as tk
from random import randrange

############################################# INITIALISATION VARIABELS GOBALES ####################################################
WIDTH = 700
HEIGHT = 500
LARGEURavcMUR = 650
HAUTEURavcMUR = 450
dx, dy = 0, 0
x, y = [100, 112], [100, 112]
snake = []
v = 0
goal = 0
i, j = 0, 0
z = 400
p = 100
r = 20
n = 1
k = 1
sauvegarde_score = r"C:Fichier_score.txt"
############################################# FONCTIONS ############################################################################

"Fonction permettant la mise en mouvement du serpent"

def move_snake():
    global dx, dy, x, y, snake, z, goal, k, j, i, déplacement
    coté = len(snake) - 1

    #Tant qu'un cercle est différent de 0, il reprendra les coordonnées du précédent dans la liste serpent 
    
    while coté != 0:
        x[coté] = x[coté - 1]
        y[coté] = y[coté - 1]
        coté -= 1

    #modification des coordonnées du premier carré

    x[0] += dx
    y[0] += dy
    coté = 0

    #On applique les nouvelles coordonnées aux carrés correspondant

    while coté != len(snake):
        canvas.coords(snake[coté], x[coté], y[coté],
                      x[coté] + 20, y[coté] + 20)
        coté += 1
    coté = 1

    #SI LE SERPENT MANGE LA POMME ALORS IL GRANDIT ET LE SCORE AUGMENTE

    if z - 7 <= x[0] <= z + 7 and p - 7 <= y[0] <= p + 7:                 
        goal += 1                                              
        score.config(text="Score = " + str(goal))           
        creation_pomme()
        augmentation_serpent()

    #MOUVEMENT CONTINUE DU SERPENT :

    if i != 1 and j != 1:
        déplacement = racine.after(k, move_snake)

    #SI LE SERPENT TOUCHE LE MUR ALORS ON A PERDU
        
    if (x[0] < 25 or x[0] > WIDTH - 35) or (y[0] < 25 or y[0] > HEIGHT - 35):
        racine.after_cancel(déplacement)
        fin_du_jeu()

    #SI LE SERPENT TOUCHE SON PROPRE CORPS ALORS ON A PERDU

    while coté != len(snake):
        if x[0] == x[coté] and y[0] == y[coté]:
            j = 1
            racine.after_cancel(déplacement)
            fin_du_jeu()
        coté += 1

def fin_du_jeu(): 
    " Fonction qui affiche le message lorsqu'on a perdu"

    f_end_game = tk.Tk()
    f_end_game.title("QUELLE DOMMAGE !")
    end_game= tk.Label(f_end_game, text = "GAME OVER " + "\n" + " Votre score est : " + str(goal))
    end_game.grid(rowspan=2,columnspan=3)
    recommencer = tk.Button (f_end_game, text= "FERMER", command= retour_menu)
    recommencer.grid(row= 4, columnspan = 5)

def retour_menu():
    " Fonction détruisant la fenètre de jeu une fois que l'on a perdu "
    racine.quit()

def creation_pomme():
    "Fonction qui crée et place aléatoirement la pomme "
    global z, p, r
    z = randrange(5, 66)
    p = randrange(5, 46)
    z = z * 10
    p = p * 10
    canvas.coords(apple, z, p, z + r, p + r)

def augmentation_serpent():
    " Fonction qui augmente la taille du serpent lorsqu'il mange une pomme "
    global n, x, y, snake, dx, dy
    serpents = canvas.create_oval(100, 100, 120, 120, fill='yellow')
    snake.append(serpents)
    x.append(x[n] + 12 + dx)
    y.append(y[n] + 12 + dy)
    n += 1

" Les fonctions permettant d'avoir 3 vitesses différentes "

def rapide(): 
    global k
    k = 30 
    fenetre_rapide = tk.Label(racine, text = "VITESSE : Rapide")
    fenetre_rapide.grid(row = 1,column=1)
    return k 

def moyen (): 
    global k
    k = 50
    fenetre_moyenne = tk.Label(racine, text = "VITESSE : Moyenne")
    fenetre_moyenne.grid(row = 1,column=1)

    return k, fenetre_moyenne 

def lent (): 
    global k
    k = 90
    fenetre_lente = tk.Label(racine, text = "VITESSE : Lente")
    fenetre_lente.grid(row = 1,column=1)
    return k, fenetre_lente


def move(event):
    " Fonction permettant le déplacement du serpent avec les flèches du clavier "
    global dx, dy, v
    key = event.keysym
    if key == "Up" or "Down" or "Left" or "Right":
        if key == "Up":
            dx, dy = 0, -10
        if key == "Down":
            dx, dy = 0, 10
        if key == "Left":
            dx, dy = -10, 0
        if key == "Right":
            dx, dy = 10, 0
        if v == 0:
            v = 1
            move_snake()

def arreter():
    "FONCTION PERMMETTANT DE METTRE PAUSE"
    canvas.after_cancel(déplacement)
    pause.config(text = "PLAY", command=play)

def play():
    "FONCTION PERMMETTANT DE METTRE PLAY APRÈS PAUSE"
    canvas.after(k, move_snake)
    pause.config(text = "PAUSE", command = arreter)
"Fonction créant un menu principal"

def menu_princiapl():
    titre_menu.grid_remove()
    pseudo_entrer.grid_remove()
    pseudo_label.grid_remove()
    démarrer.grid_remove()
    boutton_1.grid_remove()
    boutton_2.grid_remove()
    boutton_3.grid_remove()
    vitesse.grid_remove()
    pause.grid()
    canvas.grid()
    label.grid()
    score.grid()

"Fonction qui enregistre les scores ainsi que les pseudos de chaque partie "

def enregistre_sore():
    global score
    with open(sauvegarde_score, "a") as save_score:
        save_score.write(str(score) + " " + pseudo.get() + " \n")

##################################################### PROGRAMME PRINCIAPLE ################################################################
racine = tk.Tk()
racine.title("Game snake")
pseudo = tk.StringVar()

# création widjet pour le menu princiapl #

titre_menu = tk.Label(racine, text="SNAKE GAME",
                      font=("Times", "25", "italic"), fg="red")
pseudo_entrer = tk.Entry(racine, textvariable=pseudo)
pseudo_label = tk.Label(racine, text="Choisir un Pseudo :", font =("Times","20") )
démarrer = tk.Button(racine, text='DÉMARRER LE JEU', width=15, command=menu_princiapl)
vitesse = tk.Label(racine, text="À quelle vitesse voulez-vous jouer ?",
                   font=("Times","20"), fg="black")
boutton_1 = tk.Button(racine, text="Lente", command=lent)
boutton_2 = tk.Button(racine, text="Moyenne", command=moyen)
boutton_3 = tk.Button(racine, text="Rapide", command=rapide)
# positionnement des widjets dans la fenetre du menu principale #

titre_menu.grid(row=1, column=1, columnspan=3)
vitesse.grid(row=3, column=1, columnspan=4)
pseudo_entrer.grid(row=2, column=2)
pseudo_label.grid(row=2, column=1)
démarrer.grid(row=7, column=2)
boutton_1.grid(row=4, column=1)
boutton_2.grid(row=4, column=2)
boutton_3.grid(row=4, column=3)

# Création fenetre du jeu et positionenement widjet # 

canvas = tk.Canvas(racine, bg="green", width=WIDTH, height=HEIGHT)
canvas.grid(column = 0, row = 0, columnspan = 2)
canvas.grid_remove()
score = tk.Label(racine, text="POINTS : " + str(goal))
score.grid(column=0,row= 1)
score.grid_remove()
pause = tk.Button(racine, text = "PAUSE", command = arreter)
pause.grid(row = 4, columnspan = 2)
pause.grid_remove()
label = tk.Label(racine, textvariable = pseudo)
label.grid(columnspan=2, row= 3)
label.grid_remove()

#création du mur du Cnavas #

line_1 = canvas.create_line(0, 0, 700, 0, fill="black", width=45)
line_2 = canvas.create_line(700, 0, 700, 500, fill="black", width=45)
line_3 = canvas.create_line(0, 500, 700, 500, fill="black", width=45)
line_4 = canvas.create_line(0, 0, 0, 500, fill="black", width=45)

# création de la pomme et du serpent #

tete_serpent = canvas.create_oval(100, 100, 110, 110, fill="orange")
apple = canvas.create_oval(z, p, z + r, p + r, fill='red')
snake.append(tete_serpent)

# commande clavier #

canvas.bind_all("<Key>", move)

########################################################### FIN DU PROGRAMME ######################################################

racine.mainloop()