import platform
import subprocess
import json
import sys
import time

lijst_url = []
lijst_ping = []
dictionary = {'lijst_url': lijst_url, 'lijst_ping': lijst_ping}

gelogde_lijst_url = []
gelogde_lijst_ping = []
gelogde_dictionary = {'gelogde_lijst_url': gelogde_lijst_url,
                      'gelogde_lijst_ping': gelogde_lijst_ping}


def myping(host):

    parameter = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)

    if response == 0:
        lijst_ping.append(True)
        lijst_url.append(host)
    else:
        lijst_ping.append(False)
        lijst_url.append(host)

    try:
        with open("url's.json", "w") as f:
            json.dump(dictionary, f)

    except FileNotFoundError:
        with open("url's.json", "w") as f:
            json.dump(dictionary, f)


def ping_elk_minuut(host):

    parameter = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)
    time.sleep(5)

    if response == 0:
        gelogde_lijst_ping.append(True)
        gelogde_lijst_url.append(host)
    else:
        gelogde_lijst_ping.append(False)
        gelogde_lijst_url.append(host)

    try:
        with open("url_gelogd.json", "w") as f:
            json.dump(gelogde_dictionary, f)

    except FileNotFoundError:
        with open("url_gelogd.json", "w") as f:
            json.dump(gelogde_dictionary, f)


def file_verwijderen():

    verwijderen = input("Welke check wil je verwijderen? (Geef de url)  ")
    try:
        with open("url's.json", "r") as f:
            try:
                inhoud = json.load(f)
                locatie = inhoud['lijst_url'].index(verwijderen)
                inhoud['lijst_url'].remove(verwijderen)
                inhoud['lijst_ping'].pop(locatie)

                dictionary["lijst_url"].remove(verwijderen)
                dictionary["lijst_ping"].pop(locatie)
            except:
                print(f"De url {verwijderen} zit niet in de check lijst!")

        with open("url's.json", "w") as f:
            json.dump(inhoud, f)

    except FileNotFoundError:
        print("Je moet eerst checks toevoegen om files te verwijderen!")


def oplijsten():

    with open("url's.json", "r") as f:
        inhoud = json.load(f)
        tussenlijst_ping = inhoud['lijst_ping']
        tussenlijst_url = inhoud['lijst_url']
        
        for i in tussenlijst_url:
            index = tussenlijst_url.index(i)
            ping = tussenlijst_ping[index]
            
            if ping == False:
                print(f"URL: {i}           Er is GEEN ping!")
            
            else:
                print(f"URL: {i}           Er is een ping.")
            
                
            
            


def keuze_generator():

    stoppen = True
    while stoppen:
        try:
            keuze = int(input(
                "Kies '1' om check aan te maken. '2' om check te verwijderen. '3' om op te lijsten. '4' om te checken, '0' om te verlaten.    "))
            if keuze == 1:
                website_url = input("Geef een url van een website:   ")
                print(myping(website_url))
            elif keuze == 2:
                file_verwijderen()
            elif keuze == 3:
                oplijsten()
            elif keuze == 4:
                with open("url's.json", "r") as f:
                    inhoud = json.load(f)
                    tussenlijst_ping = inhoud['lijst_ping']
                    tussenlijst_url = inhoud['lijst_url']
                    stop_de_loop = True

                    while stop_de_loop:
                        index = 0
                        if index == len(tussenlijst_url):
                            index = 0
                        else:
                            for i in tussenlijst_url:
                                ping_elk_minuut(i)
                                index = index + 1
                        antwoord = input(
                            "Druk op 'Q' om te stoppen of '0' om je scherm leeg te maken. Druk op een willekeurige toets om verder te gaan:     ")
                        if antwoord == "Q" or antwoord == "q":
                            stop_de_loop = False
                        if antwoord == "0":

                            with open("url_gelogd.json", "w") as f:
                                data = {"gelogde_lijst_url": [],
                                        "gelogde_lijst_ping": []}
                                json.dump(data, f)
                                stop_de_loop = False

            elif keuze == 0:
                with open("url_gelogd.json", "w") as f:
                    data = {"gelogde_lijst_url": [], "gelogde_lijst_ping": []}
                    json.dump(data, f)
                    stop_de_loop = False
                with open("url's.json", "w") as f:
                    data = {"lijst_url": [], "lijst_ping": []}
                    json.dump(data, f)
                    stop_de_loop = False
                break
            else:
                print("Dit is een ongeldige keuze!")
        except ValueError:
            print("Ongeldige selectie!")


def main():
    # Je zorgt ervoor dat je systeem ook op dezelfde manier bedienbaar via decommand-line interface. Je gebruikt hiervoor sys.argv
    keuze_generator()


if __name__ == "__main__":
    main()
