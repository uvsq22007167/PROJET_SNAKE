# PROJET_SNAKE

Explications du Jeu et du Programme :


1-	LE JEU : 

Snake consiste à ce qu’un joueur déplace un serpent définit au départ par une taille minimale à l’aide des 4 touches de déplacements du clavier (haut, bas, droite, gauche). 
Les déplacements ciblent précisément une “pomme”, qui à chaque collision avec sa “tête” le fera grandir. Ainsi le serpent atteindra une taille à partir de laquelle il deviendra un obstacle pour lui-même. Deux règles sont donc à respecter pour ne pas perdre :

Ne pas rentrer en contact avec l’une des 4 bordures 

Ne pas rentrer en collision avec lui-même lors d’un changement de direction 

Le jeu admet plusieurs niveaux de difficultés selon ses programmeurs (comme ajouter des obstacles et davantage de règles), mais nous concernant, nous avons choisi différentes vitesses de déplacement.

2- LE PROGRAMME : 

Pour réaliser ce programme, nous avons utilisé la librairie tkinter. 

Etapes :

1) construction d’une fenêtre et 4 murs définis par leur haut

2) construction d’une fenêtre et 4 murs définis par leur hauteur et largeur à l’aide des constantes (car les dimensions de la bordure ne changent pas) “HAUTEUR”, “LARGEUR”, “LARGEURavcMUR”, “HAUTEURavecMUR”.

2) définition des variables, comprenant coordonnée(s) / position(s), vitesse initiale de départ du serpent, et de la pomme.

3) créations de fonctions : 

“move_snake” : contribue à la mobilité du serpent, à l’aide des déplacements selon ses coordonnées x et y. 

- À l’aide de “while”, on crée une première condition pour laquelle le serpent aura de nouvelles coordonnées z et p.

 - Les deux variables i et j au départ nulles, servent au mouvement continue du serpent

- On crée également une seconde condition pour laquelle, si le serpent touche l’une des bordures, reconnues en tant que HEIGHT et WIDTH, le jeu se termine 

- On crée une troisième condition pour laquelle si le serpent touche son propre corps, alors le joueur a perdu

“fin du jeu” : contribue à faire perdre le joueur lorsque qu’il aura enfreint l’une des conditions de “move_snake”. 

- Le jeu affiche “QUEL DOMMAGE !” ainsi que “GAME OVER” accompagné du score du joueur, correspondant au nombre de pommes mangées. 

- On crée un bouton “recommencer” qui redirige le joueur vers le menu, afin de reprendre une nouvelle partie.

“retour_menu” : sert à détruire la fenêtre du jeu une fois que le joueur a perdu.

“creation_pomme” : crée et place aléatoirement la pomme


“rapide”; “moyen”; “lent” : sert à définir 3 vitesses du jeu différentes.

- La variable K représente la vitesse, elle varie de 30, à 50, à 90 selon le niveau choisi.

 - Fenetre_rapide/moyenne/lente sert à afficher sur la fenêtre la vitesse choisie.

“move” : contribue à la mobilité du serpent à l’aide des 4 touches de déplacements du clavier (up, down, left, right)


- Les déplacement x et y varient entre 0 et 10 ou –10 selon la direction choisie.

“arreter” : permet de mettre pause au jeu puis de rejouer en affichant “play” 

“play" : permet au joueur de reprendre après avoir cliqué sur pause.

4) Création de widjet pour le menu principal :

- “titre_menu” affiche le nom du jeu sur la fenêtre avec différentes caractéristiques choisies : italic, red etc.. 
 
- Pseudo_entrer et pseudo_label permet au joueur de rentrer un pseudo de son choix dans “choisir un pseudo”
 - 
“démarrer” affiche “DEMARRER LE JEU” 

- “vitesse” affiche “A quelle vitesse voulez-vous jouer ?”

 - Bouton_1 / 2 / 3 correspondent aux trois vitesses du jeu

Ensuite à l’aide de .grid, on choisit l’emplacement des 8 widjets dans la fenêtre

5) création de la fenêtre du jeu à l’aide de Canvas, Score, Pause et label pour choisir la hauteur, la largeur, choisir les couleurs et afficher le score. 

6) création du mur du Canvas en définissant 4 lignes d’une largeur de 45 avec le mur principal. 

7) Création du serpent et de la pomme : pour créer la tête du serpent sous forme d’ovale, on utilise canvas.create_oval de dimension 110 et de couleur orange. Pour créer la pomme, on utilise les variables z et p du début de programme et on choisit la couleur red. 

8) la commande canvas.bind_all permet d’uiliser les touches de déplacement.

9) racine.mainloop() permet au fonctionnement des fonctions.

3 - COMMENT UTILISER LE JEU ? 

1) ENTRER UN PSEUDO 

2) INDIQUER LA VITESSE SOUHAITÉE EN CLIQUANT DESSUS (RAPIDE , LENTE , MOYENNE) 

3) CLIQUER SUR " DÉMARRER LE JEU " 

4) POUR COMMENCER, IL FAUT CLIQUER SUR L'UNE DES FLÊCHES DU CLAVIER (FLÊCHE DU HAUT : POUR ALLER EN HAUT, BAS POUR EN BAS ETC.) 

5) LORSQUE VOUS AVEZ PERDU CLIQUER SUR LE BOUTON "FERMER" CELA FERMERA LE JEU
