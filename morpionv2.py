from random import randint


# fonction principale
def main():
    # boucle qui demande la valeur jusqu'à l'obtention d'une valeur exploitable
    while True:
        try:
            # demande le type de partie souhaitée
            jeu = int(input("Voulez vous jouer avec : \n1 - L'algorithme \n2 - Un adversaire aléatoire ? "
                             "\n3 - Un autre joueur ? \nEntrez un Votre choix : "))
            if 1 <= jeu <= 3:
                break
        except ValueError:
            print("Entrez un nombre entier !")
    # appelle la fonction qui crée la grille de jeu
    colonne = choixTaille()

    # choisi le type de partie qui va être jouée
    if jeu == 1:
        print("Joueur => X \nAdversaire => O\n Bonne Chance !")
        jeuAlgo(colonne)
    elif jeu == 2:
        print("Joueur => X \nAdversaire => O\n Bonne Chance !")
        jeuAleatoire(colonne)
    elif jeu == 3:
        print("Joueur1 => X \nJoueur2 => O\n Que le meilleur gagne !")
        jeuJoueur(colonne)

    # affiche la partie une dernière fois
    afficher(colonne)
    # demande au joueur s'il veut recommencer
    while True:
        try:
            jouer = int(input("Voulez-vous rejouer ? \n1 - Oui \n 2 - Non \nVotre choix : "))
            if jouer == 1:
                main()
            elif jouer == 2:
                print("Merci d'avoir joué !")
                break
            else:
                print("S'il vous plaît, mettez un nombre entre 1 et 2 !")
        except ValueError:
            print("Mettez un nombre entier !")


# code du jeu si le choix de jouer avec l'algo est choisi
def jeuAlgo(colonne):
    while True:
        # affiche la grille
        afficher(colonne)
        # le joueur joue
        placer(colonne, "X")
        # vérifie si il gagne
        gagner = verifVictoire(colonne)
        if gagner is not None:
            if gagner:
                print("Vous avez gagné !")
            else:
                print("Vous avez perdu !")
            return
        # l'adversaire joue avec l'algorithme
        afficher(colonne)
        adversaire(colonne)
        gagner = verifVictoire(colonne)
        # vérifie à nouveau
        if gagner is not None:
            if gagner:
                print("Vous avez gagné !")
            else:
                print("Vous avez perdu !")
            return


# code pour le jeu en aléatoire
def jeuAleatoire(colonne):
    while True:
        # affiche la grille
        afficher(colonne)
        # le joueur joue
        placer(colonne, "X")
        # vérifie si il gagne
        gagner = verifVictoire(colonne)
        if gagner is not None:
            if gagner:
                print("Vous avez gagné !")
            else:
                print("Vous avez perdu !")
            return
        # l'adversaire joue aléatoirement
        afficher(colonne)
        poseAleatoire(colonne)
        gagner = verifVictoire(colonne)
        # vérifie à nouveau
        if gagner is not None:
            if gagner:
                print("Vous avez gagné !")
            else:
                print("Vous avez perdu !")
            return


# code pour le jeu avec un 2e joueur
def jeuJoueur(colonne):
    while True:
        # affiche la grille
        afficher(colonne)
        # le joueur joue
        placer(colonne, "X")
        # vérifie si il gagne
        gagner = verifVictoire(colonne)
        if gagner is not None:
            if gagner:
                print("Joueur 1 gagne !")
            else:
                print("Joueur 2 gagne !")
            return
        # l'adversaire est joué par un 2e joueur
        afficher(colonne)
        placer(colonne, "O")
        gagner = verifVictoire(colonne)
        # vérifie à nouveau
        if gagner is not None:
            if gagner:
                print("Joueur 1 gagne !")
            else:
                print("Joueur 2 gagne !")
            return


def choixTaille():
    # demande la taille de la grille
    while True:
        try:
            nombre = int(input("Entrez la taille de la grille souhaitée \n(un chiffre "
                               "trop grand entrainera des problèmes d'affichages) \nVotre choix : "))
            if nombre < 3:
                print("La taille minimale du morpion est de 3 !")
            else:
                break
        except ValueError:
            print("Veuillez entrer un chiffre entier !")
    # initialise les variables manquantes pour le fonctionnement
    colonne = []
    ligne = []

    # initialise la grille avec des espaces vides
    for i in range(nombre):
        ligne.append(" ")
    for i in range(nombre):
        colonne.append(list(ligne))
    return colonne


def afficher(colonne):
    # affiche la grille
    for i in range(len(colonne)):
        for j in range(len(colonne)):
            if j == len(colonne) - 1:
                print(colonne[i][j])
            else:
                print(f"{colonne[i][j]} |", end=" ")
        if i != len(colonne) - 1:
            print("-" * (4 * len(colonne) - 3))
    return colonne


