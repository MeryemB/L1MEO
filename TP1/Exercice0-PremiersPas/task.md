
**Utilisation du terminal** 

\> _Aide pour les commandes Unix : **man** (MANual)._

Ouvrez un terminal. Par défaut, vous êtes dans votre espace de travail (home).

a. Affichez les éléments contenus dans le répertoire principal (racine ~ = ou "répertoire home")
en utilisant la commande **ls**.

b. Si le répertoire principal ne contient pas un sous-répertoire nommé 'Documents', 
 créez-le en utilisant la commande **mkdir**.

c. Depuis 'Documents', créez un sous-répertoire nommé 'Septembre_2018'. Pour se déplacer d'un
répertoire à un autre, utilisez la commande **cd**.

d. Créez deux fichiers 'tp1.py' et 'tp2.py' dans le dossier 'Septembre_2018'. 
Pour cela, utilisez la commande **touch**.

e. Quelle est la commande qui affiche à l'écran le nom de votre répertoire courant ?
 
f. Écrivez les commandes qui vous permettent d'aller dans le répertoire principal et d'afficher récursivement son contenu
(sous-dossiers et fichiers).

g. Dessinez l’arborescence de tous les répertoires et fichiers depuis le répertoire principal.
 
f. Écrivez une commande qui déplace dans 'Documents' tous les fichiers .py du répertoire 'Septembre_2018'.
Pour cela, utilisez la commande **mv**.
 
g. Écrivez une commande qui supprime le répertoire 'Septembre_2018'.
Pour cela, utilisez la commande **rmdir**.

**Python**

 \# Ceci est un commentaire en python.

Référence Python 3: https://docs.python.org/fr/3/ 

- Python, un langage interprété.
- Vous allez d’abord utiliser  python en mode interactif, c’est-à-dire de manière à dialoguer avec lui directement depuis le  clavier.
- Vous pouvez utiliser l’interpréteur  directement comme une simple calculatrice de bureau.
- Dans la console python, entrez les expressions ci-dessous et observez le résultat :
- Pour ouvrir la console, il suffit  de cliquer sur le bouton Python console en bas de votre fenêtre de Pycharm :

> - 5+10

> - 7 - 9

> - 7+3 * 5

> - (7 +3) *5

> - 20/6

> - 8,7 / 5

- Notez que le séparateur décimal est toujours un point, et non une virgule!

- Les opérateurs arithmétiques : _+ (addition) / ( division)  - (soustraction) * ( multiplication) % (reste de la division entière) // (division entière) ** (puissance)_


Par défaut, la division est cependant une division entière, ce qui signifie que si on lui fournit des arguments qui sont des nombres entiers.
 le résultat de la division est lui-même un entier, comme dans le dernier exemple ci-dessus. Si vous voulez qu'un argument soit compris par Python comme étant un nombre réel,
il faut le lui faire savoir, en fournissant au moins un point décimal.

- Essayez par exemple :
- 20.0 / 3
- 8./5
- (comparez le résultat avec celui obtenu à l'exercice précédent)

- Si une opération est effectuée avec des arguments de types mélangés (entiers et réels), Python convertit automatiquement les opérandes en réels avant d'effectuer l'opération. Essayez :
- 4 * 2.5 / 3.3
