Manipulation des chaîne de caractères  
-
( type string ou str)

**_Préliminaires_**

- Pour les chaînes de caractères, deux opérations sont possibles,
 l’addition et la multiplication, exemple:
 
 >>> chaine = "Salut"
 
L'affichage de la variable _chaine_ donne : _'Salut'_
    
 >>> chaine = chaine + " Python"
 
 L'affichage de la variable _chaine_ donne :  _'Salut Python'_
 
 >>> chaine =  chaine * 3
 
 L'affichage de la variable _chaine_ donne :  _'SalutSalutSalut'_

- L’opérateur d’addition **_+_** permet de concaténer (assembler) 
deux chaînes de caractères et l’opérateur de multiplication **_\*_**
permet de dupliquer plusieurs fois une chaîne.

-Vous pouvez utiliser le **_"+"_** ou le **_","_** 
pour combiner deux chaînes de caractères. Si vous utilisez un **_","_**, vous aurez alors un espace entre les chaînes que vous avez combiné. Si vous utilisez un **_"+"_**, les chaînes seront reliées sans espace. 
Vous devrez en ajouter un si vous le souhaitez.

a) Affichez deux chaines de caractères ensuite combinez
 les en utilisant le **_','_** et le **_'+'_**

- Pour afficher une chaine de caractère on a deux façon de faire :

>> print('Guillemets simples')

>> print("double Guillemets")

> Essayez ces deux lignes!

b) Quelle est la différence entre ces deux instructions Python :

> x = 2018

> x = "2018"

Vous avez ici la notion de types et de typage : Chaque valeur en Python se voit associé un type, ceci précise quelles sont les opérations permises sur ces valeurs, et quel est leur sens. 
En Python les variables (comme x) n'ont pas de type au départ. C'est au moment de l'exécution, de l'évaluation des valeurs, que le système vérifie le type, et réagit "bien" ou "mal" vis à vis les opérations demandées. 
Cette propriété porte le nom de **_typage dynamique_**.

c) Vérifiez ce qui se passe quand on évalue x+x dans les deux cas.

- Si vous utilisez le "+" pour combiner des int et float ensemble, vous effectuerez une opération arithmétique. 
Si vous utilisez le ",", il les imprimera séparément, avec un espace.

>  \>>print('vous ne pouvez pas le faire',5)

- Vous ne pouvez pas utiliser le **_"+"_** pour combiner des chaînes avec ints ou floats.

d) Donnez la solution pour obtenir la combinison d'un entier a=5, 
avec la première chaine de caractère que vous avez proposé.



