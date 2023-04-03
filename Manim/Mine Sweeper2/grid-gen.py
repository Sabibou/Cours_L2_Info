# Le démineur

from manim import *
from random import randint, seed

seed(0)


class Cell(Square):

    def __init__(self, isTrapped=False, **kwargs):
        super().__init__(**kwargs)
        self.isTrapped = isTrapped
        self.circle = None
        self.neighboursNumber = 0
        self.text = Text("")

        # Si la cellule est piégée, on affiche un cercle rouge
        if self.isTrapped:
            self.circle = Circle(
                radius=self.side_length / 4,
                fill_opacity=1,
                stroke_width=0,
                color=RED,
            )
            self.circle.move_to(self.get_center())
            self.add(self.circle)

    def move(self, position):

        # On déplace la cellule
        self.generate_target()
        self.target.move_to(position)
        return self.target



class GridGen(MovingCameraScene):

    def construct(self):

        # On a une grille qui contient des mines
        self.GRID_SIZE = 11
        self.MINE_COUNT = 20
        self.CELL_SIZE = 0.5
        self.CELL_PADDING = 0.2
        self.WAIT_TIME = 0.1

        # On génère la grille
        grid = self.generateGrid()

        # On affiche la grille
        self.play(Write(grid))
        self.wait(self.WAIT_TIME)


        # On affiche la grille avec un padding
        self.showGridWithPadding(grid)
        self.wait(self.WAIT_TIME)

        # On zoom sur la grille
        self.play(self.camera.frame.animate.scale(
            0.5).move_to(grid.get_center()))

        # On ajoute les flèches
        arrows = self.addArrows(grid)
        self.play(Write(arrows))
        self.wait(self.WAIT_TIME)

        # On affiche le nombre de voisins
        self.showNeighboursNumber(grid)
        self.wait(self.WAIT_TIME)

        # On colorie les cellules
        self.colorizeCells(grid)
        self.wait(self.WAIT_TIME)

        # On affiche les cellules du centre
        self.colorizeCells(grid, colorize=False)
        self.keepCenteredCells(grid, arrows)

    def keepCenteredCells(self, grid, arrows):

        # On colorie les cellules du centre
        animations = []
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                if (i > self.GRID_SIZE // 2 - 2 and i < self.GRID_SIZE // 2 + 2 and j > self.GRID_SIZE // 2 - 2 and j < self.GRID_SIZE // 2 + 2):
                    # On veut colorier que le carré
                    animations.append(grid[i * self.GRID_SIZE + j].animate.set_fill(
                        color="#f2cc8f", opacity=1))
                    
                    if grid[i * self.GRID_SIZE + j].isTrapped:
                        animations.append(grid[i * self.GRID_SIZE + j].circle.animate.set_fill(
                            color=RED, opacity=1))
                    
        # On cache les textes et flèches
        animations.append(FadeOut(arrows))
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                if not (i > self.GRID_SIZE // 2 - 2 and i < self.GRID_SIZE // 2 + 2 and j > self.GRID_SIZE // 2 - 2 and j < self.GRID_SIZE // 2 + 2):
                    animations.append(grid[i * self.GRID_SIZE + j].text.animate.set_fill(
                        color=BLACK, opacity=1))
                    
                    
        self.play(*animations)

    def colorizeCells(self, grid, colorize=True):

        # En fonction de la valeur du nombre de voisins, on colorie la cellule
        # On va stocker les animations dans une liste
        animations = []
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):

                if not grid[i * self.GRID_SIZE + j].isTrapped:

                    value = int(grid[i * self.GRID_SIZE + j].neighboursNumber)

                    if colorize:
                        if value == 0:
                            animations.append(grid[i * self.GRID_SIZE + j].animate.set_fill(
                                color="#ffe5d9", opacity=1))
                        elif value == 1:
                            animations.append(grid[i * self.GRID_SIZE + j].animate.set_fill(
                                color="#e9edc9", opacity=0.5))
                        elif value == 2:
                            animations.append(grid[i * self.GRID_SIZE + j].animate.set_fill(
                                color="#84a98c", opacity=0.5))
                        elif value == 3:
                            animations.append(grid[i * self.GRID_SIZE + j].animate.set_fill(
                                color="#f4a261", opacity=0.5))
                        elif value >= 4:
                            animations.append(grid[i * self.GRID_SIZE + j].animate.set_fill(
                                color="#9e2a2b", opacity=0.5))
                    else:
                        animations.append(grid[i * self.GRID_SIZE + j].animate.set_fill(
                            color=WHITE, opacity=0))
        self.play(*animations)


    def showNeighboursNumber(self, grid):

        # On affiche le nombre de voisins
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                cell = grid[i * self.GRID_SIZE + j]
                if not cell.isTrapped:
                    cell.neighboursNumber = self.getNeighboursNumber(grid, i, j)

                    # On affiche le nombre de voisins
                    cell.text = Text(str(cell.neighboursNumber))
                    cell.text.move_to(cell.get_center())
                    # On scale le texte pour qu'il rentre dans la cellule
                    cell.text.scale(self.CELL_SIZE)

        self.play(*[
            Write(grid[i * self.GRID_SIZE + j].text) for i in range(self.GRID_SIZE) for j in range(self.GRID_SIZE) if not grid[i * self.GRID_SIZE + j].isTrapped
        ])

    def getNeighboursNumber(self, grid, i, j):

        # On compte le nombre de voisins
        count = 0
        if i > 0:
            if grid[(i - 1) * self.GRID_SIZE + j].isTrapped:
                count += 1
        if i < self.GRID_SIZE - 1:
            if grid[(i + 1) * self.GRID_SIZE + j].isTrapped:
                count += 1
        if j > 0:
            if grid[i * self.GRID_SIZE + j - 1].isTrapped:
                count += 1
        if j < self.GRID_SIZE - 1:
            if grid[i * self.GRID_SIZE + j + 1].isTrapped:
                count += 1

        # On ne doit pas oublier les diagonales
        if i > 0 and j > 0:
            if grid[(i - 1) * self.GRID_SIZE + j - 1].isTrapped:
                count += 1
        if i > 0 and j < self.GRID_SIZE - 1:
            if grid[(i - 1) * self.GRID_SIZE + j + 1].isTrapped:
                count += 1
        if i < self.GRID_SIZE - 1 and j > 0:
            if grid[(i + 1) * self.GRID_SIZE + j - 1].isTrapped:
                count += 1
        if i < self.GRID_SIZE - 1 and j < self.GRID_SIZE - 1:
            if grid[(i + 1) * self.GRID_SIZE + j + 1].isTrapped:
                count += 1
        return count

    def addArrows(self, grid):

        # On ajoute des flèches pour indiquer les voisins (on les rend petites pour ne pas les confondre avec les cellules, et on les relie aux extrémités des cellules)
        # On colorie les flèches en fca311
        arrows = VGroup()
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):

                if i > 0:
                    arrow = Arrow(grid[i * self.GRID_SIZE + j].get_left(), grid[(
                        i - 1) * self.GRID_SIZE + j].get_right(), buff=0, stroke_width=0.5, color="#fca311")
                    arrows.add(arrow)
                if i < self.GRID_SIZE - 1:
                    arrow = Arrow(grid[i * self.GRID_SIZE + j].get_right(), grid[(
                        i + 1) * self.GRID_SIZE + j].get_left(), buff=0, stroke_width=0.5, color="#fca311")
                    arrows.add(arrow)
                if j > 0:
                    arrow = Arrow(grid[i * self.GRID_SIZE + j].get_bottom(), grid[i *
                                  self.GRID_SIZE + j - 1].get_top(), buff=0, stroke_width=0.5, color="#fca311")
                    arrows.add(arrow)
                if j < self.GRID_SIZE - 1:
                    arrow = Arrow(grid[i * self.GRID_SIZE + j].get_top(), grid[i * self.GRID_SIZE +
                                  j + 1].get_bottom(), buff=0, stroke_width=0.5, color="#fca311")
                    arrows.add(arrow)

                # Ne pas oublier les diagonales
                if i > 0 and j > 0:
                    arrow = Arrow(grid[i * self.GRID_SIZE + j].get_bottom() + LEFT * self.CELL_SIZE / 2, grid[(
                        i - 1) * self.GRID_SIZE + j - 1].get_top() + RIGHT * self.CELL_SIZE / 2, buff=0, stroke_width=0.5, color="#fca311")
                    arrows.add(arrow)
                if i > 0 and j < self.GRID_SIZE - 1:
                    arrow = Arrow(grid[i * self.GRID_SIZE + j].get_top() + LEFT * self.CELL_SIZE / 2, grid[(
                        i - 1) * self.GRID_SIZE + j + 1].get_bottom() + RIGHT * self.CELL_SIZE / 2, buff=0, stroke_width=0.5, color="#fca311")
                    arrows.add(arrow)
                if i < self.GRID_SIZE - 1 and j > 0:
                    arrow = Arrow(grid[i * self.GRID_SIZE + j].get_bottom() + RIGHT * self.CELL_SIZE / 2, grid[(
                        i + 1) * self.GRID_SIZE + j - 1].get_top() + LEFT * self.CELL_SIZE / 2, buff=0, stroke_width=0.5, color="#fca311")
                    arrows.add(arrow)
                if i < self.GRID_SIZE - 1 and j < self.GRID_SIZE - 1:
                    arrow = Arrow(grid[i * self.GRID_SIZE + j].get_top() + RIGHT * self.CELL_SIZE / 2, grid[(
                        i + 1) * self.GRID_SIZE + j + 1].get_bottom() + LEFT * self.CELL_SIZE / 2, buff=0, stroke_width=0.5, color="#fca311")
                    arrows.add(arrow)

        return arrows

    def showGridWithPadding(self, grid):

        # On écarte les cellules entres elles de CELL_PADDING
        decalage = self.CELL_PADDING * self.GRID_SIZE / 2

        self.play(*[
            grid[i * self.GRID_SIZE + j].animate.move_to(grid[i * self.GRID_SIZE + j].get_center() + RIGHT * (-decalage + i * self.CELL_PADDING) + UP * (-decalage + j * self.CELL_PADDING)) for i in range(self.GRID_SIZE) for j in range(self.GRID_SIZE)
        ])

    def generateGrid(self):

        # On génère une grille de CELL_SIZE * CELL_SIZE
        grid = VGroup()

        # On génère les mines
        mines = []
        minesNumber = 0
        while minesNumber < self.MINE_COUNT:
            x = randint(0, self.GRID_SIZE - 1)
            y = randint(0, self.GRID_SIZE - 1)
            if (x, y) not in mines:
                mines.append((x, y))
                minesNumber += 1

        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                cell = Cell(side_length=self.CELL_SIZE,
                            isTrapped=(i, j) in mines)
                cell.move_to(LEFT * self.GRID_SIZE / 2 * self.CELL_SIZE + DOWN * self.GRID_SIZE /
                             2 * self.CELL_SIZE + RIGHT * i * self.CELL_SIZE + UP * j * self.CELL_SIZE)
                grid.add(cell)

        return grid
