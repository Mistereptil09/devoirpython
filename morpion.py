from random import randint


# fonction qui affiche le jeu
def afficher(colone, ligne, ligne2, ligne3):
    compte = 0
    for i in range(0, 5):
        # condition qui affiche les listes 'ligne' ou le else print("-----")
        if i == 0 or i == 2 or i == 4:
            print(''.join(colone[compte]))
            compte += 1
        else:
            print("-----")


# fonction qui demande ou placer la croie du joueur sur le plateau de jeu
def placer(ligne, ligne2, ligne3):
    # boucle prinicpale
    while True:
        # boucle pour le choix
        while True:
            try:
                choix = int(input("Choisissez la colonne : "))
                choix2 = int(input("Choisissez la ligne : "))

                # verifie si les choix sont dans la grille
                if 0 < choix2 < 4 and 0 < choix < 4 :
                    # ajuste les valeurs qui correspondent au cases vide dans les listes
                    if choix2 == 1:
                        choix2 = 0
                    if choix2 == 3:
                        choix2 = 4
                    break
                else:
                    print("Mettez un chiffre entre 1 et 3")

            except ValueError:
                print("Mettez un chiffre !")

        # applique le choix du joueur après avoir vérifié que la case soie vide
        if choix == 1:
            if ligne[choix2] == " ":
                ligne[choix2] = "X"
                break
            else:
                print("Cette case est déjà sélectionnée")

        elif choix == 2:
            if ligne2[choix2] == " ":
                ligne2[choix2] = "X"
                break
            else:
                print("Cette case est déjà sélectionnée")

        elif choix == 3:
            if ligne3[choix2] == " ":
                ligne3[choix2] = "X"
                break
            else:
                print("Cette case est déjà sélectionnée")

    return ligne, ligne2, ligne3


def victoire(ligne, ligne2, ligne3):
    # condition de victoire
    gagner = True
    l1 = 0
    l2 = 0
    l3 = 0
    d1 = 0
    d2 = 0
    d3 = 0
    # boucle dans les différentes la liste

    for i in range(0, 5):
        # vérifie la victoire en ligne
        
        if ligne[i] == "X":
            l1 += 1
        if ligne2[i] == "X":
            l2 += 1
        if ligne3[i] == "X":
            l3 += 1
        if l1 == 3 or l2 == 3 or l3 == 3:
            print("horizontal")
            return gagner

        if ligne[i] == "O":
            d1 -= 1
        if ligne2[i] == "O":
            d2 -= 1
        if ligne3[i] == "O":
            d3 -= 1
        if d1 == -3 or d2 == -3 or d3 == -3:
            print("horizontal")
            gagner = False
            return gagner

        # vérifie la victoire verticale
        if ligne[i] == ligne2[i] == ligne3[i] and ligne[i] != " ":
            if ligne[i] == "X":
                print("vertical")
                return gagner
            elif ligne[i] == "O":
                print("vertical")
                gagner = False
                return gagner

    # verifie la vicoire en diagonnale
    if ligne[i] == ligne2[i] == ligne3[i] and ligne[i] != " ":
        if ligne[i] == "X":
            print("diagonnale")
            return gagner
        elif ligne[i] == "O":
            print("diagonnale")
            gagner = False
        return gagner
    return None


def adversaire(ligne, ligne2, ligne3):
    while True:
        choix = randint(1,3)
        choix2 = randint(1,3)
        if choix2 == 1:
            choix2 = 0
        elif choix2 == 2:
            choix2 = 2
        if choix2 == 3:
            choix2 = 4

        elif choix == 1:
            if ligne[choix2] == " ":
                ligne[choix2] = "O"
                break
            else:
                print("Cette case est déjà sélectionnée")

        elif choix == 2:
            if ligne2[choix2] == " ":
                ligne2[choix2] = "O"
                break
            else:
                print("Cette case est déjà sélectionnée")

        elif choix == 3:
            if ligne3[choix2] == " ":
                ligne3[choix2] = "O"
                break
            else:
                print("Cette case est déjà sélectionnée")

    return ligne, ligne2, ligne3




def main():
    while True:
        # definition des variables
        ligne = [" ", "|", " ", "|", " "]
        ligne2 = [" ", "|", " ", "|", " "]
        ligne3 = [" ", "|", " ", "|", " "]
        colone = [ligne, ligne2, ligne3]

        while True:
            # appel des foncions
            gagner = victoire(ligne, ligne2, ligne3)
            if gagner == None:
                afficher(colone, ligne, ligne2, ligne3)
                ligne, ligne2, ligne3 = placer(ligne, ligne2, ligne3)
                ligne, ligne2, ligne3 = adversaire(ligne, ligne2, ligne3)
            elif gagner:
                print("Vous avez gagné !")
                break
            elif not gagner:
                print("Vous avez perdu !")
                break

        # réaffiche le jeu une dernière fois pour voir la raison de victoire/ defaite
        afficher(colone, ligne, ligne2, ligne3)
        print("Voulez vous rejouer ?")
        # petite boucle pour redémarrer une partie ou finir le jeu
        while True:
            try:
                choix = int(input("1 - Oui \n2- Non\n Votre choix : "))
                if choix == 1:
                    break
                if choix == 2:
                    print("Merci d'avoir joué")
                    return
            except ValueError:
                print("Veillez entrer un chiffre !")

if __name__ == "__main__":
    main()
