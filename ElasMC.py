from math import *

import pandas as pd

import xlwt

from xlwt import Workbook

# tenseur c
C = {
    "11": 210,
    "22": 209,
    "33": 210,
    "44": 79,
    "55": 80,
    "66": 79,
    "56": 0,
    "46": -0.2,
    "45": 0.1,
    "36":  0.1,
    "35": -0.2,
    "34": 0,
    "26": 0,
    "25": 0.1,
    "24": -0.3,
    "23": 128,
    "16": 0.05,
    "15": -0.1,
    "14": 0.2,
    "13": 130,
    "12": 129
}

# for i in range(6):
#    for j in range(6):
#        C[str(i+1)+str(j+1)] = float(input("Entre le coefficient C_" + str(i+1)+str(j+1)))
# afficher pour vérification

# calcul des dix huits invarriants suivant l'axe OZ

def calcul_des_invariants(C:dict):
    I_1 = C["11"]

    I_2 = C["11"] + C["33"]

    I_3 = C["66"]

    I_4 = C["44"] + C["55"]

    I_5 = C["16"]

    I_6 = C["12"] ** 2 + C["13"] ** 2

    I_7 = C["46"] ** 2 + C["56"] ** 2

    I_8 = C["14"] ** 2 + C["15"] ** 2

    I_9 = C["26"] ** 2 + C["36"] ** 2

    I_10 = C["22"] ** 2 + C["33"] ** 2 + 2 * C["23"] ** 2

    I_11 = C["22"] * C["33"] - C["23"] ** 2

    I_12 = C["11"] * C["22"] * C["33"] + 2 * C["12"] * C["13"] * C["23"] - C["11"] * C["23"] ** 2 - C["22"] * C["13"] ** 2 - C["33"] * C["12"] ** 2

    I_13 = C["44"] ** 2 + C["55"] ** 2 + 2 * C["45"] ** 2

    I_14 = C["44"] * C["55"] - C["45"] ** 2

    I_15 = C["44"] * C["55"] * C["66"] + 2 * C["45"] * C["46"] * C["56"] - C["44"] * C["56"] ** 2 - C["55"] * C["46"] ** 2 - \
           C["66"] * C["45"] ** 2

    I_16 = C["24"] ** 2 + C["25"] + C["34"] ** 2 + C["35"] ** 2

    I_17 = C["24"] * C["35"] - C["24"] * C["34"]

    I_18 = C["14"] * (C["25"] * C["36"] - C["26"] * C["35"]) + C["15"] * (C["26"] * C["34"] - C["24"] * C["36"]) + C[
        "16"] * (C["24"] * C["35"] - C["25"] * C["34"])

    invariants = [I_1, I_2, I_3, I_4, I_5, I_6, I_7, I_8, I_9, I_10, I_11, I_12, I_13, I_14, I_15, I_16, I_17, I_18]
    # Je met les invariants dans un dictionnaire afin de pouvoir les identifiers après les avoir ranger et je fait un arrondissement à l'ordre 6
    invariant_P8 = {}
    for i in range(18):
        invariant_P8["I_" + str(i + 1)] = round(invariants[i], 8)
    return invariant_P8

'''
# Ranger les invariants du plus petit au plus grand
Invariant_trier = sorted(Invariant_P6.items(), key=lambda t: t[1])
# min_I= plus petit invariant
min_I = Invariant_trier[0][1]
# max_I= plus grand invariant
max_I = Invariant_trier[-1][1]
'''


# Conditions and distance calculation for each class

