# -*- coding: utf-8 -*-
# vicenté quantic cabviva

import inspect
from typing import Callable

# lineno() Pour consulter le programme grâce au suivi des print’s
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno


def audio_gam(gammic, pulsif):
    """Ce module[gammes_audio.py] est appliqué au traitement des gammes selon la méthode choisie
     par l'utilisateur. Puis, en retour, il retourne une séquence destinée à être traitée par le module gensound,
     afin d'entendre les sonorités des gammes sélectionnées. """
    "Bb varie selon la sélection"
    # colis1[0] = bb  +34x
    "Cc est invariant."
    # ..1[1] = cc  {1: ['123400000567', '123000004567', '120000034567', '100000234567', '123456700000', '',
    "Colonne_gam et colonne_bin varient selon la sélection."
    # ..1[2] = colonne_gam  {(1, 0): ['0'], (1, 2): ['1'], (1, 3): ['2'], (1, 4): ['3'],
    # ..1[3] = colonne_bin  ['', '', '1111111', '1101110', '1001100', '1110111', '1111110', '1101100', '1001000',
    "Dic_indice, dic_codage, dic_force sont produits au début et sont invariants."
    # ..1[4] = dic_indice  {'o45x': 1, 'o46-': 2, 'o4': 3, 'o46+': 4, 'o45-': 5, 'o54-': 6, '*5': 7, '-34': 8,
    # ..1[5] = dic_codage  {(1, '123400000567'): [(['o45x', 1], '1000001'), (1, 2, '1000001'), (1, 3, '1000001'),
    # ..1[6] = self.dic_force {'1000001': [((1, '123400000567'), (['o45x', 1], '1000001')), (1, 2, '1000001'),
    "Le tri varie selon la sélection"
    # ..1[7] = tri  None
    # colis2[0] {'A0': [('A', 13.75), ('', 14.56761754744031), ('B', 15.433853164253879), ('C', 16.351597831287414),
    colis1 = gammic  # Colis1
    colis2 = pulsif  # Colis2
    ("gammes :", "colis1", colis1, "colis2", colis2)
    #
    "# Liste des altérations = Signature des notes."
    sup_inf = ["", "+", "x", "^", "", "^+", "o*", "-*", "*", "o", "-"]
    "# Liste des notes = Notes de musique."
    notes = ["C", "D", "E", "F", "G", "A", "B"]
    gam_maj = '102034050607'
    (lineno(), "Gammes-sup_inf[-1]", sup_inf[-1], ". notes[0]", notes[0], gam_maj)
    # 33 Gammes-sup_inf[-1] - notes[0] C 102034050607

    "# Traitement basé sur les colonnes(bin, gam), résumant l'ordre de lecture (selon le tri)."
    nom_gam = colis1[0]  # Procuration du nom de la gamme. … [0]. Variant.
    num_gam = colis1[4][nom_gam]  # Procuration du numéro de la gamme. ... [4]. Invariant.
    (lineno(), "Variants nom", nom_gam, "num", num_gam)
    num_var, cod_var = -1, -1
    # Retrouver le numéro invariant de la gamme choisie avec colis1[5], dic_codage.
    for clef in colis1[5].keys():
        if nom_gam == colis1[5][clef][0][0][0]:  # Le numéro invariant correspondant.
            num_var = clef[0]  # Num_var donne le numéro invariant de la gamme. De 1 à 66.
            cod_var = clef[1]  # Cod_var donne la gamme énumérée. Ex : 102034050607.
            print(lineno(), "clef", clef, nom_gam, "num_var", num_var, "cod_var", cod_var)
            # 51 clef (2, '123400056007') o46- num_var 2 cod_var 123400056007
            break
    # Retrouver la position variante de la gamme choisie avec colis1[2], colonne_gam.
    for g in colis1[2].keys():
        if g[1] == 0 and colis1[2][g][0] == nom_gam:  # La position variante correspondante.
            rng_gam = g[0]
            print(lineno(), "G", colis1[2][g], g, "rng_gam", rng_gam, ", dans colonne_gam.")
            # 58 G ['o46-'] (5, 0) rng_gam 5
            break
    #

    #
    for c1 in range(0, len(colis1[3])):  # Colis[3] = colonne-bin.
        (lineno(), "F-gammes c1:", c1, "nom_gam", nom_gam, "num_gam", num_gam, num_var, cod_var)
        break
    print(lineno(), "F-gammes :")
    return gam_maj
