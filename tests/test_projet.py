import importlib
import inspect
import os
import sys

import mock
import pytest

import tools_introspection
import tools_tests


def import_projet():
    try:
        import projetX as projet
        MODULE = "projetX"
    except:
        sys.path.insert(0, os.path.abspath('.'))
        projet = None
        for i in range(1, 30):
            try:
                projet = importlib.import_module(f"projet{i}")
                MODULE = f"projet{i}"
                return projet, MODULE
            except:
                pass
    return projet, MODULE


projet, MODULE = import_projet()


# ************************************************************************************************
class TestStructure:

    def test_import_module(self):

        try:
            projet, MODULE = import_projet()
            print(projet)
        except:
            message = "Votre projet n'a pas pu être importé pour les tests\n" \
                      "➔ Vérifiez l'orthographe du nom du script ou sa place dans l'arborescence...\n" \
                      "➔ Vérifiez que votre code n'a pas d'erreurs syntaxiques (vaguettes rouges)"
            assert False, tools_tests.affiche_message_erreur(message)

    # ---
    def test_declaration_main(self):
        FONCTION = "main"
        message = "Le programme principal {}.{} doit être déclaré".format(MODULE, FONCTION)
        liste = inspect.getmembers(projet)
        assert FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)


@pytest.mark.echeance1
class TestConversionDate:
    FONCTION = "conversion_date"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self):
        res = projet.conversion_date("20211016")
        assert isinstance(res, str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type str")

    @pytest.mark.parametrize("date, attendu", [
        pytest.param("20211016", "16-10-2021"),
        pytest.param("20220101", "01-01-2022"),
    ])
    def test_valeur_retour(self, date, attendu):
        resultat = projet.conversion_date(date)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance1
class TestConversionHeure:
    FONCTION = "conversion_heure"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self):
        res = projet.conversion_heure("173000")
        assert isinstance(res, str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type str")

    @pytest.mark.parametrize("heure, attendu", [
        pytest.param("173000", "17:30"),
        pytest.param("012500", "01:25"),
    ])
    def test_valeur_retour(self, heure, attendu):
        resultat = projet.conversion_heure(heure)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance1
class TestCalculDuree:
    FONCTION = "calcul_duree"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self):
        res = projet.calcul_duree("17:30", "18:00")
        assert isinstance(res, str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type str")

    @pytest.mark.parametrize("heure_debut, heure_fin, duree", [
        pytest.param("15:30", "17:30", "02:00"),
        pytest.param("08:30", "12:00", "03:30"),
        pytest.param("08:00", "09:00", "01:00"),
        pytest.param("15:30", "16:00", "00:30"),
    ])
    def test_valeur_retour(self, heure_debut, heure_fin, duree):
        resultat = projet.calcul_duree(heure_debut, heure_fin)
        assert resultat == duree, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance3
class TestCalculHeureFin:
    FONCTION = "calcul_heure_fin"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self):
        res = projet.calcul_heure_fin("17:30:00", "18:00:00")
        assert isinstance(res, str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type str")

    @pytest.mark.parametrize("heure_debut, duree, heure_fin", [
        pytest.param("15:30", "02:00", "17:30"),
        pytest.param("08:30", "03:30", "12:00"),
        pytest.param("08:00", "01:00", "09:00"),
        pytest.param("15:30", "00:30", "16:00"),
    ])
    def test_valeur_retour(self, heure_debut, duree, heure_fin):
        resultat = projet.calcul_heure_fin(heure_debut, duree)
        assert resultat == heure_fin, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance3
class TestNombreMinutes:
    FONCTION = "nombre_minutes"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self):
        res = projet.nombre_minutes("17:30")
        assert isinstance(res, int), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type int")

    @pytest.mark.parametrize("heure, nb_minutes", [
        pytest.param("00:30", 30),
        pytest.param("01:00", 60),
        pytest.param("01:05", 65),
        pytest.param("02:30", 150),
    ])
    def test_valeur_retour(self, heure, nb_minutes):
        resultat = projet.nombre_minutes(heure)
        assert resultat == nb_minutes, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance3
class TestCompareDates:
    FONCTION = "compare_dates"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self):
        res = projet.compare_dates("01-01-2021", "02-01-2021")
        assert isinstance(res, int), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type int")

    @pytest.mark.parametrize("date1, date2, attendu", [
        pytest.param("01-01-2021", "01-01-2021", 0),
        pytest.param("01-01-2021", "01-01-2022", -1),
        pytest.param("01-01-2022", "01-01-2021", 1),
        pytest.param("01-01-2021", "01-02-2021", -1),
        pytest.param("01-02-2021", "01-01-2021", 1),
        pytest.param("01-01-2021", "10-01-2021", -1),
        pytest.param("10-01-2021", "01-01-2021", 1),
    ])
    def test_valeur_retour(self, date1, date2, attendu):
        resultat = projet.compare_dates(date1, date2)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance3