def Distance_Isotropic(I: dict = {"I": 0}):
    """
    :type I: Un dictionnaire contenant les invariants en key (I_i) et leurs valeurs associées
    """
    if type(I) != dict:
        error = f"Le type de variable que vous devez fournir est < class dict>', en lieu vous avez fourni {type(I)}"
        print(error)
        return

    invariants_approached = {}
    """
    Pour le cas isotrope, les conditions sont définis sur les invariants I_2, I_3, I_6, I_10, I_11, I_12, I_13, I_14, I_15;
    le reste des invariants doivent être nuls
    
    Les valeurs de ces invaraints approchés sont ajouter au dictionnaire invariants_approached
    """

    invariants_approached["I_2ap"] = 2 * I["I_1"]
    invariants_approached["I_3ap"] = 0.5 * I["I_4"]
    invariants_approached["I_6ap"] = 2 * (I["I_1"] - I["I_4"]) ** 2
    invariants_approached["I_10ap"] = 2 * (I["I_1"] ** 2 + (I["I_1"] - I["I_4"]) ** 2)
    invariants_approached["I_11ap"] = I["I_1"] ** 2 - (I["I_1"] - I["I_4"]) ** 2
    invariants_approached["I_12ap"] = I["I_1"] ** 3 + 2 * (I["I_1"] - I["I_4"]) ** 3 - 3 * I["I_1"] * (
            I["I_1"] - I["I_4"]) ** 2
    invariants_approached["I_13ap"] = 0.5 * I["I_4"] ** 2
    invariants_approached["I_14ap"] = 0.25 * I["I_4"] ** 2
    invariants_approached["I_15ap"] = (1 / 8) * I["I_4"] ** 3
    liste_invariants_approcher = []

    for i in range(18):
        liste_invariants_approcher.append("")
        for key in invariants_approached:
            if key == f"I_{i + 1}ap":
                liste_invariants_approcher[i] = round(invariants_approached[f"I_{i + 1}ap"], 6)

    distance_by_invariant = {}
    if invariants_approached["I_2ap"] != 0:
        distance_by_invariant["dI_2"] = (I["I_2"] - invariants_approached["I_2ap"]) / invariants_approached["I_2ap"]
    else:
        distance_by_invariant["dI_2"] = 0

    if invariants_approached["I_3ap"] != 0:
        distance_by_invariant["dI_3"] = (I["I_3"] - invariants_approached["I_3ap"]) / invariants_approached["I_3ap"]
    else:
        distance_by_invariant["dI_3"] = 0

    if invariants_approached["I_6ap"] != 0:
        distance_by_invariant["dI_6"] = (I["I_6"] - invariants_approached["I_6ap"]) / invariants_approached["I_6ap"]
    else:
        distance_by_invariant["dI_6"] = 0

    if invariants_approached["I_10ap"] != 0:
        distance_by_invariant["dI_10"] = (I["I_10"] - invariants_approached["I_10ap"]) / invariants_approached["I_10ap"]
    else:
        distance_by_invariant["dI_10"] = 0

    if invariants_approached["I_11ap"] != 0:
        distance_by_invariant["dI_11"] = (I["I_11"] - invariants_approached["I_11ap"]) / invariants_approached["I_11ap"]
    else:
        distance_by_invariant["dI_11"] = 0

    if invariants_approached["I_12ap"] != 0:
        distance_by_invariant["dI_12"] = (I["I_12"] - invariants_approached["I_12ap"]) / invariants_approached["I_12ap"]
    else:
        distance_by_invariant["dI_12"] = 0

    if invariants_approached["I_13ap"] != 0:
        distance_by_invariant["dI_13"] = (I["I_13"] - invariants_approached["I_13ap"]) / invariants_approached["I_13ap"]
    else:
        distance_by_invariant["dI_13"] = 0

    if invariants_approached["I_14ap"] != 0:
        distance_by_invariant["dI_14"] = (I["I_14"] - invariants_approached["I_14ap"]) / invariants_approached["I_14ap"]
    else:
        distance_by_invariant["dI_14"] = 0

    if invariants_approached["I_15ap"] != 0:
        distance_by_invariant["dI_15"] = (I["I_15"] - invariants_approached["I_15ap"]) / invariants_approached["I_15ap"]
    else:
        distance_by_invariant["dI_15"] = 0
    """
    On calcul les résidus pour chaque invariant et on en déduis la distance par rapport à la classe isotrope
     """

    liste_distance_by_invariant = []

    for i in range(18):
        liste_distance_by_invariant.append("")
        for key in distance_by_invariant:
            if key == f"dI_{i + 1}":
                liste_distance_by_invariant[i] = round(distance_by_invariant[key], 6)

    "On calcul maintenant la distance par rapport à la classe isotrope"
    distance_to_isotropic = 0
    for key in distance_by_invariant:
        distance_to_isotropic += distance_by_invariant[key] ** 2

    distance_to_isotropic = round(sqrt(distance_to_isotropic), 6)

    return distance_to_isotropic, liste_invariants_approcher, liste_distance_by_invariant


