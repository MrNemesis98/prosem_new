1. Datensätze herunterladen
	- Terms: Maske, Virus, Variante, Mutation, Querdenker
	- DSDS Coronakorpus (2018 - 2020, Format: voll, Anzahl: 5000, Sortierung: zufällig)
	- DWDS Webkorpus  1  (2018 - 2020, Format: voll, Anzahl: 5000, Sortierung: zufällig)
	- DWDS Webkorpus  2  (2010 - 2012, Format: voll, Anzahl: 5000, Sortierung: zufällig)
	
	Menge: min. 200 pro Wort, sodass bei 5 Terms insgesamt 1000 Daten vorliegen.
		-> Größe test data set ca. 80


2. Daten vorbereiten
	- Daten können im .csv Format vorliegen
	- Vorlage für Formatierung: ./notebooks/1.1-Single-Span--Data-Processing.ipynb
		- span steht für den gesuchten / relevanten Begriff
		- single-span: nur ein Begriff
		- dual-span: mehrere Begriffe
		- im Format gibt die Span Spalte den Index des Begriffs an, beginnend bei 0!
			- Angabe: Position [von (inlusive), bis (exklusive)]
			- Beispiel: "Beide erhoben sich, Viren am schnellsten, un..."
					span: [4, 5] bezieht sich auf "Viren"
			- Tokenizing nach Standard NLTK Tokenizer (hauptsächlich Leerzeichen)
	- am besten eigenen Ordner unter ./data/single_span erstellen und Daten da ablegen
	
	Automatische Datenvorbereitung mihilfe des Programms "data_preprocessor.py"
	unter data/single_span/time_classification/tp. 
	-> Daten werden automatisch in richtiges Format übertragen, Spans werden automatisch erstellt.
	-> Manuell muss "idx" in Spalte 1, Zeile 1 entfernt werden (in Zeile 2 kann es stehen bleiben.)
		-> Zusätzlich nach "[]" suchen, gegebenenfalls mithilfe der NLTK Spalte nach dem Fehler
		   suchen und Suchbegriffsliste ergänzen.

    Automatische Datensatzkontrolle mithilfe des Programms "data_consistor.py"
    unter data/single_span/time_classification/tp.
    -> Datensatz wird automtisch überprüft auf Existenz eines validen Wertes in der Span-Spalte
    -> zeigt alle Zeilen an, die diesbezüglich einen Fehler enthalten
    -> bei Bedarf korrigiert das Programm die betreffenden Zeilen im Sinne von Löschen
        (steuerbar über Variable "make_corrections" der "scan_for_errors"-Funktion)


3. Setup Datei anpassen
	- Ort: ./time_classification/subword_first/setup.toml oder ./time_classification/subword_mean/setup.toml
	- Pfad zu den Daten einstellen
	- label_classes einstellen
	- eventuell trainer variablen einstellen

4. Makefile anpassen
	- debug_classification_single_span: eventuell pfad anpassen. Sonst werden die Ergebnisse von
	  Kugler überschrieben
	- das @ statement kopieren und in Kommandozeile ausführen


-------------------------------------------------------------------------------------------
Neue Instruktionen nach Pipeline Update

1. Datensätze herunterladen
    - direct_cpd Terms: [Maske, Virus, Variante, Mutation, Querdenker]
    - indirect_cpd Terms: [Haus, Leben, Mensch, Tier, Urlaub]
    - non_cpd Terms: [!, bei, manche, schlafen, warum]

	- DSDS Coronakorpus (2018 - 2020, Format: voll, Anzahl: 5000, Sortierung: zufällig)
	- DWDS Webkorpus 1 (2018 - 2020, Format: voll, Anzahl: 5000, Sortierung: zufällig)
	- DWDS Webkorpus 2 (2010 - 2012, Format: voll, Anzahl: 5000, Sortierung: zufällig)

	Menge: min. 5000 pro Wort, sodass bei 5 Terms insgesamt 25000 Roh-Daten vorliegen.


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


4. Datensätze mit Simons Notebook zusammenfügen

