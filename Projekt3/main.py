"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Lech Gajdzica
email: lech.gajdzica@gmail.com
"""

import sys
from requests import get
from bs4 import BeautifulSoup as bs
import csv
from typing import Tuple, List

def ziskat_argumenty() -> Tuple[str, str]:
    """
    Získá argumenty z příkazového řádku.
    Vrací odkaz na stránku a název výstupního CSV souboru.
    """
    if len(sys.argv) < 3:
        print("Použiti: python main.py <odkaz> <nazev_souboru.csv>")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

def parsovani_odkazu(odkaz: str) -> bs:
    """
    Stáhne HTML stránku ze zadaného odkazu a převede ji na objekt BeautifulSoup.
    """
    return bs(get(odkaz).text, "html.parser")

def najdi_odkaz_obec(soup: bs) -> Tuple[List[str], List[str]]:
    """
    Najde a vrátí seznam kódů a názvů obcí z tabulek na hlavní stránce.
    """
    tabulky = soup.find_all("table", {"class": "table"})
    
    if len(tabulky) < 2:
        print("Chyba: Nebyly nalezeny tabulky se seznamem obcí.")
        return [], []

    obec_cislo, obec_nazev = [], []

    for tabulka in tabulky[0:]:
        obce_list = tabulka.find_all("tr")[2:]
        
        for obec in obce_list:
            tds = obec.find_all("td")
            if len(tds) > 1:
                obec_cislo.append(tds[0].text.strip())
                obec_nazev.append(tds[1].text.strip())

    return obec_cislo, obec_nazev

def ziskat_data_obce(odkaz: str) -> Tuple[str, str, str, List[Tuple[str, str]]]:
    """
    Získá podrobné volební údaje pro konkrétní obec.
    Vrací počet registrovaných voličů, vydaných obálek, platných hlasů a seznam hlasů pro jednotlivé strany.
    """
    soup = parsovani_odkazu(odkaz)
    html_list = soup.find_all("table", {"class": "table"})
    obec_data = []
    volici, obalky, platne_hlasy = "0", "0", "0"
    if len(html_list) > 1:
        statistika = html_list[0].find_all("td", {"data-rel": "L1"})
        
        if len(statistika) >= 3:
            volici, obalky, platne_hlasy = [td.get_text(strip=True).replace('\xa0', '') for td in statistika[:3]]
        for table in html_list[1:]:
            for tr in table.find_all("tr")[1:]:
                tds = tr.find_all("td")
                if len(tds) >= 3:
                    strana = tds[1].get_text(strip=True)
                    hlasy = tds[2].get_text(strip=True).replace('\xa0', '')
                    if strana != "-" and hlasy != "-":
                        obec_data.append((strana, hlasy))
    return volici, obalky, platne_hlasy, obec_data

def main() -> None:
    """
    Hlavní funkce programu:
    1. Získá argumenty (odkaz a výstupní soubor).
    2. Stáhne a zpracuje seznam obcí.
    3. Vytvoří odkazy na podrobnosti pro každou obec.
    4. Získá volební data a uloží je do CSV souboru.
    """
    odkaz, nazev_souboru = ziskat_argumenty()
    soup = parsovani_odkazu(odkaz)
    obec_cislo, obec_nazev = najdi_odkaz_obec(soup)
    kraj_cislo, kraj_znaceni = odkaz[-4:], odkaz[-16:-14]
    obec_odkaz_list = [
        f"https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj={kraj_znaceni}&xobec={i}&xvyber={kraj_cislo}"
        for i in obec_cislo
    ]
    
    vysledky = [ziskat_data_obce(url) for url in obec_odkaz_list]
    vsechny_strany = list(dict.fromkeys(strana for _, _, _, obec in vysledky for strana, _ in obec))
    hlavicka = ["code", "location", "registered", "envelopes", "valid"] + vsechny_strany
    with open(nazev_souboru, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(hlavicka)
        for i in range(min(len(obec_cislo), len(obec_nazev), len(vysledky))):
            volici, obalky, platne_hlasy, obec_data = vysledky[i]
            vysledky_dict = {strana: hlasy for strana, hlasy in obec_data}
            radek = [obec_cislo[i], obec_nazev[i], volici, obalky, platne_hlasy]
            radek.extend([vysledky_dict.get(strana, "0") for strana in vsechny_strany])
            writer.writerow(radek)

if __name__ == "__main__":
    main()