def Distance_Cubic(I: dict = {"I": 0}):
    """
    :type I: Un dictionnaire contenant les invariants en key (I_i) et leurs valeurs associées
    """
    if type(I) != dict:
        error = f"Le type de variable que vous devez fournir est < class dict>', en lieu vous avez fourni {type(I)}"
        print(error)
        return

    invariants_approached = {}
    """
    Pour le cas cubic, les conditions sont définis sur les invariants I_2, I_3, I_10, I_11, I_12, I_13, I_14, I_15;
    le reste des invariants doivent être nuls
    
    Les valeurs de ces invaraints approchés sont ajouter au dictionnaire invariants_approached
    """

    invariants_approached["I_2ap"] = 2 * I["I_1"]
    invariants_approached["I_3ap"] = 0.5 * I["I_4"]
    invariants_approached["I_10ap"] = 2 * I["I_1"] ** 2 + I["I_6"]
    invariants_approached["I_11ap"] = I["I_1"] ** 2 - 0.5 * I["I_6"]
    invariants_approached["I_12ap"] = I["I_1"] ** 3 + (1 / sqrt(2)) * I["I_6"] ** (3 / 2) - (3 / 2) * I["I_1"] * I[
        "I_6"]
    invariants_approached["I_13ap"] = 0.5 * I["I_4"] ** 2
    invariants_approached["I_14ap"] = 0.25 * I["I_4"] ** 2
    invariants_approached["I_15ap"] = (1 / 8) * I["I_4"] ** 3

    """
    On calcul les résidus pour chaque invariant et on en déduis la distance par rapport à la classe cubic
    """
    distance_by_invariant = {}
    if invariants_approached["I_2ap"] != 0:
        distance_by_invariant["dI_2"] = (I["I_2"] - invariants_approached["I_2ap"]) / invariants_approached["I_2ap"]
    else:
        distance_by_invariant["dI_2"] = 0

    if invariants_approached["I_3ap"] != 0:
        distance_by_invariant["dI_3"] = (I["I_3"] - invariants_approached["I_3ap"]) / invariants_approached["I_3ap"]
    else:
        distance_by_invariant["dI_3"] = 0

    if invariants_approached["I_10ap"] != 0:
        distance_by_invariant["dI_10"] = (I["I_10"] - invariants_approached["I_10ap"]) / invariants_approached["I_10ap"]
    else:
        distance_by_invariant["dI_10"] = 0

    if invariants_approached["I_11ap"] != 0:
        distance_by_invariant["dI_11"] = (I["I_11"] - invariants_approached["I_11ap"]) / invariants_approached["I_11ap"]
    else:
        distance_by_invariant["dI_11"] = 0

    if invariants_approached["I_12ap"] != 0:
        distance_by_invariant["dI_12"] = (I["I_12"] - invariants_approached["I_12ap"]) / invariants_approached["I_12ap"]
    else:
        distance_by_invariant["dI_12"] = 0

    if invariants_approached["I_13ap"] != 0:
        distance_by_invariant["dI_13"] = (I["I_13"] - invariants_approached["I_13ap"]) / invariants_approached["I_13ap"]
    else:
        distance_by_invariant["dI_13"] = 0

    if invariants_approached["I_14ap"] != 0:
        distance_by_invariant["dI_14"] = (I["I_14"] - invariants_approached["I_14ap"]) / invariants_approached["I_14ap"]
    else:
        distance_by_invariant["dI_14"] = 0

    if invariants_approached["I_15ap"] != 0:
        distance_by_invariant["dI_15"] = (I["I_15"] - invariants_approached["I_15ap"]) / invariants_approached["I_15ap"]
    else:
        distance_by_invariant["dI_15"] = 0

    liste_invariants_approcher = []
    for i in range(18):
        liste_invariants_approcher.append("")
        for key in invariants_approached:
            if key == f"I_{i + 1}ap":
                liste_invariants_approcher[i] = round(invariants_approached[f"I_{i + 1}ap"], 6)

    liste_distance_by_invariant = []
    for i in range(18):
        liste_distance_by_invariant.append("")
        for key in distance_by_invariant:
            if key == f"dI_{i + 1}":
                liste_distance_by_invariant[i] = round(distance_by_invariant[key], 6)

    "On calcul maintenant la distance par rapport à la classe cubic"
    distance_to_cubic = 0
    for key in distance_by_invariant:
        distance_to_cubic += distance_by_invariant[key] ** 2

    distance_to_cubic = round(sqrt(distance_to_cubic), 6)

    return distance_to_cubic, liste_invariants_approcher, liste_distance_by_invariant


def Distance_Hexagonale(I: dict = {"I": 0}):
    """
    :type I: Un dictionnaire contenant les invariants en key (I_i) et leurs valeurs associées
    """
    if type(I) != dict:
        error = f"Le type de variable que vous devez fournir est < class dict>', en lieu vous avez fourni {type(I)}"
        print(error)
        return

    invariants_approached = {}
    """
    Pour le cas hexagonale ou isotrope transverse, les conditions sont définis sur les invariants I_2, I_3, I_10, I_11, I_12, I_13, I_14, I_15;
    le reste des invariants doivent être nuls
    
    Les valeurs de ces invaraints approchés sont ajouter au dictionnaire invariants_approached
    """

    invariants_approached["I_12ap"] = (I["I_2"] - I["I_1"]) * (I["I_1"] ** 2 - (I["I_1"] - 2 * I["I_3"]) ** 2) - 4 * I[
        "I_3"] * (I["I_6"] - (I["I_1"] - 2 * I["I_3"]) ** 2)
    invariants_approached["I_13ap"] = 0.5 * I["I_4"] ** 2
    invariants_approached["I_14ap"] = 0.25 * I["I_4"] ** 2
    invariants_approached["I_15ap"] = (1 / 4) * I["I_3"] * I["I_4"] ** 2

    """
    On calcul les résidus pour chaque invariant et on en déduis la distance par rapport à la classe hexagonale
    """
    distance_by_invariant = {}

    if invariants_approached["I_12ap"] != 0:
        distance_by_invariant["dI_12"] = (I["I_12"] - invariants_approached["I_12ap"]) / invariants_approached["I_12ap"]
    else:
        distance_by_invariant["dI_12"] = 0

    if invariants_approached["I_13ap"] != 0:
        distance_by_invariant["dI_13"] = (I["I_13"] - invariants_approached["I_13ap"]) / invariants_approached["I_13ap"]
    else:
        distance_by_invariant["dI_13"] = 0

    if invariants_approached["I_14ap"] != 0:
        distance_by_invariant["dI_14"] = (I["I_14"] - invariants_approached["I_14ap"]) / invariants_approached["I_14ap"]
    else:
        distance_by_invariant["dI_14"] = 0

    if invariants_approached["I_15ap"] != 0:
        distance_by_invariant["dI_15"] = (I["I_15"] - invariants_approached["I_15ap"]) / invariants_approached["I_15ap"]
    else:
        distance_by_invariant["dI_15"] = 0

    liste_invariants_approcher = []
    for i in range(18):
        liste_invariants_approcher.append("")
        for key in invariants_approached:
            if key == f"I_{i + 1}ap":
                liste_invariants_approcher[i] = round(invariants_approached[f"I_{i + 1}ap"], 6)

    liste_distance_by_invariant = []
    for i in range(18):
        liste_distance_by_invariant.append("")
        for key in distance_by_invariant:
            if key == f"dI_{i + 1}":
                liste_distance_by_invariant[i] = round(distance_by_invariant[key], 6)

    "On calcul maintenant la distance par rapport à la classe hexagonale"
    distance_to_hexagonal = 0
    for key in distance_by_invariant:
        distance_to_hexagonal += distance_by_invariant[key] ** 2

    distance_to_hexagonal = round(sqrt(distance_to_hexagonal), 6)

    return distance_to_hexagonal, liste_invariants_approcher, liste_distance_by_invariant