def placer(colonne, pose):
    # permet au joueur de placer son jeton sur la grille
    while True:
        # boucle qui permet de demander des inputs jusqu'avoir une valeur qui correspond aux demandes
        try:
            choix = int(input("Choisissez la ligne : ")) - 1
            choix2 = int(input("Choisissez la colonne : ")) - 1
            # vérifie que le choix est dans le tableau
            if 0 <= choix < len(colonne) and 0 <= choix2 < len(colonne):
                # vérifie si la case est vide
                if colonne[choix][choix2] == " ":
                    colonne[choix][choix2] = pose
                    break
                else:
                    print("La case est déjà utilisée. Choisissez une autre case !")
            else:
                print(f"Veuillez choisir des indices dans la plage [1, {len(colonne)}]")
        except ValueError:
            print("Veuillez entrer des nombres entiers!")


def adversaire(colonne):
    # Algorithme qui place des jetons sur la grille
    # attribution de la variable pour que ce soit plus clair
    resultat = attaque(colonne)
    if resultat == None:
        resultat2 = defence(colonne)
        if resultat2 == None:
            poseAleatoire(colonne)


# algorithme d'attaque
def attaque(colonne):
    taille = len(colonne)
    # Pose horizontale
    for i in range(taille):
        if all(colonne[i][j] == "O" for j in range(taille - 1)) and colonne[i][taille - 1] == " ":
            colonne[i][taille - 1] = "O"
            return

    # Pose verticale
    for i in range(taille):
        count_O = sum(colonne[j][i] == "O" for j in range(taille))
        if count_O == taille - 1 and colonne[taille - 1][i] == " ":
            colonne[taille - 1][i] = "O"
            return

    # Pose diagonale (haut-gauche à bas-droite)
    count_O_diag1 = sum(colonne[i][i] == "O" for i in range(taille))
    if count_O_diag1 == taille - 1 and colonne[taille - 1][taille - 1] == " ":
        colonne[taille - 1][taille - 1] = "O"
        return

    # Pose diagonale (haut-droite à bas-gauche)
    count_O_diag2 = sum(colonne[i][taille - 1 - i] == "O" for i in range(taille))
    if count_O_diag2 == taille - 1 and colonne[taille - 1][0] == " ":
        colonne[taille - 1][0] = "O"
        return
    return None

# algorithme de défence
def defence(colonne):
    taille = len(colonne)
    # Pose horizontale
    for i in range(taille):
        if all(colonne[i][j] == "X" for j in range(taille - 1)) and colonne[i][taille - 1] == " ":
            colonne[i][taille - 1] = "O"
            return

    # Pose verticale
    for i in range(taille):
        count_X = sum(colonne[j][i] == "X" for j in range(taille))
        if count_X == taille - 1 and colonne[taille - 1][i] == " ":
            colonne[taille - 1][i] = "O"
            return

    # Pose diagonale (haut-gauche à bas-droite)
    count_X_diag1 = sum(colonne[i][i] == "X" for i in range(taille))
    if count_X_diag1 == taille - 1 and colonne[taille - 1][taille - 1] == " ":
        colonne[taille - 1][taille - 1] = "O"
        return

    # Pose diagonale (haut-droite à bas-gauche)
    count_X_diag2 = sum(colonne[i][taille - 1 - i] == "X" for i in range(taille))
    if count_X_diag2 == taille - 1 and colonne[taille - 1][0] == " ":
        colonne[taille - 1][0] = "O"
        return
    return None

# fonction de pose aléatoire
def poseAleatoire(colonne):
    taille = len(colonne)
    # Pose un jeton au hasard dans la grille
    while True:
        choix = randint(0, taille - 1)
        choix2 = randint(0, taille - 1)
        if colonne[choix][choix2] == " ":
            colonne[choix][choix2] = "O"
            print("Aléatoire")
            return


def verifVictoire(colonne):
    # Vérification horizontale
    for l in range(len(colonne)):
        if all(colonne[l][i] == "X" for i in range(len(colonne[l]))):
            return True
        elif all(colonne[l][i] == "O" for i in range(len(colonne[l]))):
            return False

    # Vérification verticale
    for i in range(len(colonne)):
        if all(colonne[l][i] == "X" for l in range(len(colonne))):
            return True
        elif all(colonne[l][i] == "O" for l in range(len(colonne))):
            return False

    # Vérification diagonale gauche vers la droite
    if all(colonne[i][i] == "X" for i in range(len(colonne))):
        return True
    elif all(colonne[i][i] == "O" for i in range(len(colonne))):
        return False

    # Vérification diagonale droite vers la gauche
    if all(colonne[i][len(colonne) - 1 - i] == "X" for i in range(len(colonne))):
        return True
    elif all(colonne[i][len(colonne) - 1 - i] == "O" for i in range(len(colonne))):
        return False

    # Aucune victoire
    return None


if __name__ == "__main__":
    main()
