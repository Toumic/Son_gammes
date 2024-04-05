#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vicenté quantic cabviva
"""Ce programme consiste à donner une sonorité diatonique aux gammes.
Cette gamme est en Do et elle retrace les gammes fondamentales.
L'architecture de cet assemblage ressemble à cette image (images/ClassBooLsIII.png)."""
# https://cabviva.com/musicmp3/gamcop!s.mp3

from tkinter import *
from tkinter.constants import *
from tkinter.font import *
from PIL import ImageTk, Image
import gammes_audio as gamma
import binomes_audio as biner

"# Initialisation du visuel, sous forme d'un tableur."
root = Tk()
root.title("Base illusion")
root.geometry("1824x1000+30+10")
table_x = Canvas(root, width=60, height=30)  # Coin (haut, gauche) pour l'image favicon.
table_x.grid(row=1, column=1)
table_b = Canvas(root, width=60, height=884, bg="white")  # Colonne dédiée aux boutons binaires. (Verticale)
table_b.grid(row=2, column=1)
frame_b = Frame(table_b)
frame_b.grid()
table_y = Canvas(root, width=84, height=30, bg="thistle")  # Coin (haut, droite).
table_y.grid(row=1, column=3)
table_o = Canvas(root, width=84, height=884, bg="thistle")  # Colonne dédiée aux binaires ordonnés. (Verticale)
table_o.grid(row=2, column=3)
table_z = Canvas(root, width=84, height=60, bg="thistle")  # Coin (bas, droite).
table_z.grid(row=3, column=3)
table_g = Canvas(root, width=1656, height=30, bg="seashell")  # Colonne dédiée aux boutons gammes. (Horizontale)
table_g.grid(row=1, column=2)
frame_g = Frame(table_g)
frame_g.grid()
tableau = Canvas(root, width=1656, height=884, bg="ivory")  # Affichage des gammes (noms, binaires) liées.
tableau.grid(row=2, column=2)
tableau.config(borderwidth=3, relief=RAISED)
police1, police2 = "Courier 8 bold", "Courrier 10"
'''Pour une colonne binaire de soixante-six éléments, un intervalle de treize = Hauteur (67*13 = 871).
Ayant un nombre de colonnes égal aux gammes (66), plus une pour les binaires = Longueur (67*24 = 1608).'''
long1, haut1, long2, haut2 = 1656, 884, 1608, 871
deb_col, deb_lin = (long1 - long2) // 2, (haut1 - haut2) // 2
col, lin = 24, 13  # Espace entre les colonnes_26 et espace entre les lignes_13.
tot_col, tot_lin = 67 * 24, 67 * 13
"# Tracer le quadrillage principal."
fin_col, fin_lin = deb_col + tot_col, deb_lin + tot_lin
deb_col0, deb_lin0 = deb_col, deb_lin
for i in range(67):
    tableau.create_line(deb_col, deb_lin0, fin_col, deb_lin0, fill="lightblue", dash=(1, 1))
    tableau.create_line(deb_col0, deb_lin, deb_col0, fin_lin, fill="lightblue", dash=(1, 1))
    deb_col0 += col
    deb_lin0 += lin

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
dic_codage = {}  # Dictionnaire des gammes et de leurs modes.
dic_binary = {}  # Dictionnaire, clé = binaire, valeur = zob (['o45x', 1], '1000001'), (1, 2, '1000001')...
dic_indice = {}  # Dictionnaire, clé = Nom de la gamme, valeur = Numéro de la gamme.
pre_codage = open('globdicTcoup.txt', 'r')
mod, cod1 = '', 1

"# Lire un globdicTcoup.txt pour construire un dictionnaire de tous les modèles diatoniques."
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
                dic_indice[gam_classic[mod_cod][0]] = []  # Dictionnaire, clé = Nom_gamme, valeur = Rang_gamme.
                dic_indice[gam_classic[mod_cod][0]].append(cod1)
                # print("     gam_classic[mod_cod]", gam_classic[mod_cod])
            else:
                zob = cod1, cod2, mod
            dic_codage[cod1, pre_cod[:12]].append(zob)
            # print("dic_codage[cod1, pre_cod[:12]]", dic_codage[cod1, pre_cod[:12]])
            dic_binary[zob[-1]] = []  # 'dic_mode01' = Clé Binaire, = Rang numérique.
            dic_binary[zob[-1]].append(zob)
            # print("zob", zob[-1])
            # print("dic_codage :", dic_codage[cod1, pre_cod[:12]])
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
        cod1 += 1
