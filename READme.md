# Commentaires généraux
#### Remarques importantes
    Approfondir la compréhension des cumulations binaires des modes
    On ne peut choisir qu'une seule conversion sur quatre[int, bin, hex, oct].
#### Remarques historiques
    L'application dans sa création a pris un tournant, du fait que composée de fonctions, elle a changé en classe.
## Quelle utilité pour cette application
    Nous avons les boutons de la colonne des nombres entiers, et ceux de la barre horizontale des noms des gammes.
### Les boutons verticaux des binaires
    Nous pouvons avoir des méthodes de lecture :
    La méthode de lire à partir du bouton vertical, les gammes qui utilisent ce bouton (mono-note ou accord).
    Ou, lire les gammes à partir de la hauteur du bouton, la totalité des gammes.
**On peut créer plusieurs genres de lecture.**
* Lecture des gammes ayant ce modèle binaire.
  * Cette lecture suit l'ordre affiché, le changement de gamme se fera en respectant la concordance de la tonalité.
  * Il y a plusieurs choix concernant les sens de lectures :
    * De haut en bas, de bas en haut, du binaire en accord haut et bas, en suivant l'ordre des degrés.
    * En ne lisant que la ligne du binaire sélectionné, la ligne en accord,
### Les boutons horizontaux des gammes
    Nous pouvons avoir des méthodes de lecture :
    Tout comme les boutons verticaux, les boutons horizontaux peuvent lire les gammes qui ont les mêmes propriétés.
    Ou, lire les gammes à partir de ce bouton jusqu'à la fin de la liste.
**On peut créer plusieurs genres de lecture.**
* La lecture de la gamme peut se faire de façon unique ou en accord.
  * Il y a plusieurs choix concernant les sens de lectures :
    * La gamme de bas en haut, de haut en bas, en suivant les degrés.
    * On peut aussi lire les gammes qui ont des correspondances binaires. De droite à gauche ou l'inverse, en accord.
#### La fonction clic_image
    La liste selon '(self.dic_binary.keys())'.
    La liste selon 'self.colonne_bin.copy()'.
## Méthodes du traitement des modes binaires
_Il existe une seule constance au démarrage, ce sont les modes naturels binaires._<br>
_Les modes binaires sont issus du type classique des gammes primordiales, le type physique n’a pas encore été vu._<br>
_'songammes' : Construit les gammes et les binaires selon le type classique = Dictionnaire alimenté par le fichier_<br>
_'globdicTcoup.txt' : Une création des 462 formules numériques, exemple = '102034050607'._<br>
### La méthode par défaut
    Elle initialise les sept premières lignes de la colonne des modes binarisés.
    Ensuite, elle fait un sondage sur les formes binarisées restantes et à venir,
    pour définir quelle forme contient le plus de modes 'binaires' présents grâce aux modes déjà traités.
* Tel qu'il a été écrit à son départ, le traitement est en mode 'append()'<br>
C’est ainsi, que grâce aux gammes fondamentales, la colonne des binaires a été remplie.
#### La méthode des entiers (Nombres entiers)
    La liste originale des binaires a un ordre donné par **la méthode par défaut**.
    En transformant le tri en ordre croissant remplace la séquence originale.
    En inversant l'ordre croissant trié, on opère sur le tempérament original.
##### Le bouton ego et le bouton iso.
##### Le bouton ego et le bouton iso, sont inversés.
##### Les boutons int, l'un est ordonné et l'autre est inversé.
_______________________________________________________________________________
### Les réglages

Choisir la tonalité, le signe, les durées des notes et des silences.<br>
* Menus déroulants.<br>
* Par défaut, la tonalité est en DO[C].

Régler le volume.
* Curseur.<br>

Accès sur les accords typiques.
*   Radios-boutons dans une fenêtre contextuelle.<br>

### Les lectures

Types : De bas en haut, de haut en bas, de gauche à droite, de droite à gauche. <br>
Du niveau de la sélection, puis vers la gauche et la droite, l'accord est possible. <br>
Une lecture au niveau de la sélection (binaire ou gamme).
* Ne lire que la ligne (binaire, gamme).
* Lire les gammes au même binaire.
* Lire les gammes aux mêmes degrés (binaires, gammes).
* Lire à partir de la sélection (binaires, gammes).

La lecture respecte l'ordre donné par les degrés, <br>
avec la possibilité d'enregistrer et de mémoriser (gammes, accords).
* Bouton d'enregistrement.
* Bouton de mémorisation.

<br>
<br>
<br>
<br>
<br>

