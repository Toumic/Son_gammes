#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vicenté quantic cabviva
"""Ce programme consiste à donner une sonorité diatonique aux gammes.
Cette gamme est en Do et elle retrace les gammes fondamentales.
L'architecture de cet assemblage ressemble à cette image (images/ClassBooLsIII.png)."""
# https://cabviva.com/musicmp3/gamcop!s.mp3

import inspect
from typing import Callable
from tkinter import *
from tkinter.constants import *
from tkinter.font import *
from PIL import ImageTk, Image
# Les modules personnels.
import gammes_audio as gamma  # Faire sonner les gammes.
import binomes_audio as biner  # Faire sonner les gammes.

# lineno() Pour consulter le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

gam_classic = {
    "102034050607": ["0", 336], "120034050607": ["-2", 210], "100234050607": ["+2", 392],
    "102304050607": ["-3", 301], "102034500607": ["-5", 341], "102034056007": ["-6", 330],
    "102034050067": ["+6", 339], "120304050607": ["-23", 175], "120034500607": ["-25", 215],
    "120034005607": ["-25+", 201], "120034056007": ["-26", 204], "120034050067": ["-26+", 213],
    "100234500607": ["+25-", 397], "100234056007": ["+26-", 386], "100234050067": ["+26", 395],
    "102340050607": ["-4", 272], "102304500607": ["-35", 306], "102304005607": ["-35+", 292],
    "102304056007": ["-36", 295], "102304050067": ["-36+", 304], "102034506007": ["-56", 338],
    "102034500067": ["-56+", 342], "102034005067": ["+56", 333], "120340050607": ["-24", 146],
    "102030045067": ["x46+", 356], "102030400567": ["+45x", 343], "100234000567": ["+25x", 379],
    "123004500607": ["o35-", 110], "102003400567": ["+35x", 358], "120034560007": ["-26o", 206],
    "102340005607": ["-45+", 258], "102340050067": ["-46+", 278], "102300045607": ["-34x", 320],
    "102003045607": ["+34", 370], "102340500607": ["-45", 281], "102034000567": ["x5", 323],
    "102030040567": ["x45+", 353], "102340560007": ["-46o", 265], "100200345607": ["+23x", 431],
    "120345000607": ["-25o", 160], "102000345067": ["x36+", 376], "123040050607": ["-34", 76],
    "102000345607": ["x3", 375], "123045000607": ["o63-", 90], "123004050607": ["o3", 105],
    "102345060007": ["o65-", 277], "123405000607": ["o54-", 50], "102030004567": ["^4", 357],
    "102003004567": ["+34x", 372], "123400050607": ["o4", 27], "123400500607": ["o45-", 41],
    "123400056007": ["o46-", 12], "102345000607": ["o5", 286], "123004050067": ["o36+", 108],
    "123004005607": ["o35+", 96], "102345600007": ["*6", 267], "123400050067": ["o46+", 37],
    "123450000607": ["*5", 55], "123004000567": ["o35x", 92], "123000045607": ["o34x", 124],
    "102340000567": ["-45x", 253], "102034560007": ["o6", 332], "100023456007": ["x26-", 440],
    "100002345607": ["^2", 458], "102000034567": ["^3", 378], "123400000567": ["o45x", 1]
}
gam_physic = {
    "102034050607": ["0", 336], "120034050607": ["-2", 210], "100234050607": ["+2", 392],
    "102304050607": ["-3", 301], "102034500607": ["-5", 341], "102034056007": ["-6", 330],
    "102034050067": ["+6", 339], "120304050607": ["-23", 175], "120034500607": ["-25", 215],
    "120034005607": ["-25+", 201], "100234005607": ["+25", 383], "120034050067": ["-26+", 213],
    "100234500607": ["+25-", 397], "100234056007": ["+26-", 386], "100234050067": ["+26", 395],
    "102340050607": ["-4", 272], "102304500607": ["-35", 306], "102304005607": ["-35+", 292],
    "102034005607": ["+5", 327], "102304050067": ["-36+", 304], "102034506007": ["-56", 338],
    "102034500067": ["-56+", 342], "100203450607": ["+23", 422], "120340050607": ["-24", 146],
    "102030045067": ["x46+", 356], "102030400567": ["+45x", 343], "100023450067": ["x26+", 444],
    "123004500607": ["o35-", 110], "102003400567": ["+35x", 358], "100023400567": ["x25", 435],
    "102340005607": ["-45+", 258], "102340050067": ["-46+", 278], "102300045607": ["-34x", 320],
    "102003045607": ["+34", 370], "102340500607": ["-45", 281], "100023450607": ["x2", 443],
    "102030040567": ["x45+", 353], "100023045607": ["x24+", 447], "100200345607": ["+23x", 431],
    "120345000607": ["-25o", 160], "102000345067": ["x36+", 376], "123040050607": ["-34", 76],
    "102304000567": ["x53-", 288], "100020345607": ["x23+", 452], "123004050607": ["o3", 105],
    "102345060007": ["o65-", 277], "102000304567": ["x34+", 377], "102030004567": ["^4", 357],
    "102003004567": ["+34x", 372], "123400050607": ["o4", 27], "123400500607": ["o45-", 41],
    "100234560007": ["+26o", 388], "102345000607": ["o5", 286], "123004050067": ["o36+", 108],
    "102345006007": ["o56-", 283], "100002304567": ["^24+", 460], "100020034567": ["x23", 455],
    "100002034567": ["^23+", 461], "120030004567": ["^42-", 231], "102345000067": ["+65o", 287],
    "102340000567": ["-45x", 253], "102034560007": ["o6", 332], "100023456007": ["x26-", 440],
    "102300004567": ["^43-", 322], "102000034567": ["^3", 378], "100000234567": ["+^2", 462]
}
gam_maj = '102034050607'
dic_codage = {}  # Dictionnaire des gammes et de leurs modes. PRÉALABLE
dic_indice = {}  # Dictionnaire, clé = Nom de la gamme, valeur = Numéro de la gamme. PRÉALABLE
dic_binary = {}  # Dictionnaire, clé = binaire, valeur = zob (['o45x', 1], '1000001'), (1, 2, '1000001'). PRÉALABLE
dic_force = {}  # Dictionnaire, clé = binaire, valeur = dic_codage avec le même binaire. PRÉALABLE
dic_colon = [""]  # Liste, clés = binaires liées aux choix de conversions.

