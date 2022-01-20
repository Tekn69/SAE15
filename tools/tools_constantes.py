"""
Module listant toutes les constantes pouvant être utilisées pour faciliter l'écriture du code de la SAE15
"""

# *****************************************************************************
# Les enseignants
#: Liste des enseignants permanents
ENSEIGNANTS_PERMANENTS = ["BARAS CLEO",
                          "DUCHAMP JEAN-MARC",
                          "GOEURIOT LORRAINE",
                          "MORAND ALAIN",
                          "SICLET CYRILLE",
                          "BENECH PHILIPPE",
                          "NOVAKOV EMIL",
                          "THIRIET JEAN MARC",
                          "CHOLLET REMY",
                          "DELNONDEDIEU YVES",
                          "DESPINASSE BRUNO",
                          "DUPONT BELRHALI KARINE",
                          "FAYOLLE GERARD",
                          "KASPER KEVIN",
                          "LUBINEAU DENIS",
                          "ROYER SANDRA",
                          "VEDEL FRANCK",
                          "ESCANDE ERIC",
                          "MARTIN JEROME"]


#: Liste des enseignants vacataires
ENSEIGNANTS_VACATAIRES = ["BARFIELD VERONIQUE",
                          "DOLMAZON THOMAS",
                          "GIRAUD CATHERINE",
                          "GOBIN PIERRE",
                          "HOFMANN CAROLINE",
                          "NICOLL NICOLA",
                          "ROCHE JEAN-PHILIPPE",
                          "ROCHETTE VERONIQUE",
                          "SAILLARD RAPHAELLE",
                          "TISSERAND BRUNO"]

# *********************************************************
#: Liste de modalités d'enseignement
MODALITES = ["TD", "TP", "CM", "Proj"]

# ************************************************************************
# Les ressources / SAés / module par semestre :

# Liste des modules du semestre 1 découpés en ressources et en SAés
#: Liste des ressources du semestre 1 de BUT
RESSOURCES_S1 = ["R101-InitRes",
                 "R102-ArchiRes",
                 "R103-LAN",
                 "R104-ELN",
                 "R105-Lignes",
                 "R106-ArchiInfo",
                 "R107-Python1",
                 "R108-Shell",
                 "R109-TechnoWeb",
                 "R110-Anglais",
                 "R111-ExprCom",
                 "R112-PPP",
                 "R113-MathSignal",
                 "R114-MathTX",
                 "R115-GestProj"]

#: Liste des SAés du semestre 1 de BUT
SAES_S1 = ["SAÉ11-HygièneInfo",
           "SAÉ12",
           "SAÉ13",
           "SAÉ14-CVWeb",
           "SAÉ15",
           "SAÉ16-Portfolio"]

#: Liste des ressources du semestre 2 de BUT
RESSOURCES_S2 = ["R201-TechnoIP",
                 "R202-AdminSys",
                 "R203-ServRes",
                 "R204-Téléphonie",
                 "R205-Signal",
                 "R206-Numérisation",
                 "R207-SGBD",
                 "R208-Python2",
                 "R209-DevWeb",
                 "R210-Anglais",
                 "R211-ExprCom",
                 "R212-PPP",
                 "R213-MathNum",
                 "R214-MathAnalyse"]

#: Liste des SAés du semestre 2 de BUT
SAES_S2 = ["SAÉ21", "SAÉ22", "SAÉ23", "SAÉ24-ProjIntégratif", "SAÉ25-Portfolio"]

#: Listes des modules du semestre 3 de DUT
MODULES_S3 = ["M3101-Wifi",
              "M3102-ResOp",
              "M3103-TechnoAccès",
              "M3104-LDAP",
              "M3105-SrvRes",
              "M3106-TransNum",
              "M3107-ResCell",
              "M3109-ProjTut",
              "M3201-Anglais",
              "M3202-ExprCom",
              "M3203-PPP",
              "M3204-MathRice",
              "M3205-FO-HF",
              "M3206-Crypto",
              "OSP06-SystEln",
              "RCPI01-POO"
              ]

#: Listes des modules du semestre 4 de DUT
MODULES_S4 = ["M4101-ProjTut",
              "M4102-Stage",
              "M4201-Anglais",
              "M4202-ExprCom",
              "M4203-PPP",
              "M4204-Droit",
              "M4205-ToIP",
              "M4206-ProgMob",
              "M4208-Antenne",
              "M4209-FO",
              "M4210-InfraSécu",
              "OSM01-MathLine",
              "RCPD02-BDD"
              ]

#: Intervention sans module
SANS_CODE = "Autre"

# *********************************************************************
# Les 3 unités d'enseignements du BUT1

