# getränkeautomat (boss-version): mehrere käufe mit guthaben und rückgeld-ausgabe aufgabe 2 von schule 

import time

getränke = {
    "1": {"name": "wasser", "preis": 1.00},
    "2": {"name": "saft", "preis": 1.75},
    "3": {"name": "limo", "preis": 2.30}
}

akzeptierte_geldbeträge = [20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.20, 0.10, 0.05]

# funktion zur rückgeldberechnung
def rückgeld_berechnen(betrag):
    rückgeld = {}
    cent_betrag = int(round(betrag * 100))
    for münze in [2000, 1000, 500, 200, 100, 50, 20, 10, 5]:
        anzahl = cent_betrag // münze
        if anzahl > 0:
            rückgeld[münze] = anzahl
            cent_betrag -= anzahl * münze
    return rückgeld

# hauptfunktion boss automat
def getränkeautomat_boss():
    while True:   # endlosschleife: automat startet immer neu
        print("willkommen beim getränkeautomaten (boss-version)!")
        print("folgende getränke stehen zur auswahl:")

        for nummer, info in getränke.items():
            print(f"{nummer}: {info['name']} - {info['preis']:.2f} €")

        print("\nbitte betrag einwerfen --> bis max. 20€ pro einwurf")
        guthaben = 0.0

        # startguthaben einzahlen
        while True:
            try:
                geld = float(input("geld einwerfen (oder 0 für kauf starten): "))
                if geld == 0:
                    break
                if geld in akzeptierte_geldbeträge:
                    guthaben += geld
                    print(f"aktuelles guthaben: {guthaben:.2f} €")
                else:
                    print("beitrag wird nicht angenommen.")
            except ValueError:
                print("ungültige eingabe. gültigen betrag eingeben.")

        # solang noch guthaben da ist kann gekauft werden 
        while guthaben >= min(getränk["preis"] for getränk in getränke.values()):
            print(f"\nihr aktuelles guthaben: {guthaben:.2f} €")
            for nummer, info in getränke.items():
                print(f"{nummer}: {info['name']} - {info['preis']:.2f} €")

            wahl = input("getränkenummer auswählen (oder x zum beenden): ").strip().lower()

            if wahl == "x":
                break  

            if wahl in getränke:
                preis = getränke[wahl]["preis"]
                name = getränke[wahl]["name"]

                if guthaben >= preis:
                    guthaben -= preis
                    print(f"\nhier ist dein {name}. gönn dir")
                else:
                    print("nicht genug moneten dafür.")
            else:
                print("ungültige auswahl.")

        # rückgeld am ende ausgeben
        if guthaben > 0:
            print(f"\nrückgeld: {guthaben:.2f} €")
            rückgeld_stücke = rückgeld_berechnen(guthaben)
            print("rückgeld stückelung:")
            for münze, anzahl in rückgeld_stücke.items():
                print(f"{anzahl} × {münze/100:.2f} €")

        print("\ndanke malaga!")


# automaten-programm starten
getränkeautomat_boss()
