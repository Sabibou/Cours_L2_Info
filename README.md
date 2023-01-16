# Introduction 

Ce repo contient mes notes de cours pour le second semestre de **2e Année de licence en Informatique** (2022-2023) avec comme mineure Prep'ISIMA.

Ayant fait Prep'ISIMA, je n'ai pas eu de mineure commune avec la L2 Info, donc il y aura des cours en moins (remplacés par Projets pour l'ingénieur, et Réalité Virtuelle).

# Organisation

Il y a un dossier par matière (Cf l'arborescence), contenant des `.md` (markdown) de prise de note, ainsi que des `.pdf` de prises de note 🙏🏻

Les `.pdf` sont souvent les slides de cours auquelles j'ai rajouté des annotations du prof, informations supplémentaires 😁

# Utilisation

*N'hésitez pas à me contacter pour de l'aide pour la compilation / l'ouverture des fichiers. 😋*

## Markdown

### Sur un IDE (`Vscode`)

Pour pouvoir bien lire le markdown (surtout s'il y a du code), je conseille l'utilisation de l'extension de `Vscode` suivante : **Markdown Preview Enhanced** par *Yiyi Wang*.

Il suffit ensuite de faire `CTRL-k v` (windows / linux) ou `CMD-k v` (MacOS) pour avoir le preview à droite.

### Exporter en PDF

Vous pouvez aussi exporter les notes en `pdf` depuis un markdown avec l'outil `pandoc` [téléchargeable ici](https://pandoc.org/installing.html).

Notes : 

$\LaTeX$ doit être installé :

- [télécharger](https://www.latex-project.org/get/) pour *Windows*
- [télécharger](https://doc.ubuntu-fr.org/latex) pour *Ubuntu*
- [télécharger](https://formulae.brew.sh/cask/mactex) pour *MacOs*

On peut compiler de deux façons.

#### Méthode simple

On peut utiliser la commande suivante :

- `pandoc -f markdown -t pdf --mathjax --table-of-contents -o "rapport.pdf" --pdf-engine=xelatex "tonmarkdown.md"`

#### Ajout du formatage du code

On peut rajouter du color syntaxing dans le code en rajoutant des arguments :

- rajouter le code suivant dans le dossier courant, sous le nom `listings-setup.tex`

```tex
% Contents of listings-setup.tex
\usepackage{xcolor}

\lstset{
    basicstyle=\ttfamily,
    keywordstyle=\color[rgb]{0.13,0.29,0.53}\bfseries,
    stringstyle=\color[rgb]{0.31,0.60,0.02},
    commentstyle=\color[rgb]{0.56,0.35,0.01}\itshape,
    backgroundcolor=\color[RGB]{248,248,248},
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    tabsize=2,
    captionpos=b,
    breaklines=true,
    breakatwhitespace=true,
    breakautoindent=true,
    escapeinside={\%*}{*)},
    linewidth=\textwidth,
    basewidth=0.5em,
}
```

On rajoute aussi les arguments suivants : `--listings -H ./listings-setup.tex`. On obtient la commande de compilation :

- `pandoc -f markdown -t pdf --mathjax --table-of-contents -o "rapport.pdf" --listings -H ./listings-setup.tex --pdf-engine=xelatex "tonmarkdown.md"`

Derrière la compilation, `pandoc` transforme le `markdown` en `latex`, puis compile le `latex`. On peut donc rajouter des codes `latex` en header permettant de modifier le code (d'où `listings-setup.tex`).

## Contribution

Le but de ce repo est aussi de permettre la contribution des autres étudiants, si jamais il y a des fautes / erreurs dans mes cours n'hésitez pas à me DM discord : ***UnSavantFou#2534***. 

De même, comme je n'ai pas de mineure, si des étudiants veulent rajouter leurs cours je peux les rajouter en édition.


*PS : me tapez pas sur la vitesse de publication 🙄*