# ("dic_codage", dic_codage)
pre_codage.close()

colonne_bin = []  # Première colonne contenant les modes binaires uniques. L'index de l'élément = La ligne.
colonne_gam = {}  # Colonnes contenant les gammes de 1 à 66. Première ligne = Noms.
colonne_lis = {}  # Le dictionnaire clé=N°gamme, valeur=Ensemble degrés à même niveau.
gammes_bin = {}  # Dictionnaire des gammes aux modes binaires existants.
images_liste = ["BoutonTriInt.png", "BoutonTriBin.png", "BoutonTriHex.png", "BoutonTriOct.png"]
images_copie = images_liste.copy()


def clic_image(event):
    """Cette fonction convertit les modes binaires.
        En changeant le type, on change aussi son ordre croissant.
        'dic_indice' ; un dictionnaire = Les clés sont les noms et les valeurs sont les numéros des gammes.
        Il faut modifier le dictionnaire original, afin d'établir une nouvelle correspondance."""
    liste_iso = list(set(list(dic_binary.keys())))
    # print("dic_indice", "dic_indice", "dic_binary", "dic_binary", "\n liste_iso", liste_iso, len(liste_iso))
    x, y = event.x, event.y
    item_id = table_o.find_closest(x, y)[0]  # Récupère l'ID de l'objet le plus proche
    if item_id == 1:  # Conversion des modes originaux en nombres entiers.
        liste_int = [int(x) for x in liste_iso]
        liste_int.sort()
        print("Type de nombre entier", liste_int, len(liste_int))
    elif item_id == 2:  # Conversion des modes originaux en nombres binaires.
        liste_bin = [bin(int(x)) for x in liste_iso]
        liste_bin.sort()
        print("Type de nombre binaire", liste_bin, len(liste_bin))
    elif item_id == 3:  # Conversion des modes originaux en nombres hexadécimaux.
        liste_hex = [hex(int(x)) for x in liste_iso]
        liste_hex.sort()
        print("Type de nombre hexadécimal", liste_hex, len(liste_hex))
    else:  # Conversion des modes originaux en nombres octaux.
        liste_oct = [oct(int(x)) for x in liste_iso]
        liste_oct.sort()
        print("Type de nombre octal", liste_oct, len(liste_oct))
    print("\n item_id", item_id, images_copie[item_id - 1], "x/y", x, y)


# _________________________________________________________________________________________
"# Placer les boutons-images sur le volet de droite 'table_o'"
# table_o = Canvas(root, width=84, height=884, bg="thistle"), (row=2, column=3)
esp, deb = 60, 48
image_id = ["", "", ""]
'# images_liste = ["BoutonTriInt.png", "BoutonTriBin.png", "BoutonTriHex.png", "BoutonTriOct.png"]'
for il, image in enumerate(images_liste):
    images_liste[il] = Image.open(image)
    images_liste[il] = ImageTk.PhotoImage(images_liste[il])
    image_id = table_o.create_image(deb, esp, image=images_liste[il])
    table_o.tag_bind(image_id, "<Button-1>", clic_image)
    esp += 100