pre_codage = open('globdicTcoup.txt', 'r')
mod, cod1 = '', 1
"# Lire un globdicTcoup.txt pour construire un dictionnaire de tous les modèles diatoniques = dic_codage"
for pre_cod in pre_codage:
    mod_cod = pre_cod[:12]  # 'mod_cod' = Copie du mode tonique.
    if pre_cod[:12] in gam_classic.keys():
        cod2 = 0
        dic_codage[cod1, mod_cod] = []
        "# Binariser les modulations diatoniques."
        while cod2 < 12:
            cod2 += 1
            for p_c in mod_cod:
                if p_c != '0':
                    ind_maj = gam_maj.index(p_c)
                    ind_cod = mod_cod.index(p_c)
                    if ind_maj == ind_cod:
                        mod += '1'
                    else:
                        mod += '0'
            # C'est une section des premiers degrés, des noms gammes et des numéros des gammes.
            if cod2 == 1:
                zob = gam_classic[mod_cod], mod
                # self.dic_indice = Dictionnaire, clé = Nom_gamme, valeur = Rang_gamme.
                dic_indice[gam_classic[mod_cod][0]] = cod1
                (lineno(), "cod1", cod1, "dic_indice", dic_indice[gam_classic[mod_cod][0]])
            else:
                zob = cod1, cod2, mod
            dic_codage[cod1, pre_cod[:12]].append(zob)
            # print("dic_codage[cod1, pre_cod[:12]]", dic_codage[cod1, pre_cod[:12]])
            dic_binary[zob[-1]] = []  # 'dic_mode01' = Clé Binaire, = Rang numérique.
            dic_binary[zob[-1]].append(zob)
            (lineno(), "zob", zob, "zob[-1]")
            (lineno(), "dic_codage :", dic_codage[cod1, pre_cod[:12]])
            mod = ''
            "# Renversements diatoniques."
            mod_cod = mod_cod[1:] + mod_cod[:1]
            while mod_cod[0] == '0':
                mod_cod = mod_cod[1:] + mod_cod[:1]
            mov, mut = 0, ''  # Renuméroter les degrés = 'mov'
            "# Binariser chaque mode."
            for m in mod_cod:
                if m != '0':
                    mov += 1
                    mut += str(mov)
                else:
                    mut += '0'
            mod_cod = mut
            if mod_cod == pre_cod[:12]:
                break
        cod1 += 1  # ("dic_codage", dic_codage, "Les gammes formatées.")
pre_codage.close()

"# Construire un dictionnaire 'dic_force' avec les valeurs ayant les mêmes binaires, de dic_codage original."
liste_keys, liste_copy = list(dic_codage.keys()), []  # Liste les clés de dic_codage original.
for lk in liste_keys:
    (lineno(), "lk", lk, "dic_codage", dic_codage[lk])
    for dc in dic_codage[lk]:
        if dc[-1] not in liste_copy:
            liste_copy.append(dc[-1])
            pas_lk = lk, dc
            dic_force[dc[-1]] = []
            dic_force[dc[-1]].append(pas_lk)
            (lineno(), "IF pas_lk", dc[-1], dc, "*", pas_lk)
            (lineno(), "IF dic_force", dc[-1], dic_force[dc[-1]])
        else:
            dic_force[dc[-1]].append(dc)
            (lineno(), "ELSE dc", dc[-1], dc)
            (lineno(), "ELSE dic_force", dc[-1], dic_force[dc[-1]])
(lineno(), "dic_force", list(dic_force)[0], dic_force[list(dic_force)[0]], len(dic_force.keys()))
(lineno(), "dic_force", dic_force.keys())


def bouton_bin(bb):
    """Pratiquer les redirections des boutons d'en-tête[noms des gammes] et latéral gauche[binaires].
        Cette fonction est située après avoir initialisé les dictionnaires nécessaires."""
    (lineno(), "**   Fonction bouton_bin bb ", bb)
    if len(bb) < 7:
        a = "# Jonction module gammes_audio"
    else:
        a = "# Jonction module binomes_audio"
    (lineno(), "Bb", bb, len(bb), "\t A", a)


def func_ima(ami):
    """Fonction de récupération des données de la fonction def clic_image(), ami = Paramètre de clic_image,
    ami[0] = Type de conversion. # item_id : (1=iso, 2=int, 3=bin, 4=hex, 5=oct)."""
    (lineno(), "ami[0]", ami[0], list(dic_codage)[0], "dic_codage, dic_binary, dic_indice, dic_force, dic_colon\n")
    # 160 ami[0] 2 (1, '123400000567') dic_codage, dic_binary, dic_indice, dic_force, dic_colon
    (lineno(), "func_ima", ami[0])
    # Ok = dic_codage, dic_binary, dic_indice, dic_force, dic_colon
    '''"# 160 ami[0] 1 [1, {'type': 'Entiers libres', '1000001': 1000001, : ami"
        * Ami = Les binaires selon la demande utilisateur.
    "# 160 ami[0] 1 {(1, '123400000567'): [(['o45x', 1], '1000001'), (1, 2, '1000001'), : dic_codage"
        * Dic_codage = Les gammes utilisées par l'appli songammes.py, dans un ordre original.
            Clef=(1, '123400000567'): => Clef[0] = Rang. Clef[1] = Forme numéraire des gammes.
            Val=(1, 2, '1000001') => Val[0] = Nom gamme ou numéro de colonne. Val[1] = Numéro de ligne ou degré.
                                        Val[2] = Code du mode binaire.
    "# 160 ami[0] 1 {'1000001': [(66, 5, '1000001')], '1000000': [(66, 2, '1000000')], : dic_binary"
        * Dic_binary = Clefs binaires et gammes relatives selon l'ordre original.
            Clef=Binaire. Val=[(66, 2, '1000000')] => Val[0] = Numéro de gamme ou colonne. 
                                                        Val[1] = Numéro de ligne ou degré.
                                                        Val[2] = Code du mode binaire.
    "# 160 ami[0] 1 {'o45x': [1], 'o46-': [2], 'o4': [3], 'o46+': [4], 'o45-': [5], : dic_indice"
        * Dic_indice = Clefs composées des noms des gammes et leurs indices des rangs des gammes.
    "# 160 ami[0] 1 {'1000111': [(3, '123400050607'), (43, '102034005067'), : dic_force"
        * Dic_force = Clefs binaires aux valeurs égales aux clefs de dic_codage original.
            Val[0] = Numéro de la gamme. Val[1] = Valeur énumérée de la gamme.
    def func_ima(ami):
        relance_instance = Relance(di_code=ami)
    # Accéder à la fonction gammes_arp dans la classe Relance.
    relance_instance.gammes_arp()'''
    "# Consultation du paramètre 'ami'. Modification de la liste des binaires (appliquée dans gammes_arp())."
    for ai in ami:  # Dictionnaire dans lequel se range l'ordre du typage.
        if type(ai) is dict:  # Dictionnaire à partir du deuxième niveau.
            keys_ai = list(ai.keys())
            for kai in keys_ai:  # Kai = Clef Binaire de mise à jour de l'utilisateur.
                if len(str(kai)) == 7:
                    (lineno(), "kai", kai)
                    dic_colon.append(kai)
                    (lineno(), "kai", kai, "dic_force", dic_force[str(kai)])
    "'dic_colon' = Paramètre nouvelle liste binaire"
    (lineno(), "func_ima dic_colon = Nouveaux binaires", dic_colon[:6])
    return dic_colon


