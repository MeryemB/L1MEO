**Remarques préliminaires**

- Les variables sont utilisées pour stocker des valeurs afin que 
nous puissions nous y référer ultérieurement. 
- Un nom de variable est une séquence de lettres (a → z , A → Z) 
et de chiffres (0 → 9), qui doit toujours commencer par une lettre. Seules les lettres ordinaires sont autorisées. Les lettres accentuées, les cédilles, les espaces, les
caractères spéciaux tels que $, #, @, etc. sont interdits, à l’exception 
du caractère _ (souligné).
•- La casse est significative (les caractères majuscules et minuscules sont distingués).
Attention : Joseph, joseph, JOSEPH sont donc des variables différentes. Soyez attentifs !

- L'opération d’affectation est représentée par le signe égale _"="_ exemple: **nom_de_la_variable** par la valeur **2** en Python:
  _nom_de_la_variable = 2_
  
- Sous Python, on peut assigner une valeur à plusieurs variables 
simultanément. Exemple : a = b = 8  
On peut aussi effectuer des affectations parallèles à l’aide d’un seul opérateur :
a, b = 2, 4.35
- **print()** : permet d'afficher la valeur d’une variable.
Exemple:  _print(nom_de_la_variable)_
- Il est possible de connaître le type d’une variable en utilisant la 
fonction type :  _print(type(nom_de_la_variable))_
- **int** : désigne un entier
- **float** : désigne un décimale 
- **print("Résultat est {:3.2f}" .format(nom_de_la_variable))**:  le résultat est formaté de manière à comporter un total de 3 caractères,
dont 2 chiffres après le point décimal


**Exercice**

**a.** Affectez les variables **a** et **b** par les valeurs **7.692** et **21.8**.
Calculez et affichez leur somme (variable nommée **resultat**).
Améliorez l'affichage en imposant un chiffre après le point décimal.

**b.** Affectez la variable c  par un entier (représentant une valeur en euros)
 et convertissez-le en francs. Rappel: 1 euro = 6.55957 francs. 
 Stocker le résultat de conversion dans une variable nommée **francs**
 
 **c.**  Déclarez une variable **_ma_variable_** et affectez-lui la valeur **2**. 
 Quel est le type de cette variable ? Répétez l’opération avec les 
 valeurs suivantes: 
- 2.5
- 2 + 2.5
- 'z'
- 10 / 3

**Note :**


Sous Python, il n’est pas nécessaire d’écrire des lignes de programme spécifiques
 pour définir le type des variables avant de pouvoir les utiliser. Il vous suffit
  en effet d’assigner une valeur à un nom de variable pour que celle-ci soit 
  automatiquement créée avec le type qui correspond au mieux à la valeur
fournie.
 

La variable _**ma_variable**_ de la partie **c.** de l'exercice a été créée automatiquement
 avec un type différent pour chaque déclaration(« nombre entier » pour 2, « chaîne de caractères »
pour 'z', « nombre à virgule flottante » (ou « float », en anglais) pour 2.5 , etc.
 