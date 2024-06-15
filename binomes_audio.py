# -*- coding: utf-8 -*-
# vicenté quantic cabviva

import inspect
from typing import Callable

# lineno() Pour consulter le programme grâce au suivi des print’s
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno


def audio_bin(gammic, plus):
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
    colis2 = plus  # Colis2
    ("binomes :", "colis1", colis1, "colis2", colis2)
    #
    "# Liste des altérations = Signature des notes."
    sup_inf = ["", "+", "x", "^", "", "^+", "o*", "-*", "*", "o", "-"]
    "# Liste des notes = Notes de musique."
    notes = ["C", "D", "E", "F", "G", "A", "B"]
    gam_maj = '102034050607'
    (lineno(), "Binary-sup_inf[-1]", sup_inf[-1], ". Notes[0]", notes[0], gam_maj)
    # 33 Binary-sup_inf[-1] – Notes[0] C 102034050607
    #
    "# Traitement basé sur colonne-bin, résumant l'ordre de lecture (selon le tri)."
    print(lineno(), "F-binomes :")
    return gam_maj
