This project is a copy from the existing repository "cltrier_prosem" by Simon Münker (@smnmnkr) from Trier University.


Instruktionen:

1. Datensätze herunterladen
    - direct_cpd Terms: [Maske, Virus, Variante, Mutation, Querdenker]
    - indirect_cpd Terms: [Haus, Leben, Mensch, Tier, Urlaub]
    - non_cpd Terms: [!, bei, manche, schlafen, warum]

	- DSDS Coronakorpus (2018 - 2020, Format: voll, Anzahl: 5000, Sortierung: zufällig)
	- DWDS Webkorpus 1 (2018 - 2020, Format: voll, Anzahl: 5000, Sortierung: zufällig)
	- DWDS Webkorpus 2 (2010 - 2012, Format: voll, Anzahl: 5000, Sortierung: zufällig)


2. Datensätze mergen (erstmal Wort-weise)
    Beispiel: Maske,
    alle heruntergeladenen Daten von Maske (also aus corona, web 1 und web 2)
    in einer Tabelle zusammenfügen, bevor es ans vorprozessieren geht.
    Warum? Weil dann eine Gesamttabelle verfügbar ist, auf deren Basis die Indices für die
    Sätze erstellt werden.


3. Datensätze vorprozessieren
    - kein Tokenisieren mehr nötig
    - nur noch Wort im Satz suchen → Characterspan!
    - Tabellen Format: wie gehabt (Style im Jupiter Notebook hinterlegt)
        → am besten noch Zusatzspalte nur mit dem gesuchten Wort
        → nltk Spalte kann wie gesagt weg

4. Datensätze mit Simons preprocessor (notebook 1) in .parquet files umwandeln. 

5. Datensätze mit Simons Pipeline (notebook 2) klassifizieren.

