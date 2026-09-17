# Manuel d'utilisation de Songammes

## 1. Présentation

Songammes est une application Windows qui permet de visualiser, comparer et écouter des gammes diatoniques. Elle organise 66 gammes fondamentales et leurs sept modes selon plusieurs ordres.

L'application produit des sons simples à partir d'ondes sinusoïdales. Elle sert à comparer les degrés, les intervalles, les tonalités et les ordres de lecture ; elle ne simule pas le timbre d'un instrument réel.

## 2. Installation

### Prérequis

- Windows ;
- Python 3.12 ou une version compatible ;
- un périphérique audio fonctionnel.

Depuis PowerShell, ouvrir le dossier du projet puis exécuter :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install numpy Pillow PyAudio
```

### Démarrage

```powershell
python songammes.py
```

Les fichiers de données et les images doivent rester dans le même dossier que `songammes.py`.

## 3. Organisation de la fenêtre

La fenêtre principale comprend :

- une grille centrale présentant les gammes, les degrés et les modes binaires ;
- une colonne de boutons binaires à gauche ;
- une rangée de boutons de gammes en haut ;
- cinq zones de boutons radio pour choisir le parcours ;
- six images de tri à droite ;
- les commandes de lecture et le volume en bas.

Les zones `X`, `Y` et `Z` sont des repères visuels de l'interface.

## 4. Les boutons radio

### Toutes ou une seule gamme ?

- **Global** : parcourt toutes les gammes concernées par la sélection ;
- **Unique** : s'arrête après la gamme sélectionnée.

### En Do ou tonalité dynamique ?

- **Statique** : rapporte les gammes à la tonalité de référence, généralement Do ;
- **Dynamique** : utilise les correspondances entre gammes voisines pour faire évoluer la tonalité.

### Ordre de lecture

- **Groupement** : conserve l'organisation principale des degrés ;
- **Diatonique** : suit l'ordre des degrés diatoniques ;
- **Hertzien** : classe les notes selon leur fréquence, du grave vers l'aigu.

### Audio

- **Couper l'audio** : parcourt et affiche les notes sans les jouer ;
- **Entendre** : joue les notes pendant le parcours.

### Forme traitée

- **Modes binarisés** : traite les codes binaires de sept positions ;
- **Gammes énumérées** : traite les formes numériques des gammes ;
- **Contient intervalles** : traite les quantités d'intervalles entre les degrés.

## 5. Les boutons de tri

Les six images de tri correspondent à trois organisations et à leurs inversions :

- **Tri EGO** : organisation construite à partir de la gamme naturelle ;
- **Anti EGO** : même organisation inversée ;
- **Tri ISO** : organisation construite à partir des formules de `globdicTcoup.txt` ;
- **Anti ISO** : organisation ISO inversée ;
- **Tri INT** : organisation numérique croissante ;
- **Anti INT** : organisation numérique décroissante.

Cliquer sur une image de tri reconstruit l'affichage selon l'organisation choisie. Lorsque `Gammes` ou `Contient` est sélectionné, l'application peut demander l'étendue du traitement.

## 6. Lire une gamme ou un mode

1. Choisir une gamme avec un bouton horizontal, ou un mode binaire avec un bouton vertical.
2. Choisir les options radio souhaitées.
3. Choisir éventuellement une image de tri.
4. Cliquer sur **Lecture**.
5. Observer la progression dans la grille et, si l'audio est activé, écouter les notes.

La gamme ou le mode sélectionné sert de point de départ au parcours.

## 7. Commandes de lecture

- **Lecture** : démarre le parcours depuis la position préparée. Après une modification d'un bouton radio, la lecture repart au début ;
- **Arrêter** : demande l'arrêt et vide les sons en attente ;
- **Reprise** : reprend à la dernière position mémorisée ;
- **Réinitialiser** : arrête la lecture, efface les notes affichées et remet la progression au début.

Modifier un bouton radio arrête automatiquement la lecture et réinitialise l'affichage. Le volume et les commandes de lecture ne déclenchent pas cette réinitialisation.

## 8. Volume et audio

Le curseur **Volume** règle le niveau de sortie entre 0 et 100. Il ne change pas l'organisation de la grille et ne réinitialise pas la lecture.

Le son produit est une sinusoïde mono à 44 100 échantillons par seconde, avec un court fondu d'entrée et de sortie. Le volume maximal du signal est limité avant l'application du réglage du curseur.

## 9. Lire les informations d'une note

Cliquer sur une note affichée ouvre une fenêtre d'information contenant notamment :

- la gamme choisie ;
- la note tonique ;
- le modèle énuméré ;
- le degré modal ;
- le mode diatonique ;
- la formule tonale.

Lorsqu'un symbole regroupe plusieurs degrés, le survol affiche les notes concernées et le clic permet d'examiner leur information.

## 10. Dépannage

### La fenêtre ne démarre pas

Vérifier que Python est actif dans l'environnement virtuel et que les dépendances sont installées :

```powershell
python -m pip install numpy Pillow PyAudio
```

### Une image ou un fichier est introuvable

Vérifier que les fichiers suivants sont toujours à côté de `songammes.py` :

- `globdicTcoup.txt` ;
- `gamme_majeure.txt` ;
- les six images `Bouton*.png`.

### Le son ne sort pas

Vérifier le périphérique audio Windows, sélectionner **Entendre** et augmenter le curseur **Volume**. Le mode **Couper l'audio** n'émet volontairement aucun son.

### La lecture semble bloquée

Une lecture longue peut occuper l'interface pendant son déroulement. Utiliser **Arrêter**, puis **Réinitialiser** avant de relancer une lecture.

## 11. Limites connues

- l'application est actuellement conçue pour Windows ;
- le son est une sinusoïde et ne reproduit pas un instrument réel ;
- les changements de boutons radio prennent effet avec la prochaine lecture ou le prochain tri ;
- les options `Modes`, `Gammes` et `Contient` ne produisent pas exactement les mêmes tableaux ;
- les gammes fantômes et l'enregistrement de parcours ne sont pas implémentés.

## 12. Documentation complémentaire

- [README du projet](READme.md) : installation rapide et architecture ;
- [Contexte physique](CONTEXTE_PHYSIQUE.md) : fréquences, octaves et génération sonore ;
- [Notes techniques](READnotes_songammes.md) : historique et détails internes.
