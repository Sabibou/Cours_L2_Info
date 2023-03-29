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

        MINE_PERCENTAGE = 0.2
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

        self.wait(2)

        # On fait un groupe pour les voisines
        neighbors_group = VGroup()

        # On colorie ses voisines en vert (on les remplies) sauf celle du milieu
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x != 0 or y != 0:
                    neighbors_group.add(
                        grid_group[GRID_SIZE * GRID_SIZE // 2 + GRID_SIZE // 2 + x + y * GRID_SIZE])

        self.play(neighbors_group.animate.set_fill(GREEN, opacity=.5))

        self.wait(2)

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

        self.wait(2)

        # On déplace la caméra de CELL_SIZE vers le bas
        self.play(self.camera.frame.animate.move_to(
            [CELL_SIZE/2, -CELL_SIZE/2, 0]))

        # On colorie la case du bas en bleu (on la remplie)
        self.play(grid_group[GRID_SIZE * GRID_SIZE // 2 +
                             GRID_SIZE // 2 - 1].animate.set_fill(BLUE, opacity=.5))

        self.wait(1)

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

        self.wait(4)

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

        self.wait(4)

        # On enlève les flèches
        self.play(FadeOut(neighbors_arrows))

        self.wait(1)

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

        self.wait(1)

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

                    self.play(FadeOut(number), run_time=.05)

                    self.play(Write(arrow), run_time=.15)

                    if (x == 0 and y == -1) or (x == -1 and y == 1):
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

        self.wait(2)

        # On enlève les flèches
        self.play(FadeOut(arrowGroup))
