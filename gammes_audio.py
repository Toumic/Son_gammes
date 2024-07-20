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


def initie(neo_maj=None, dico=None):
    """Recoder les infos[]. Nouvelle gamme majeure pour 'dic_maj' """
    "# Processus de reconnaissance de la signature tonique."
    if neo_maj:
        (lineno(), "Neo", neo_maj)
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
        if neo_maj not in dic_maj.keys():
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

    "# Processus de conception de la gamme relative à la demande du dico."
    retour_dico = {}
    nkd_maj, note_classic = '102034050607', "CDEFGAB"
    if dico:
        print(lineno(), "Dico", dico)
        for kdc, vdc in dico.items():
            # , vdc = Les notes recueillies correspondantes aux lignes couplées.
            for dc2 in vdc:  # Lire les notes toniques une par une.
                (lineno(), kdc, "DC2", dc2, dic_maj[dc2])
                tonique = dc2  # Premier degré de la gamme à développer et à comparer.
                retour_dico[tonique] = []
                cdm = -1
                for dm in dic_maj[dc2]:  # Diatoniser les toniques pour comparaisons.
                    cdm += 1  # Donne les indices de la gamme à comparer.
                    nkd = kdc[cdm]  # Séquence la gamme à développer.
                    mkd = nkd_maj[cdm]  # Séquence la gamme majeure.
                    if nkd != "0":
                        ind_mkd = nkd_maj.index(nkd)  # Donne l'indice du degré majeur.
                        dif_dia = cdm - ind_mkd  # Donne la différence pour signer les notes à développer.
                        sig, ind_sig = "", None
                        for sdm in dic_maj[dc2][ind_mkd]:
                            if sdm not in note_classic:
                                sig += sdm
                        note0, deg_note = sig + dic_maj[dc2][ind_mkd][-1], ""
                        (lineno(), note0, " sig", sig)

                        "# Première évaluation de la signature. Traitement de la note."
                        if sig in tab_inf:
                            ind_sig0 = tab_inf.index(sig) - len(tab_inf)
                            ind_sig0 += dif_dia
                            (lineno(), note0, "IF ind_sig0", ind_sig0)
                        else:
                            ind_sig0 = tab_sup.index(sig)
                            ind_sig0 += dif_dia
                            (lineno(), note0, "ELSE ind_sig0", ind_sig0)
                        (lineno(), note0, "**1er** ind_sig0", ind_sig0, "dif_dia", dif_dia)

                        if ind_sig0 > -1:
                            sig = tab_sup[ind_sig0]
                            (lineno(), note0, " sig", sig)
                        else:
                            # ind_sig2 = tab_inf.index(ind_sig0)
                            sig = tab_inf[ind_sig0]
                            (lineno(), note0, " sig", sig)
                        (lineno(), note0, "**2me** sig", sig, "dif_dia", dif_dia)

                        "# Deuxième évaluation de la signature."
                        if dif_dia == 0:  # La signature des notes est majeure.
                            deg_note = nkd, note0
                            (lineno(), "deg_note", deg_note)
                        else:  # La signature est modifiée.
                            if sig in tab_inf:
                                ind_sig = tab_inf.index(sig) - len(tab_inf)
                                note1 = tab_inf[ind_sig] + dic_maj[dc2][ind_mkd][-1]
                                if dif_dia < 0:
                                    ind_deg = tab_inf[dif_dia]
                                else:
                                    ind_deg = tab_sup[dif_dia]
                                deg1 = ind_deg + nkd
                                deg_note = deg1, note1
                                (lineno(), "INF note1", deg1, note1, "signe_note", ind_sig)
                            elif sig in tab_sup:
                                ind_sig = tab_sup.index(sig)
                                note1 = tab_sup[ind_sig] + dic_maj[dc2][ind_mkd][-1]
                                if dif_dia < 0:
                                    ind_deg = tab_inf[dif_dia]
                                else:
                                    ind_deg = tab_sup[dif_dia]
                                deg1 = ind_deg + nkd
                                deg_note = deg1, note1
                                (lineno(), "SUP note1", deg1, note1, "signe_note", ind_sig)
                            (lineno(), "signe", sig, "Majeure", note0, "dif_dia", dif_dia, "ind_sig", ind_sig)
                        retour_dico[tonique].append(deg_note)
                        (lineno(), "dic_maj", dic_maj[dc2][ind_mkd], "deg_note", deg_note)
                        (lineno(), "nkd", nkd, "ind_mkd", ind_mkd, dic_maj[dc2][ind_mkd])
                    (lineno(), kdc, "DC2", dc2, "nkd", nkd, "mkd", mkd, dm, "\t cdm", cdm)
                (lineno(), "retour_dico", retour_dico)
        return retour_dico


