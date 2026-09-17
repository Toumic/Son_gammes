# Contexte physique de Songammes

## Objet du document

Songammes ne simule pas un instrument acoustique complet. L'application transforme des structures musicales en une suite de hauteurs sonores, puis génère des sons simples pour permettre l'écoute et la comparaison des gammes.

Le fonctionnement repose sur quatre notions physiques :

- la fréquence, mesurée en hertz (Hz) ;
- la hauteur perçue, principalement liée à la fréquence fondamentale ;
- l'octave, qui correspond au doublement de la fréquence ;
- la représentation numérique des degrés et des intervalles.

## Du code numérique à la hauteur sonore

Les fichiers de données de Songammes décrivent des gammes sous forme de chaînes numériques. Dans une forme énumérée comme `102034050607`, les positions correspondent aux degrés de la gamme et les chiffres indiquent leur emplacement relatif dans la représentation utilisée par l'application.

Les codes binaires utilisent une logique de présence ou d'absence. Un `1` représente un degré ou une position retenue, tandis qu'un `0` représente une position vide. Ces codes servent surtout à classer, comparer et parcourir les gammes ; ils ne sont pas directement des fréquences.

Le module `gammes_audio.py` transforme ensuite les degrés en noms de notes, en tenant compte de la tonalité et des signes représentés par les symboles internes de Songammes.

## Tempérament égal

Le calcul des fréquences suit le principe du tempérament égal à douze subdivisions par octave. Deux notes séparées d'un demi-ton ont un rapport de fréquences égal à :

$$
2^{1/12}
$$

Pour une note située à `n` demi-tons du La 440 Hz, la fréquence théorique est :

$$
f(n) = 440 \times 2^{n/12}
$$

Une octave plus haute multiplie la fréquence par 2 ; une octave plus basse la divise par 2. Ce modèle permet de transposer une même structure de gamme vers plusieurs tonalités tout en conservant les rapports intervalliques du tempérament choisi.

Dans le code, les fréquences sont construites à partir de valeurs de référence d'octave et de la formule `2 ** ((x - 1) / 12)`. Les fréquences sont arrondies à deux décimales lorsqu'elles sont préparées pour l'interface.

## Octaves et registres

Songammes prépare une série d'octaves dont les références commencent à 13,75 Hz et progressent par doublement :

- 13,75 Hz ;
- 27,5 Hz ;
- 55 Hz ;
- 110 Hz ;
- 220 Hz ;
- 440 Hz ;
- 880 Hz ;
- puis les registres supérieurs.

La référence 440 Hz correspond au La utilisé pour accorder les instruments modernes. Les notes affichées dans l'interface portent un numéro d'octave interne, par exemple `C6` ou `A3`. Ce numéro sert à organiser la tessiture et ne doit pas être confondu avec le numéro de demi-ton utilisé dans les calculs.

## Signes et hauteur relative

Les symboles internes comme `+`, `-`, `o`, `x` ou `^` codent des modifications de hauteur ou des relations de transposition dans les structures de Songammes. Ils appartiennent au vocabulaire numérique et modal de l'application.

Ils ne doivent pas être interprétés automatiquement comme une notation standard unique : leur signification dépend de la table de conversion du module `gammes_audio.py`. L'application les utilise pour conserver la relation entre :

- la note naturelle ;
- sa signature ou son altération ;
- le degré modal ;
- la tonalité de référence ;
- l'octave choisie pour la lecture.

## Génération du son

Lorsque la lecture audible est activée, Songammes génère une onde sinusoïdale :

$$
s(t) = A \sin(2\pi f t)
$$

avec :

- `A`, l'amplitude, fixée ici à environ `0,5` ;
- `f`, la fréquence de la note ;
- `t`, le temps ;
- une fréquence d'échantillonnage de 18 000 échantillons par seconde.

L'onde est convertie en valeurs flottantes `float32`, puis envoyée à PyAudio dans un flux mono. La lecture utilise donc un son de référence très simple : une sinusoïde sans harmoniques ajoutées.

## Ce que l'oreille entend

La fréquence fondamentale donne principalement la sensation de hauteur. Dans un instrument réel, le son contient aussi des harmoniques dont les amplitudes varient selon l'instrument, la note et la manière de jouer.

La sinusoïde de Songammes permet donc de comparer clairement :

- les hauteurs ;
- les écarts entre les notes ;
- les changements de tonalité ;
- l'ordre de lecture des degrés ;
- les notes communes entre deux gammes.

En revanche, elle ne reproduit pas le timbre d'un piano, d'une voix ou d'un instrument à cordes.

## Lecture statique et lecture dynamique

En lecture statique, chaque gamme est rapportée à la tonalité de référence, généralement Do. Cette option facilite la comparaison directe des structures : les différences entendues viennent principalement des degrés et des intervalles.

En lecture dynamique, la tonalité de la gamme suivante dépend des correspondances calculées entre les gammes voisines. Le parcours sonore devient alors une succession de transpositions. Cette méthode met davantage en évidence les relations de continuité entre les gammes.

La lecture dynamique ne constitue pas une modélisation complète de l'acoustique d'un instrument. Elle est une règle musicale et algorithmique de changement de tonalité.

## Limites physiques actuelles

Le moteur sonore actuel est volontairement minimal :

- une seule forme d'onde, la sinusoïde ;
- un canal mono ;
- pas d'enveloppe d'attaque ou d'extinction ;
- pas de modèle de résonance ;
- pas de filtrage ni d'égalisation ;
- pas de normalisation perceptive entre les notes ;
- pas de simulation de salle ou de propagation spatiale.

Ces limites sont utiles pour l'analyse des structures, car elles réduisent les effets qui pourraient masquer les rapports entre les fréquences.

## Évolutions possibles

Un futur modèle physique ou perceptif pourrait ajouter :

1. une enveloppe ADSR pour éviter les attaques et coupures abruptes ;
2. plusieurs formes d'onde avec un choix de timbre ;
3. des harmoniques contrôlées pour simuler différents instruments ;
4. un volume normalisé selon la tessiture ;
5. une sortie stereo ou une spatialisation des voix ;
6. une comparaison entre tempérament égal et justesse naturelle ;
7. un affichage simultané des fréquences, des intervalles et des rapports physiques.

## Résumé

Songammes relie une organisation discrète des gammes à un phénomène continu : la vibration sonore. Les codes numériques choisissent les degrés et leur ordre ; le calcul de tempérament détermine les fréquences ; PyAudio transforme enfin ces fréquences en une onde audible.

L'application est donc principalement un outil de comparaison musicale et numérique, avec une restitution physique simplifiée, stable et lisible.