def gammes_arp():
    """Cette fonction est destinée à trier les modèles binaires, en commençant par la gamme naturelle.
    Concerne l'initialisation des tables par la gamme naturelle exprimée en modulations (binaires et degrés)."""
    gammes_col = list(dic_codage.values())
    "# À chaque ligne, correspond un mode binaire. La ligne zéro, c'est pour les noms des gammes."
    # La ligne peut être donnée par l'index de l'élément de la liste des modes binaires présents.
    colon = 1  # À chaque colonne, correspond une gamme répertoriée. Une gamme a autant de modes que de lignes.
    "# Initialisation de la colonne binaire par les modulations binaires de la gamme naturelle."
    for gc in gammes_col[43]:
        if len(gc) == 2:
            colonne_bin.append("")
            colonne_bin.append(gc[-1])
            ligne = colonne_bin.index(gc[-1])
            colonne_gam[colon, 0] = []
            colonne_gam[colon, 0] = [gc[0][0]]
            colonne_gam[colon, ligne] = []
            colonne_gam[colon, ligne].append('1')
            # print("colonne_bin[0]", colonne_bin[0])
            # print("\t colonne_gam", colonne_gam[colon, ligne])
        else:
            colonne_bin.append(gc[-1])
            ligne = colonne_bin.index(gc[-1])
            colonne_gam[colon, ligne] = []
            colonne_gam[colon, ligne].append(str(gc[1]))
            # print("\t colonne_gam", colonne_gam[colon, ligne])
        # print("Colon :", colon, "Ligne :", ligne, colonne_gam[colon, ligne], "\t gc[1]", gc)
    gammes_col.pop(43)  # Effacement de la gamme majeure, afin de ne pas revenir dessus.

    "# Approvisionnement des tables binaires et modales."
    cumul_gam = {}  # Dictionnaire aux gammes comparées.
    encore_une = True
    while encore_une:
        "# Poursuite du triage comparatif avec marquage lorsqu'il y a un lien commun."
        for gam_col in gammes_col:
            ind_col = gammes_col.index(gam_col)  # Index de la gamme sélectionnée.
            cumul_gam[gam_col[0][0][0]] = [ind_col]
            for mod_c in gam_col:  # , gam_col = Liste une gamme diatonique.
                if mod_c[-1] in colonne_bin:  # , mod_c[-1] = Unième mode binaire.
                    ind_bin = colonne_bin.index(mod_c[-1])  # Indexe la ligne correspondant au mode binaire.
                    cumul_gam[gam_col[0][0][0]].append(ind_bin)
                    # print("colonne_bin", gam_col[0], mod_c[-1], "\t colonne_bin[ind_bin]", ind_bin, ind_col)

        "# Les gammes qui ont des modes binaires communs existentiels."
        liste_sel = [[va, len(va)] for va in cumul_gam.values() if len(va) > 1]  # Référence gamme.
        liste_len = [len(va) for va in cumul_gam.values() if len(va) > 1]  # Liste les poids des modes binaires.
        max_liste = max(liste_len)  # Détecte le poids modal maximum.
        val_max = liste_sel[liste_len.index(max_liste)]  # Détecte la gamme aux modes binaires.
        # print("val_max =", val_max)

        "# Mise à jour de la colonne binaire et celle des gammes."
        colon += 1
        n_gam = val_max[0][0]  # Index de la gamme sélectionnée à supprimer.
        lignes, nbr_bin = [], 0
        for gc in gammes_col[val_max[0][0]]:
            # print("Gc", gc)
            # Gc (47, 2, '1100110')
            colonne_lis[str(gc[0])] = []
            if len(gc) == 2:  # Première ligne dédiée au nom de la gamme.
                colonne_gam[colon, 0] = []
                colonne_gam[colon, 0] = [gc[0][0]]  # Mise à jour du nom de la gamme.
                if gc[-1] in colonne_bin:
                    nbr_bin += 1
                    ligne = colonne_bin.index(gc[-1])
                    if ligne not in lignes:
                        colonne_gam[colon, ligne] = []
                        lignes.append(ligne)
                    colonne_gam[colon, ligne].append('1')
                    # print("***2 col_bin0", gc, "index =", colonne_bin.index(gc[-1]))
                else:
                    colonne_bin.append(gc[-1])
                    ligne = colonne_bin.index(gc[-1])
                    if ligne not in lignes:
                        colonne_gam[colon, ligne] = []
                        lignes.append(ligne)
                    colonne_gam[colon, ligne].append('1')
                    # print("Not col_bin0 gc", gc, gc[-1])
            else:
                if gc[-1] in colonne_bin:
                    nbr_bin += 1
                    ligne = colonne_bin.index(gc[-1])
                    if ligne not in lignes:
                        colonne_gam[colon, ligne] = []
                        lignes.append(ligne)
                    elif (colon, ligne) not in colonne_lis[str(gc[0])]:  # Ensembles à même figure binaire.
                        colonne_lis[str(gc[0])].append((colon, ligne))
                        # print("CORPS yes_bin not_lis", colonne_gam[colon, ligne], "\t colon, ligne", colon, ligne)
                        # CORPS yes_bin ['1', '2', '3', '4', '6'] 	 colon, ligne 3 11
                    colonne_gam[colon, ligne].append(str(gc[1]))
                    # print("*** col_bin0", gc, "index =", colonne_bin.index(gc[-1]))
                else:
                    colonne_bin.append(gc[-1])
                    ligne = colonne_bin.index(gc[-1])
                    if ligne not in lignes:
                        colonne_gam[colon, ligne] = []
                        lignes.append(ligne)
                    colonne_gam[colon, ligne].append(str(gc[1]))
                    # print("___ Not col_bin0 gc", gc, gc[-1])
            if nbr_bin > 6:
                gammes_bin[colonne_gam[colon, 0][0]] = 'Ok'
                # print("\t \t nbr_bin", nbr_bin, "colonne_gam[colon, 0]", colonne_gam[colon, 0][0])
            # print("Colon", colon, "Ligne", ligne, "gc", gc)
            # print("Colon / Ligne", colon, ligne, "colonne_gam", colonne_gam[colon, ligne])
        gammes_col.pop(n_gam)  # Effacement de la gamme traitée, afin de ne pas revenir dessus.
        if len(gammes_col) == 0:
            encore_une = False
        # print(". len(gammes_col) =", len(gammes_col))
        # print("max_liste", max_liste, "\n liste_sel", liste_sel, "\n", val_max, val_max[0][0])


