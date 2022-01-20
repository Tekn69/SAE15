"""
===================
Module `tools_sae`
===================

A télécharger :download:`ici <../../src/tools/tools_sae.py>`.

"""
import datetime
import os.path
import typing

import tools_constantes, tools_date


def lecture_fichier(chemin: str) -> typing.Optional[str]:
    """
    Lecture d'un fichier.

    :param chemin: le chemin du fichier
    :return: la chaine de caractère contenant tout le fichier ou None si le fichier n'a pu être lu
    """

    try:
        with open(chemin, encoding="utf8") as fh:
            return fh.read()
    except:
        print("Le fichier n'existe pas %s", os.path.abspath(chemin))
        return None


def theme_module(module: str) -> str:
    """
    Retourne le thème d'un module donné par son code.

    :param module: le code du module (par exemple R107)
    :return: le thème associé dans la liste: réseau, télécommunication, informatique, mathématiques, transverses ou 'N/A' si le module n'existe pas
    """
    MODULE_THEME = {tools_constantes.THEME_RESEAU: tools_constantes.MODULES_RESEAU_BUT1 + tools_constantes.MODULES_RESEAU_DUT2,
                    tools_constantes.THEME_INFO: tools_constantes.MODULES_INFO_BUT1 + tools_constantes.MODULES_INFO_DUT2,
                    tools_constantes.THEME_TELECOM: tools_constantes.MODULES_TELECOM_BUT1 + tools_constantes.MODULES_TELECOM_DUT2,
                    tools_constantes.THEME_MATHS: tools_constantes.MODULES_MATHS_BUT1 + tools_constantes.MODULES_MATHS_DUT2,
                    tools_constantes.THEME_TRANSVERSES: tools_constantes.MODULES_TRANSVERSES_BUT1 + tools_constantes.MODULES_TRANSVERSES_DUT2
                    }
    theme_module = {mod: theme for theme in MODULE_THEME for mod in MODULE_THEME[theme]}
    try:
        return theme_module[module]
    except KeyError:
        return "N/A"


def get_event_by_id(events: typing.List[str], id: str):
    """Pour débuggage: Recherche l'événement d'``id`` donné dans une liste d'événements ``events``.
    Renvoie l'événement trouvé ou ``None`` s'il n'est pas dans la liste.

    :return: L'événement
    """
    for event in events:
        if event.startswith(id):
            return event
    return None


def get_jours_ouvres():
    """Renvoie la liste de tous les jours ouvrés de l'année universitaire (hors WE, jours fériés et vacances).

    :return: Liste des jours ouvrés
    """
    annee = int(tools_constantes.DEBUT_ANNEE.split("-")[-1])
    [heure_deb, minutes_deb] = [int(val) for val in tools_constantes.HEURE_DEBUT.split(":")] # début des cours
    [heure_fin, minutes_fin] = [int(val) for val in tools_constantes.HEURE_FIN.split(":")]   # fin des cours

    periodes_scolaires = []
    for [debut, fin] in tools_constantes.PERIODES_SCOLAIRES:
        val_debut = tuple([int(val) for val in debut.split("-")][::-1])
        val_fin = tuple([int(val) for val in fin.split("-")][::-1])
        date_debut = datetime.datetime(*val_debut, hour=heure_deb, minute=minutes_deb)
        date_fin = datetime.datetime(*val_fin, hour=heure_fin, minute=minutes_fin)
        periodes_scolaires.append( (date_debut, date_fin) )# date + heures des périodes de cours

    # L'année universitaire (mois, annee) hors vacances
    jours = []
    annee_universitaire = [(m, annee) for m in range(9, 13)]  # septembre-décembre
    annee_universitaire += [(m, annee + 1) for m in range(1, 9)]  # janvier-août inclus
    for (m, a) in annee_universitaire:
        for j in range(1, 32):
            valide = tools_date.est_valide(j, m, a)  # est une date valide
            jour_semaine = tools_date.get_numero_jour_semaine(j, m, a)  # le jour de la semaine
            if valide and 1 <= jour_semaine <= 5:  # les jours valides de la semaine
                # dans périodes scolaires ?
                ddate = datetime.datetime(year=a, month=m, day=j, hour=12, minute=0)  # le jour j à 12h
                dans_periode = False
                for p in periodes_scolaires:
                    if p[0] <= ddate <= p[1]:
                        dans_periode = True
                if dans_periode:
                    jours.append("{:02d}-{:02d}-{:4d}".format(j, m, a))

    # Suppression des fériés
    jours_ouvres = jours[::]
    for ferie in tools_constantes.JOURS_FERIES:
        if ferie in jours_ouvres:
            i_deb = jours_ouvres.index(ferie)  # le jour ferié
            jours_ouvres = jours_ouvres[:i_deb] + jours_ouvres[i_deb + 1:]
    return jours_ouvres


def get_event_trie_par_date(events):
    """Retourne une liste d'événements triés par date croissante"""

    return sorted(events, key=lambda e: "-".join(e.split(";")[1].split("-")[::-1]))