# Pour chaque UE, les modules rattachés aux UE (car ayant le coefficient est le plus élévé dans l'UE)
#: UE1 du BUT1
UE1_RT1_Administrer = ["R101", "R102", "R103", "R104", "R106", "SAÉ11", "SAÉ12"]
#: UE2 du BUT1
UE2_RT2_Connecter = ["R105", "R110", "R111", "R112", "R113", "R114", "SAÉ13"]
#: UE3 du BUT1
UE3_RT3_Programmer = ["R107", "R108", "R109", "R115", "SAÉ14", "SAÉ15", "SAÉ16"]
#: UE1 du DUT2
UE1_DUT2 = ["M3101", "M3102", "M3103", "M3104", "M3105",
              "M3106", "M3107", "M3109", "M4101", "M4102"]
#: UE2 du DUT2
UE2_DUT2 = ["M3201", "M3202", "M3203", "M3204", "M3205",
              "M3206", "OSP06", "RCPI01", "M4201", "M4202",
              "M4203", "M4204", "M4205", "M4206", "M4208",
              "M4209", "M4210", "OSM01", "RCPD02"]

# Liste des coeffs de chaque module du S1 dans chaque UE, les modules étant listés
# dans l'ordre RESSOURCES_S1 + SAES_S1
COEFF_UE1 = [12, 12, 8, 8, 0, 10, 0, 6, 0, 3, 3, 2, 5, 4, 0, 16, 33, 0, 0, 0, 0]
COEFF_UE2 = [4, 0, 4, 5, 5, 0, 0, 0, 0, 5, 5, 3, 8, 8, 2, 0, 0, 33, 0, 0, 0]
COEFF_UE3 = [4, 0, 0, 0, 0, 0, 22, 7, 4, 5, 4, 4, 0, 0, 4, 0, 0, 0, 16, 26, 0]


# *******************************************************************************
# Les thématiques d'enseignement en BUT1 : Réseau, Télécom, Informatique, Math, (Vie en) Entreprise

#: Thématique réseau
THEME_RESEAU = "Réseau"
#: Liste des ressources et SAés du BUT1 dans le thème réseau
MODULES_RESEAU_BUT1 = ['R102', 'R103', 'SAÉ12', 'R201', 'R202', 'R203', 'SAÉ21']
#: Liste des modules du DUT2 dans le thème réseau
MODULES_RESEAU_DUT2 = ['M3101', 'M3102', 'M3103', 'M3104', 'M3105', 'M4210']

#: Thématique télécommunication
THEME_TELECOM = "Télécommunication"
#: Liste des ressources et des SAés du BUT1 dans le thème télécom
MODULES_TELECOM_BUT1 = ['SAÉ13', 'R204', 'R205', 'R206', 'SAÉ22']
#: Liste des modules du DUT2 dans le thème télécom
MODULES_TELECOM_DUT2 = ['M3106', 'M3107', 'M3205', 'M3206', 'M4205', 'M4208', 'M4209']

#: Thématique informatique
THEME_INFO = "Informatique"
#: Liste des ressources et des SAés du BUT1 dans le thème informatique
MODULES_INFO_BUT1 = ['R107', 'R108', 'R109', 'SAÉ15', 'R207', 'R208', 'R209', 'SAÉ23']
#: Liste des modules du DUT2 dans le thème informatique
MODULES_INFO_DUT2 = ['RCPI01', 'M4206', 'RCPD02']

#: Thématique mathématiques
THEME_MATHS = "Mathématiques"
#: Liste des ressources et des Saés dans le thème mathématiques
MODULES_MATHS_BUT1 = ['R105', 'R113', 'R114', 'R213', 'R214']
#:Liste des modules dans le théme mathématiques
MODULES_MATHS_DUT2 = ['M3204', 'OSM01']

#: Thématique transverse
THEME_TRANSVERSES = "Transverses"
#: Liste des ressources et des Saés dans le thème transverses
MODULES_TRANSVERSES_BUT1 = ['R101', 'R104', 'R106', 'R110', 'R111', 'R112', 'R115', 'SAÉ11', 'SAÉ14', 'SAÉ16', 'R210', 'R211', 'R212', 'SAÉ24', 'SAÉ25']
#: Liste des modules dans le thème transverses
MODULES_TRANSVERSES_DUT2 = ['M3109', 'M3201', 'M3202', 'M3203', 'OSP06', 'M4101', 'M4102', 'M4201', 'M4202', 'M4203', 'M4204']

# Liste des noms de thèmes
THEMES = [THEME_RESEAU, THEME_INFO, THEME_MATHS, THEME_TELECOM, THEME_TRANSVERSES]