gammes_arp()


def bouton_bin(bb):
    """Pratiquer les redirections des boutons d'en-tête[noms des gammes] et latéral gauche[binaires].
        Cette fonction est située après avoir initialisé les dictionnaires nécessaires."""
    if len(bb) < 7:
        a = "# Jonction module gammes_audio"
    else:
        a = "# Jonction module binomes_audio"
    print("Bb", bb, len(bb), "\t A", a)


# _________________________________________________________________________________________
"# Mise en forme des tables dans la grille"
font_coins = "Courrier 18 bold"
# table_x = Canvas(root, width=72, height=30, bg="white"), (row=1, column=1)
"72/2=36/2=18, 30/2=15, 54=18+36"
tx1, tx2 = (18, 2), (54, 30)
table_x.create_oval(tx1, tx2, fill="gold", width=0)  # Table du favicon.
table_x.create_text(36, 15, fill="white", text="X", font=font_coins)  # Table du favicon. Lettre X.
image_pil = Image.open("favicon_16.png")
image_tk = ImageTk.PhotoImage(image_pil)
# Image = 16×16. Table_x = 72×30. Emplacement = 54×5
table_x.create_image(12, 16, image=image_tk)  # Table du favicon.
# table_g = Canvas(root, width=1656, height=30, bg="seashell"), (row=1, column=2)
tx1, tx2 = (2, 2), (1656, 30)
table_g.create_oval(tx1, tx2, fill="blanchedalmond", width=0)  # Colonne dédiée aux boutons gammes.
# table_y = Canvas(root, width=84, height=30, bg="thistle"), (row=1, column=3)
table_y.create_text(44, 16, fill="white", text="Y", font=font_coins)  # Table décorative. Lettre Y.
# table_z = Canvas(root, width=84, height=60, bg="thistle"), (row=3, column=3)
table_z.create_text(44, 31, fill="white", text="Z", font=font_coins)  # Table décorative. Lettre Y.
# _________________________________________________________________________________________
"# Analyse des modes binaires et des gammes."
coq0, coq1 = 0, 0
deb_col0, deb_lin0 = deb_col + 6, deb_lin + 26
# Visionner les modes binaires par l'écriture.
for colin in colonne_bin:
    tableau.create_text(deb_col0, deb_lin0, text=colonne_bin[coq1], font=police1)
    coq1 += 1
    deb_lin0 += lin
    # print("colon_lin", colon_lin, " = colonne_bin[coq1]", colonne_bin[coq1])
# _________________________________________________________________________________________
"# Repérer les gammes ayant deux ensembles de degrés séparés."
multi, sage, passe = {}, 0, ''
for k_bis in colonne_gam.keys():
    k_val = colonne_gam[k_bis]
    if k_bis[1] == 0:
        passe = 0
        sage = k_val[0]
        multi[sage] = []
        # print("1 k_val", k_val, k_val[0], type(k_val[0]))
    if len(k_val) > 1:
        passe += 1
        multi[sage].append(passe)
