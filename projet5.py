# coding: UTF-8
"""
Script: SAE15/projet5
Création: nicoletv, le 08/11/2021
"""

# Imports
from tools_constantes import *
import tools_sae
from datetime import *
import matplotlib.pyplot as plt

# Fonctions

# Programme principal


def extract_events(ics: str):  # extract ics's events
    event_list = []
    temp = ics.split("BEGIN:VEVENT\n")  # split at the begin of the each event
    temp.pop(0)  # delete the header (START:VCALENDAR, version ect..)
    for event in temp:  # iteration of all event
        event_list.append(event.split("END:VEVENT")[
                              0])  # append the split END VEVENT[0] because we just want the event and we want to delete the end of the ics after the last event
    return event_list


def conversion_date(date: str):  # return date at format JJ-MM-AAAA
    return f"{date[6:8]}-{date[4:6]}-{date[0:4]}"  # slicing the string to take information we need


def conversion_heure(heure: str):  # return hour at format HH:MM
    return f"{heure[0:2]}:{heure[2:4]}"  # slicing the string to take information we need


def calcul_duree(heure_debut: str, heure_fin: str):
    heure_debut = heure_debut.replace(":", "")  # HH:MM -> HHMM
    heure_fin = heure_fin.replace(":", "")  # HH:MM -> HHMM
    minute = int(heure_fin[2:4]) - int(heure_debut[2:4])  # We do the difference to know the duration
    heure = int(heure_fin[0:2]) - int(heure_debut[0:2])
    if minute < 0:  # if the difference return a negative numbers
        minute = abs(minute)  # we do the absolute value
        heure -= 1  # Decrement the hour
    return f"{heure:02}:{minute:02}"  # return the duration at format HH:MM


def parse_event(ics: str):
    liste = ics.split("\n")  # split all lines
    dico = {}  # create a dictionnary
    if liste[
        -1] == '':  # delete the last item in list if it's equal to '' because when we split lines it may rest a last empty item
        liste.pop(-1)
    for chaine in liste:  # iterate each line
        items = chaine.split(":")  # separate ID and the value
        dico[items[0]] = items[1]  # create a key for each ID in the dict and assign the value associated
    date = conversion_date(dico["DTSTART"].split("T")[
                               0])  # use conversion_date() to have the date in the right format, we split the value because we just want the string before the "T"
    heure = conversion_heure(dico["DTSTART"].split("T")[
                                 1])  # use conversion_heure() to have the hour in the right format, we split the value because we just want the string after the "T"
    duree = calcul_duree(dico["DTSTART"].split("T")[1], dico["DTEND"].split("T")[
        1])  # we use compare_duree we split the start value and the end value to get hours
    summary = dico['SUMMARY'].split('-')  # we split summary
    if len(summary) == 1:  # if there is no "-" in summary we replace summary by ["Autre", ""]
        summary = ["Autre", ""]
    if not 'DESCRIPTION' in dico.keys():  # if there is no ID named description we create a key named description with an empty string value
        dico['DESCRIPTION'] = ''

    return f"{dico['UID']};{date};{heure};{duree};{dico['CATEGORIES'][:2]};{summary[0]};{summary[1]};{dico['SUMMARY']};{dico['LOCATION'].replace(',', '|')};{dico['DESCRIPTION'].replace(',', '|')};{dico['CATEGORIES'].replace(',', '|')}"
    # return f string with expected values separated by ";" and replace "," by ";" when it's necessary


def parse_fichier_ics(fichier_ics: str):
    ics = tools_sae.lecture_fichier(fichier_ics)  # read the ics file
    liste_event_ics = []  # create a list where parsed event will be stocked
    for event in extract_events(ics):  # for each event in ics
        liste_event_ics.append(parse_event(event))  # append parsed event in list_event
    return liste_event_ics  # return the list


def calcul_heure_fin(heure_debut: str, duree: str):  # calcule the end time
    h = int(heure_debut[0:2]) + int(duree[0:2])  # sum of start time and duration
    m = int(heure_debut[3:5]) + int(duree[3:5])
    if m >= 60:  # if the minute is greater than or equal to 60
        m = m % 60  # minutes modulo 60 because minutes can't be greater than 60
        h += 1  # increament hours
    return f"{h:02}:{m:02}"  # return with the right format


def nombre_minutes(heure: str):  # return the number of minutes from an hour
    return int(heure[0:2]) * 60 + int(heure[3:5])


def compare_dates(date1: str, date2: str):  # compare two dates
    liste = [(6, 10), (3, 5),
             (0, 2)]  # liste of tuple who contains start index and end index of year, month, day from a string
    for x, y in liste:  # iterate in the list x will take the start index value and y the end index value
        if not date1[x:y] == date2[x:y]:  # if years, months or days are not equal
            return (int(date1[x:y]) > int(date2[x:y])) - (
                    int(date1[x:y]) < int(date2[x:y]))  # return 1 if date1>date2 else return -1
    return 0  # return 0 if dates are the same


def date_dans_intervalle(date: str, debut: str, fin: str):  # return True if date in the interval
    return compare_dates(date, debut) != -1 and compare_dates(date, fin) <= 0  # use compare date


