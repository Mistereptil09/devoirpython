from random import randint


# fonction principale
def main():
    # appelle la foction qui crée la grille de jeu
    colonne = choixTaille()
    # boucle principale du jeu

    while True:
        afficher(colonne)

        # le joueur joue
        placer(colonne)
        gagner = verifVictoire(colonne)
        # verifie si il gagne
        if gagner is not None:
            if gagner:
                print("Vous avez gagné !")
            else:
                print("Vous avez perdu !")
            break

        # l'adversaire joue
        adversaire(colonne)
        gagner = verifVictoire(colonne)
        # vérifie à nouveau
        if gagner is not None:
            if gagner:
                print("L'adversaire a gagné !")
            else:
                print("L'adversaire a perdu !")
            break

    # affiche la partie une dernière fois
    afficher(colonne)
    # demande au joueur si il veut recommencer
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


def choixTaille():
    # demande la taille de la grille
    while True:
        try:
            nombre = int(input("Entrez la taille de la grille souhaitée \n(un chiffre "
                               "trop grand entrainera des problemes d'affichages) \nVotre choix : "))
            if nombre < 3 :
                print("La taille minimale du morpion est de 3 !")
            else:
                break
        except ValueError:
            print("Veuillez entrer un chiffre entier !")
    # initialise les variables manquantes pour le foncionnement
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


def placer(colonne):
    # permet au joueur de placer son jeton sur la grille
    while True:
        # boucle qui permet de demander des inputs jusqu'a avoir une valeur qui correspond au demandes
        try:
            choix = int(input("Choisissez la ligne : ")) - 1
            choix2 = int(input("Choisissez la colone : ")) - 1
            # verifie que le choix est dans le tableau
            if 0 <= choix < len(colonne) and 0 <= choix2 < len(colonne):
                # vérifie si la case est vide
                if colonne[choix][choix2] == " ":
                    colonne[choix][choix2] = "X"
                    break
                else:
                    print("La case est déjà utilisée. Choisissez une autre case !")
            else:
                print(f"Veuillez choisir des indices dans la plage [1, {len(colonne)}]")
        except ValueError:
            print("Veuillez entrer des nombres entiers!")

def adversaire(colonne):
    # Algorithme qui place des jetons sur la grille
    # reatribution de la variable pour que ce soit plus clair
    taille = len(colonne)

    # defence
    # pose horizontale
    for i in range(taille):
        # verifie si chaque emplacement dans la ligne est egal a "O" et si la derniere case est vide
        if all(colonne[i][j] == "X" for j in range(taille - 1)) and colonne[i][taille - 1] == " ":
            # met un "O" dans la case libre
            colonne[i][taille - 1] = "O"
            return

    # pose verticale
    for i in range(taille):
        if all(colonne[j][i] == "X" for j in range(taille - 1)) and colonne[taille - 1][i] == " ":
            colonne[taille - 1][i] = "O"
            return

    # pose diagonale
    if all(colonne[i][i] == "X" for i in range(taille - 1)) and colonne[taille - 1][taille - 1] == " ":
        colonne[taille - 1][taille - 1] = "O"
        return

    # pose diagonale
    if all(colonne[i][taille - 1 - i] == "X" for i in range(taille - 1)) and colonne[taille - 1][0] == " ":
        colonne[taille - 1][0] = "O"
        return

    # attaque
    # pose horizontale
    for i in range(taille):
        if all(colonne[i][j] == "O" for j in range(taille - 1)) and colonne[i][taille - 1] == " ":
            colonne[i][taille - 1] = "O"
            return

    # pose verticale
    for i in range(taille):
        if all(colonne[j][i] == "O" for j in range(taille - 1)) and colonne[taille - 1][i] == " ":
            colonne[taille - 1][i] = "O"
            return

    # pose diagonale
    if all(colonne[i][i] == "O" for i in range(taille - 1)) and colonne[taille - 1][taille - 1] == " ":
        colonne[taille - 1][taille - 1] = "O"
        return

    # pose diagonale
    if all(colonne[i][taille - 1 - i] == "O" for i in range(taille - 1)) and colonne[taille - 1][0] == " ":
        colonne[taille - 1][0] = "O"
        return

    # pose un jeton au hasard dans la grille
    while True:
        choix = randint(0, taille - 1)
        choix2 = randint(0, taille - 1)
        if colonne[choix][choix2] == " ":
            colonne[choix][choix2] = "O"
            print("Aléatoire")
            break


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


main()
