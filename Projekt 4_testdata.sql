INSERT INTO "Person" ("Sozialversicherungsnummer", "Vorname", "Nachname", "Postleitzahl", "Ort", "Straße", "Hausnummer", "Telefonnummer") VALUES
(123456789, 'Anna', 'Müller', 10115, 'Berlin', 'Musterstraße', 1, 1234567),
(234567890, 'Max', 'Schmidt', 80331, 'München', 'Hauptstraße', 15, 2345678),
(345678901, 'Maria', 'Gonzalez', 10179, 'Berlin', 'Friedrichstraße', 25, 3456789),
(456789012, 'John', 'Doe', 10117, 'Berlin', 'Unter den Linden', 7, 4567890),
(567890123, 'Laura', 'Lee', 60311, 'Frankfurt', 'Kaiserstraße', 10, 5678901);

INSERT INTO "Passagier" ("Passagiernummer", "Sozialversicherungsnummer")
VALUES
    (1, 123456789),
    (2, 234567890),
    (3, 345678901),
    (4, 456789012),
    (5, 567890123);

INSERT INTO Angestellter (Angestelltennummer, Sozialversicherungsnummer)
VALUES (1, 123456789),
       (2, 234567890),
       (3, 345678901),
       (4, 456789012),
       (5, 567890123);
       
INSERT INTO Gehaltskonto (Kontonummer, Bankleitzahl, Konstostand, Bankname, Angestelltennummer)
VALUES 
    (123456, 10020030, 5000, 'Deutsche Bank', 1),
    (789012, 21045001, 10000, 'Commerzbank', 2),
    (345678, 43071016, 15000, 'Postbank', 3),
    (901234, 70080000, 20000, 'HypoVereinsbank', 4),
    (567890, 30020900, 25000, 'ING-DiBa', 5);
    
INSERT INTO Passage (Passagennummer, Abfahrtshafen, Zielhafen, Abfahrtszeit, Ankunftszeit)
VALUES (1, 'New York', 'London', '12:30:00', '09:45:00'),
       (2, 'Paris', 'Tokyo', '16:15:00', '06:00:00'),
       (3, 'Sydney', 'San Francisco', '08:00:00', '18:30:00'),
       (4, 'Los Angeles', 'Rio de Janeiro', '22:00:00', '07:30:00'),
       (5, 'Shanghai', 'Dubai', '19:45:00', '06:15:00');
       
       
INSERT INTO Anschlusspassage ("Passagennummer 1", "Passagennummer 2")
VALUES
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 1);


INSERT INTO Schifftyp (Typennummer, Bruttoregistertonnen, Besatzungsstärke, Typenbezeichnung, Name) VALUES
  (1, 1000.5, 10, 'Containerschiff', 'Hersteller A'),
  (2, 1500.2, 15, 'Tankschiff', 'Hersteller B'),
  (3, 2000.9, 20, 'Frachtschiff', 'Hersteller A'),
  (4, 3000.3, 25, 'Kreuzfahrtschiff', 'Hersteller C'),
  (5, 500.7, 5, 'Fähre', 'Hersteller B');
  
  
INSERT INTO Buchung (Buchungsnummer, Passagennummer, Passagiernummer, Bunchungsdatum, Klasse)
VALUES (1, 3, 5, '2023-03-18', 'First'),
	   (2, 2, 2, '2023-03-17', 'Economy'),
	   (3, 1, 3, '2023-03-19', 'Business'),
	   (4, 4, 4, '2023-03-16', 'Economy'),
	   (5, 5, 1, '2023-03-15', 'First');
	   
	   
INSERT INTO Schiff (Inventarnummer, Typennummer, "Jahr der Fertigung", Seemeilen)
VALUES (1, 3, 2010, 1528.5),
       (2, 1, 2007, 1846.2),
       (3, 2, 2005, 2123.9),
       (4, 4, 2009, 1963.7),
       (5, 1, 2008, 1739.4);


INSERT INTO Kapitän (Kapitänspatentnummer, Angestelltennummer, Seemeilen)
VALUES 
  (123456, 1, 5000.50),
  (789012, 2, 2500.25),
  (456789, 3, 1500.75),
  (234567, 4, 8000.00),
  (890123, 5, 3500.50);


INSERT INTO "Logbuch" ("Code", "Inventarnummer", "Angestelltennummer")
VALUES
    (1, 3, 5),
    (2, 1, 4),
    (3, 4, 3),
    (4, 2, 1),
    (5, 5, 2);
    
    
INSERT INTO "Bank" ("Bankleitzahl", "Bankname")
VALUES 
    (10020030, 'Deutsche Bank'),
    (21045001, 'Commerzbank'),
    (43071016, 'Postbank'),
    (70080000, 'HypoVereinsbank'),
    (30020900, 'ING-DiBa');
    
    
    
INSERT INTO "Hersteller" ("Name") VALUES
('Fender'),
('Gibson'),
('Martin'),
('Taylor'),
('Ibanez');


INSERT INTO "Techniker" ("Lizenznummer", "Angestelltennummer", "Grad der Ausbildung", "Typennummer") VALUES
    (1001, 1, 'Bachelor of Science in Electrical Engineering', 1),
    (1002, 2, 'Master of Science in Mechanical Engineering', 2),
    (1003, 3, 'Bachelor of Science in Marine Engineering', 3),
    (1004, 4, 'Master of Science in Materials Engineering', 4),
    (1005, 5, 'Associate Degree in Welding Technology', 5);
    
    
INSERT INTO "Kapitän_Passage" ("Kapitänspatentnummer", "Passagennummer", "Typennummer")
VALUES
  (123456, 1, 1),
  (789012, 2, 2),
  (456789, 3, 3),
  (234567, 4, 4),
  (890123, 5, 5);