class TestDateDansIntervalle:
    FONCTION = "date_dans_intervalle"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 3)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 3, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        res = projet.date_dans_intervalle("15-01-2021", "01-01-2021", "21-01-2021")
        assert isinstance(res, bool), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type bool")

    @pytest.mark.parametrize("date, resultat", [
        pytest.param("15-01-2021", True),
        pytest.param("15-12-2020", False),
        pytest.param("10-02-2021", False),
        pytest.param("15-01-2022", False)
    ])
    def test_valeur_retour(self, date, resultat):
        actual = projet.date_dans_intervalle(date, "01-01-2021", "31-01-2021")
        assert actual == resultat, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")

    def test_appel_compare_date(self):
        with mock.patch(f"{MODULE}.compare_dates", return_value=1) as mocked:
            projet.date_dans_intervalle("15-01-2021", "01-01-2021", "21-01-2021")
            mocked.assert_called()


@pytest.mark.echeance1
class TestExtractEvents:
    FONCTION = "extract_events"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        event = datadir["exemple1.ics"].read_text(encoding="utf8")
        res = projet.extract_events(event)
        assert isinstance(res, list), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list")
        assert isinstance(res[0], str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list de str")

    @pytest.mark.parametrize("fichier_events", [
        pytest.param("exemple1"),
        pytest.param("exemple2"),
    ])
    def test_valeur_retour(self, fichier_events, datadir):
        event = datadir[f"{fichier_events}.ics"].read_text(encoding="utf8")
        actual = projet.extract_events(event)
        expected = tools_tests.lecture_fichier_yaml(datadir[f"_expected/{fichier_events}.yaml"])
        assert actual == expected, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance2
class TestParseEvent:
    FONCTION = "parse_event"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        event = tools_tests.lecture_fichier(datadir["deuxprofs.txt"])
        res = projet.parse_event(event)
        assert isinstance(res, str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type str")

    @pytest.mark.parametrize("fichier_event", [
        pytest.param("deuxprofs"),
        pytest.param("troisprofs-deuxsalles"),
        pytest.param("deuxgroupes"),
        pytest.param("reunionrentreeufa"),
        pytest.param("ds-partieltp-eln"),
        pytest.param("ds-infrasec"),
        pytest.param("ds-eln"),
    ])
    @pytest.mark.parse_event_v1
    def test_valeur_retour(self, fichier_event, datadir):
        event = tools_tests.lecture_fichier(datadir[f"{fichier_event}.txt"])
        actual = projet.parse_event(event)
        expected = tools_tests.lecture_fichier(datadir[f"_expected/{fichier_event}.txt"])
        assert actual == expected, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")

    @pytest.mark.parametrize("fichier_event", [
        pytest.param("deuxprofs"),
        pytest.param("troisprofs-deuxsalles"),
        pytest.param("deuxgroupes"),
        pytest.param("reunionrentreeufa"),
        pytest.param("ds-partieltp-eln"),
        pytest.param("ds-infrasec"),
        pytest.param("ds-eln"),
    ])
    @pytest.mark.parse_event_v2
    def test_valeur_retour_v2(self, fichier_event, datadir):
        event = tools_tests.lecture_fichier(datadir[f"{fichier_event}.txt"])
        actual = projet.parse_event(event)
        expected = tools_tests.lecture_fichier(datadir[f"_expected/v2/{fichier_event}.csv"])
        assert actual == expected, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance2
class TestParseFichierIcs:
    FONCTION = "parse_fichier_ics"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        chemin = str(datadir["exemple1.ics"])
        res = projet.parse_fichier_ics(chemin)
        assert isinstance(res, list), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list")
        assert isinstance(res[0], str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list de str")

    @pytest.mark.parametrize("fichier_events", [
        pytest.param("exemple1"),
        pytest.param("exemple2"),
    ])
    @pytest.mark.parse_event_v1
    def test_valeur_retour(self, fichier_events, datadir):
        chemin = str(datadir[f"{fichier_events}.ics"])
        actual = projet.parse_fichier_ics(chemin)
        expected = tools_tests.lecture_fichier_yaml(datadir[f"_expected/{fichier_events}.yaml"])
        assert actual == expected, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")

    @pytest.mark.parametrize("fichier_events", [
        pytest.param("exemple1"),
        pytest.param("exemple2"),
    ])
    @pytest.mark.parse_event_v2
    def test_valeur_retour_v2(self, fichier_events, datadir):
        chemin = str(datadir[f"{fichier_events}.ics"])
        actual = projet.parse_fichier_ics(chemin)
        expected = tools_tests.lecture_fichier_yaml(datadir[f"_expected/v2/{fichier_events}.yaml"])
        assert actual == expected, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance5
class TestExportMarkdown:
    FONCTION = "export_markdown"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)