def Distance_Tetragonale(I: dict = {"I": 0}):
    """
    :type I: Un dictionnaire contenant les invariants en key (I_i) et leurs valeurs associées
    """
    if type(I) != dict:
        error = f"Le type de variable que vous devez fournir est < class dict>', en lieu vous avez fourni {type(I)}"
        print(error)
        return

    invariants_approached = {}
    """
    Pour le cas tétragonale , les conditions sont définis sur les invariants I_2, I_3, I_10, I_11, I_12, I_13, I_14, I_15;
    le reste des invariants doivent être nuls
    
    Les valeurs de ces invaraints approchés sont ajouter au dictionnaire invariants_approached
    """

    invariants_approached["I_9ap"] = I["I_5"] ** 2
    invariants_approached["I_13ap"] = 0.5 * I["I_4"] ** 2
    invariants_approached["I_14ap"] = 0.25 * I["I_4"] ** 2
    invariants_approached["I_15ap"] = (1 / 4) * I["I_3"] * I["I_4"] ** 2

    """
    On calcul les résidus pour chaque invariant et on en déduis la distance par rapport à la classe tétragonale
    """
    distance_by_invariant = {}
    if invariants_approached["I_9ap"] != 0:
        distance_by_invariant["dI_9"] = (I["I_9"] - invariants_approached["I_9ap"]) / invariants_approached["I_9ap"]
    else:
        distance_by_invariant["dI_9"] = 0

    if invariants_approached["I_13ap"] != 0:
        distance_by_invariant["dI_13"] = (I["I_13"] - invariants_approached["I_13ap"]) / invariants_approached["I_13ap"]
    else:
        distance_by_invariant["dI_13"] = 0

    if invariants_approached["I_14ap"] != 0:
        distance_by_invariant["dI_14"] = (I["I_14"] - invariants_approached["I_14ap"]) / invariants_approached["I_14ap"]
    else:
        distance_by_invariant["dI_14"] = 0

    if invariants_approached["I_15ap"] != 0:
        distance_by_invariant["dI_15"] = (I["I_15"] - invariants_approached["I_15ap"]) / invariants_approached["I_15ap"]
    else:
        distance_by_invariant["dI_15"] = 0

    liste_invariants_approcher = []
    for i in range(18):
        liste_invariants_approcher.append("")
        for key in invariants_approached:
            if key == f"I_{i + 1}ap":
                liste_invariants_approcher[i] = round(invariants_approached[f"I_{i + 1}ap"], 6)

    liste_distance_by_invariant = []
    for i in range(18):
        liste_distance_by_invariant.append("")
        for key in distance_by_invariant:
            if key == f"dI_{i + 1}":
                liste_distance_by_invariant[i] = round(distance_by_invariant[key], 6)

    "On calcul maintenant la distance par rapport à la classe tétragonale"
    distance_to_tetragonal = 0
    for key in distance_by_invariant:
        distance_to_tetragonal += distance_by_invariant[key] ** 2

    distance_to_tetragonal = round(sqrt(distance_to_tetragonal), 6)

    return distance_to_tetragonal, liste_invariants_approcher, liste_distance_by_invariant


