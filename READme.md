# Commentaires généraux
### Remarques importantes
Approfondir la compréhension des cumulations binaires des modes<br>
On ne peut choisir qu'une seule conversion sur quatre[int, bin, hex, oct].
#### Remarques historiques
L'application dans sa création a pris un tournant, du fait que composée de fonctions, elle a changé en classe.<br>
## Quelle utilité pour cette application
Nous avons les boutons de la colonne des nombres entiers, et ceux de la barre horizontale des noms des gammes.<br>
### Les boutons verticaux
Nous pouvons avoir des méthodes de lecture :<br>
La méthode de lire à partir du bouton vertical, les gammes qui utilisent ce bouton (mono-note ou accord). Ou, <br>
lire les gammes à partir de la hauteur du bouton, la totalité des gammes.
### Les boutons horizontaux
Nous pouvons avoir des méthodes de lecture :<br>
Tout comme les boutons verticaux, les boutons horizontaux peuvent se lire les gammes qui ont les mêmes propriétés.<br>
Ou bien, lire les gammes à partir de ce bouton jusqu'à la fin de la liste.
## Méthodes du traitement des modes binaires
_Il existe une seule constance au démarrage, ce sont les modes naturels binaires._<br>
_Les modes binaires sont issus du type classique des gammes primordiales, le type physique n'a pas encore été vu._<br>
_'songammes' : Construit les gammes et les binaires selon le type classique = Dictionnaire alimenté par le fichier_<br>
_'globdicTcoup.txt' : Une création des 462 formules numériques, exemple = '102034050607'._<br>
### La méthode par défaut
Elle initialise les sept premières lignes de la colonne des modes binaires.<br>
Ensuite, elle fait un sondage sur les formes binaires restantes et à venir, <br>
pour définir quelle forme contient le plus de modes binaires présents grâce aux modes déjà traités.<br>
* Tel qu'il a été écrit à son départ, le traitement des binaires est en mode 'append()'<br>
C'est ainsi, que grâce aux gammes fondamentales, la colonne des binaires a été remplie.
### La méthode des entiers (Nombres entiers)
La liste originale des binaires a un ordre donné par **la méthode par défaut**.<br>
En transformant l'ordre après avoir modifié le type de nombre en nombre entier, le tri en ordre croissant<br>
remplace la séquence originale.
### La méthode des binaires (Nombres binaires)
La liste des modulations binaires existe, parce qu'elle a été réalisée dans les premières lignes du code.<br>
En triant cette liste en ordre croissant numérique, on parvient à un alignement des gammes originales.<br>
Ainsi, un ordre croissant des nombres entiers binaires, change l'ordre des gammes préétabli.<br>
### La méthode des binaires (Nombres hexadécimaux)
### La méthode des binaires (Nombres octaux)
<br>
<br>
<br>
<br>
<br>
<br>