def traitement(events: list, enseignant: str):
    vacances = ['Toussaint', 'Noël', 'Hiver', 'Printemps', 'Ete']
    periods = [PERIODE1, PERIODE2, PERIODE3, PERIODE4, PERIODE5]  # list of period of each holidays
    event_period = []

    for i in range(4):  # for each holidays except summer
        event_period.append(";".join([vacances[i], choix_cours_enseignant(events, enseignant, periods[i], 1),
                                      # use choix_cours_enseignant() to select the last event before holidays and the last event after holidays
                                      choix_cours_enseignant(events, enseignant, periods[i + 1],
                                                             0)]))  # join the holiday's name with events and append it in event_period
    event_period.append(  # the same for summer without first event after holiday
        ";".join([vacances[4], choix_cours_enseignant(events, enseignant, periods[4], 1),
                  f"-;{DEBUT_ANNEE_2022};-"]))  # we use tools.constante.DEBUT_ANNEE_2022 to obtain the date after summer
    for i in range(len(event_period)):  # for each period
        split = event_period[i].split(";")  # split events
        if split[2] != "-" and split[-2] != "-":  # if the date of classes different than "-"
            split.append(calcul_nombre_jour(split[2], split[
                -2]))  # calcul_nombre_jour() calculates the number of days between two dates
        else:
            split.append("-")  # if there is no date append "-"
        event_period[i] = f"{split[0]};{split[1]};{split[2]};{split[3]};{split[-1]}"
    return event_period


def calcul_nombre_jour(date0, date1):  # we use the module datetime
    day0, month0, year0 = date0.split("-")  # split the date to extract the day, the month and the year values
    day1, month1, year1 = date1.split("-")
    delta = date(int(year1), int(month1), int(day1)) - date(int(year0), int(month0),
                                                            int(day0))  # it calculates the difference (delta) between two dates
    return str(delta.days - 1)  # return the number of day with the method .days()


def choix_cours_enseignant(events: list, enseignant: str, periode: list,
                           last: int):  # select the first or the last event
    return recherche_cours_periode_enseignant(events, enseignant, periode)[last]


def recherche_cours_periode_enseignant(events: list, enseignant: str, periode: list):
    prof_event = []
    for event in events:  # keep events where the teacher participate
        if enseignant in event.split(";")[-2]:
            prof_event.append(event)

    event_period = []
    for event in prof_event:  # keep event in the right period
        if date_dans_intervalle(event.split(";")[1], periode[0], periode[1]):
            event_period.append(event)

    event_final = recherche_cours_periode(
        event_period)  # recherche_cours_periode() sort events to keep only the first and the last event
    if event_final == [[], []]:  # if there is no event in the period return a list without events
        return [f"-;-", f"-;-"]

    cours0 = event_final[0][0].split(";")  # split first event
    cours1 = event_final[1][0].split(";")  # split last event
    return [f"{cours0[7]};{cours0[1]};{cours0[2]}",
            f"{cours1[7]};{cours1[1]};{cours1[2]}"]  # return a list with the name, the date and the hour of events


def recherche_cours_periode(events: list):
    event_final = [events, [event for event in events]]  # we do a list comprehension to make a deepcopy
    for i in [0, 1]:  # loop two times for the first and last event in the period  if we want the first i=0 else i=1
        while len(event_final[i]) > 1:  # while there is two events or more
            date_event0 = event_final[i][0].split(";")  # split two event to compare them
            date_event1 = event_final[i][1].split(";")
            if compare_dates(date_event0[1], date_event1[1]) == 1:  # if the first date is bigger
                event_final[i].pop(
                    i)  # pop the first event of the list if we want the first event of the period if we want the last pop second event
            elif compare_dates(date_event0[1], date_event1[1]) == -1:  # if the second date is bigger
                event_final[i].pop(
                    1 - i)  # pop the second event of the list if we want the first event of the period if we want the las pop first event
            else:  # if dates are the same we compare hours
                if i:  # if we want the last
                    event_final[i].pop(
                        int(date_event0[2][:2]) > int(date_event1[2][:2]))  # delete the event who have the smaller hour
                else:
                    event_final[i].pop(
                        int(date_event0[2][:2]) < int(date_event1[2][:2]))  # delete the event who have the biggest hour
    return event_final  # return [first event, last event]


def export_markdown(resultats: list):
    ch = "|Vacances (date au soir)|Date du dernier cours|Heure|Intitulé|Nombre de jours de vacances\n|:---|:---|:---|:---|:---\n"  # create and format columns
    for event in resultats:  # for each period
        for element in event.split(";"):  # concatenate element in the right column
            ch += f"|{element}"
        ch += ".00\n"  # add \n at the end
    print(ch)  # print mardown
    fichier = open("export_markdown.md", "w")  # export markdown in export_markdown.md
    fichier.write(ch)
    fichier.close()


def export_png(resultats: list):
    colonnes_labels = ["Vacances (date au soir)", "Date du dernier cours", "Heure", "Intitulé",
                       "Nombre de jours de vacances"]
    data = []
    for event in resultats:
        event += ".00"
        data.append(event.split(";"))
    plt.axis("off")
    table = plt.table(cellText=data, colLabels=colonnes_labels, loc="center", cellLoc='center')

    plt.savefig("projet5.png", dpi=1200)


def main():
    chemin = tools_sae.lecture_fichier("tests/data/data.csv").split("\n")
    chemin.pop()
    export_png(traitement(chemin, "KASPER KEVIN"))
    pass


if __name__ == '__main__':
    main()
# Fin