def audio_gam(gammic, pulsif, selon):
    """Ce module[gammes_audio.py] est appliqué au traitement des gammes selon la méthode choisie
     par l'utilisateur. Puis, en retour, il retourne une séquence destinée à être traitée par le module gensound,
     afin d'entendre les sonorités des gammes sélectionnées. """
    colis1 = gammic  # Colis1
    colis2 = pulsif  # Colis2
    titre1 = selon  # Le titre est selon le type de données en entrée, soit gamme ou binôme.
    liste_gen = []  # Retour de la liste des gammes à lire.
    num_mem2 = {}  # Deuxième dictionnaire de passage.
    ("gammes :", "colis1", colis1, "colis2", colis2, "titre1", titre1)

    "Bb varie selon la sélection"
    # colis1[0] = bb  +34x
    "Cc est invariant."
    # ..1[1] = cc  {1: ['123400000567', '123000004567', '120000034567', '100000234567', '123456700000', '',
    "Colonne_gam et colonne_bin varient selon la sélection."
    # ..1[2] = colonne_gam  {(1, 0): ['0'], (1, 2): ['1'], (1, 3): ['2'], (1, 4): ['3'],
    for co in list(colis1[2].keys()):  # Montrer un amalgame de degrés.
        if 3 == co[0]:
            (lineno(), "Colis1[2]", co, colis1[2][co])
            # 104 Colis1[2] (3, 0) ['o45x']
            # 104 Colis1[2] (3, 12) ['1', '2', '3', '4', '6', '7']
            # 104 Colis1[2] (3, 13) ['5']
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
    del num_mem['0', 1]
    notes_maj = notes.copy()
    gam_maj = '102034050607'
    (lineno(), "Gammes. notes", notes, gam_maj)
    # 125 Gammes. notes ['C', 'D', 'E', 'F', 'G', 'A', 'B'] 102034050607

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

    (lineno(), "colis1[0]", colis1[0], "Liste_gen :", liste_gen[:8], "\n")
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
    tab_gen, tab_ok = {}, True  # Dictionnaire, clef = nom gamme, valeur = numéro statique/dynamique.
    for ddc in dic_dic.keys():
        (lineno(), "\n Premier_tour = Clé dictionnaire principal,", "ddc", ddc)
        # 266 premier_tour = Clé dictionnaire principal, ddc -3

        "# Nous avons besoin d'une mémorisation de la gamme précédente."
        mem0 = {}  # Dictionnaire (gammes, degrés, notes, lignes). Facilite le traitement (mem1, mem2).

        "# Le dictionnaire secondaire 'dic_deg' a la séquence des gammes suivantes."
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
                    for lg2 in liste_gen:
                        if lg2[1] == 0:
                            nom_dyn = colis1[2][lg2][0]
                            num_sto = colis1[4][nom_dyn]
                            for c15 in colis1[5].keys():
                                if num_sto in c15:
                                    tab_gen[nom_dyn] = c15 + lg2
                                    (lineno(), "tab_gen2", tab_gen[nom_dyn])
                                    break
                    tab_ok = False
                    (lineno(), ddg[0], "tab_gen", tab_gen)
                    # 298 -3 tab_gen {'-3': (36, '102304050607', 64, 0), '-6': (41, '102034056007', 65, 0),
                    # '+6': (46, '102034050067', 66, 0)}

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

                    "# Élaboration du dictionnaire 'num_mem', qui comprend les degrés et les notes en tonalité de DO."
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
                                    initie(passage[1], None)  # passage[1] (a servi de test pour les signatures).
                                    (lineno(), "ddg[0], 1", ddg[0], 1, "passage", passage)
                notes.clear()
                notes = [nm[1] for nm in num_mem[ddg[0], 1]]
                (lineno(), "\n Notes", notes, "ddg[0]", ddg[0])

            "# Lecture des gammes et seule la précédente compte pour le passage de la tonalité."
            # Les tests sélectionnant la gamme mélodique[-3] donnent deux gammes relatives qui
            # n'ont pas de points communs avec leurs origines. La première [-3] n'a pas de point commun
            # avec la seconde [-6] qui a plusieurs points communs avec la tierce [+6].
            # Dans ce cas, n'ayant aucun commun, la gamme repart en DO.
            for knm in num_mem.keys():
                if num_mem[knm]:
                    ("\n", lineno(), "knm", knm, "num_mem[knm]", num_mem[knm], "\n ****************************")
                    # 359 knm ('-3', 1) num_mem[knm] [('1', 'C'), ('2', 'D'), ('-3', '-E'), ('4', 'F'), ('5', 'G'),
                    # ('6', 'A'), ('7', 'B')]
                    num_mem2[knm[0]] = num_mem[knm].copy()
                    ind_knm = tab_gen[knm[0]][-2]  # Le dico tab_gen a les numéros des gammes.
                    (lineno(), "knm[0]", knm[0], "tab_gen[knm[0]][-2] = ind_knm", ind_knm)
                    # 362 knm[0] -3 tab_gen[knm[0]][-2] = ind_knm 64
                    if colis1[2][ind_knm, 0][0] == knm[0]:  # La clé [ind knm, 0] vérifie le nom de la gamme.
                        ("# Poursuite de la gamme concernée parmi les gammes dans 'colis1[2]. (colonne_gam)"
                         "Ce qui rend possible l'incrémentation des données de 'colis1[2]'.")
                        mem0[knm[0]] = []  # Déclaration d'une liste pour ce nom(knm[0]).
                        for c12 in range(1, len(colis1[3]) + 1):  # Nombre de lignes qui étalent les degrés modaux.
                            if (ind_knm, c12) in colis1[2].keys():  # Dans colonne_gam dynamique (colis1[2])
                                trans = (ind_knm, c12), colis1[2][ind_knm, c12]
                                mem0[knm[0]].append(trans)
                                (lineno(), (ind_knm, c12), "colis1", colis1[2][ind_knm, c12], "c12", c12)
                                # 372 (60, 12) colis1 ['4', '5'] c12 12

            code_dg = dic_deg[ddg]
            (lineno(), "code_dg", code_dg, "dic_deg", dic_deg[ddg])
            # 377 code_dg ['102304050607', 1] dic_deg ['102304050607', 1], 338 code_dg [2] dic_deg [2]
            # 377 code_dg [3] dic_deg [3], 338 code_dg [4] dic_deg [4], 338 code_dg [5] dic_deg [5]
            # 377 code_dg [6] dic_deg [6], 338 code_dg [7] dic_deg [7]

        "# Repères obtenus pour la production des tonalités."
        (lineno(), "tab_gen", tab_gen)
        # 382 tab_gen {'-3': (36, '102304050607', 64, 0), '-6': (41, '102034056007', 65, 0),
        # '+6': (46, '102034050067', 66, 0)}
        (lineno(), "num_mem2", num_mem2)
        # 382 num_mem2 {'-3': [('1', 'C'), ('2', 'D'), ('-3', '-E'), ('4', 'F'), ('5', 'G'), ('6', 'A'), ('7', 'B')],
        # '-6': [('1', 'C'), ('2', 'D'), ('3', 'E'), ('4', 'F'), ('5', 'G'), ('-6', '-A'), ('7', 'B')],
        # '+6': [('1', 'C'), ('2', 'D'), ('3', 'E'), ('4', 'F'), ('5', 'G'), ('+6', '+A'), ('7', 'B')]}
        "# ((Colonne = 60, Ligne = 12), Degrés = ['4', '5'])"
        (lineno(), list(mem0)[0], "Mem0", mem0[list(mem0)[0]])
        # 381 o5 Mem0 [((60, 12), ['4', '5']), ((60, 13), ['7']), ((60, 20), ['3']), ((60, 50), ['1']),
        # ((60, 51), ['2']), ((60, 53), ['6'])]

        "# Commencement de la séquence des modulations dynamiques."
        mem0_key, len0_key, count_gam = list(mem0.keys()), len(mem0.keys()), 0
        for rng1 in range(len0_key):
            for rng2 in range(len0_key):
                if rng1 == rng2 - 1:
                    count_gam += 1
                    "# Comparaison des deux gammes mémorisées."
                    un, u2 = mem0[mem0_key[rng1]], mem0_key[rng1]
                    de, d2 = mem0[mem0_key[rng2]], mem0_key[rng2]
                    print(lineno(), "______________________________________________", count_gam, "U2", u2, "D2", d2)
                    (lineno(), "_________________________", "\n Un", u2, un, "\n De", d2, de)
                    # 402 _________________________
                    #  Un [((60, 12), ['4', '5']), ((60, 13), ['7']), ((60, 20), ['3']), ((60, 50), ['1']),
                    #  ((60, 51), ['2']), ((60, 53), ['6'])] o5
                    #  De [((61, 13), ['5']), ((61, 25), ['7']), ((61, 50), ['3']), ((61, 51), ['2']),
                    #  ((61, 52), ['6']), ((61, 54), ['1']), ((61, 55), ['4'])] -35+
                    lig, deg = 0, 0
                    tab_adn, tab_anm = [], []  # Tables de récupération.
                    for un2 in un:
                        for de2 in de:
                            "# Comparaison des lignes binaires."
                            if un2[0][1] == de2[0][1]:
                                "# Condition requise pour une recherche de tonalité approximative."
                                lig += 1
                                (lineno(), "Lig u2", u2, un2, un2[0][1], "d2", d2, de2, de2[0][1], "LIG", lig)
                                # 414 Lig u2 -6 ((65, 17), ['3']) 17 d2 +6 ((66, 17), ['3']) 17 LIG 1
                                ("# Des lignes binaires concordent et les notes correspondantes de la gamme précédente"
                                 "sont utiles. Elles peuvent jouer un rôle pour tonifier la gamme suivante.")
                                for nm1 in range(len(num_mem2[u2])):  # Comparaison des notes diatoniques.
                                    # adn1 = Instance pour les notes inégales, elle est la référence tonale.
                                    adn1, adn2 = num_mem2[u2][nm1], num_mem2[d2][nm1]
                                    "# La note précédente est vue, elle est différente de la suivante."
                                    if adn1[0] == un2[1][0] or un2[0][1] == de2[0][1]:
                                        if adn1 not in tab_adn:
                                            adn12 = u2, adn1, un2, d2, de2
                                            tab_adn.append(adn12)
                                        (lineno(), "\t Inégaux adn1", u2, adn1, un2, "adn2", d2, adn2, de2)
                                        # 425 	 Inégaux adn1 o35x ('4', 'F') ((8, 17), ['4']) adn2 x26- ('+4', '+F')
                                        break
                                "# Comparaison des degrés diatoniques aux mêmes lignes binaires."
                                if un2[1][0] == de2[1][0]:
                                    "# Condition requise pour une recherche du degré approximatif."
                                    deg += 1
                                    (lineno(), "Deg u2", u2, un2, un2[1][0], "d2", d2, de2, de2[1][0], "DEG", deg)
                                    # 432 Deg u2 -6 ((65, 17), ['3']) 3 d2 +6 ((66, 17), ['3']) 3 DEG 1
                                    ("# Plusieurs degrés sont semblables, ils enchainent "
                                     "une analyse ses notes diatoniques.")
                                    for nm2 in range(len(num_mem2[u2])):  # Comparaison des notes diatoniques.
                                        # anm1 = anm2 = Instances de référence des degrés aux notes égales.
                                        anm1, anm2 = num_mem2[u2][nm2], num_mem2[d2][nm2]
                                        if anm1[0][0] == anm2[0][0]:
                                            if anm1 not in tab_anm:
                                                anm12 = u2, anm1, un2, d2, anm2, de2
                                                tab_anm.append(anm12)
                                            (lineno(), "\t Égaux anm1", u2, anm1, "\t anm2", d2, anm2)
                                            # 443 		 Égaux anm1 -6 ('3', 'E') 	 anm2 +6 ('3', 'E')
                                            break
                                (lineno(), u2, "* Un2", un2, "tab_gen", tab_gen[u2])
                                (lineno(), d2, "** De2", de2, "tab_gen", tab_gen[d2], "\n ______   ______")
                                # 446 -6 * Un2 ((65, 61), ['1']) tab_gen (41, '102034056007', 65, 0)
                                # 447 +6 ** De2 ((66, 61), ['1']) tab_gen (46, '102034050067', 66, 0)
                                #  ______   ______

                    if 0 < lig >= deg > 0:
                        "# Le nombre de lignes est supérieur à zéro et il est égal à celui des degrés."
                        print(lineno(), "elif 0 < lig >= deg > 0: =================", lig, deg)
                        print(lineno(), "ADN num_mem2[u2]", u2, num_mem2[u2])
                        (lineno(), "ANM num_mem2", d2, num_mem2[d2])
                        anm0, dico_anm = False, {}
                        dico_anm[tab_gen[d2][1]] = []
                        if tab_anm:
                            (lineno(), " DEG", deg, "\n ANM", tab_anm, "Long", len(tab_anm))
                            for td_anm1 in num_mem2[u2]:
                                for td_anm2 in num_mem2[d2]:
                                    "# Relevé des mêmes notes"
                                    (lineno(), "td_anm1", td_anm1[-1], "|2", td_anm2[-1], tab_gen[d2][1])
                                    if td_anm1[-1] == td_anm2[-1] and td_anm1[-1] not in dico_anm[tab_gen[d2][1]]:
                                        dico_anm[tab_gen[d2][1]].append(td_anm1[-1])
                                        (lineno(), "td_anm1", td_anm1[-1], td_anm2[-1], dico_anm[tab_gen[d2][1]])
                            "# Il y a six notes égales et une seule différence qui est la tonique."
                            if len(dico_anm[tab_gen[d2][1]]) == 6:
                                dico_anm[tab_gen[d2][1]].clear()

                            for da in dico_anm[tab_gen[d2][1]]:
                                if da not in dic_maj.keys():
                                    initie(da, dico=None)
                                    (lineno(), "Initie Da", da)
                            (lineno(), " dico_anm", dico_anm)

                        retour_init = initie("", dico_anm)
                        for ri_gam in retour_init.values():
                            print(lineno(), " retour_init", ri_gam, len(retour_init))
                            # 584  retour_init {'xG': [('1', 'xG'), ('2', 'xA'), ('3', 'xB'), ('x4', '+^C'),
                            # ('x5', '+^D'), ('+6', '^E'), ('7', '^F')]} 1
                        if retour_init:
                            (lineno(), "tab_gen", d2, tab_gen[d2])
                            if len(retour_init) == 1:
                                del num_mem2[d2]
                                passe = retour_init.values()
                                num_mem2[d2] = list(passe)[0]
                                (lineno(), "Une clé passe", list(passe)[0])
                            else:
                                key_riz = list(retour_init.keys())
                                dic_vrai, tab_vrai, nbr_vrai = {}, [], 0
                                ton_u2 = num_mem2[u2][0][1]
                                (lineno(), "Key_riz", key_riz, "ton_u2", ton_u2, "\n num_mem2", num_mem2[u2])

                                for varie in key_riz:  # Lecture par clés délivrées de la fonction[initie].
                                    dic_vrai[varie] = 0
                                    for rive in retour_init[varie]:  # Lecture de chacune des gammes à clés.
                                        (lineno(), "Varie", varie, rive[1])
                                        for carie in num_mem2[u2]:
                                            if carie[1] == rive[1]:
                                                nbr_vrai += 1
                                                (lineno(), "carie[1]", carie[1])
                                    dic_vrai[varie] = nbr_vrai
                                    tab_vrai.append(nbr_vrai)
                                    nbr_vrai = 0
                                    (lineno(), "dic_vrai", varie, dic_vrai[varie])
                                max_vrai = max(tab_vrai)
                                print(lineno(), "dic_vrai", dic_vrai, "max_vrai", max_vrai, "ton_u2", ton_u2)
                                if ton_u2 in dic_vrai.keys():
                                    if dic_vrai[ton_u2] == max_vrai:
                                        num_mem2[d2] = retour_init[ton_u2]
                                        (lineno(), "[ton=max] num_mem2[d2]", d2, num_mem2[d2])
                                    else:
                                        print(lineno(), "Else[ton=max]")
                                else:
                                    for q_vrai in dic_vrai.keys():
                                        if dic_vrai[q_vrai] == max_vrai:
                                            num_mem2[d2] = retour_init[q_vrai]
                                            (lineno(), "ton n'est pas une clé")
                            (lineno(), "dico_anm", dico_anm)

                    elif 0 == lig == deg:
                        "# Le nombre de lignes et de degrés égaux est égal à zéro."
                        "# Quand le nombre de ligne/degré est nul, on ne fait rien, la gamme reste en DO[C]"
                        print(lineno(), "elif 0 == lig == deg: ================", lig, deg)
                        print(lineno(), lig, "ADN num_mem2[u2]", u2, num_mem2[u2])

                    else:
                        "# Les lignes vont de un à plus et les degrés sont toujours à zéro."
                        print(lineno(), "else: ================================", lig, deg)
                        adn0, dico_adn = True, {}
                        dico_adn[tab_gen[d2][1]] = []
                        (lineno(), "LIG", lig, "ADN", tab_adn, "Long", len(tab_adn))
                        print(lineno(), lig, "ADN num_mem2[u2]", u2, num_mem2[u2])
                        (lineno(), deg, "ANM num_mem2", d2, num_mem2[d2])
                        for tad in tab_adn:
                            for td in tad:
                                if td == u2:
                                    if not adn0:  # Remise à True au second tour
                                        adn0 = True
                                    (lineno(), "Nom 1", td, "len", len(td))
                                elif td == d2:
                                    adn0 = False
                                    (lineno(), "Nom 2", td)
                                elif adn0:
                                    if isinstance(td[-1], str):
                                        (lineno(), "elif (str) Nom 1", td, "len", len(td))
                                    else:
                                        for td_adn in num_mem2[u2]:
                                            if td_adn[0][-1] == td[-1][0]:
                                                dico_adn[tab_gen[d2][1]].append(td_adn[-1])
                                                (lineno(), "elif Nom 1 td", u2, td, "td_adn", td_adn, tab_gen[d2])
                                (lineno(), "td", td)
                            (lineno(), "tad", tad, "Len", len(tad))
                        for da in dico_adn.values():
                            for d in da:
                                if d not in dic_maj.keys():
                                    initie(d, None)
                        retour_init = initie("", dico_adn)
                        "# Retourne les gammes demandées sous les toniques trouvées."
                        for k_rie, v_rie in retour_init.items():
                            (lineno(), "retour_init", retour_init[k_rie], len(retour_init))
                        # 628 retour_init {'-G': [('1', '-G'), ('-2', 'oA'), ('o3', '*B'), ('o4', '*C'), ('5', '-D'),
                        # ('+6', 'E'), ('7', 'F')], '+D': [('1', '+D'), ('-2', 'E'), ('o3', 'F'), ('o4', '-G'),
                        # ('5', '+A'), ('+6', 'xB'), ('7', 'xC')]} 2
                        dic_rit, tab_rit, max_rit = {}, [], ""
                        for ri in retour_init.keys():
                            if lig == 1:  # Il n'y a qu'un seul choix pour la note tonique.
                                del num_mem2[d2]
                                num_mem2[d2] = retour_init[ri].copy()
                            else:
                                tab_rit.clear()
                                for kiri in retour_init.keys():
                                    dic_rit[kiri] = 0
                                    kr = 0
                                    for rire in retour_init[kiri]:
                                        # Compter le nombre de similitudes.
                                        for nmu2 in num_mem2[u2]:
                                            if rire[1] == nmu2[1]:
                                                kr += 1
                                                (lineno(), "num_mem2", rire[1], nmu2[1])
                                    dic_rit[kiri] = kr
                                    tab_rit.append(kr)
                                max_rit = max(tab_rit)
                                for calor, rigolo in dic_rit.items():
                                    if max_rit == rigolo:
                                        del num_mem2[d2]
                                        num_mem2[d2] = retour_init[calor].copy()
                                        (lineno(), "calor", calor, "rigolo", rigolo, "\n", retour_init[calor])
                                        break
                        "# Quand le nombre de comparaison est nul, on ne fait rien la gamme reste en DO[C]"
                        (lineno(), "max_rit", max_rit)
                        print(lineno(), "dic_rit", dic_rit, "tab_rit", tab_rit, "lignes", lig)
                        (lineno(), "dico_adn", dico_adn, "retour_init", retour_init)
                    print(lineno(), "ANM num_mem2[d2]", d2, num_mem2[d2])
                    break

    (lineno(), dic_maj.keys())
    # 514 dict_keys(['C', 'D', 'E', 'F', 'G', 'A', 'B', '-G', '-D', 'oE', 'oF', 'xG', '+A', '-A', 'oA', '+D', 'xD',
    # '+E', '+F', '*G', 'oG', '-F', 'xF', '+G', '-E', '*A', '^F', 'xE', '^E', '^D'])

    "# colis2 {'A0': [('A', 13.75), ('', 14.56761754744031), ('B', 15.433853164253879),"
    for khz in colis2.keys():
        print(lineno(), "\n khz", khz, "colis2.keys()", len(colis2.keys()), "Octaves.")
        break

    "# Situer les degrés diatoniques : grâce au dictionnaire 'colis1[1]'."
    (lineno(), "\n colis1[1]", colis1[1].keys())
    print(lineno())

    return liste_gen
