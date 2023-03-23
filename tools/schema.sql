BEGIN TRANSACTION;

DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "Person" (
	"Sozialversicherungsnummer"	INTEGER,
	"Vorname"	TEXT,
	"Nachname"	TEXT,
	"Postleitzahl"	INTEGER,
	"Ort"	TEXT,
	"Straße"	TEXT,
	"Hausnummer"	INTEGER,
	"Telefonnummer"	INTEGER,
	PRIMARY KEY("Sozialversicherungsnummer")
);
CREATE TABLE IF NOT EXISTS "Passagier" (
	"Passagiernummer"	INTEGER,
	"Sozialversicherungsnummer"	INTEGER NOT NULL,
	PRIMARY KEY("Passagiernummer"),
	FOREIGN KEY("Sozialversicherungsnummer") REFERENCES "Person"("Sozialversicherungsnummer")
);
CREATE TABLE IF NOT EXISTS "Angestellter" (
	"Angestelltennummer"	INTEGER,
	"Sozialversicherungsnummer"	INTEGER NOT NULL,
	PRIMARY KEY("Angestelltennummer"),
	FOREIGN KEY("Sozialversicherungsnummer") REFERENCES "Person"("Sozialversicherungsnummer")
);
CREATE TABLE IF NOT EXISTS "Gehaltskonto" (
	"Kontonummer"	INTEGER,
	"Bankleitzahl"	INTEGER NOT NULL,
	"Konstostand"	INTEGER,
	"Bankname"	TEXT,
	"Angestelltennummer"	INTEGER UNIQUE,
	FOREIGN KEY("Bankleitzahl") REFERENCES "Bank"("Bankleitzahl"),
	PRIMARY KEY("Angestelltennummer","Kontonummer")
);
CREATE TABLE IF NOT EXISTS "Passage" (
	"Passagennummer"	INTEGER,
	"Abfahrtshafen"	TEXT,
	"Zielhafen"	TEXT,
	"Abfahrtszeit"	TIME,
	"Ankunftszeit"	TIME,
	PRIMARY KEY("Passagennummer")
);
CREATE TABLE IF NOT EXISTS "Anschlusspassage" (
	"Passagennummer 1"	INTEGER,
	"Passagennummer 2"	INTEGER,
	PRIMARY KEY("Passagennummer 1","Passagennummer 2")
);
CREATE TABLE IF NOT EXISTS "Schifftyp" (
	"Typennummer"	INTEGER,
	"Bruttoregistertonnen"	NUMERIC,
	"Besatzungsstärke"	INTEGER,
	"Typenbezeichnung"	TEXT,
	"Name"	TEXT,
	PRIMARY KEY("Typennummer"),
	FOREIGN KEY("Name") REFERENCES "Hersteller"("Name")
);
CREATE TABLE IF NOT EXISTS "Buchung" (
	"Buchungsnummer"	INTEGER,
	"Passagennummer"	INTEGER,
	"Passagiernummer"	INTEGER NOT NULL,
	"Buchungsdatum"	DATE,
	"Klasse"	TEXT,
	FOREIGN KEY("Passagiernummer") REFERENCES "Passagier"("Passagiernummer"),
	FOREIGN KEY("Passagennummer") REFERENCES "Passage"("Passagennummer"),
	PRIMARY KEY("Buchungsnummer")
);
CREATE TABLE IF NOT EXISTS "Schiff" (
	"Inventarnummer"	INTEGER,
	"Typennummer"	INTEGER,
	"Jahr der Fertigung"	INTEGER,
	"Seemeilen"	NUMERIC,
	FOREIGN KEY("Typennummer") REFERENCES "Schifftyp"("Typennummer"),
	PRIMARY KEY("Inventarnummer")
);
CREATE TABLE IF NOT EXISTS "Kapitän" (
	"Kapitänspatentnummer"	INTEGER,
	"Angestelltennummer"	INTEGER NOT NULL,
	"Seemeilen"	NUMERIC,
	PRIMARY KEY("Kapitänspatentnummer"),
	FOREIGN KEY("Angestelltennummer") REFERENCES "Angestellter"("Angestelltennummer")
);
CREATE TABLE IF NOT EXISTS "Logbuch" (
	"Code"	INTEGER,
	"Inventarnummer"	INTEGER UNIQUE,
	"Angestelltennummer"	INTEGER,
	FOREIGN KEY("Inventarnummer") REFERENCES "Schiff"("Inventarnummer"),
	FOREIGN KEY("Angestelltennummer") REFERENCES "Angestellter"("Angestelltennummer"),
	PRIMARY KEY("Code")
);
CREATE TABLE IF NOT EXISTS "Telefonnummer" (
	"Telefonnummer"	INTEGER,
	"Sozialversicherungsnummer"	INTEGER,
	FOREIGN KEY("Sozialversicherungsnummer") REFERENCES "Person"("Sozialversicherungsnummer"),
	PRIMARY KEY("Telefonnummer")
);
CREATE TABLE IF NOT EXISTS "Bank" (
	"Bankleitzahl"	INTEGER,
	"Bankname"	TEXT,
	PRIMARY KEY("Bankleitzahl")
);
CREATE TABLE IF NOT EXISTS "Hersteller" (
	"Name"	TEXT,
	PRIMARY KEY("Name")
);
CREATE TABLE IF NOT EXISTS "Techniker" (
	"Lizenznummer"	INTEGER,
	"Angestelltennummer"	INTEGER NOT NULL,
	"Grad der Ausbildung"	TEXT,
	"Typennummer"	INTEGER NOT NULL,
	PRIMARY KEY("Lizenznummer","Angestelltennummer"),
	FOREIGN KEY("Angestelltennummer") REFERENCES "Angestellter"("Angestelltennummer"),
	FOREIGN KEY("Typennummer") REFERENCES "Schifftyp"("Typennummer")
);
CREATE TABLE IF NOT EXISTS "Kapitän_Passage" (
	"Kapitänspatentnummer"	INTEGER,
	"Passagennummer"	INTEGER,
	"Typennummer"	INTEGER,
	FOREIGN KEY("Typennummer") REFERENCES "Schiff"("Typennummer"),
	FOREIGN KEY("Passagennummer") REFERENCES "Passage"("Passagennummer"),
	PRIMARY KEY("Kapitänspatentnummer","Passagennummer"),
	FOREIGN KEY("Kapitänspatentnummer") REFERENCES "Kapitän"("Kapitänspatentnummer")
);
COMMIT;
