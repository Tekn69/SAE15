"""
Tests unitaires du projet 5.
Màj 11/12/2021
"""

import inspect

import pytest

import tools_constantes
import tools_introspection
import tools_tests

# Import du projet
try:
    import projet5
except:
    pass
MODULE = "projet5"


@pytest.mark.fonction_facultative
@pytest.mark.echeance4
class TestRechercheCoursPeriodeEnseignant:
    FONCTION = "recherche_cours_periode_enseignant"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet5)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 3)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet5)
        assert len(inspect.signature(fct).parameters) == 3, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        events = tools_tests.lecture_lignes_fichier_csv(datadir["periode1.csv"])
        res = projet5.recherche_cours_periode_enseignant(events, "CHOLLET REMY", tools_constantes.PERIODE1)
        assert isinstance(res, list), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list")
        assert isinstance(res[0], str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list de str")

    @pytest.mark.parametrize("data", [
        # pytest.param("data2"),
        pytest.param("data"),
    ])
    @pytest.mark.parametrize("nom_periode, periode", [
        pytest.param("periode1", tools_constantes.PERIODE1, id="periode1"),
        pytest.param("periode2", tools_constantes.PERIODE2, id="periode2"),
    ])
    def test_valeur_retour(self, datadir, data, nom_periode, periode):
        events = tools_tests.lecture_lignes_fichier_csv(datadir[f"{data}.csv"])
        attendu = tools_tests.lecture_lignes_fichier_csv(datadir[f"_expected/{data}-{nom_periode}.csv"])

        resultat = projet5.recherche_cours_periode_enseignant(events, "CHOLLET REMY", periode)
        assert sorted(resultat) == sorted(attendu), \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance4
class TestTraitement:
    FONCTION = "traitement"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet5)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet5)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        events = tools_tests.lecture_lignes_fichier_csv(datadir["data.csv"])
        res = projet5.traitement(events, "BARAS CLEO")
        assert isinstance(res, list), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list")
        assert isinstance(res[0], str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list de str")

    @pytest.mark.parametrize("prof", [
        "BARAS CLEO",
        "MARTIN JEROME",
        "KASPER KEVIN",
    ])
    def test_valeur_retour(self, datadir, prof):
        events = tools_tests.lecture_lignes_fichier_csv(datadir["data.csv"])
        attendu = tools_tests.lecture_lignes_fichier_csv(
            datadir[f"_expected/{prof.lower().replace(' ', '_')}.csv"])
        resultat = projet5.traitement(events, prof)
        assert sorted(resultat) == sorted(attendu), \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")