# *******************************************************************************
# Les salles regroupées par fonction pour le département

#: Salles de TD appartenant au département RT
SALLES_TD_RT = ["IUT1_010", "IUT1_06", "IUT1_08",
                "IUT1_112B", "IUT1_119", "IUT1_120",
                "IUT1_120b", "IUT1_121_GE", "IUT1_T23_24"]

#: Salles de TP appartenant au département RT
SALLES_TP_RT = ["IUT1_126", "IUT1_T14 tel", "IUT1_T16 tel2",
                "IUT1_T22 info2", "IUT1_T25 info1", "IUT1_T26 proj",
                "IUT1_T27 res3", "IUT1_T32 res2", "IUT1_T33 res1"]

#: Amphis pour les CM partagés/mutualisés entre plusieurs départements de l'IUT
AMPHI = ["IUT1_AMPHI BELLEDONNE", "IUT1_AMPHI CHARTREUSE"]

#: Autres salles mutualisées/partagées entre plusieurs départements de l'IUT
SALLES_BAT_CENTRAL = ["IUT1_C003", "IUT1_C007", "IUT1_C011",
                      "IUT1_C103", "IUT1_C104", "IUT1_C105",
                      "IUT1_C201", "IUT1_C202", "IUT1_C215"]

# **********************************************************************
# Les groupes (de TD) d'étudiants

#: Groupes de TD du BUT1 et du DUT2
GROUPES = ["S1G1", "S1G2", "S1G3", "S1G4",
           "S2G1", "S2G2", "S2G3", "S2G4",
           "S3G1", "S3G2", "S3UFA",
           "S4G1", "S4G2", "S4UFA"]

# ***********************************************************************
# L'année universitaire 2021-2022

#: Début de l'année universitaire pour les étudiants de S1 et de S3
DEBUT_ANNEE = "01-09-2021"
DEBUT_ANNEE_2022 = "01-09-2022"

#: Fin d'année universitaire (correspondant à la fin des semestres S2 et S4)
FIN_ANNEE = "31-07-2022"

#: L'heure de début des cours (le matin)
HEURE_DEBUT = "08:00"

#: L'heure de fin (l'après-midi)
HEURE_FIN = "17:30"

# Période de cours entre deux vacances scolaires sous la forme d'une liste [debut_periode, fin_periode],
# la fin de la période indiquant la date du vendredi au soir à partir duquel débutent les vacances)
#: Période pédagogique entre la Rentrée et la Toussaint
PERIODE1 = [DEBUT_ANNEE, "29-10-2021"]
#: Période pédagogique entre la Toussaint et Noël
PERIODE2 = ["08-11-2021", "17-12-2021"]
#: Période pédagogque entre Noël et les vacances d'Hiver
PERIODE3 = ["03-01-2022", "18-02-2022"]
#: Période pédagogique entre les vacances d'Hiver et celles de Printemps
PERIODE4 = ["28-02-2022", "22-04-2022"]
#: Période pédagogique entre les vacances de Printemps et celles d'Eté
PERIODE5 = ["02-05-2022", FIN_ANNEE]

#: La liste de toutes les périodes
PERIODES_SCOLAIRES = [PERIODE1, PERIODE2, PERIODE3, PERIODE4, PERIODE5]

#: Noms des temps marquants de l'année
NOMS_PERIODES = ["Rentrée", "Toussaint", "Noël", "Hiver", "Printemps", "Eté"]

#: Jours fériés de l'année universitaire
JOURS_FERIES = ["11-11-2021",  # Armistice
                "18-04-2022",  # Lundi de Pâques
                "01-05-2022",  # Fête du travail
                "08-05-2022",  # Victoire 1945
                "26-05-2022",  # Ascension
                "27-05-2022"  # Pont de l'ascension
                ]

# *****************************************************
# Semestres

#: Début et fin du semestre 1 de BUT (semestre de début d'année)
BUT1_SEMESTRE1 = [DEBUT_ANNEE, "21-01-2022"]
#: Début et fin du semestre 2 de BUT
BUT1_SEMESTRE2 = ["24-01-2022", "17-06-2022"]
#: Début et fin du semestre 3 de DUT (semestre de début d'année)
DUT2_SEMESTRE3 = [DEBUT_ANNEE, "14-01-2022"]
#: Début et fin du semestre 4 de DUT
DUT2_SEMESTRE4 = ["17-01-2022", "25-06-2022"]

# *********************************************************************
# Evènements (donnant lieu à amphi)
EVENEMENTS = ['Conf CyberSécu WatchGuard', 'Open Day']