def Distance_Trigonale(I: dict = {"I": 0}):
    """
    :type I: Un dictionnaire contenant les invariants en key (I_i) et leurs valeurs associées
    """
    if type(I) != dict:
        error = f"Le type de variable que vous devez fournir est < class dict>', en lieu vous avez fourni {type(I)}"
        print(error)
        return

    invariants_approached = {}
    """
    Pour le cas trigonale , les conditions sont définis sur les invariants I_2, I_3, I_10, I_11, I_12, I_13, I_14, I_15;
    le reste des invariants doivent être nuls
    
    Les valeurs de ces invaraints approchés sont ajouter au dictionnaire invariants_approached
    """
    invariants_approached["I_7ap"] = (I["I_7"] + I["I_8"] + I["I_16"])/3
    invariants_approached["I_13ap"] = 0.5 * I["I_4"] ** 2
    invariants_approached["I_14ap"] = 0.25 * I["I_4"] ** 2
    invariants_approached["I_15ap"] = (1 / 4) * I["I_3"] * I["I_4"] ** 2 - 0.5 * I["I_4"] * I["I_7"]

    """
    On calcul les résidus pour chaque invariant et on en déduis la distance par rapport à la classe trigonale
    """
    distance_by_invariant = {}

    if invariants_approached["I_7ap"] != 0:
        distance_by_invariant["dI_7"] = (I["I_7"] - invariants_approached["I_7ap"]) / invariants_approached["I_7ap"]
    else:
        distance_by_invariant["dI_7"] = 0

    if invariants_approached["I_13ap"] != 0:
        distance_by_invariant["dI_13"] = (I["I_13"] - invariants_approached["I_13ap"]) / invariants_approached["I_13ap"]
    else:
        distance_by_invariant["dI_13"] = 0

    if invariants_approached["I_14ap"] != 0:
        distance_by_invariant["dI_14"] = (I["I_14"] - invariants_approached["I_14ap"]) / invariants_approached["I_14ap"]
    else:
        distance_by_invariant["dI_14"] = 0

    if invariants_approached["I_15ap"] != 0:
        distance_by_invariant["dI_15"] = (I["I_15"] - invariants_approached["I_15ap"]) / invariants_approached["I_15ap"]
    else:
        distance_by_invariant["dI_15"] = 0

    "On calcul maintenant la distance par rapport à la classe trigonale"
    distance_to_trigonal = 0
    for key in distance_by_invariant:
        distance_to_trigonal += distance_by_invariant[key] ** 2

    distance_to_trigonal = round(sqrt(distance_to_trigonal), 6)

    liste_invariants_approcher = []
    for i in range(18):
        liste_invariants_approcher.append("")
        for key in invariants_approached:
            if key == f"I_{i + 1}ap":
                liste_invariants_approcher[i] = round(invariants_approached[f"I_{i + 1}ap"], 6)

    liste_distance_by_invariant = []
    for i in range(18):
        liste_distance_by_invariant.append("")
        for key in distance_by_invariant:
            if key == f"dI_{i + 1}":
                liste_distance_by_invariant[i] = round(distance_by_invariant[key], 6)

    return distance_to_trigonal, liste_invariants_approcher, liste_distance_by_invariant


def Distance_Orthotropic(I: dict = {"I": 0}):
    """
    :type I: Un dictionnaire contenant les invariants en key (I_i) et leurs valeurs associées
    """
    if type(I) != dict:
        error = f"Le type de variable que vous devez fournir est < class dict>', en lieu vous avez fourni {type(I)}"
        print(error)
        return

    invariants_approached = {}
    """
    Pour le cas orthotropic , les conditions sont définis sur les invariants I_2, I_3, I_10, I_11, I_12, I_13, I_14, I_15;
    le reste des invariants doivent être nuls
    
    Les valeurs de ces invaraints approchés sont ajouter au dictionnaire invariants_approached
    """

    invariants_approached["I_13ap"] = I["I_4"] ** 2 - 2 * I["I_14"]
    invariants_approached["I_15ap"] = I["I_3"] * I["I_14"]

    """
    On calcul les résidus pour chaque invariant et on en déduis la distance par rapport à la classe orthotropic
    """
    distance_by_invariant = {}

    if invariants_approached["I_13ap"] != 0:
        distance_by_invariant["dI_13"] = (I["I_13"] - invariants_approached["I_13ap"]) / invariants_approached["I_13ap"]
    else:
        distance_by_invariant["dI_13"] = 0

    if invariants_approached["I_15ap"] != 0:
        distance_by_invariant["dI_15"] = (I["I_15"] - invariants_approached["I_15ap"]) / invariants_approached["I_15ap"]
    else:
        distance_by_invariant["dI_15"] = 0


    "On calcul maintenant la distance par rapport à la classe orthotropic"
    distance_to_orthotropic = 0
    for key in distance_by_invariant:
        distance_to_orthotropic += distance_by_invariant[key] ** 2

    distance_to_orthotropic = round(sqrt(distance_to_orthotropic), 6)

    liste_invariants_approcher = []
    for i in range(18):
        liste_invariants_approcher.append("")
        for key in invariants_approached:
            if key == f"I_{i + 1}ap":
                liste_invariants_approcher[i] = round(invariants_approached[f"I_{i + 1}ap"], 6)

    liste_distance_by_invariant = []
    for i in range(18):
        liste_distance_by_invariant.append("")
        for key in distance_by_invariant:
            if key == f"dI_{i + 1}":
                liste_distance_by_invariant[i] = round(distance_by_invariant[key], 6)

    return distance_to_orthotropic, liste_invariants_approcher, liste_distance_by_invariant


