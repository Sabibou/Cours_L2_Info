---
author: VAN DE MERGHEL Robin
date: Semestre 4
lang: fr
title: Web-Client, correction Annales
geometry: margin=3cm
---

*Note supplémentaire : Sur certaines questions, il se peut que j'hésite sur une réponse, je donnerai une réponse (mon interprétation), et je rajouterai une note ainsi qu'une astérisque pour indiquer que je ne suis pas sûr de la réponse.*

# Annale CC 2021-2022

## Exercice 1

### Question 1

> **Qu'est-ce que le web? Quels en sont les principes ?**

Le Web c'est l'ensemble des ressources qui sont accessibles et distribuées sur internet (sites, images, documents, ...). 

Ses principes sont les suivants :

- **évolutif** : le web est un système qui évolue constamment, il est donc nécessaire de pouvoir le mettre à jour facilement
- **universel** : le web est accessible à tous, il n'y a pas de restriction d'accès

### Question 2

> **Quel est le principe du DNS ? Quelle en est l'utilité ?**

Le principe du DNS est de convertir une **URI** en **adresse IP**. 

L'utilité est de pouvoir accéder à une ressource sur internet sans avoir à connaître son adresse IP (il est plus facile de retenir le nom d'un site, qu'une suite de 12 chiffres).

### Question 3

> **Expliquez le concept d'hypermédia.**

L'hypermédia c'est l'ensemble des données qui sont reliées entre elles. Ex : un site web, un document, ...

Ils ont une URI qui permet de les identifier.

### Question 4*

> **Expliquez le concept d'opacité des URL. En quoi est-ce important?**

Une adresse URL n'est pas censée être lisible par l'utilisateur. C'est le serveur qui doit comprendre l'URL et savoir comment la traiter.

L'utilisateur ne fait que suivre un lien, il ne doit pas avoir à comprendre ce qu'il y a derrière. Exemple : les URL des vidéos youtubes sont illisibles pour l'utilisateur, mais le serveur sait comment les traiter.

> *Note : je ne suis pas sûr de la réponse suivante, mais je pense que c'est ça :*

C'est important car l'utilisateur ne doit pas avoir à comprendre ce qu'il y a derrière, il doit juste suivre le lien. 


## Exercice 2

### Question 1

> **Qu'est-ce que le CSS ? Quel est l'intérêt de son utilisation ?**

Le CSS ou **Cascading Style Sheets** est un langage de style qui permet de définir l'apparence d'un document HTML. Il utilise des sélecteurs pour cibler les éléments HTML, et leur appliquer des styles (ex : couleur, taille, ...).

L'intérêt de son utilisation est de pouvoir définir l'apparence d'un document HTML sans avoir à modifier le document lui-même. On peut garder la même structure HTML (en définissant des mots importants, des titres, etc...) et changer l'apparence du document en modifiant le CSS.

### Question 2

> **Expliquer le principe de la cascade des règles CSS.**

Le principe de la cascade, c'est qu'une règle appliquée à un élément du CSS s'appliquera en cascade sur tout les sous-éléments de cet élément. Ex : si on applique une couleur au bloc `article`, cette couleur s'appliquera à tous les éléments qui sont dans le bloc `article`.

### Question 3

> **Que sont les « media queries » en CSS ? Quels en sont les intérêts ?**

Les media queries sont des règles CSS qui permettent de définir des styles en fonction du type d'appareil qui affiche le document. Ex : si on affiche le document sur un ordinateur, on peut appliquer un style différent de celui qui s'applique sur un téléphone.

On peut donc définir des règles pour dire "Si l'appareil a une taille d'écran inférieure à 500px, alors applique ce style".

```css
@media screen and (max-width: 500px) { /* Si l'écran a une taille inférieure à 500px */
    /* style */
}
```

## Exercice 3

### Question 1

> **Qu'est-ce que le HTML?**

Le HTML ou **HyperText Markup Language** est un langage de balisage qui permet de définir la structure d'un document. Il utilise des balises pour définir les éléments du document (ex : titre, paragraphe, image, ...).

### Question 2

> **Qu'appelle-t-on du HTML « sémantique » ? Quels en sont les intérêts?**

La sémantique HTML c'est l'utilisation des balises HTML pour définir le sens des éléments du document. Ex : on utilise la balise `<h1>` pour définir un titre, et la balise `<p>` pour définir un paragraphe.

On ne veut pas définir la forme d'un élément, mais son sens. Ex : on ne veut pas définir un titre avec la balise `<p>`, mais avec la balise `<h1>`.

Ça servira ensuite aux agents utilisateurs (navigateurs, moteurs de recherche, ...) pour comprendre le sens du document.

### Question 3

> **Que signifie être valide pour du HTML ? Pourquoi est-ce important ?**

Un document HTML est valide s'il respecte la syntaxe du langage HTML : il n'y a pas de balises mal fermées, les balises sont bien imbriquées, les balises existent, ...

