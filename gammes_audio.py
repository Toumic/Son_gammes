# -*- coding: utf-8 -*-
# vicenté quantic cabviva

import inspect
from typing import Callable

# lineno() Pour consulter le programme grâce au suivi des print’s
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

"# dic_maj = Référence des tonalités majeures primaires à transposer"
dic_maj = {'C': ['C', '', 'D', '', 'E', 'F', '', 'G', '', 'A', '', 'B'],
           'D': ['D', '', 'E', '', '+F', 'G', '', 'A', '', 'B', '', '+C'],
           'E': ['E', '', '+F', '', '+G', 'A', '', 'B', '', '+C', '', '+D'],
           'F': ['F', '', 'G', '', 'A', '-B', '', 'C', '', 'D', '', 'E'],
           'G': ['G', '', 'A', '', 'B', 'C', '', 'D', '', 'E', '', '+F'],
           'A': ['A', '', 'B', '', '+C', 'D', '', 'E', '', '+F', '', '+G'],
           'B': ['B', '', '+C', '', '+D', 'E', '', '+F', '', '+G', '', '+A']}
tab_sup = ['', '+', 'x', '^', '+^', 'x^', '^^', '+^^', 'x^^', '^^^', '+^^^', 'x^^^', '^^^^', '+^^^^', 'x^^^^',
           '^^^^^', '+^^^^^', 'x^^^^^', '^^^^^^', '+^^^^^^', 'x^^^^^^', '^^^^^^^', '+^^^^^^^', 'x^^^^^^^', '^^^^^^^^']
tab_inf = ['********', 'o*******', '-*******', '*******', 'o******', '-******', '******', 'o*****', '-*****', '*****',
           'o****', '-****', '****', 'o***', '-***', '***', 'o**', '-**', '**', 'o*', '-*', '*', 'o', '-']
(lineno(), "Inverser convenablement (12 * -1 = -12) tab_inf", tab_inf[::-1])


def initie(neo_maj):
    """Recoder les infos[]. Nouvelle gamme majeure pour 'dic_maj' """
    "# Processus de reconnaissance de la signature tonique."
    signe_nat, note_classic = "", "CDEFGAB"
    for sn in neo_maj:
        if sn not in note_classic:
            signe_nat += sn
    # Valeur numérique de 'sign_nat'.
    ind_signe = 0
    if signe_nat in tab_inf:
        ind_signe = tab_inf.index(signe_nat) - len(tab_inf)
        (lineno(), "inf", signe_nat, len(tab_inf))
    elif signe_nat in tab_sup:
        ind_signe = tab_sup.index(signe_nat)
        (lineno(), "sup", signe_nat)
    (lineno(), "Valeur du signe entrant", ind_signe)
    note_nat = neo_maj[-1]
    (lineno(), "Fonction initie neo_maj", neo_maj, "signe et note", signe_nat, note_nat)
    # 32 Fonction/initie neo_maj -E Le signe et la note - E

    "# Calcul de la nouvelle gamme majeure et enregistrement dans le dictionnaire 'dic_maj"
    dic_maj[neo_maj] = []
    ind_signe2 = ind_signe3 = 0
    for nm in dic_maj[note_nat]:
        nm2, signe2, nm3, signe3 = "", "", "", 0
        if nm != "":
            if len(nm) == 1:
                nm2 += signe_nat + nm
                (lineno(), "Nm unique", nm, "nm2", nm2)
            else:
                note2 = nm[-1]
                for sn2 in nm:
                    if sn2 not in note_classic:
                        signe2 += sn2
                if signe2 in tab_inf:
                    ind_signe2 = tab_inf.index(signe2) - len(tab_inf)  # Signature majeure originale.
                    ind_signe3 = ind_signe + ind_signe2
                    if ind_signe3 > -1:
                        signe3 = tab_sup[ind_signe3]
                    else:
                        signe3 = tab_inf[ind_signe3]
                    nm3 = signe3 + note2
                    (lineno(), "inf", signe2, len(tab_inf), signe3)
                elif signe2 in tab_sup:
                    ind_signe2 = tab_sup.index(signe2)  # Signature avant modification.
                    ind_signe3 = ind_signe + ind_signe2
                    if ind_signe3 < 0:
                        signe3 = tab_inf[ind_signe3]
                    else:
                        signe3 = tab_sup[ind_signe3]
                    nm3 = signe3 + note2
                    (lineno(), "sup", signe2, signe3)
                nm2 = nm3
                (lineno(), "Nm pluriel", nm, "nm2", nm2, "signe2", signe2, "signe3", signe3)
                (lineno(), "ind_signe", ind_signe, "ind_signe2", ind_signe2, "ind_signe3", ind_signe3)
            (lineno(), "Nm", nm, "signe_nat", signe_nat)
        dic_maj[neo_maj].append(nm2)
    (lineno(), "Fonction Majeure neo_maj", neo_maj, "dic_maj", dic_maj[neo_maj])
    # 82 Fonction Majeure neo_maj -E dic_maj ['-E', '', 'F', '', 'G', '-A', '', '-B', '', 'C', '', 'D']