def Distance_Monoclinic(I: dict = {"I": 0}):
    """
    :type I: Un dictionnaire contenant les invariants en key (I_i) et leurs valeurs associées
    """
    if type(I) != dict:
        error = f"Le type de variable que vous devez fournir est < class dict>', en lieu vous avez fourni {type(I)}"
        print(error)
        return

    invariants_approached = {}
    """
    Pour le cas monoclinic , les conditions sont définis sur les invariants I_2, I_3, I_10, I_11, I_12, I_13, I_14, I_15;
    le reste des invariants doivent être nuls
    
    Les valeurs de ces invaraints approchés sont ajouter au dictionnaire invariants_approached
    """

    invariants_approached["I_13ap"] = I["I_4"] ** 2 - 2 * I["I_14"]
    invariants_approached["I_15ap"] = I["I_3"] * I["I_14"]

    """
    On calcul les résidus pour chaque invariant et on en déduis la distance par rapport à la classe orthotropic
    """
    distance_by_invariant = {}

    if invariants_approached["I_13ap"] != 0:
        distance_by_invariant["dI_13"] = (I["I_13"] - invariants_approached["I_13ap"]) / invariants_approached["I_13ap"]
    else:
        distance_by_invariant["dI_13"] = 0

    if invariants_approached["I_15ap"] != 0:
        distance_by_invariant["dI_15"] = (I["I_15"] - invariants_approached["I_15ap"]) / invariants_approached["I_15ap"]
    else:
        distance_by_invariant["dI_15"] = 0


    "On calcul maintenant la distance par rapport à la classe monoclinic"
    distance_to_monoclinic = 0
    for key in distance_by_invariant:
        distance_to_monoclinic += distance_by_invariant[key] ** 2

    distance_to_monoclinic = round(sqrt(distance_to_monoclinic), 6)

    liste_invariants_approcher = []
    for i in range(18):
        liste_invariants_approcher.append("")
        for key in invariants_approached:
            if key == f"I_{i + 1}ap":
                liste_invariants_approcher[i] = round(invariants_approached[f"I_{i + 1}ap"], 6)

    liste_distance_by_invariant = []
    for i in range(18):
        liste_distance_by_invariant.append("")
        for key in distance_by_invariant:
            if key == f"dI_{i + 1}":
                liste_distance_by_invariant[i] = round(distance_by_invariant[key], 6)

    return distance_to_monoclinic, liste_invariants_approcher, liste_distance_by_invariant

def rechercher_les_invariants_nulls(I:dict, precision: int):
    list_invariants_nulls = []
    """ Vérifier les invariants nulls"""

    invariant_a_verifier = ["I_5", "I_7", "I_8", "I_9", "I_16", "I_17", "I_18"]
    invariants_premieD = ["I_1", "I_2", "I_3", "I_4", "I_5"]
    invariants_deuxiemeD = ["I_6", "I_7", "I_8", "I_9", "I_10", "I_11", "I_13", "I_14", "I_16", "I_17"]

    invariants_troisiemeD = ["I_12", "I_15", "I_18"]


    #verifier si I_5 est null
    for i in I:
        if I[i] == 0:
            list_invariants_nulls.append(i)

    for inv_a_verif in invariant_a_verifier:

        invariants_nulls_deuxiemeD = ["I_7", "I_8", "I_9", "I_16", "I_17"]
        invariants_of_same_degre_invariants = [invariants_premieD, invariants_deuxiemeD, invariants_troisiemeD]

        if I[inv_a_verif] != 0:
            invariants_nulls_deuxiemeD.remove(inv_a_verif)
            for invariants_of_same_degre in invariants_of_same_degre_invariants:
                if inv_a_verif in invariants_of_same_degre:
                    invariants_of_same_degre.remove(inv_a_verif)
                    p=[]
                    for i in invariants_of_same_degre:
                        multiplicity = int(round(abs(I[i]/I[inv_a_verif]), 0))
                        if (multiplicity < precision) and (i not in invariants_nulls_deuxiemeD):
                            p.append(i)
                    if len(p) == 0:
                        list_invariants_nulls.append(inv_a_verif)

    return list_invariants_nulls

def classification_du_materiau(Invariants_nulls : list, Residus:list, classes: list):

    classes_residus_G = {}

    i_g1 = 0
    i_g2 = 0
    i_g3 = 0
    for inv in Invariants_nulls:
        if inv in ["I_5", "I_7","I_8", "I_9", "I_16", "I_17", "I_18"]:
            i_g1 += 1
        if inv in ["I_7","I_8", "I_16", "I_17", "I_18"]:
            i_g2 += 1
        if inv in ["I_5", "I_9", "I_17", "I_18"]:
            i_g3 += 1
    if i_g1 == 7:
        for classe in classes:
            if classe in ["isotropic", "Cubic", "Hexagonal", "Orthotropic"]:
                classes_residus_G[classe] = Residus[classes.index(classe)]
        classes_residus_G_ranger = sorted(classes_residus_G.items(), key=lambda t: t[1])

        classe_du_materiau = classes_residus_G_ranger[0][0]

    elif i_g2 == 5:
        for classe in classes:
            if classe in ["Tetragonal", "Monoclinic"]:
                classes_residus_G[classe] = Residus[classes.index(classe)]
        classes_residus_G_ranger = sorted(classes_residus_G.items(), key=lambda t: t[1])

        classe_du_materiau = classes_residus_G_ranger[0][0]


    elif i_g3 == 4:
        classe_du_materiau = "Trigonal"
    else:
        classe_du_materiau = "Triclinic"

    return classe_du_materiau