C'est important car les agents utilisateurs (navigateurs, moteurs de recherche, ...) peuvent utiliser ces informations pour comprendre le sens du document (exemple : les malvoyants utilisent des lecteurs d'écran qui lisent le document HTML pour les aider à comprendre le document).


## Exercice 4

### Question 1

> **Donnez-la valeur de $x$ et expliquez**

```javascript
let v = (function(x) {
    let c = x;
    return function(y) {
        c *= y;
        return c;
    }
})(7);

v(2);
let x = v(3);
```

$x = 42$ car la fonction `v` est appelée avec l'argument `3`, donc $c = 7 \times 3 = 21$. Ensuite, la fonction `v` est appelée avec l'argument `2`, donc $c = 21 \times 2 = 42$.

### Question 2

> **Qu'est-ce que le DOM ? Comment l'utiliser ?**

Le DOM ou **Document Object Model** est une représentation de l'arbre HTML sous forme d'objet. On peut y trouver qui est le parent d'un élément, qui sont les enfants d'un élément, ...

On peut l'utiliser en utilisant les méthodes de l'objet `document` (ex : `document.getElementById`, `document.getElementsByClassName`, ...).

### Question 3

> **Donner et expliquer la valeur de :**

#### Question 3.1

```javascript   
[1, 2, 3] == [1, 2, 3]
```

La valeur est `false` car les tableaux sont des objets, et les objets sont comparés par référence. Donc même si les tableaux ont les mêmes valeurs, ils ne sont pas égaux.

#### Question 3.2

```javascript
[1, 2, 3] === [1, 2, 3]
```

La valeur est `false` car les tableaux sont des objets, et les objets sont comparés par référence. Donc même si les tableaux ont les mêmes valeurs, ils ne sont pas égaux.

### Question 4

> **Expliquer le fonctionnement de la programmation événementielle.**

La programmation événementielle c'est l'utilisation d'événements pour déclencher des actions. Ex : on peut définir une action qui se déclenche quand on clique sur un bouton.

En français, on peut traduire "Quand on clique sur le bouton, on affiche un message" par `button.addEventListener("click", function() { alert("Hello world"); });`.

### Question 5*

> **Quelle est la praticularité du système objet de javascript ? Comment fonctionne-t-il ?**

> *Note : je n'ai aucune idée pour cette question, j'attends le cours / que je vois par moi-même.*



# Annales 2021-2022 1ère session

## Exercice 1

### Question 1*

> **Quelles sont les trois couches fondamentales dans une application ? Où sont-elles situées dans une application Web ?**

Les trois couches fondamentales sont la couche présentation, la couche métier et la couche persistance.

- La couche présentation est située dans le navigateur. Elle est chargée de l'affichage des données et de la gestion des événements.
- La couche métier est située sur le serveur. Elle est chargée de la logique métier de l'application.
- La couche persistance est située sur le serveur. Elle est chargée de la persistance des données.

Elles permettent de séparer les différentes responsabilités de l'application.


### Question 2

> **En quoi le design des URL est important ? Qu'est-ce qu'uene "bonne" URL ?**

Une URL doit être comphénsible par le serveur, mais pas forcément par les utilisateurs. On arrive sur une ressource qu'après avoir navigué URL par URL, donc on peut se permettre d'avoir des URL un peu longues et complexes.

De plus, l'utilisateur n'est pas sencé comprendre l'URL. Même des fois, il ne vaut mieux pas comme pour Google Drive sinon on pourrait accéder à des fichiers dont on n'a pas les droits. Avoir une ressource avec le même nom aurait provoqué une erreur car les deux ressources auraient eu la même URL.


### Question 3*

> **Quels sont les buts recherchés dans l'architecture du Web ?**

Les buts recherchés dans l'architecture du Web sont :

- La portabilité : le Web doit être accessible depuis n'importe quel appareil (ex : ordinateur, téléphone, tablette, ...)
- La simplicité : le Web doit être simple à utiliser (ex : pas besoin de télécharger une application pour utiliser un service)
- La performance : le Web doit être performant (ex : pas de latence, pas de temps de chargement long, ...)
- La fiabilité : le Web doit être fiable (ex : pas de pannes, pas de défaillance, ...)


### Question 4

> **Que signifie l'accessibilité pour un contenu Web ? En quoi est-ce important ?**

L'accessibilité pour un contenu Web c'est que le contenu est accessible à tous les utilisateurs, y compris les personnes handicapées. C'est important car on veut que tout le monde puisse accéder au contenu.

Par exemple, une image de chat ne sera pas accessible pour les malvoyants car ils ne pourront pas la voir. Il faudrait donc ajouter un texte alternatif (`alt`) pour que les malvoyants puissent comprendre ce que représente l'image.

## Exercice 2

### Question 1

> **Donner les différentes manières de spécifier une couleur en CSS.**

On peut spécifier une couleur en CSS de plusieurs manières :