def audio_gam(gammic, pulsif, selon):
    """Ce module[gammes_audio.py] est appliqué au traitement des gammes selon la méthode choisie
     par l'utilisateur. Puis, en retour, il retourne une séquence destinée à être traitée par le module gensound,
     afin d'entendre les sonorités des gammes sélectionnées. """
    colis1 = gammic  # Colis1
    colis2 = pulsif  # Colis2
    titre1 = selon  # Le titre est selon le type de données en entrée, soit gamme ou binôme.
    liste_gen = []  # Retour de la liste des gammes à lire.
    ("gammes :", "colis1", colis1, "colis2", colis2, "titre1", titre1)

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
    "La répartition des hertz sur douze octaves"
    # colis2 {'A0': [('A', 13.75), ('', 14.56761754744031), ('B', 15.433853164253879), ('C', 16.351597831287414),

    "# Liste des notes = Notes de musique."
    num_mem = {('0', 1): [('1', 'C'), ('2', 'D'), ('3', 'E'), ('4', 'F'), ('5', 'G'), ('6', 'A'), ('7', 'B')]}
    notes = [nm[1] for nm in num_mem['0', 1]]
    # ["C", "D", "E", "F", "G", "A", "B"]
    num_mem.clear()
    notes_maj = notes.copy()
    gam_maj = '102034050607'
    (lineno(), "Gammes. notes[0]", notes[0], gam_maj)
    # 33 Gammes-sup_inf[-1] - notes[0] C 102034050607

    if titre1 == "Gammes":
        """C’est une fonction de trouver la gamme sélectionnée et de séparer sa valeur invariable et variable. Le
        traitement se base sur les colonnes (bin ou gam), résumant l'ordre de lecture (selon le tri). """
        nom_gam = colis1[0]  # Procuration du nom de la gamme. … [0]. Variant.
        num_gam = colis1[4][nom_gam]  # Procuration du numéro de la gamme. ... [4]. Invariant.
        (lineno(), "Variants nom", nom_gam, "num", num_gam)
        # Retrouver le numéro invariant de la gamme choisie avec colis1[5], dic_codage.
        for clef in colis1[5].keys():
            if nom_gam == colis1[5][clef][0][0][0]:  # Le numéro invariant correspondant.
                num_var = clef[0]  # Num_var donne le numéro invariant de la gamme. De 1 à 66.
                cod_var = clef[1]  # Cod_var donne la gamme énumérée. Ex : 102034050607.
                (lineno(), "Invariant, clef", clef, nom_gam, cod_var, "num_var", num_var, "dans dic_codage.")
                # 51 Invariant, clef (41, '102034056007') -6 num_var 41 dans dic_codage.
                break
        # Retrouver la position variante de la gamme choisie avec colis1[2], colonne_gam.
        rng_gam = 0
        for g in colis1[2].keys():
            if g[1] == 0 and colis1[2][g][0] == nom_gam:  # La position variante correspondante.
                rng_gam = g[0]
                (lineno(), "Variant, G", colis1[2][g], g, "rng_gam", rng_gam, ", dans colonne_gam.")
                # 58 Variant, G ['-6'] (64, 0) rng_gam 64 , dans colonne_gam.
                break
        "À ce moment, on a l'emplacement de la gamme dans les hiérarchies suivantes : constante/variante."
        "Ainsi, qu'un modèle de lecture audio relatif à la sélection."
        # Lire les gammes à partir du point 'rng_gam' correspondant à la gamme sélectionnée.
        liste_gen.clear()
        for g2 in colis1[2].keys():
            if g2[0] >= rng_gam:
                liste_gen.append(g2)
                (lineno(), "colis1[2] G2", g2, colis1[2][g2])

    elif titre1 == "Binomes":
        """C’est une fonction de trouver le binaire sélectionné et de séparer sa valeur invariable et variable. Le
        traitement se base sur les colonnes (bin ou gam), résumant l'ordre de lecture (selon le tri)."""
        nom_bin = colis1[0]  # Procuration du nom du binaire. … [0]. Variant.
        num_bin = colis1[3].index(nom_bin)  # Procuration de l'index du binaire. … [0]. Variant.
        (lineno(), "Variants nom_bin", nom_bin, "num_bin", num_bin)
        # Retrouver les gammes qui correspondent à ce nom binaire par # ..1[6] = self.dic_force.
        "# Commencer par les gammes invariables, afin de retrouver les mêmes après le tri."
        bin_invariant, bina = set(), ""
        (lineno(), "nom_bin", nom_bin, "colis1[6]", colis1[6][nom_bin])
        for key6 in colis1[6][nom_bin]:  # Cherche les noms des gammes ayant le binaire 'nom_bin' Invariant.
            if len(key6) < 3 and key6[0][0] not in bin_invariant:
                if isinstance(key6[0][0], str):
                    bina = key6[0][0]
                    (lineno(), "key6<3 STR", key6[0][0], "bina", bina)
                elif isinstance(key6[0][0], int):
                    (lineno(), "key6<3 INT", key6[0][0], "bina", bina)
                    # 89 key6<3 INT 2 bina
                    for di4 in colis1[4].keys():  # Clé = nom, valeur = numéro. Invariant.
                        if colis1[4][di4] == key6[0][0]:
                            bina = di4
                            (lineno(), "2 key6", key6[1][0], "di4", di4, colis1[4][di4], "bina", bina)
                            break
                    (lineno(), "key6(nom)", key6[0][0], "bina", bina)
            else:
                for di4 in colis1[4].keys():
                    if colis1[4][di4] == key6[0]:
                        bina = di4
                (lineno(), "key6=3", key6[0], "bina", bina)
            if bina != "":
                bin_invariant.add(bina)
        (lineno(), "bin_invariant =", bin_invariant, "Long =", len(bin_invariant))
        "# La liste des gammes d'origine invariable est complétée dans 'bin_invariant'."
        # Transformer la liste des numéros invariables, pour une compatibilité variante.
        liste_gen.clear()  # Liste des gammes ordonnées selon la sélection de tri de l'utilisateur.
        ok = None
        for bi in bin_invariant:
            for co2 in colis1[2].keys():  # ..1[2] = colonne_gam  {(1, 0): ['0'], (1, 2) : selon sélection.
                if co2[1] == 0 and colis1[2][co2][0] == bi:
                    ok = co2[0]
                if ok == co2[0] and co2 not in liste_gen:
                    liste_gen.append(co2)
                    (lineno(), "co2", co2, colis1[2][co2])
        (lineno(), "liste_gen", liste_gen)

    print(lineno(), "colis1[0]", colis1[0], "Liste_gen :", liste_gen[:8], "\n")
    # 197 colis1[0] -3 Liste_gen : [(64, 0), (64, 59), (64, 57), (64, 44), (64, 60)...
    ("# La liste 'liste_gen' contient des tuples ayant (numéro de colonne, numéro de ligne)."
     "Ces tuples ont été produits selon le bouton (nom ou binôme) sélectionné par l'utilisateur."
     "Maintenant, il faut situer chaque degré avec sa fréquence hz et ses notes diatoniques."
     "Situer les fréquences hz : grâce au dictionnaire 'colis2[0]'."
     "Situer les notes diatoniques : grâce au dictionnaire 'colis1[1]'.")

    "# Situation des fréquences hertziennes : grâce au dictionnaire 'colis2[0]'."
    (lineno(), "colis2", colis2.keys())
    # 206 colis2 dict_keys(['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11'])
    ("Il y a douze octaves, la note LA 440hz est à la clef 'A5' et les limites d'audibilité sont de 'A1' à 'A9'."
     "En comptant les soixante-six gammes, elles peuvent s'étaler sur six octaves et la clef 440 est en 'A5'."
     "Pour connaitre le bon emplacement d'une gamme par rapport à la clef 'A5', il faut l'indice de la gamme."
     "L'indice de la gamme est détenu dans la liste 'colonne_gam' --> 'colis1[2]'.")

    "# Commencer par découvrir les tonalités diatoniques des gammes choisies, afin d'établir les bonnes octaves."
    # La première des gammes, qui est aussi celle choisie, commence en DO par défaut.
    # Ainsi, à partir du numéro de colonne, à la ligne zéro, on trouve le nom de la gamme.
    dic_dic, dic_deg = {}, {}  # Dictionnaire du dictionnaire aux degrés au même binaire.
    dic_log = {}  # Dictionnaire, clé = le nom de la gamme, valeurs = les données diatoniques[Notes réelles]
    for lg in liste_gen:
        if lg[1] == 0:
            nom_lg = colis1[2][lg][0]  # La donnée variable est insuffisante pour sa forme invariante. 'colonne_gam'.
            dic_log[lg[0]] = [nom_lg]
            num_lg = colis1[4][nom_lg]  # Donne le numéro de la gamme invariante. 'dic_indice'.
            (lineno(), "nom_lg", nom_lg)  # Fourni les noms des gammes relatives.
            # 145 nom_lg x3. 145 nom_lg -45. ...
            "# Trouver les degrés au même binaire."
            for kd5 in colis1[5].keys():  # Gamme diatonique selon 'dic_codage' qui est invariant.
                if num_lg in kd5:
                    cop_kd5 = kd5  # Clef invariable (1, '123400000567')
                    dic_dic[colis1[0]] = dic_deg  # Le dico 'dic_dic', clé=nom, valeur=dictionnaire 'dic_deg'.
                    bin_inf = colis1[5][kd5][0][-1]
                    (lineno(), "bin_inf", bin_inf, "1er binaire-clé")
                    dic_deg[(nom_lg, bin_inf)] = [cop_kd5[1], 1]
                    (lineno(), "num_lg", num_lg, "cop_kd5", cop_kd5, "\n colis1[5]", colis1[5][cop_kd5])
                    # 154 num_lg 56 cop_kd5 (56, '102000345607')
                    #  colis1[5] [(['x3', 375], '1100011'), (56, 2, '1000110'), (56, 3, '1000000'),
                    for kc5 in colis1[5][cop_kd5]:  # Scruter les degrés aux binaires.
                        if len(kc5) > 2:
                            if (nom_lg, kc5[-1]) in dic_deg.keys():
                                dic_deg[(nom_lg, kc5[-1])].append(kc5[1])
                            else:
                                dic_deg[(nom_lg, kc5[-1])] = []
                                dic_deg[(nom_lg, kc5[-1])].append(kc5[1])
                            set(dic_deg[(nom_lg, kc5[-1])])
                        (lineno(), "kc5", kc5)
                        # 164 kc5 (56, 2, '1000110')
                    (lineno(), "\n dic_dic", dic_dic[colis1[0]], "\n dic_deg", dic_deg)
                    # dic_dic {('-4', '1100111'): [1], ('-4', '1001110'): [2], ('-4', '1010011'): [3]
            (lineno(), "\n dic_dic", dic_dic[colis1[0]], "\n dic_deg", dic_deg)
            #  dic_deg {('-3', '1101111'): ['102304050607', 1], ('-3', '1001110'): [2], ('-3', '1110011'): [3]
    "# À ce niveau, le dictionnaire de dictionnaire a rangé les degrés dans leurs binaires respectifs."
    (lineno(), "* dic_dic", dic_dic.keys(), "\n dic_deg", list(dic_deg.keys())[:5])
    # 251 * dic_dic dict_keys(['-3'])
    #  dic_deg [('-3', '1101111'), ('-3', '1001110'), ('-3', '1110011'), ('-3', '1110110'), ('-3', '1111100')]

    "# Détailler la gamme sélectionnée diatoniquement à l'aide d'un dictionnaire à une seule clé."
    tab_gen, tab_ok = {}, True  # Dictionnaire, clef = nom gamme, valeur = numéro dynamique de la gamme.
    for ddc in dic_dic.keys():
        # deg_note, deg_mode = 0, 0
        (lineno(), "premier_tour = Clé dictionnaire principal,", "ddc", ddc)
        # 258 premier_tour = Clé dictionnaire principal, ddc -3

        "# Le dictionnaire 'dic_deg' a la séquence des gammes suivantes."
        for ddg in dic_deg.keys():
            num_mem[ddg[0], 1] = []  # Le dictionnaire 'num_mem' et ses valeurs diatoniques en mode tonique.
            (lineno(), "ddg[0]", ddg[0], "num_mem", num_mem)
            # 264 ddg[0] -3 num_mem {('-3', 1): []}
            if isinstance(dic_deg[ddg][0], str):  # Va de gamme en gamme
                num_dia = dic_deg[ddg][0]
                num_log = colis1[4][ddg[0]]  # Donne le numéro de la gamme invariante. 'dic_indice'.
                (lineno(), "Forme énumérée num_dia", num_dia, "ddg", ddg, "num_log", num_log)
                # 269 Forme énumérée num_dia 102304050607 ddg ('-3', '1101111') num_log 36
                # 269 Forme énumérée num_dia 102034056007 ddg ('-6', '1111101') num_log 41
                # 269 Forme énumérée num_dia 102034050067 ddg ('+6', '1111101') num_log 46

                "# Trouver le numéro dynamique de la gamme dans la liste 'liste_gen'"
                if tab_ok:
                    tab_gen[ddg[0]] = []
                    for lg2 in liste_gen:
                        if lg2[0] not in tab_gen[ddg[0]]:
                            tab_gen[ddg[0]].append(lg2[0])
                            (lineno(), ddg[0], "tab_gen", tab_gen[ddg[0]], "lg2", lg2)
                            # 215 -3 tab_gen [64, 65, 66] lg2 (66, 0)
                    tab_ok = False

                "# Lecture de la liste des formes énumérées (num_dia). Mode tonique uniquement."
                deg_note = deg_gam = 0
                for num in num_dia:  # Lecture de la tonique énumérée.
                    "# Partie correspondante à la première exécution ayant la note DO comme tonique par défaut."
                    num_note = ""  # num_note = tab_inf[val_num] + notes[deg_note]
                    deg_niv = ""  # deg_niv = tab_inf[val_num] + str(deg_gam)

                    "# Si la valeur de 'num' n'est pas un intervalle vide (= '0')"
                    if num != '0':
                        (lineno(), ddg[0], num, "num_dia", num_dia, "____Lecture diatonique___deg_note ", deg_note)
                        # 294 -3 C1 102304050607 ____________Lecture diatonique____________________ 0
                        ind_num0 = num_dia.index(num)  # num_dia = 102304050607
                        ind_num1 = gam_maj.index(num)  # gam_maj = '102034050607'
                        val_num = ind_num0 - ind_num1
                        deg_gam += 1
                        (lineno(), "ind_num0_1", ind_num0, ind_num1, "val_num", val_num, "num", num)
                        if val_num != 0:
                            if val_num < 0:
                                num_note = tab_inf[val_num] + notes_maj[deg_note]
                                deg_niv = tab_inf[val_num] + str(deg_gam)
                                (lineno(), "\t*tab_inf", deg_niv, "num_note", num_note)
                            else:
                                num_note = tab_sup[val_num] + notes_maj[deg_note]
                                deg_niv = tab_sup[val_num] + str(deg_gam)
                                (lineno(), "\t*tab_sup", deg_niv, "num_note", num_note)
                        else:
                            num_note = notes_maj[deg_note]
                            deg_niv = str(deg_gam)
                            (lineno(), "\t* Naturelle", deg_niv, "num_note", num_note)
                        (lineno(), deg_note, "*Origine", deg_niv, "num_note", num_note, "deg_gam", deg_gam)
                        # 317 0 *Note originale num_note C deg_gam 1
                        deg_note += 1

                    passage = deg_niv, num_note
                    (lineno(), "passage", passage, "", deg_niv, num_note)
                    if passage != ('', ''):
                        if passage not in num_mem[ddg[0], 1]:
                            num_mem[ddg[0], 1].append(passage)
                            (lineno(), "Clé [ddg[0], 1]", ddg[0], "num_mem", num_mem[ddg[0], 1])
                            # 325 Clé [ddc, niv] -3 1 num_mem {('-3', 1): [('1', 'C'), ('2', 'D'), ('-3', '-E'),
                            # ('4', 'F'), ('5', 'G'), ('6', 'A'), ('7', 'B')]}
                            if len(passage[1]) > 1:
                                if passage[1] not in dic_maj.keys():
                                    initie(passage[1])  # passage[1] (a servi de test pour les signatures).
                                    (lineno(), "ddg[0], 1", ddg[0], 1, "passage", passage)
                notes.clear()
                notes = [nm[1] for nm in num_mem[ddg[0], 1]]
                (lineno(), "\n Notes", notes, "ddg[0]", ddg[0])

            "# Lecture des gammes mémorisées, seule la précédente compte pour le passage de la tonalité."
            for knm in num_mem.keys():
                if num_mem[knm]:
                    (lineno(), "num_mem", knm, num_mem[knm])
                    # 333 num_mem ('-3', 1) [('1', 'C'), ('2', 'D'), ('-3', '-E'), ('4', 'F'),
                    # ('5', 'G'), ('6', 'A'), ('7', 'B')]...

            code_dg = dic_deg[ddg]
            (lineno(), "code_dg", code_dg, "dic_deg", dic_deg[ddg])
            # 338 code_dg ['102304050607', 1] dic_deg ['102304050607', 1], 338 code_dg [2] dic_deg [2]
            # 338 code_dg [3] dic_deg [3], 338 code_dg [4] dic_deg [4], 338 code_dg [5] dic_deg [5]
            # 338 code_dg [6] dic_deg [6], 338 code_dg [7] dic_deg [7]
        (lineno(), "ddc", ddc)
        # 208 ddc -3

    "# colis2 {'A0': [('A', 13.75), ('', 14.56761754744031), ('B', 15.433853164253879),"
    for khz in colis2.keys():
        (lineno(), "\n khz", khz, colis2[khz])

    "# Situer les degrés diatoniques : grâce au dictionnaire 'colis1[1]'."
    (lineno(), "\n colis1[1]", colis1[1].keys())

    return liste_gen
