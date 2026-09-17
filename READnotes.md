# BLOC NOTES songammes.py


## Défaut de lecture au type 'Anti iso'
    Une erreur se produit lorsque l'organisation des binaires est au type 'Anti iso'
## Vérification des fréquences.
    Seulement à corriger si besoin.
Le problème vient à cause du manque de précision du rapport (ligne/octave). Par exemple : <br>
* 1212 freq1 ['E3', 164.81] key_don ('+6', '3') dic_donne (66, 17)
* 1212 freq1 ['B3', 123.47] key_don ('+6', '7') dic_donne (66, 18) <br>
Où la note MI ayant une `ligne inférieure` avec une fréquence plus élevée que la note SI. <br>
Y a besoin de calibrer les octaves à l'aide des notes réelles signées.


    Les fréquences hertziennes anormalement élevées, dans cette série de gammes.
Cette liste a des fréquences anormales [-26o, *6, o6, -36].

**Solution :** <br>
Se corrige avec l'amélioration du code.

## Dissociation des analyses intermodales
    Les réparations intermodales ne sont pas réalisées en mode de lecture binaire.
À la ligne 889 du module `gammes_audio.py` l'instruction `if titre1 == 'Gammes':` est arbitraire. <br>
En effet, les modes terminaux binaires pouvant recevoir cette analyse, n'y sont pas traités.

**Solution :** <br>
L'arrangement a été produit grâce à la création, d'une nouvelle liste située à `if titre1 == 'Binomes':`.


## Problématique liée aux mêmes modes binaires
    Le dictionnaire 'self.dic_multiples' ne distingue pas les différents rassemblements.
Voici deux choix d'une même gamme ayant deux assemblages distincts.
* 1089 self.dic_multiples [('C', '1'), ('+D', '3'), ('E', '4'), ('+A', '7')] gamme +25x note ☺
* 1089 self.dic_multiples [('C', '1'), ('+D', '3'), ('E', '4'), ('+A', '7')] gamme +25x note ☺
* Chacune des lignes correspond à un mode binaire dissemblable.<br>

**Solution :** <br>
Modifier les valeurs du dictionnaire, en leur ajoutant les coordonnées des rectangles d'arrière-plan. <br>
1. [ ] col0[1], lig0[1]. Où, col0 = coin haut-gauche[x, y] et lig0 = coin bas-droit[x, y].


    Lors de la sélection d'un bouton binaire, la lecture se comporte anormalement.
Les gammes ne sont pas lues selon l'ordre apparaissant dans l'interface de l'utilisateur. <br>
Le rectangle toute hauteur, "celui qui signale le niveau de lecture sonore", ne s'affiche pas. <br>
**Le problème ne vient pas de :**
* Le dictionnaire self.colonne_gam, le changement après le tri a bien eu lieu. (Ligne 428) <br>

**Solution :** <br>
A changé l'identification du rectangle, par un indice équivalant ici : `ind_gam = liste_gam.index(k2)` <br>


## Constitution des paramètres.
    Interfaçage des sonorités (volume, tempo, audio ou pas)
    Paramétrer les fréquences aux positions réelles, quand (ligne//8 = Octave)
    -   Il y a soixante-trois lignes liées aux modes binaires et huit octaves pan['A2'...'A9']

## Contrôler la lecture sonore.
    En ajoutant des boutons[marche, arrêt, pause, enregistrement]
Un bouton radio a été ajouté offrant le choix d'entendre ou pas les gammes lors de la sélection.

## Utilisation des gammes fantômes.
    ???