- En utilisant le nom de la couleur (ex : `red`, `blue`, `green`, ...)
- En utilisant le code hexadécimal de la couleur (ex : `#ff0000`, `#0000ff`, `#00ff00`, ...)
- En utilisant le code RGB de la couleur (ex : `rgb(255, 0, 0)`, `rgb(0, 0, 255)`, `rgb(0, 255, 0)`, ...)
- En utilisant le code HSL de la couleur (ex : `hsl(0, 100%, 50%)`, `hsl(240, 100%, 50%)`, `hsl(120, 100%, 50%)`, ...)
- En utilisant le code CMYK de la couleur (ex : `cmyk(0, 100%, 100%, 0)`, `cmyk(100%, 0, 100%, 0)`, `cmyk(100%, 100%, 0, 0)`, ...)
- En utilisant une couleur transparente (ex : `transparent`, `rgba(0, 0, 0, 0)`, `hsla(0, 0%, 0%, 0)`, ...), on rajoute un canal alpha
- En utilisant une couleur dégradée (ex : `linear-gradient(90deg, red, blue)`, `radial-gradient(red, blue)`, ...)


### Question 2

> **Donner la syntaxe générale d'une règle CSS.**

La syntaxe générale d'une règle CSS est la suivante :

```css
selector {
    property: value;
}
```

### Question 3

> **Qu'est-ce qu'un design de page flexible (ou fluide) ? Pourquoi est-ce important ?**

Un design de page flexible (ou fluide) c'est un design de page qui s'adapte à la taille de l'écran. C'est important car les utilisateurs peuvent avoir des écrans de différentes tailles, et on veut que le site soit lisible sur tous les écrans.

En effet, sur un écran de 1920x1080, on peut afficher 1920 pixels de largeur. Mais sur un écran de 1280x720, on ne peut afficher que 1280 pixels de largeur. Si on a un design de page fixe, on ne pourra pas afficher tout le contenu sur un écran de 1280x720.

### Question 4

> **Quelles sont les différentes manières d'appliquer du CSS aux éléments HTML ? Donner les avantages et inconvénients de chacunes, et dans quel cas les utiliser.**

On a 3 manières d'appliquer du CSS aux éléments HTML :

- Modifier `inline` : on modifie l'attribut `style` de l'élément HTML. C'est pratique pour faire des tests, mais c'est pas pratique pour appliquer du CSS à plusieurs éléments. `<p style="color: red;">Hello world</p>`
- Modifier `internal` : on modifie la balise `<style>` dans le `<head>`. C'est pratique pour appliquer du CSS à plusieurs éléments, mais c'est pas pratique pour faire des tests. `<style> p { color: red; } </style>`
- Modifier `external` : on modifie le fichier CSS externe. C'est pratique pour appliquer du CSS à plusieurs éléments et pour partager le code CSS à plusieurs pages. `<link rel="stylesheet" href="style.css">`

### Question 5

> **Quel est le principe des web fonts ?**

Le principe des web fonts c'est de pouvoir utiliser des polices de caractères qui ne sont pas installées sur l'ordinateur de l'utilisateur. On peut utiliser des polices de caractères payantes ou gratuites. 

Cela permet de pouvoir vraiment choisir la police de caractères qu'on veut utiliser, et de pouvoir utiliser des polices de caractères qui ne sont pas installées sur l'ordinateur de l'utilisateur.

## Exercice 3

### Question 1

> **Que signifie pour un document d'être bien formé ?**

Un document est bien formé s'il respecte la syntaxe du langage de balisage. C'est-à-dire que les balises sont bien fermées, que les attributs sont bien écrits, que les balises sont bien imbriquées, ...

### Question 2

> **Qu'indique un DOCTYPE d'un fichier HTML ? Pourquoi est-ce important et comment est-ce utilisé ?**

Un DOCTYPE d'un fichier HTML indique le type de document. C'est important car cela permet au navigateur de savoir comment interpréter le document. Cela permet aussi de savoir si le document est bien formé.

On peut ainsi préciser la version du langage de balisage utilisé, et le navigateur va interpréter le document en fonction de la version du langage de balisage utilisé.

On peut l'utiliser en écrivant `<!DOCTYPE html>` en haut du fichier HTML.

### Question 3*

*Note : jsp quoi rep, c'est assez spécial*

> **Comment fonctionnent les formulaires HTML, du points de vue de l'intéraction avec le serveur ?**

Le serveur reçoit les données du formulaire quand l'utilisateur clique sur le bouton `submit`. Le serveur peut ensuite traiter les données du formulaire. Selon la nature de la requête, le serveur peut renvoyer une page HTML, une image, un fichier, ...

### Question 4

> **Donner des exemples d'éléments HTML permettant de structurer le document de manière sémantique (au moins cinq).**

On peut structurer le document de manière sémantique avec les éléments suivants :

- `<header>` : pour le header
- `<nav>` : pour la navigation
- `<main>` : pour le contenu principal
- `<article>` : pour un article
- `<section>` : pour une section
- `<aside>` : pour un contenu secondaire
- `<footer>` : pour le footer
- `<h1>` à `<h6>` : pour les titres
- ...