class Relance(Tk):
    """Permet de relancer l'affichage avec une nouvelle orientation"""

    # Relance(dic_codage, dic_binary, dic_indice, dic_force, dic_colon, dic_titres).mainloop()
    def __init__(self, di_code=None, di_bine=None, di_indi=None, di_fort=None, di_colon=None):
        """ Initialisation du visuel, sous forme d'un tableur.
        di_code = dic_codage ; di_indi = dic_indice ; di_bine = dic_binary
        di_fort = dic_force ; di_colon = dic_colon ; di_nom = dic_titres"""
        Tk.__init__(self)
        self.title("Base illusion")
        self.geometry("1824x1000+30+10")
        self.borne = {1: "       "}
        self.quitter("1111111")
        self.focus_force()  # Donnez l'intérêt à la fenêtre
        "# Assemblage, clé = binaire, valeur = dic_codage.keys() à même binaire."
        self.dic_force = di_fort  # Dictionnaire clé=Binaire valeur=Clé_dic_codage original
        self.dic_codage = di_code  # Dictionnaire des gammes et de leurs modes.
        self.dic_binary = di_bine  # Clé = binaire, valeur = zob (['o45x', 1], '1000001'), (1, 2, '1000001')
        self.dic_indice = di_indi  # Dictionnaire, clé = Nom de la gamme, valeur = Numéro de la gamme.
        self.font_coins = "Courrier 18 bold"
        self.table_x = Canvas(self, width=60, height=30)  # Coin (haut, gauche) pour l'image favicon.
        self.table_x.grid(row=1, column=1)
        self.table_b = Canvas(self, width=60, height=884, bg="white")  # Colonne dédiée aux boutons binaires.
        self.table_b.grid(row=2, column=1)
        self.frame_b = Frame(self.table_b)
        self.frame_b.grid()
        self.table_y = Canvas(self, width=84, height=30, bg="thistle")  # Coin (haut, droite).
        self.table_y.grid(row=1, column=3)
        self.table_o = Canvas(self, width=84, height=884, bg="thistle")  # Colonne dédiée aux binaires ordonnés.
        self.table_o.grid(row=2, column=3)
        self.table_z = Canvas(self, width=84, height=60, bg="thistle")  # Coin (bas, droite).
        self.table_z.grid(row=3, column=3)
        self.table_g = Canvas(self, width=1656, height=30, bg="seashell")  # Colonne dédiée aux boutons gammes.
        self.table_g.grid(row=1, column=2)
        self.frame_g = Frame(self.table_g)
        self.frame_g.grid()

        "# Mise en forme des tables dans la grille"
        "72/2=36/2=18, 30/2=15, 54=18+36"
        tx1, tx2 = (18, 2), (54, 30)
        self.table_x.create_oval(tx1, tx2, fill="gold", width=0)  # Table décorative.
        self.table_x.create_text(36, 15, fill="white", text="X", font=self.font_coins)  # Table décorative. Lettre X.
        tx1, tx2 = (2, 2), (1656, 30)
        self.table_g.create_oval(tx1, tx2, fill="blanchedalmond", width=0)  # Colonne dédiée aux boutons gammes.
        self.table_y.create_text(44, 16, fill="white", text="Y", font=self.font_coins)  # Table décorative. Lettre Y.
        self.table_z.create_text(44, 31, fill="white", text="Z", font=self.font_coins)  # Table décorative. Lettre Y.
        self.tableau = Canvas(self, width=1656, height=884, bg="ivory")  # Affichage des (noms, binaires) liées.
        self.tableau.grid(row=2, column=2)
        self.tableau.config(borderwidth=3, relief=RAISED)

        "# Initialisation métrique de l'affichage."
        self.police1, self.police2 = "Courier 8 bold", "Courrier 10"
        '''Pour une colonne binaire de soixante-six éléments, un intervalle de treize = Hauteur (67*13 = 871).
        Ayant un nombre de colonnes égal aux gammes (66), plus une pour les binaires = Longueur (67*24 = 1608).'''
        long1, haut1, long2, haut2 = 1656, 884, 1608, 871
        self.deb_col, self.deb_lin = (long1 - long2) // 2, (haut1 - haut2) // 2
        self.col, self.lin = 24, 13  # Espace entre les colonnes_26 et espace entre les lignes_13.
        self.tot_col, self.tot_lin = 67 * 24, 67 * 13

        "# Tracer le quadrillage principal en bleu clair."
        self.fin_col, self.fin_lin = self.deb_col + self.tot_col, self.deb_lin + self.tot_lin
        self.deb_col0, self.deb_lin0 = self.deb_col, self.deb_lin
        for i in range(68):
            self.tableau.create_line(self.deb_col, self.deb_lin0, self.fin_col, self.deb_lin0,
                                     fill="lightblue", dash=(1, 1))
            self.tableau.create_line(self.deb_col0, self.deb_lin, self.deb_col0, self.fin_lin,
                                     fill="lightblue", dash=(1, 1))
            self.deb_col0 += self.col
            self.deb_lin0 += self.lin

        (lineno(), "di_colon", di_colon[:6])
        if di_colon == [""]:
            di_colon = []
        self.colonne_bin = di_colon  # Première colonne aux modes binaires uniques. L'index de l'élément = La ligne.
        self.colonne_gam = {}  # Colonnes contenant les gammes de 1 à 66. Première ligne = Noms.
        self.colonne_lis = {}  # Le dictionnaire clé=N°gamme, valeur=Ensemble degrés à même niveau.
        self.gammes_bin = {}  # Dictionnaire des gammes aux modes binaires existants.
        (lineno(), "self.colonne_bin", self.colonne_bin, "\n di_colon", di_colon)

        "# Exécution de la fonction qui sert à alimenter les boutons horizontaux et verticaux."
        if len(di_colon) == 0:
            "# self.gammes_arp()  # Fonction découvertes binaires selon les gammes."
            self.gammes_arp()  # Fonction découvertes des gammes binarisées.
            self.borne[1] = int([self.dic_codage[(44, '102034050607')][0][1]][0])
            ("self borne[1]", self.borne[1], type(self.borne[1]), "|", None, lineno())
            # self borne[1] 1111111 <class 'int'> | None 281.
        else:
            "# self.gammes_log()  # Fonction découvertes des gammes selon les binaires."
            self.gammes_log()  # Fonction découvertes des gammes binarisées.
            self.borne[1] = di_colon[0]
            ("self borne[1]", self.borne[1], type(self.borne[1]), "|", di_colon[0], lineno())
            # self borne[1] 1000001 <class 'int'> | 1000001 287

        # Clé = iso, valeur = (iso, int, bin, hex, oct)
        self.dic_ego, self.dic_iso, self.dic_int = {}, {}, {}
        self.dic_ego_inv, self.dic_iso_inv, self.dic_int_inv = {}, {}, {}
        self.mod_type = []
        self.dic_trans = {}
        self.table_bin = self.colonne_bin.copy()
        (lineno(), "colonne_bin", self.colonne_bin, "\n colonne_gam", self.colonne_gam.keys())
        (lineno(), "Long colonne_bin", len(self.colonne_bin), "Long colonne_gam", len(self.colonne_gam.keys()))

        "# Visionner les modes binaires par l'écriture."
        if self.colonne_bin.count("") == 0:
            self.colonne_bin.insert(0, "")
            self.colonne_bin.insert(0, "")
        elif self.colonne_bin.count("") == 1:
            self.colonne_bin.insert(0, "")
        (lineno(), " colonne_bin", self.colonne_bin[:6])
        deb_col1, deb_lin1 = self.deb_col + 6, self.deb_lin + 26
        (lineno(), "deb_col1, deb_lin1", deb_col1, deb_lin1)
        for colin in range(len(self.colonne_bin)):
            self.tableau.create_text(deb_col1, deb_lin1, text=self.colonne_bin[colin], font=self.police1)
            deb_lin1 += self.lin
            (lineno(), " colonne_bin[colin]", self.colonne_bin[colin], "colin", colin)

        "# Mise en place des boutons binaires sur le panneau gauche."
        coq0 = 0
        poli0, poli1 = Font(size=5, weight="bold"), Font(size=7, weight="bold")
        for colin in range(len(self.table_bin)):
            if self.table_bin[colin]:
                nom0 = self.table_bin[colin]
                self.table_bin[colin] = Button(self.frame_b, font=poli0, text=nom0,
                                               command=lambda bab=self.table_bin[colin]: bouton_bin(bab))
                self.table_bin[colin].grid(pady=1)
                coq0 += 1

        "# Repérer les gammes ayant deux ensembles de degrés séparés."
        multi, sage, passe = {}, 0, 0
        for k_bis in self.colonne_gam.keys():
            k_val = self.colonne_gam[k_bis]
            (lineno(), "k_bis", k_bis, "k_val", k_val)
            if k_bis[1] == 0:
                passe = 0
                sage = k_val[0]
                multi[sage] = []
                (lineno(), "k_val", k_val, k_val[0], type(k_val[0]))
            if len(k_val) > 1:
                passe += 1
                multi[sage].append(passe)
            (lineno(), "k_bis", k_bis, "passe", passe, "multi[sage]", multi[sage])
        for k_sage in multi.keys():
            if len(multi[k_sage]) < 2:
                multi[k_sage] = {}

        "# Écriture des noms et les degrés des soixante-six gammes."
        #  gammes_bin = Les gammes aux modes binaires existants.
        (lineno(), "self.gammes_bin", self.gammes_bin, " ")
        # 342 self.gammes_bin {'x26-': 'Ok', '*5': 'Ok', '-34': 'Ok', 'o63-': 'Ok', 'o34x': 'Ok', '-25o': 'Ok',
        # '-45x': 'Ok', '-46o': 'Ok', '*6': 'Ok', 'o65-': 'Ok', '+34x': 'Ok', 'x36+': 'Ok', '^3': 'Ok', '^2': 'Ok',
        # '+35x': 'Ok', '+23x': 'Ok', 'o35-': 'Ok', '+45x': 'Ok', 'x46+': 'Ok', '^4': 'Ok', 'o6': 'Ok', '+56': 'Ok',
        # '-56': 'Ok', '-56+': 'Ok', '+25-': 'Ok', '-26+': 'Ok', '+26-': 'Ok', '+26': 'Ok', '+2': 'Ok', '-34x': 'Ok',
        # '+34': 'Ok', 'x3': 'Ok', 'o5': 'Ok', '-35': 'Ok', '+6': 'Ok'}
        (lineno(), "self.colonne_gam", self.colonne_gam, "")
        (lineno(),  " *********************************************** ")
        coq2 = 1
        color1, color2 = "black", "lavender"
        mul_bin = False  # Si la gamme en cours a plusieurs ensembles de degrés.
        col0, lin0 = self.deb_col + 24, self.deb_lin + 26
        recaler = True
        for k_col, v_lin in self.colonne_gam.items():
            col1, sig = (k_col[0] * self.col) + col0, 0
            (lineno(), "colonne_gam", self.colonne_gam[k_col], "mul_bin", mul_bin)
            for val in v_lin:
                if k_col[1] == 0:
                    if val in self.gammes_bin.keys():
                        color1 = "red"
                        color2 = "pink"
                    else:
                        color1 = "black"
                        color2 = "lavender"
                lin1 = (k_col[1] * self.lin) + lin0
                (lineno(), "___   col1", col1, "lin1", lin1, "v_lin", v_lin)
                (lineno(), "*** k_col", k_col[1], "val", type(val), len(val), val)
                if len(val) > 1:  # Le dictionnaire 'multi' informe sur les multilistes.
                    if val in multi.keys() and multi[val]:
                        mul_bin = True  # print("val", val, colonne_gam[k_col], "multi", multi[val])
                    else:
                        mul_bin = False
                if len(v_lin) == 1:  # Écriture des noms en quinconce pour une meilleure lisibilité.
                    coq2 += 1
                    if k_col[1] == 0:
                        if recaler:
                            sig = -12
                            row0 = 1
                            recaler = False
                        else:
                            row0 = 2
                            recaler = True
                        gam_bouton = Button(self.frame_g, font=poli1, text=str(val), bg=color2,
                                            command=lambda bag=str(val): bouton_bin(bag))
                        gam_bouton.grid(row=row0, column=coq2)
                    if v_lin[0] == '1':
                        col3, lin3 = (col1 - 6, lin1 - 6), (col1 + 6, lin1 + 6)
                        self.tableau.create_rectangle(col3, lin3, fill="gold", width=0)
                    self.tableau.create_text(col1, lin1 + sig, text=str(val), font=self.police2, fill=color1)
                    (lineno(), "col1, lin1 + sig", col1, lin1 + sig)
                else:  # 'len(v_lin)'. Quand, plusieurs degrés correspondent à un même emplacement.
                    ce = len(v_lin)
                    col2, lin2 = (col1 - ce, lin1 - ce), (col1 + ce, lin1 + ce)
                    if mul_bin:
                        # print("multi=", mul_bin, "col_gam=", multi[colonne_gam[k_col[0], 0][0]],
                        # colonne_gam[k_col[0], 0][0])
                        # multi= True col_gam= [1, 2] o46-
                        cran = -6
                        for ici in v_lin:
                            if ici == '1':
                                col3, lin3 = (col1 - 12, lin1 - 6), (col1, lin1 + 6)
                                self.tableau.create_rectangle(col3, lin3, fill="gold", width=0)
                            self.tableau.create_text(col1 + cran, lin1, text=ici, font=self.police2, fill="maroon")
                            (lineno(), "col1 + cran, lin1", col1 + cran, lin1)
                            cran += 12
                            # print("Ici", ici, "col2, lin2", col2, lin2, val, "v_lin", v_lin,
                            # colonne_gam[k_col[0], 0][0])
                    else:
                        col3, lin3 = (col1 - 7, lin1 - 7), (col1 + 7, lin1 + 7)
                        if '1' in v_lin:
                            self.tableau.create_rectangle(col3, lin3, fill="gold", width=0)
                    self.tableau.create_oval(col2, lin2, fill="black", width=0)
                    # print("*** ELSE k_col", k_col, "col2", col2, "lin2", lin2, "\t len(v_lin)", v_lin, "val", val)
                    # print("", )
                    break

        if self.borne[1] != 1111111:
            self.protocol("WM_DELETE_WINDOW", self.quitter("0000000"))

        "# Traitement des images préalable."
        self.images_liste = ["BoutonTriEgo.png", "BoutonAntiEgo.png", "BoutonTriIso.png",
                             "BoutonAntiIso.png", "BoutonTriInt.png", "BoutonAntiInt.png"]
        self.images_references = []
        self.charger_image()

    def charger_image(self):
        """Placer les boutons-images sur le volet de droite 'table_o'"""
        # table_o = Canvas(root, width=84, height=884, bg="thistle"), (row=2, column=3)
        self.table_o.delete("all")
        # self.images_references.clear()
        esp, deb, image_id, photo_image = 60, 48, None, 0
        """self.images_liste = ["BoutonTriEgo.png", "BoutonAntiEgo.png", "BoutonTriIso.png", "BoutonAntiIso.png",
                             "BoutonTriInt.png", "BoutonAntiInt.png"]"""
        for index, image in enumerate(self.images_liste):
            photo_image = ImageTk.PhotoImage(Image.open(image))
            self.images_references.append(photo_image)
            image_id = self.table_o.create_image(deb, esp, image=photo_image)
            self.table_o.tag_bind(image_id, "<Button-1>", self.clic_image)
            esp += 100
            (lineno(), "index", index, "image_id", image_id, "image", self.images_liste[image_id - 1])

    def quitter(self, tag):
        """Pour effectuer une transition en fenêtrage"""
        "# Connaitre l'état actuel avec un repère de fermeture réelle."
        (lineno(), "\t Quitter(tag)", tag)
        if self.borne[1] == 1111111 and tag in ("1111111", "0000000"):
            (lineno(), "Quitter/if borne", self.borne[1], "\t tag", tag)
            # 430 Quitter/if borne 1111111 	 tag clic_image
            self.destroy()
        elif tag == "clic_image":
            self.colonne_bin.clear()
            self.destroy()
            (lineno(), "Quitter/elif/clic_image borne", self.borne[1], "\t tag", tag)
            # 436 Quitter/elif/clic_image borne 1111111 	 tag clic_image
        else:  # 'self.borne[1] = "       " ou 1000001
            (lineno(), "Quitter/else borne", self.borne[1], "\t tag", tag)
            # 439 Quitter/else borne 1000001 tag 0000000

    def gammes_arp(self):
        """Cette fonction est destinée à trier les modèles binaires, en commençant par la gamme naturelle.
        Concerne l'initialisation des tables par la gamme naturelle exprimée en modulations (binaires et degrés)."""
        ("\t", lineno(), "**   Fonction gammes_arp ", "gammes_mode", "self.gammes_mode")
        gammes_col = list(self.dic_codage.values())  # "dic_codage" = Les gammes issues de 'globdicTcoup.txt'
        (lineno(), "gammes_col", len(gammes_col))
        "# À chaque ligne, correspond un mode binaire. La ligne zéro, c'est pour les noms des gammes."
        # La ligne peut être donnée par l'index de l'élément de la liste des modes binaires présents.
        colon = 1  # À chaque colonne, correspond une gamme répertoriée. Une gamme a autant de modes que de lignes.

        "# Initialisation de la colonne binaire par les modulations binaires de la gamme naturelle."
        for gc in gammes_col[43]:
            if len(gc) == 2:
                self.colonne_bin.append("")
                self.colonne_bin.append("")
                self.colonne_bin.append(gc[-1])
                ligne = self.colonne_bin.index(gc[-1])
                self.colonne_gam[colon, 0] = [gc[0][0]]
                self.colonne_gam[colon, ligne] = []
                self.colonne_gam[colon, ligne].append('1')
                (lineno(), "colonne_bin[0]", self.colonne_bin, "ligne", ligne)
                (lineno(), "\t colonne_gam", self.colonne_gam[colon, ligne])
            else:
                self.colonne_bin.append(gc[-1])
                ligne = self.colonne_bin.index(gc[-1])
                self.colonne_gam[colon, ligne] = []
                self.colonne_gam[colon, ligne].append(str(gc[1]))
                (lineno(), "\t colonne_gam", self.colonne_gam[colon, ligne], "\n colonne_bin", self.colonne_bin)
            (lineno(), "Col:", colon, "Lig:", ligne, self.colonne_gam[colon, ligne], "gc", gc, len(gc), gc[-1])
            # 441 Col: 1 Lig: 1 ['1'] gc (['0', 336], '1111111') 2 1111111
            # 441 Col: 1 Lig: 2 ['2'] gc (44, 2, '1101110') 3 1101110/...
        gammes_col.pop(43)  # Effacement de la gamme majeure, afin de ne pas revenir dessus.

        "# Approvisionnement des tables binaires et modales."
        cumul_gam = {}  # Dictionnaire aux gammes comparées.
        (lineno(), "\n********** Marque Repère Répétition Hors While = (Pas de Répétition) *************\n")
        while 1:
            cumul_gam.clear()  # Dictionnaire aux gammes comparées.
            (lineno(), "\n********** Marque Repère Répétition Dans While *************\n")

            "# Poursuite du triage comparatif avec marquage lorsqu'elle y a un lien commun."
            # gammes_col = list(self.dic_codage.values())  # "dic_codage" = Les gammes issues de 'globdicTcoup.txt'
            for gam_col in gammes_col:
                ind_col = gammes_col.index(gam_col)  # 'ind_col' = Index de la gamme sélectionnée.
                cumul_gam[gam_col[0][0][0]] = [ind_col]
                (lineno(), "  cumul_gam", cumul_gam[gam_col[0][0][0]], "gam_col", gam_col)
                for mod_c in gam_col:  # 'gam_col' = Liste une gamme diatonique.
                    if mod_c[-1] in self.colonne_bin:  # 'mod_c[-1]' = Unième mode binaire.
                        ind_bin = self.colonne_bin.index(mod_c[-1])  # 'ind_bin' = Index correspondant au mode binaire.
                        cumul_gam[gam_col[0][0][0]].append(ind_bin)
                        ("_*", lineno(), "cumul_gam", cumul_gam[gam_col[0][0][0]], "mod_c", mod_c)
                ("_", lineno(), "cumul_gam", cumul_gam[gam_col[0][0][0]])
            ("\n", lineno(), "cumul_gam", cumul_gam)

            "# Les gammes qui ont des modes binaires communs existentiels."
            liste_sel = [va for va in cumul_gam.values() if len(va) > 1]  # Référence gamme.
            if liste_sel:
                liste_len = [len(va) for va in cumul_gam.values() if len(va) > 1]  # Les poids des modes binaires.
                max_liste = max(liste_len)  # Détecte le poids modal maximum.
                val_max = liste_sel[liste_len.index(max_liste)]  # Détecte la gamme aux modes binaires.
                (lineno(), "val_max", val_max[0], "\ngammes_col", gammes_col[val_max[0]])

                "# Mise à jour de la colonne binaire et celle des gammes."
                colon += 1
                n_gam = val_max[0]  # Index de la gamme sélectionnée à supprimer.
                lignes, nbr_bin = [], 0
                for gc in gammes_col[val_max[0]]:
                    # print("Gc", gc)
                    # Gc (47, 2, '1100110')
                    self.colonne_lis[str(gc[0])] = []
                    if len(gc) == 2:  # Première ligne dédiée au nom de la gamme.
                        self.colonne_gam[colon, 0] = []
                        self.colonne_gam[colon, 0] = [gc[0][0]]  # Mise à jour du nom de la gamme.
                        if gc[-1] in self.colonne_bin:
                            nbr_bin += 1
                            ligne = self.colonne_bin.index(gc[-1])
                            if ligne not in lignes:
                                self.colonne_gam[colon, ligne] = []
                                lignes.append(ligne)
                            self.colonne_gam[colon, ligne].append('1')
                            # print("***2 col_bin0", gc, "index =", colonne_bin.index(gc[-1]))
                        else:
                            self.colonne_bin.append(gc[-1])
                            ligne = self.colonne_bin.index(gc[-1])
                            if ligne not in lignes:
                                self.colonne_gam[colon, ligne] = []
                                lignes.append(ligne)
                            self.colonne_gam[colon, ligne].append('1')
                            # print("Not col_bin0 gc", gc, gc[-1])
                    else:
                        if gc[-1] in self.colonne_bin:
                            nbr_bin += 1
                            ligne = self.colonne_bin.index(gc[-1])
                            if ligne not in lignes:
                                self.colonne_gam[colon, ligne] = []
                                lignes.append(ligne)
                            elif (colon, ligne) not in self.colonne_lis[str(gc[0])]:  # Ensembles à même figure binaire.
                                self.colonne_lis[str(gc[0])].append((colon, ligne))
                                # print("CORPS yes_bin not_lis", colonne_gam[colon, ligne], "\t col/lig", colon, ligne)
                                # CORPS yes_bin ['1', '2', '3', '4', '6'] 	 colon, ligne 3 11
                            self.colonne_gam[colon, ligne].append(str(gc[1]))
                            # print("*** col_bin0", gc, "index =", colonne_bin.index(gc[-1]))
                        else:
                            self.colonne_bin.append(gc[-1])
                            ligne = self.colonne_bin.index(gc[-1])
                            if ligne not in lignes:
                                self.colonne_gam[colon, ligne] = []
                                lignes.append(ligne)
                            self.colonne_gam[colon, ligne].append(str(gc[1]))
                            # print("___ Not col_bin0 gc", gc, gc[-1])
                    if nbr_bin > 6:
                        self.gammes_bin[self.colonne_gam[colon, 0][0]] = 'Ok'
                        (lineno(), "\t\tnbr_bin", nbr_bin, "colonne_gam[colon, 0]", self.colonne_gam[colon, 0][0])
                        (lineno(), "self.gammes_bin", self.gammes_bin[self.colonne_gam[colon, 0][0]], )
                    # print("Colon", colon, "Ligne", ligne, "gc", gc)
                    # print("Colon / Ligne", colon, ligne, "colonne_gam", colonne_gam[colon, ligne])
                gammes_col.pop(n_gam)  # Effacement de la gamme traitée, afin de ne pas revenir dessus.
                # print(lineno(), "self.dic_force", list(self.dic_force.keys())[0], "||", len(self.dic_force.keys()))
            else:
                break
            (lineno(), ". len(gammes_col) =", len(gammes_col), "self.dic_force", self.dic_force)
            # 525 . len(gammes_col) = 64 self.dic_force {'1111001': [(48, '102034500067'), (43, '102034005067'),
            # print("max_liste", max_liste, "\n liste_sel", liste_sel, "\n", val_max, val_max[0][0])
        for k, v in self.colonne_gam.items():
            if len(v) > 1:
                (lineno(), "GAM_ARP self.colonne_gam", self.colonne_gam[k])
                # 578 GAM_ARP self.colonne_gam ['1', '2', '3', '4', '6', '7']
        (lineno(), "GAM_ARP self.colonne_gam", list(self.colonne_gam)[:3])
        (lineno(), "GAM_ARP self.dic_binary", self.dic_binary, "\nself.colonne_bin", self.colonne_bin)

    def gammes_log(self):
        """Fonction complémentaire au traitement original,
        elle traite le signal original comme des nombres entiers. Contrairement à la fonction
        du traitement original, qui découvrait les gammes selon les dispositions binaires.
        Elle compose l'intégralité des définitions binaires, qui de par celles-ci, va structurer
        la série des gammes fondamentales en fonction de leurs dispositions binaires. Soit,
        qu'elles sont les gammes qui contiennent le plus de binaires rapprochés, en rapport
        avec la liste intégrale des modes binaires."""
        ("\t", lineno(), "**   Fonction gammes_log, self.dic_force", list(self.dic_force)[0])
        "# Définir les contenants par quantité des sept premiers binaires cumulatifs."
        gammes_loc = list(self.dic_codage.values())  # "dic_codage" = Les gammes issues de 'globdicTcoup.txt'
        (lineno(), "gammes_loc", len(gammes_loc))
        (lineno(), "gammes_loc[0]", gammes_loc[0], "\n force", self.dic_force, "\n Clés", self.dic_force.keys())
        # 541 gammes_loc[0] [(['o45x', 1], '1000001'), (1, 2, '1000001'), (1, 3, '1000001'),
        # force {'1000001': [((1, '123400000567'), (['o45x', 1], '1000001')), (1, 2, '1000001'),
        # Clés dict_keys(['1000001', '1000000', '1000101', '1011000', '1011001', '1000111',

        "# Un dictionnaire ayant les clefs[Noms des gammes] et valeurs[Numéros des gammes]"
        # Accessible et enregistré dans le dictionnaire 'dic_titres'

        "# Faire une copie des clés 'dic_force', qui assemble les gammes aux mêmes clés."
        force_cop = self.colonne_bin  # 'force_cop' = Liste les clés de 'self.colonne_bin'.
        force_gam = {}  # Dictionnaire, clés binaires et gammes relatives. Classe-gamme quantitative.
        liste_gam = []  # Liste les numéros des gammes sans répétition.

        "# Initialisation de l'assembleur des numéros des 66 gammes quantifiés."
        globe_num = {}  # Dictionnaire, clé = Numéro de gamme, valeur = Index + Quantité.
        val_vn2 = []  # Liste regroupant les gammes traitées.
        repos_num = []  # Liste des numéros anciens, afin d'éviter de refaire le traitement.
        colonne_cop = [""]
        cc, colon = 7, 1

        "# globe_num = Dictionnaire, clé = Numéro, value = Quantité"
        for ss in range(1, 67):
            globe_num[ss] = 0  # Quand 'globe_num'[ss] > 6 = La gamme aux modes binaires est terminée.

        while cc <= len(force_cop):
            "# colonne_cop = Liste native des clés binaires utilisées."
            (lineno(), "_________________________________WHILE 1______ cc", cc)
            colonne_cop.clear()
            for cop_cc in force_cop[:cc]:
                colonne_cop.append(str(cop_cc))
                (lineno(), "cop_cc", type(cop_cc))
            col_count = colonne_cop.count("")
            if col_count == 0:
                colonne_cop.insert(0, "")
                colonne_cop.insert(1, "")
            if col_count == 1:
                colonne_cop.insert(0, "")
            (lineno(), " § colonne_cop", colonne_cop[:6], "long", len(colonne_cop), "col_count", col_count)
            # force_cop ['1000001', '1000000', '1000101', '1011000', '1011001', '1000111', '1111000']
            # colonne_cop ['1000001', '1000000', '1000101', '1011000', '1011001', '1000111', '1111000']

            "# Réajustement et réinitialisation de 'globe_num' à l'aide de 'repos_num'."
            if cc <= len(force_cop):
                globe_num.clear()
            for ss in range(1, 67):
                if ss not in repos_num:  # 'repos_num' = Gammes traitées.
                    globe_num[ss] = 0  # Quand 'globe_num'[ss] > 6 = La gamme aux modes binaires est terminée.
            (lineno(), "____________________________________________________________")
            (lineno(), " °°° Réajustement repos_num", repos_num, "Reste globe_num", globe_num)

            "# Tournée de tous les binaires de 'colonne_cop' en évolution. Et, rassembleur 'globe_num'"
            for cop in colonne_cop[2:]:
                liste_gam.clear()
                force_gam[cop] = []  # Liste les gammes et contrôle quantitatif.
                (lineno(), "colonne_cop", colonne_cop[2:], "cop", cop, type(cop))

                "# Lire le rassembleur 'self.dic_force[cop]', pour un mode binaire qui compte les 'globe_num'."
                for fc in self.dic_force[str(cop)]:
                    (lineno(), "-- for fc in self.dic_force[cop]-- FC", fc, fc[0])
                    if len(fc) < 3:
                        # Parfois 'flop' = Nom de gamme sans numéro de gamme.
                        flop = fc[0][0]
                        if isinstance(flop, str):
                            flop = dic_indice[flop]
                            (lineno(), "flop", flop)
                        (lineno(), "fc", fc, "flop", flop, type(flop))
                    else:
                        (lineno(), "fc", fc)
                        flop = fc[0]
                        (lineno(), "---ELSE---- fc", fc, " flop", flop)
                    if flop in globe_num.keys():
                        # Pointer les gammes aux mêmes binaires.
                        if len(fc) < 3:
                            ind_gam = fc[0][0]
                            if isinstance(ind_gam, str):
                                "# Capturer le numéro de la gamme avec le nom de la gamme."
                                indic = fc[0][0]
                                ind_gam = self.dic_indice[indic]
                                (lineno(), "\t if<3 str ind_gam", ind_gam, indic, "cop", cop,)
                            force_gam[cop].append(ind_gam)
                            (lineno(), "ind_gam", ind_gam, cop, "force_gam[cop]", force_gam[cop], "fc", fc)
                        else:
                            ind_gam = fc[0]
                            force_gam[cop].append(ind_gam)
                            (lineno(), "else ind_gam", ind_gam, cop, "fc", fc)
                        # Alimenter 'liste_gam',
                        if ind_gam not in liste_gam:
                            liste_gam.append(ind_gam)
                        globe_num[ind_gam] += 1
                        (lineno(), "cop", cop, "fc", fc, "ind_gam", ind_gam, "globe_num", globe_num[ind_gam])
                        (lineno(), "cop", cop, "fc", fc, " | gammes_loc", gammes_loc[ind_gam - 1])
                (lineno(), "cop", cop, "force_gam[cop]", force_gam[cop])
                # 645 cop 1111000 force_gam[cop] [3, 8, 12, 16, 18]. Liste les numéros de gammes aux mêmes binaires.

            "# Contrôler le nombre d'apparition des numéros des gammes dans le contexte 'colonne_cop'."
            "# Donner les valeurs aux emplacements via 'colonne_gam'. Clé[colonne, ligne], valeur[Noms. Degré]."
            (lineno(), "globe_num", globe_num)
            val_vn1 = [(ky, vl) for ky, vl in globe_num.items() if vl > 6]
            val_vn2.append(val_vn1)
            # Commencer à un (1) l'écriture en colonne des gammes.
            for gn, vn in globe_num.items():
                "# Contrôle des valeurs, si elles sont supérieures à six, c'est que la gamme est entière."
                if vn > 6 and gn not in repos_num:  # Trouver les gammes avec les numéros non-traités.
                    ("\n", lineno(), "=== if vn > 6 and gn not in repos_num: gn, vn", gn, vn, "val_vn2", val_vn2)
                    (lineno(), "globe_num", globe_num, "\ncolonne_cop", colonne_cop)
                    repos_num.append(gn)
                    ind_loc, halte0 = None, True
                    (lineno(), "gn", gn, "repos_num", repos_num)
                    "# Il peut y avoir quelques degrés avec un binaire, et le reste diatonique avec un autre binaire."
                    for cc1 in colonne_cop[2:]:  # 'colonne_cop' = Les binaires ou clefs 'self.dic_force'.
                        force_g1 = self.dic_force[str(cc1)]  # 'dic_force' = Total, 'force_gam' = Numéros.
                        gl_index, fg2 = -1, None
                        (lineno(), " ****** Tous les modes aux cc1", cc1, "\n♦ force_g1[:3]", force_g1)
                        if halte0:
                            for fg1 in force_g1:  # 'force_g1' = Toutes les gammes aux 'cc1'
                                if len(fg1) < 3 and len(fg1[1]) < 3:
                                    fg2 = fg1[0]  # (lineno(), "fg2", fg2)  # = 673 fg2 (['o45x', 1], '1000001')
                                    if gn in fg2:
                                        fg2 = fg1[1]
                                        (lineno(), "fg1", fg1[0], "fg2", fg2)
                                        halte0 = False
                                        break
                                elif len(fg1) == 3:
                                    fg2 = fg1
                                    if gn == fg2[0]:
                                        (lineno(), "fg1", fg1, "fg2", fg2)
                                        halte0 = False
                                        break
                                (lineno(), "---- fg1", fg1, "fg2", fg2)
                                # 691 fg1 ((1, '123400000567'), (['o45x', 1], '1000001')) fg2 (['o45x', 1], '1000001')
                        if fg2:
                            for gl in gammes_loc:  # "gammes_loc = dic_codage" = Les gammes de 'globdicTcoup.txt'
                                gl_index += 1
                                (lineno(), "gl[0]", gl, "gn", gn, "fg2", fg2)
                                if fg2 in gl:  # Le numéro de gamme[gn] est présent.
                                    ind_loc = gammes_loc[gl_index]
                                    (lineno(), "fg2", fg2, "gl", gl, "gn", gn, "\t ind_loc", ind_loc)
                                    # 704 gl [(['o45x', 1], '1000001'), (1, 2, '1000001'), (1, 3, '1000001'),
                                    break  # La gamme est trouvée, la recherche est finie.

                    (lineno(), "ind_loc", ind_loc)
                    # 688 ind_loc [(['o45x', 1], '1000001'), (1, 2, '1000001'), (1, 3, '1000001'), (1, 4, '1000001'
                    if ind_loc:  # Gamme intégrale aux sept degrés aux binaires parfois identiques.
                        (" ", lineno(), "ind_loc", list(ind_loc)[0], "\t globe_num", gn, globe_num[gn])
                        # 691 ind_loc [(['o45x', 1], '1000001'), (1, 2, '1000001'), (1, 3, '1000001'),
                        # (1, 4, '1000001'), (1, 5, '1000000'), (1, 6, '1000001'), (1, 7, '1000001')]
                        (lineno(), "colonne_cop", colonne_cop)
                        # 695 colonne_cop ['', '1000001', '1000000', '1000101', '1011000', '1011001', '1000111',
                        gl_count = 0
                        for gl_gam in ind_loc:
                            (lineno(), "gl_gam", gl_gam, type(gl_gam[-1]))
                            bin_gl = gl_gam[-1]
                            ligne = colonne_cop.index(bin_gl)
                            (lineno(), "colon", colon, "ligne", ligne, "bin_gl", bin_gl)
                            if gl_count == 0:
                                nom_gl = gl_gam[0][0]
                                deg_gl = 1
                                self.colonne_gam[colon, 0] = [nom_gl]
                                (lineno(), colon, ligne, "\t nom_gl", nom_gl, "deg_gl", deg_gl, bin_gl)
                                (lineno(), "colonne_gam", self.colonne_gam)
                            else:
                                deg_gl = gl_gam[1]
                                (lineno(), colon, ligne, "\t deg_gl", deg_gl, bin_gl)
                            if (colon, ligne) not in self.colonne_gam.keys():
                                self.colonne_gam[colon, ligne] = []
                            self.colonne_gam[colon, ligne].append(str(deg_gl))
                            gl_count = 1
                            (lineno(), "colonne_gam", self.colonne_gam[colon, ligne])
                            (lineno(), "colon", colon, "ligne", ligne, "bin_gl", bin_gl, "vn_nbr",)
                            (lineno(), "colonne_cop[ligne]", colonne_cop[ligne])
                        colon += 1

                    (lineno(), "colonne_cop", colonne_cop)
                    (lineno(), "colonne_gam", self.colonne_gam, "\n colon", colon)
                    (lineno(), "gn", gn, "vn", vn, "colonne_gam", self.colonne_gam)
                    (lineno(), "gammes_loc", "gammes_loc")
            (lineno(), "colonne_gam", self.colonne_gam.keys())

            cc += 1  # Nombre d'accompagnements des binaires dans la liste (en cours). Utile boucle 'while'

        "# colonne_gam = Clé (colonne, ligne). Valeur (Position zéro = Nom-gamme. Autres = Degrés numériques (1234567)"
        "# Intégrer 'self.gammes_bin' et repérer les gammes aux mêmes binaires (colorations)."
        # 342 self.gammes_bin {'x26-': 'Ok', '*5': 'Ok', '-34': 'Ok', 'o63-': 'Ok', 'o34x': 'Ok', '-25o': 'Ok'...
        "# Construction dictionnaire "
        dic_keys = {}
        for g_key in self.colonne_gam.keys():
            if g_key[1] == 0:
                dic_keys[g_key[0]] = []
            dic_keys[g_key[0]].append(g_key)
        (lineno(), "dic_keys", dic_keys.keys())
        (lineno(), "gammes_loc", len(gammes_loc), len(self.colonne_gam.keys()))

        "# Reconnaissance des binaires anciens, pour une coloration des degrés."
        key_lig = []  # Enregistre les nouvelles lignes.
        for c_col0 in range(0, 66):
            c_col = c_col0 + 1
            if c_col == 1:
                for dk in dic_keys[c_col]:
                    key_lig.append(dk[1])
            else:
                long_k, lo = len(dic_keys[c_col]), 0
                for dk in dic_keys[c_col]:
                    if dk[1] not in key_lig:  # Provient des nouvelles lignes.
                        key_lig.append(dk[1])
                        (lineno(), "If c_col", c_col, "long_k", long_k)
                    else:  # dk[1] in key_lig
                        lo += 1
                        # print(lineno(), "c_col", c_col, "lo", lo, "self.colonne_gam", self.colonne_gam[c_col, 0])
                if long_k == lo:
                    self.gammes_bin[self.colonne_gam[c_col, 0][0]] = "Ok"
                (lineno(), "long_k", long_k, "\n dic_keys", dic_keys[c_col], dic_keys)
            (lineno(), " **************************************************** ")
        (lineno(), "key_lig", key_lig, "\n dic_keys", "dic_keys")
        (lineno(), "self.gammes_bin", self.gammes_bin)

    def clic_image(self, event):
        """Cette fonction convertit les modes binaires.
            En changeant le type, on ne change pas son ordre croissant, sauf pour les entiers libres.
            'self.dic_codage.values()' = le dictionnaire original.
            'dic_indice' = un dictionnaire = Les clés sont les noms et les valeurs sont les numéros des gammes.
            Il faut modifier le dictionnaire original, afin d'établir une nouvelle correspondance."""
        # Relance(dic_codage, dic_binary, dic_indice, dic_force, dic_colon, dic_titres).mainloop()
        self.mod_type.clear()
        "# "
        liste_iso0 = list(self.dic_binary.keys())  # 'liste_iso0' = Liste selon self.dic_binary.keys() INITIAL
        liste_iso1 = self.colonne_bin.copy()  # 'liste_iso1' = Liste selon self.colonne_bin.copy() ORIGINAL
        # , "codage_cop" = Transformé de "dic_codage"
        # print("dic_indice", "dic_indice", "dic_binary", "dic_binary", "\n liste_iso", liste_iso, len(liste_iso))
        x, y = event.x, event.y
        item_id = self.table_o.find_closest(x, y)[0]  # Récupère l'ID de l'objet le plus proche
        # item_id : (1=iso[non trié], 2=int[trié])
        (lineno(), "item_id", item_id, "liste_iso0", liste_iso0, "\ncolonne_bin", self.colonne_bin)
        if item_id == 1:  # Conversion des modes originaux en nombres entiers.
            "# 'liste_iso1' = Liste selon self.colonne_bin.copy()"
            liste_ego = liste_iso1
            self.dic_ego["type"] = "Images libres"
            for ind in range(len(liste_ego)):
                self.dic_ego[liste_ego[ind]] = liste_ego[ind]
                (lineno(), "ind", ind, liste_keys[ind], liste_ego[ind])
            self.dic_trans = self.dic_ego.copy()
            (lineno(), "self.dic_trans", self.dic_trans)
        elif item_id == 2:  # Inversion des modes originaux en nombres entiers.
            "# 'liste_iso1' = Liste selon self.colonne_bin.copy()"
            liste_ego_inv = liste_iso1
            liste_ego_inv.reverse()
            self.dic_ego_inv["type"] = "Images libres inversées"
            for ind in range(len(liste_ego_inv)):
                self.dic_ego_inv[liste_ego_inv[ind]] = liste_ego_inv[ind]
                (lineno(), "ind", ind, liste_keys[ind], liste_ego_inv[ind])
            self.dic_trans = self.dic_ego_inv.copy()
            (lineno(), "self.dic_trans[inv]", self.dic_trans)
        elif item_id == 3:  # Conversion des modes originaux en nombres entiers.
            "# 'liste_iso0' = Liste selon self.dic_binary.keys()"
            liste_iso = [int(x) for x in liste_iso0 if x != '']
            self.dic_iso["type"] = "Entiers libres"
            for ind in range(len(liste_iso)):
                self.dic_iso[liste_iso[ind]] = liste_iso[ind]
                (lineno(), "ind", ind, liste_keys[ind], liste_iso[ind])
            self.dic_trans = self.dic_iso.copy()
        elif item_id == 4:  # Inversion des modes originaux en nombres entiers.
            "# 'liste_iso0' = Liste selon self.dic_binary.keys()"
            liste_iso_inv = [int(x) for x in liste_iso0 if x != '']
            liste_iso_inv.reverse()
            self.dic_iso_inv["type"] = "Entiers libres inversées"
            for ind in range(len(liste_iso_inv)):
                self.dic_iso_inv[liste_iso_inv[ind]] = liste_iso_inv[ind]
                (lineno(), "ind", ind, liste_keys[ind], liste_iso_inv[ind])
            self.dic_trans = self.dic_iso_inv.copy()
        elif item_id == 5:  # Conversion des modes originaux en nombres entiers.
            "# 'liste_iso0' = Liste selon self.dic_binary.keys()"
            liste_int = [int(x) for x in liste_iso0 if x != '']
            liste_int.sort()
            self.dic_int["type"] = "Entiers triés"
            for ind in range(len(liste_iso0)):
                self.dic_int[liste_int[ind]] = liste_int[ind]
            self.dic_trans = self.dic_int.copy()
        elif item_id == 6:  # Inversion des modes originaux en nombres entiers.
            "# 'liste_iso0' = Liste selon self.dic_binary.keys()"
            liste_int_inv = [int(x) for x in liste_iso0 if x != '']
            liste_int_inv.sort()
            liste_int_inv.reverse()
            self.dic_int_inv["type"] = "Entiers triés inversées"
            for ind in range(len(liste_iso0)):
                self.dic_int_inv[liste_int_inv[ind]] = liste_int_inv[ind]
            self.dic_trans = self.dic_int_inv.copy()
        if item_id == 1:
            self.mod_type = ["Vide"]
            (lineno(), "self.dic_trans", self.dic_trans)
        else:
            self.mod_type.append(item_id)
            self.mod_type.append(self.dic_trans)
        (lineno(), "Clic_image : item_id", item_id, "self.mod_type", self.mod_type, len(list(self.mod_type)))
        clic_tag = "clic_image"
        self.quitter(clic_tag)
        retour_func = func_ima(self.mod_type)
        (lineno(), "clic_image retour_func", retour_func[:3])
        (lineno(), "\n _______________________________________________ \n")

        Relance(dic_codage, dic_binary, dic_indice, dic_force, retour_func)

    # , "gammes_copie" : Remplace : "gammes_col" par une autre demande utilisateur.
    # , "gammes_mode" : Informe pour le remplacement de "gammes_copie", True ou False.
    # _________________________________________________________________________________________
    # _________________________________________________________________________________________

    gamma.audio_gam("colonne_gam")
    biner.audio_bin("colonne_bin")


(lineno(), "dic_indice", dic_indice)
Relance(dic_codage, dic_binary, dic_indice, dic_force, dic_colon).mainloop()
