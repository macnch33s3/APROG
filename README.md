# APROG - Angewandte Programmierung (Wirtschaftsingenieurwesen OST)
## Modul-Informationen

- **Modulname:** Angewandte Programmierung (APROG)  
- **Hochschule:** Ostschweizer Fachhochschule (OST)  
- **Autoren PROJECT:** macnch33s3 & Riccardo8645

## Verzeichnisstruktur
Dieses APROG-Projektverzeichnis hat folgende wichtigen Inhalte:
- Verzeichnisse **SW-01, SW-02, ...:** Skripte.
- Verzeichnis **PROJECT:** In diesem Verzeichnis konnte unser eigenes Projekt erstellt und bearbeitet werden.
- Datei **main.py:** Demo-Datei für micro:bit aus VSCode (Details siehe 'APROG0_0_Installation_Python.pdf')
- Datei **sinusplot.py:** Demo-Datei zum Testen der Python-Programmierung aus VSCode (Details siehe 'APROG0_0_Installation_Python.pdf')
- Datei **README.md:**
- Datei **pyproject.toml:** Verwaltung libraries

**Voraussetzungen**
-----
- Git installiert
- Python (empfohlen: 3.13.1)

**Repo klonen**
-----
1. Repository klonen:
```bash
git clone https://github.com/macnch33s3/APROG.git
```
2. In das Projektverzeichnis wechseln:
```bash
cd APROG
```
3. In ../APROG/tree/main/PROJECT/api_bridge.ipynb finden:
```bash
cd ../APROG/tree/main/PROJECT/
```
4. Falls nötig module installieren mit pip oder uv
```bash
pip install pandas
pip install requests
pip install io
pip install matplotlib
pip install seaborn
```
```bash
uv init
uv add pandas
uv add requests
uv add io
uv add matplotlib
uv add seaborn
uv sync
```

**Daten**
-----
- Daten die benötigt werden sind: 
  - api_daten von https://daten.sg.ch/api/explore/v2.1/catalog/datasets/ladestationen-fur-elektroautos-im-kanton-stgallen/exports/csv
  - installierte module initialisiert

**Fehlerbehebung (Troubleshooting)**
-------------------------------
- Fehlende Abhängigkeit: `pip install <paket>`
- ImportError: Überprüfen, ob die virtuelle Umgebung aktiviert ist und ob der PYTHONPATH korrekt ist.
- Datenproblem: Dateipfade kontrollieren, Dateinamen und Zugriffsrechte.
- Bei Problemen: Ausgabe und Traceback kopieren und ein Issue im Repository öffnen.

**Lizenz & Kontakt**
----------------
- Lizenz: MIT
- (Alle files die der Hochschule gehören wurden aus Lizenzgründen nicht veröffentlicht.)
- Bei Fragen: @macnch33s3 oder ein Issue im Repo öffnen.
