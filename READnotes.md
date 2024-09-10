# BLOC NOTES songammes.py

## Vérification des fréquences.
    Seulement à corriger si besoin.
Le problème vient à cause du manque de précision du rapport (ligne/octave). Par exemple : <br>
* 1212 freq1 ['E3', 164.81] key_don ('+6', '3') dic_donne (66, 17)
* 1212 freq1 ['B3', 123.47] key_don ('+6', '7') dic_donne (66, 18) <br>
Où la note MI ayant une `ligne inférieure` avec une fréquence plus élevée que la note SI.

## Problématique liée aux mêmes modes binaires
    Le dictionnaire 'self.dic_multiples' ne distingue pas les différents rassemblements.
Voici deux choix d'une même gamme ayant deux assemblages distincts.
* 1089 self.dic_multiples [('C', '1'), ('+D', '3'), ('E', '4'), ('+A', '7')] gamme +25x note ☺
* 1089 self.dic_multiples [('C', '1'), ('+D', '3'), ('E', '4'), ('+A', '7')] gamme +25x note ☺

Chacune des lignes correspond à un mode binaire dissemblable.<br>
**Solution :** <br>
Modifier les valeurs du dictionnaire, en leur ajoutant les coordonnées des rectangles d'arrière-plan. <br>
1. [ ] col0[1], lig0[1]. Où, col0 = coin haut-gauche[x, y] et lig0 = coin bas-droit[x, y].





## Constitution des paramètres.
    Interfaçage des sonorités (volume, tempo,)
    Interfaçage des méthodes (lire une seule gamme, en ordre des degrés ou des niveaux Htz,)

## Contrôler la lecture sonore.
    En ajoutant des boutons[marche, arrêt, pause,]

## Utilisation des gammes fantômes.
    ???
