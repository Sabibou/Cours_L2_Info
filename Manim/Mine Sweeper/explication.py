from manim import *
import random

# On met la seed
random.seed(0)


class Explication(MovingCameraScene):
    def construct(self):
        # On va faire une animation sur des listes doublement chaînées :

        # On veut représenter un démineur
        # On a une grille de 10x10 cases
        # Chaque case est reliée à ses voisines doublement (nord, sud, est, ouest, nord-est, nord-ouest, sud-est, sud-ouest)
        # Chaque case peut être vide, contenir un mine, ou contenir un nombre
        # On va représenter les cases par des carrés, et les mines par des cercles
        # On va représenter les nombres par des textes

        # On met un titre "L'algorithme du démineur"
        title = Text("L'algorithme du démineur")
        self.play(Write(title))

        # On attend 3s
        self.wait(7)

        # On efface le titre
        self.play(FadeOut(title))

        MINE_PERCENTAGE = 0.4
        GRID_SIZE = 10
        CELL_SIZE = 0.5
        CELL_PADDING = 0.1
        CELL_COLOR = WHITE
        MINE_COLOR = RED
        NUMBER_COLOR = BLACK

        # On va générer la grille pour pouvoir la manipuler
        grid = []

        for i in range(GRID_SIZE):
            grid.append([])
            for j in range(GRID_SIZE):
                grid[i].append({
                    "type": "empty",  # Type a pour valeur "empty", "mine" ou "number"
                    "neighbors": 0  # Nombre de voisins
                })

        # On va générer les mines
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if random.random() < MINE_PERCENTAGE:
                    grid[i][j]["type"] = "mine"

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if grid[i][j]["type"] == "mine":
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if i + x >= 0 and i + x < GRID_SIZE and j + y >= 0 and j + y < GRID_SIZE:
                                grid[i + x][j + y]["neighbors"] += 1

        # On va dessiner la grille, les mines, et les nombres, l'animation au total doit durer 3s
        # La grille va s'afficher instantanément, les mines et les nombres vont apparaître progressivement

        # On va créer un groupe pour la grille
        grid_group = VGroup()

        # On va créer un groupe pour les mines
        mines_group = VGroup()

        # On va créer un groupe pour les nombres
        numbers_group = VGroup()

        # On va créer un groupe pour tout
        all_group = VGroup()

        # On va tout créer au centre de l'écran
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                # On va créer la case
                cell = Square(side_length=CELL_SIZE, color=CELL_COLOR)

                # On va la positionner
                cell.move_to([i * CELL_SIZE - GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2,
                             j * CELL_SIZE - GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2, 0])

                # On va l'ajouter au groupe de la grille
                grid_group.add(cell)

                # On va créer la mine
                if grid[i][j]["type"] == "mine":
                    mine = Circle(radius=CELL_SIZE / 2 -
                                  CELL_PADDING, color=MINE_COLOR)

                    # On va la positionner
                    mine.move_to([i * CELL_SIZE - GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2,
                                 j * CELL_SIZE - GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2, 0])

                    # On va l'ajouter au groupe des mines
                    mines_group.add(mine)

                # On va créer le nombre
                if grid[i][j]["type"] == "number":
                    number = Text(
                        str(grid[i][j]["neighbors"]), color=NUMBER_COLOR)

                    # On va le positionner
                    number.move_to([i * CELL_SIZE - GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2,
                                   j * CELL_SIZE - GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2, 0])

                    # On va l'ajouter au groupe des nombres
                    numbers_group.add(number)

        # On va ajouter les groupes à all_group
        all_group.add(grid_group)
        all_group.add(mines_group)
        all_group.add(numbers_group)

        # On va faire apparaître la grille
        self.play(Write(grid_group))

        # On va faire apparaître les mines
        self.play(Write(mines_group))

        # On va faire apparaître les nombres
        self.play(Write(numbers_group))

        # On attend 2s
        self.wait(2)

        # On zoom sur la case du milieu, on centre bien la case
        self.play(self.camera.frame.animate.scale(1/3).move_to(
            grid_group[GRID_SIZE * GRID_SIZE // 2 + GRID_SIZE // 2]))

        # On colorie la case du milieu en bleu (on la remplie)
        self.play(grid_group[GRID_SIZE * GRID_SIZE // 2 +
                  GRID_SIZE // 2].animate.set_fill(BLUE, opacity=.5))

        self.wait(4)

        # On fait un groupe pour les voisines
        neighbors_group = VGroup()

        # On colorie ses voisines en vert (on les remplies) sauf celle du milieu
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x != 0 or y != 0:
                    neighbors_group.add(
                        grid_group[GRID_SIZE * GRID_SIZE // 2 + GRID_SIZE // 2 + x + y * GRID_SIZE])

        self.play(neighbors_group.animate.set_fill(GREEN, opacity=.5))

        self.wait(6)

        # On fait des flèches pour les voisines
        neighbors_arrows = VGroup()

        for x in range(-1, 2):
            for y in range(-1, 2):
                if x != 0 or y != 0:
                    arrow = Arrow(
                        grid_group[GRID_SIZE * GRID_SIZE //
                                   2 + GRID_SIZE // 2].get_center(),
                        grid_group[GRID_SIZE * GRID_SIZE // 2 +
                                   GRID_SIZE // 2 + x + y * GRID_SIZE].get_center(),
                        buff=0,
                        color=RED
                    )

                    neighbors_arrows.add(arrow)

        self.play(Write(neighbors_arrows))

        self.wait(10)

        # On déplace la caméra de CELL_SIZE vers le bas
        self.play(self.camera.frame.animate.move_to(
            [CELL_SIZE/2, -CELL_SIZE/2, 0]))

        # On colorie la case du bas en bleu (on la remplie)
        self.play(grid_group[GRID_SIZE * GRID_SIZE // 2 +
                             GRID_SIZE // 2 - 1].animate.set_fill(PURPLE, opacity=.5))

        self.wait(4)

        # On enlève les flèches
        self.play(FadeOut(neighbors_arrows))

        self.wait(.5)

        # On ajoute une flèche pour la case du bas vers la case du milieu
        arrow = Arrow(
            grid_group[GRID_SIZE * GRID_SIZE // 2 +
                       GRID_SIZE // 2 - 1].get_center(),
            grid_group[GRID_SIZE * GRID_SIZE //
                       2 + GRID_SIZE // 2].get_center(),
            buff=0,
            color=RED
        )

        self.play(Write(arrow))

        self.wait(8)

        # On enlève la flèche
        self.play(FadeOut(arrow))

        # On déplace la caméra de CELL_SIZE vers le haut
        self.play(self.camera.frame.animate.move_to(
            [CELL_SIZE/2, CELL_SIZE/2, 0]))

        # On colorie les cases autour de la case du milieu en jaune (on les remplies)
        self.play(neighbors_group.animate.set_fill(YELLOW, opacity=.5))

        # On fait des flèches qui partent des voisines vers la case du milieu
        neighbors_arrows = VGroup()

        for x in range(-1, 2):
            for y in range(-1, 2):
                if x != 0 or y != 0:
                    arrow = Arrow(
                        grid_group[GRID_SIZE * GRID_SIZE // 2 +
                                   GRID_SIZE // 2 + x + y * GRID_SIZE].get_center(),
                        grid_group[GRID_SIZE * GRID_SIZE //
                                   2 + GRID_SIZE // 2].get_center(),
                        buff=0,
                        color=RED
                    )

                    neighbors_arrows.add(arrow)

        self.play(Write(neighbors_arrows))

        self.wait(6)

        # On enlève les flèches
        self.play(FadeOut(neighbors_arrows))

        self.wait(4)

        # On va :
        # Pour chaque voisine, faire une flèche du milieu vers la voisine
        # Puis incrémenter le nombre de voisines QUI CONTIENNENT UNE BOMBE et afficher le nouveau nombre dans la cellule du milieu
        n = 0

        # On affiche le nombre de voisines de la case du milieu
        number = Text(
            str(n), color=WHITE)

        # On va le positionner
        number.move_to([CELL_SIZE/2, CELL_SIZE/2, 10])

        # Réduire sa taille
        number.scale(1/2)

        # On l'ajoute au groupe des nombres
        numbers_group.add(number)

        # On fait apparaître le nombre en noir
        self.play(Write(number))

        self.wait(3)

        arrowGroup = VGroup()

        for x in range(-1, 2):
            for y in range(-1, 2):
                if x != 0 or y != 0:
                    # On fait une flèche du milieu vers la voisine
                    arrow = Arrow(
                        grid_group[GRID_SIZE * GRID_SIZE //
                                   2 + GRID_SIZE // 2].get_center(),
                        grid_group[GRID_SIZE * GRID_SIZE // 2 +
                                   GRID_SIZE // 2 + x + y * GRID_SIZE].get_center(),
                        buff=0,
                        color=RED
                    )

                    arrowGroup.add(arrow)

                    self.play(Write(arrow), run_time=.15)

                    # Si la case actuelle contient une bombe, on utilise le grid[x][y]["type"] == "mine" pour vérifier
                    # On doit calculer la position de la case actuelle dans le tableau à partir de la position de la case du milieu
                    cellX = GRID_SIZE // 2 + x
                    cellY = GRID_SIZE // 2 + y

                    if grid[cellX][cellY]["type"] == "mine":

                        self.play(FadeOut(number))

                        # On incrémente le nombre de voisines qui contiennent une bombe
                        n += 1

                        # On affiche le nouveau nombre de voisines de la case du milieu
                        number = Text(
                            str(n), color=WHITE)

                        # On va le positionner
                        number.move_to([CELL_SIZE/2, CELL_SIZE/2, 10])

                        # Réduire sa taille
                        number.scale(1/2)

                        # On l'ajoute au groupe des nombres
                        numbers_group.add(number)

                        # On fait apparaître le nombre en noir
                        self.play(Write(number))

        self.wait(5)

        # On enlève les flèches
        self.play(FadeOut(arrowGroup))

        # On enlève le nombre
        self.play(FadeOut(number))

        self.wait(1)

        # On dézoom et on déplace la caméra en 00
        self.play(self.camera.frame.animate.scale(
            1/CELL_SIZE).move_to([0, 0, 0]))

        self.wait(3)

        # On va faire apparaître les nombres de voisines de chaque case
        neighbors_numbers = VGroup()

        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):

                if (grid[x][y]["type"] == "mine"):
                    continue

                # On affiche le nombre de voisines de la case du milieu
                number = Text(
                    str(grid[x][y]["neighbors"]), color=WHITE)

                # On va le positionner
                number.move_to([x * CELL_SIZE - GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2,
                                y * CELL_SIZE - GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2, 0])

                # Réduire sa taille
                number.scale(1/2)

                # On fait apparaître le nombre en noir
                neighbors_numbers.add(number)

        self.play(Write(neighbors_numbers))

        self.wait(8)

        # On enlève les nombres et on enlève les cases et les cercles
        self.play(FadeOut(neighbors_numbers), FadeOut(grid_group),
                  FadeOut(mines_group), FadeOut(numbers_group))

        # On fait du texte avec écrit "Génération de la grille"
        text = Text("Génération de la grille", color=WHITE)

        # On le positionne
        text.move_to([0, 0, 0])

        # On l'affiche
        self.play(Write(text))

        self.wait(7)

        # On enlève le texte
        self.play(FadeOut(text))

        # On fait apparaître une cellule en haut à gauche
        cell = Square(
            side_length=CELL_SIZE,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=0
        )

        # On la positionne
        cell.move_to([-GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2,
                      GRID_SIZE * CELL_SIZE / 2 - CELL_SIZE / 2, 0])

        # On l'affiche
        self.play(Write(cell))

        self.wait(.4)

        # On zoom sur la cellule
        self.play(self.camera.frame.animate.scale(CELL_SIZE).move_to([-GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2,
                                                                      GRID_SIZE * CELL_SIZE / 2 - CELL_SIZE / 2, 0]))

        # On ajoute des flèches orientées
        arrows = VGroup()

        for x in range(-1, 2):
            for y in range(-1, 2):
                if x != 0 or y != 0:
                    arrow = Arrow(
                        cell.get_center(),
                        cell.get_center() + [x * CELL_SIZE, y * CELL_SIZE, 0],
                        buff=0,
                        color=RED
                    )

                    arrows.add(arrow)

        self.play(Write(arrows))

        self.wait(8)

        # On ne garde que les flèches orientées vers la droite, le bas, et bas droite
        for arrow in arrows:
            if arrow.get_end()[0] < cell.get_center()[0] or arrow.get_end()[1] > cell.get_center()[1]:
                self.play(FadeOut(arrow), run_time=.1)

        self.wait(4)

        # On ajoute une cellule à droite de la première
        cell2 = Square(
            side_length=CELL_SIZE,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=0
        )

        # On la positionne avec un écart de CELL_SIZE
        cell2.move_to([-GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2,
                       GRID_SIZE * CELL_SIZE / 2 - CELL_SIZE / 2, 0])

        # On l'affiche
        self.play(Write(cell2))

        self.wait(.4)

        # On ajoute une flèche orientée en bleu depuis la cellule de droite vers la cellule de gauche
        arrow = Arrow(
            cell2.get_center(),
            cell.get_right(),
            buff=0,
            color=BLUE
        )

        self.play(Write(arrow))

        self.wait(5)

        # On enlève la flèche
        self.play(FadeOut(arrow))

        # On rajoute une cellule encore plus à droite
        cell3 = Square(
            side_length=CELL_SIZE,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=0
        )

        # On la positionne avec un écart de CELL_SIZE
        cell3.move_to([-GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2,
                       GRID_SIZE * CELL_SIZE / 2 - CELL_SIZE / 2, 0])

        # On l'affiche
        self.play(Write(cell3))

        # On ajoute une flèche orientée en bleu depuis la cellule 3 vers la cellule 2
        arrow = Arrow(
            cell3.get_center(),
            cell2.get_right(),
            buff=0,
            color=BLUE
        )

        self.play(Write(arrow))

        self.wait(5)

        # On enlève la flèche
        self.play(FadeOut(arrow))

        # On rajoute trois petits points pour indiquer qu'il y a des cellules après
        dots = Text("...", color=WHITE)

        # On les positionne
        dots.move_to([-GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2,
                      GRID_SIZE * CELL_SIZE / 2 - CELL_SIZE / 2, 0])

        # On les affiche
        self.play(Write(dots))

        self.wait(4)

        # On dézoom légèrement

        self.play(self.camera.frame.animate.scale(1/CELL_SIZE).move_to([-GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2,
                                                                            GRID_SIZE * CELL_SIZE / 2 - CELL_SIZE / 2, 0]))

        self.wait(6)

        # On rajoute une cellule en bas à gauche
        cell4 = Square(
            side_length=CELL_SIZE,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=0
        )

        # On la positionne avec un écart de CELL_SIZE
        cell4.move_to([-GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2,
                          GRID_SIZE * CELL_SIZE / 2 - CELL_SIZE / 2 - CELL_SIZE - CELL_SIZE / 2, 0])
        
        # On l'affiche
        self.play(Write(cell4))

        self.wait(.4)

        # On ajoute une flèche orientée en bleu depuis la cellule 4 vers la cellule 1
        arrow = Arrow(
            cell4.get_center(),
            cell.get_center(),
            buff=0,
            color=BLUE
        )

        self.play(Write(arrow))

        self.wait(4)

        # On enlève la flèche
        self.play(FadeOut(arrow))

        # On rajoute une flèche orientée en bleu depuis la cellule 4 vers la cellule 2
        arrow = Arrow(
            cell4.get_center(),
            cell2.get_center(),
            buff=0,
            color=BLUE
        )

        self.play(Write(arrow))

        self.wait(4)

        # On enlève la flèche
        self.play(FadeOut(arrow))

        # On rajoute une flèche orientée en bleu depuis la cellule 2 vers la cellule 4
        arrow = Arrow(
            cell2.get_center(),
            cell4.get_center(),
            buff=0,
            color=ORANGE
        )

        self.play(Write(arrow))

        self.wait(3)

        # On enlève la flèche
        self.play(FadeOut(arrow))

        # On ajoute une cellule en bas à droite
        cell5 = Square(
            side_length=CELL_SIZE,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=0
        )

        # On la positionne avec un écart de CELL_SIZE
        cell5.move_to([-GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2,
                            GRID_SIZE * CELL_SIZE / 2 - CELL_SIZE / 2 - CELL_SIZE - CELL_SIZE / 2, 0])
        
        # On l'affiche
        self.play(Write(cell5))

        self.wait(.2)

        # On ajoute une flèche orientée en bleu depuis la cellule 5 vers la cellule 1

        arrow = Arrow(
            cell5.get_center(),
            cell.get_center(),
            buff=0,
            color=BLUE
        )

        self.play(Write(arrow))

        self.wait(.2)

        # On enlève la flèche
        self.play(FadeOut(arrow))

        # On ajoute une flèche orientée en bleu depuis la cellule 5 vers la cellule 2
        arrow = Arrow(
            cell5.get_center(),
            cell2.get_center(),
            buff=0,
            color=BLUE
        )

        self.play(Write(arrow))

        self.wait(.2)

        # On enlève la flèche
        self.play(FadeOut(arrow))

        # On ajoute une flèche orientée en bleu depuis la cellule 5 vers la cellule 3
        arrow = Arrow(
            cell5.get_center(),
            cell3.get_center(),
            buff=0,
            color=BLUE
        )

        self.play(Write(arrow))

        self.wait(.2)

        # On enlève la flèche
        self.play(FadeOut(arrow))


        # On ajoute une flèche orientée en bleu depuis la cellule 5 vers la cellule 4
        arrow = Arrow(
            cell5.get_center(),
            cell4.get_center(),
            buff=0,
            color=BLUE
        )

        self.play(Write(arrow))

        self.wait(.2)

        # On enlève la flèche
        self.play(FadeOut(arrow))


        # On ajoute une flèche orientée en bleu depuis la cellule 3 vers la cellule 5
        arrow = Arrow(
            cell3.get_center(),
            cell5.get_center(),
            buff=0,
            color=ORANGE
        )

        self.play(Write(arrow))

        self.wait(.2)

        # On enlève la flèche
        self.play(FadeOut(arrow))

        # On ajoute une flèche orientée en bleu depuis la cellule 2 vers la cellule 5
        arrow = Arrow(
            cell2.get_center(),
            cell5.get_center(),
            buff=0,
            color=ORANGE
        )

        self.play(Write(arrow))

        self.wait(.2)

        # On enlève la flèche
        self.play(FadeOut(arrow))

        # On ajoute une flèche orientée en bleu depuis la cellule 4 vers la cellule 5
        arrow = Arrow(
            cell4.get_center(),
            cell5.get_center(),
            buff=0,
            color=ORANGE
        )

        self.play(Write(arrow))


        # On rajoute trois petits points pour indiquer qu'il y a des cellules après
        dots2 = Text("...", color=WHITE)

        # On les positionne
        dots2.move_to([-GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2,
                        GRID_SIZE * CELL_SIZE / 2 - CELL_SIZE / 2 - CELL_SIZE - CELL_SIZE / 2, 0])
        
        # On les affiche
        self.play(Write(dots2))

        # On affiche le texte "Et ainsi de suite..."
        text = Text("Et ainsi de suite...", color=WHITE)

        # On le positionne
        text.move_to([-GRID_SIZE * CELL_SIZE / 2 + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2,
                        GRID_SIZE * CELL_SIZE / 2 - CELL_SIZE / 2 - CELL_SIZE - CELL_SIZE / 2 - CELL_SIZE - CELL_SIZE / 2, 0])
        
        # On l'affiche
        self.play(Write(text))

        self.wait(5)


        # On enlève les petits points
        self.play(FadeOut(dots), FadeOut(dots2), FadeOut(cell), FadeOut(
            cell2), FadeOut(cell3), FadeOut(cell4), FadeOut(cell5), FadeOut(arrow), FadeOut(arrows), FadeOut(text))

        self.wait(1)

        # On affiche "En cas de question me contacter Discord @UnSavantFou#2534"
        text = Text("En cas de question me contacter", color=WHITE)


        # On réduit la taille du texte
        text.scale(0.5)

        # On le positionne au centre
        text.move_to([0, 0, 0])

        # On centre le texte (pour que le texte soit centré par rapport à la position)
        text.center()

        # On l'affiche
        self.play(Write(text))

        self.wait(9)

        # On enlève le texte
        self.play(FadeOut(text))

        self.wait(7)