for k_sage in multi.keys():
    if len(multi[k_sage]) < 2:
        multi[k_sage] = {}
# _________________________________________________________________________________________
"# Mise en place des boutons binaires sur le panneau gauche."
coq0, tab_bin = 0, colonne_bin.copy()
poli0, poli1 = Font(size=5, weight="bold"), Font(size=7, weight="bold")
for colin in range(len(tab_bin)):
    if tab_bin[colin]:
        nom0 = tab_bin[colin]
        tab_bin[colin] = Button(frame_b, font=poli0, text=nom0,
                                command=lambda bab=tab_bin[colin]: bouton_bin(bab))
        tab_bin[colin].grid(pady=1)
        coq0 += 1
# _________________________________________________________________________________________
"# Écriture des noms et les degrés des soixante-six gammes."
#  gammes_bin = Les gammes aux modes binaires existants.
coq2 = 1
color1, color2 = "black", "lavender"
mul_bin = False  # Si la gamme en cours a plusieurs ensembles de degrés.
col0, lin0 = deb_col + 24, deb_lin + 26
recaler = True
for k_col, v_lin in colonne_gam.items():
    col1, sig = (k_col[0] * col) + col0, 0
    # print("colonne_gam", colonne_gam[k_col], "mul_bin", mul_bin)
    for val in v_lin:
        if k_col[1] == 0:
            if val in gammes_bin.keys():
                color1 = "red"
                color2 = "pink"
            else:
                color1 = "black"
                color2 = "lavender"
        lin1 = (k_col[1] * lin) + lin0
        # print("___   col1", col1, "lin1", lin1, "v_lin", v_lin)
        # print("*** k_col", k_col[1], "val", type(val), len(val), val)
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
                gam_bouton = Button(frame_g, font=poli1, text=str(val), bg=color2,
                                    command=lambda bag=str(val): bouton_bin(bag))
                gam_bouton.grid(row=row0, column=coq2)
            if v_lin[0] == '1':
                col3, lin3 = (col1 - 6, lin1 - 6), (col1 + 6, lin1 + 6)
                tableau.create_rectangle(col3, lin3, fill="gold", width=0)
            tableau.create_text(col1, lin1 + sig, text=str(val), font=police2, fill=color1)
        else:  # 'len(v_lin)'. Quand, plusieurs degrés correspondent à un même emplacement.
            ce = len(v_lin)
            col2, lin2 = (col1 - ce, lin1 - ce), (col1 + ce, lin1 + ce)
            if mul_bin:
                # print("multi=", mul_bin, "col_gam=", multi[colonne_gam[k_col[0], 0][0]], colonne_gam[k_col[0], 0][0])
                # multi= True col_gam= [1, 2] o46-
                cran = -6
                for ici in v_lin:
                    if ici == '1':
                        col3, lin3 = (col1 - 12, lin1 - 6), (col1, lin1 + 6)
                        tableau.create_rectangle(col3, lin3, fill="gold", width=0)
                    tableau.create_text(col1 + cran, lin1, text=ici, font=police2, fill="maroon")
                    cran += 12
                    # print("Ici", ici, "col2, lin2", col2, lin2, val, "v_lin", v_lin, colonne_gam[k_col[0], 0][0])
            else:
                col3, lin3 = (col1 - 7, lin1 - 7), (col1 + 7, lin1 + 7)
                if '1' in v_lin:
                    tableau.create_rectangle(col3, lin3, fill="gold", width=0)
            tableau.create_oval(col2, lin2, fill="black", width=0)
            # print("*** ELSE k_col", k_col, "col2", col2, "lin2", lin2, "\t len(v_lin)", v_lin, "val", val)
            # print("", )
            break
    # print(" FOR colonne_gam   cadrer", cadrer)
    # break

gamma.audio_gam(colonne_gam)
biner.audio_bin(colonne_bin)

print("\n LONGUEURS : \n _ colonne_bin", len(colonne_bin), "\n _ colonne_gam", len(colonne_gam.keys()), "\n", col, lin)

root.mainloop()