"""
programme de calcul des distances
"""
file=True

if file==True:
    Invariant_P8 = calcul_des_invariants(C)

    distances_to_isotropic = Distance_Isotropic(Invariant_P8)
    distances_to_cubic = Distance_Cubic(Invariant_P8)
    distances_to_hexagonal = Distance_Hexagonale(Invariant_P8)
    distances_to_tetragonal = Distance_Tetragonale(Invariant_P8)
    distances_to_trigonal = Distance_Trigonale(Invariant_P8)
    distances_to_orthotropic = Distance_Orthotropic(Invariant_P8)
    distances_to_monoclinic = Distance_Monoclinic(Invariant_P8)

    #___________________________arrangement des données et etiquetage________________________________________________________________________________
    list_invariants = ["I_1", "I_2", "I_3", "I_4", "I_5", "I_6", "I_7", "I_8", "I_9", "I_10", "I_11", "I_12", "I_13",
                       "I_14", "I_15", "I_16", "I_17", "I_18"]
    list_invariants_calculer = []
    for i in range(18):
        list_invariants_calculer.append(Invariant_P8["I_" + str(i + 1)])



    #isotropic
    list_condi_iso = ["I_1", "2I_1", "0,5*I_4", "I_4", "0", "I_6", "0", "0", "0", "2I_1^2+I_6",
                      "I_1^2-0,5I_6", "I_1^3+(1/racine(2))I_6^(3/2)-(3/2)I_1I_6", "0,5*I_4^2", "0,25*I_4^2", "(1/8)*I_4^3",
                      "0", "0", "0"]
    liste_distance_by_invariant_iso = distances_to_isotropic[2]
    liste_invariants_approcher_iso = distances_to_isotropic[1]
    distance_to_iso = distances_to_isotropic[0]

    #cubic
    list_condi_cub = ["I_1", "2I_1", "0,5*I_4", "I_4", "0", "2(I_1-I_4)^2", "0", "0", "0", "2(I_1^2+(I_1-I_4)^2)",
                      "I_1^2-(I_1-I_4)^2", "I_1^3+2(I_1-I_4)^3-3I_1(I_1-I_4)^2", "0,5*I_4^2", "0,25*I_4^2", "(1/8)*I_4^3",
                      "0", "0", "0"]
    liste_distance_by_invariant_cub = distances_to_cubic[2]
    liste_invariants_approcher_cub = distances_to_cubic[1]
    distance_to_cub = distances_to_cubic[0]

    #hexagonal
    list_condi_hex = ["I_1", "I_2", "I_3", "I_4", "0", "I_6", "0", "0", "0", "I_10",
                      "I_11", "(I_2-I_1)[I_1^2-(I_1-2I_3)^2]-4I_3[I_6-(I_1-2I_3)^2]", "0,5*I_4^2", "0,25*I_4^2", "(1/4)I_3I_4^2",
                      "0", "0", "0"]
    liste_distance_by_invariant_hex = distances_to_hexagonal[2]
    liste_invariants_approcher_hex = distances_to_hexagonal[1]
    distance_to_hex = distances_to_hexagonal[0]

    #tetragonal
    list_condi_tetra = ["I_1", "I_2", "I_3", "I_4", "0", "I_6", "0", "0", "I_5^2", "I_10",
                      "I_11", "(I_2-I_1)[I_1^2-(I_1-2I_3)^2]-4I_3[I_6-(I_1-2I_3)^2]", "0,5*I_4^2", "0,25*I_4^2", "(1/4)I_3I_4^2",
                      "0", "0", "0"]
    liste_distance_by_invariant_tetra = distances_to_tetragonal[2]
    liste_invariants_approcher_tetra = distances_to_tetragonal[1]
    distance_to_tetra = distances_to_tetragonal[0]

    #trigonal
    list_condi_tri = ["I_1", "I_2", "I_3", "I_4", "0", "I_6", "I_7=I_8=I_16", "I_7=I_8=I_16", "0", "I_10",
                      "I_11", "I_12", "0,5*I_4^2", "0,25*I_4^2", "(1/4)I_3I_4^2-0,5I_4I_7",
                      "I_7=I_8=I_16", "0", "0"]
    liste_distance_by_invariant_tri = distances_to_trigonal[2]
    liste_invariants_approcher_tri = distances_to_trigonal[1]
    distance_to_tri = distances_to_trigonal[0]

    #orthotrop
    list_condi_ortho = ["I_1", "I_2", "I_3", "I_4", "0", "I_6", "0", "0", "0", "I_10",
                      "I_11", "I_12", "I_4^2-2I_14", "I_14", "I_3I_14",
                      "0", "0", "0"]
    liste_distance_by_invariant_ortho = distances_to_orthotropic[2]
    liste_invariants_approcher_ortho = distances_to_orthotropic[1]
    distance_to_ortho = distances_to_orthotropic[0]

    #monoclinique
    list_condi_mono = ["I_1", "I_2", "I_3", "I_4", "I_5", "I_6", "0", "0", "I_9", "I_10",
                      "I_11", "I_12", "I_4^2-2I_14", "I_14", "I_3I_14",
                      "0", "0", "0"]
    liste_distance_by_invariant_mono = distances_to_monoclinic[2]
    liste_invariants_approcher_mono = distances_to_monoclinic[1]
    distance_to_mono = distances_to_monoclinic[0]

    #______________________Exportation des données________________________________________________________________________
    wb = Workbook()

    sheet1 = wb.add_sheet("Sheet 1")
    # sheet1.write(row,col, data, style)
    sheet1.write(1, 1, "Invariants")
    sheet1.write(2, 1, "Calculés")
    #Isotrope
    sheet1.write(4, 0, "Cas Isotrope")
    sheet1.write(4, 1, "Conditions")
    sheet1.write(5, 1, "Approchés")
    sheet1.write(6, 1, "résidus=(Cal-Apro)/Apro")
    for i in range(18):
        sheet1.write(1, 2 + i, list_invariants[i])
        sheet1.write(2, 2 + i, list_invariants_calculer[i])
        ""
        sheet1.write(4, 2 + i, list_condi_iso[i])
        sheet1.write(5, 2 + i, liste_invariants_approcher_iso[i])
        sheet1.write(6, 2 + i, liste_distance_by_invariant_iso[i])
    sheet1.write(7, 1, "Distance")
    sheet1.write(7, 2, distance_to_iso)

    #cubic
    sheet1.write(9, 0, "Cas cubic")
    sheet1.write(9, 1, "Conditions")
    sheet1.write(10, 1, "Approchés")
    sheet1.write(11, 1, "résidus=(Cal-Apro)/Apro")
    for i in range(18):
        sheet1.write(9, 2 + i, list_condi_cub[i])
        sheet1.write(10, 2 + i, liste_invariants_approcher_cub[i])
        sheet1.write(11, 2 + i, liste_distance_by_invariant_cub[i])
    sheet1.write(12, 1, "Distance")
    sheet1.write(12, 2, distance_to_cub)

    #hexagonal
    sheet1.write(14, 0, "Cas Hexagonal")
    sheet1.write(14, 1, "Conditions")
    sheet1.write(15, 1, "Approchés")
    sheet1.write(16, 1, "résidus=(Cal-Apro)/Apro")
    for i in range(18):
        sheet1.write(14, 2 + i, list_condi_hex[i])
        sheet1.write(15, 2 + i, liste_invariants_approcher_hex[i])
        sheet1.write(16, 2 + i, liste_distance_by_invariant_hex[i])
    sheet1.write(17, 1, "Distance")
    sheet1.write(17, 2, distance_to_hex)

    #TETRAgonal
    sheet1.write(19, 0, "Cas Tetragonal")
    sheet1.write(19, 1, "Conditions")
    sheet1.write(20, 1, "Approchés")
    sheet1.write(21, 1, "résidus=(Cal-Apro)/Apro")
    for i in range(18):
        sheet1.write(19, 2 + i, list_condi_tetra[i])
        sheet1.write(20, 2 + i, liste_invariants_approcher_tetra[i])
        sheet1.write(21, 2 + i, liste_distance_by_invariant_tetra[i])
    sheet1.write(22, 1, "Distance")
    sheet1.write(22, 2, distance_to_tetra)

    #Trigonal
    sheet1.write(23, 0, "Cas Trigonal")
    sheet1.write(23, 1, "Conditions")
    sheet1.write(24, 1, "Approchés")
    sheet1.write(25, 1, "résidus=(Cal-Apro)/Apro")
    for i in range(18):
        sheet1.write(23, 2 + i, list_condi_tri[i])
        sheet1.write(24, 2 + i, liste_invariants_approcher_tri[i])
        sheet1.write(25, 2 + i, liste_distance_by_invariant_tri[i])
    sheet1.write(26, 1, "Distance")
    sheet1.write(26, 2, distance_to_tri)

    #Orthotropic
    sheet1.write(28, 0, "Cas Orthotropic")
    sheet1.write(28, 1, "Conditions")
    sheet1.write(29, 1, "Approchés")
    sheet1.write(30, 1, "résidus=(Cal-Apro)/Apro")
    for i in range(18):
        sheet1.write(28, 2 + i, list_condi_ortho[i])
        sheet1.write(29, 2 + i, liste_invariants_approcher_ortho[i])
        sheet1.write(30, 2 + i, liste_distance_by_invariant_ortho[i])
    sheet1.write(31, 1, "Distance")
    sheet1.write(31, 2, distance_to_ortho)

    #Monoclinique
    sheet1.write(33, 0, "Cas Monoclinique")
    sheet1.write(33, 1, "Conditions")
    sheet1.write(34, 1, "Approchés")
    sheet1.write(35, 1, "résidus=(Cal-Apro)/Apro")
    for i in range(18):
        sheet1.write(33, 2 + i, list_condi_mono[i])
        sheet1.write(34, 2 + i, liste_invariants_approcher_mono[i])
        sheet1.write(35, 2 + i, liste_distance_by_invariant_mono[i])
    sheet1.write(36, 1, "Distance")
    sheet1.write(36, 2, distance_to_mono)

    wb.save("data_global_academic_EXACADEMIC_CBIC_genericV01.xls")
