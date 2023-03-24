from app import db, User, Person, Passagier, Gehaltskonto, Schiff, Schifftyp, Angestellter, Kapitaen, Logbuch, Telefonnummer, Bank, Hersteller, Techniker, KapitaenPassage, Passage, Anschlusspassage, Buchung
from datetime import datetime

def create_test_data():
    # create a new user
    user1 = User(username='john', email='john@gmail.com', joined_at=datetime.utcnow(), Sozialversicherungsnummer=111111111)
    user1.set_password('password1')

    # add the user to the session
    db.session.add(user1)

    # commit the session to the database
    db.session.commit()

    # Create some test Persons
    person1 = Person(Sozialversicherungsnummer=111111111, Vorname='John', Nachname='Doe', Postleitzahl=12345,
                    Ort='Testort', Straße='Teststraße', Hausnummer=1, Telefonnummer=123456789)

    person2 = Person(Sozialversicherungsnummer=222222222, Vorname='Jane', Nachname='Doe', Postleitzahl=67890,
                    Ort='Testort', Straße='Teststraße', Hausnummer=2, Telefonnummer=987654321)

    # Add the Persons to the database
    db.session.add(person1)
    db.session.add(person2)
    db.session.commit()

    # Create some test Passagiere
    passagier1 = Passagier(Passagiernummer=1, Sozialversicherungsnummer=111111111)
    passagier2 = Passagier(Passagiernummer=2, Sozialversicherungsnummer=222222222)

    # Add the Passagiere to the database
    db.session.add(passagier1)
    db.session.add(passagier2)
    db.session.commit()

    # Create some test Angestellte
    Angestellter1 = Angestellter(Angestelltennummer= 1, Sozialversicherungsnummer=111111111)
    Angestellter2 = Angestellter(Angestelltennummer= 2, Sozialversicherungsnummer=222222222)

    # Add the Angestellte to the database
    db.session.add(Angestellter1)
    db.session.add(Angestellter2)
    db.session.commit()

    # Create some test Gehaltskonten
    Gehaltskonto1 = Gehaltskonto(Kontonummer= 1, Bankleitzahl= 1, Konstostand= 1000, Bankname= 'Testbank', Angestelltennummer= 1)
    Gehaltskonto2 = Gehaltskonto(Kontonummer= 2, Bankleitzahl= 2, Konstostand= 2000, Bankname= 'Testbank', Angestelltennummer= 2)

    # Add the Gehaltskonten to the database 
    db.session.add(Gehaltskonto1)
    db.session.add(Gehaltskonto2)
    db.session.commit()

    # Create some test Passage

    Passage1 = Passage(Passagennummer= 1, Abfahrtshafen= "Testhafen", Zielhafen= 'Testhafen2', Abfahrtszeit= datetime.utcnow(), Ankunftszeit= datetime.utcnow()) # Time muss mit der datetime Function implementiert werden
    Passage2 = Passage(Passagennummer= 2, Abfahrtshafen= "Testhafen2", Zielhafen= 'Testhafen3', Abfahrtszeit= datetime.utcnow(), Ankunftszeit= datetime.utcnow())

    # Add the Passage to the database
    db.session.add(Passage1)
    db.session.add(Passage2)
    db.session.commit()

    # Create some test Anschlusspassage
    Anschlusspassage1 = Anschlusspassage(passagennummer_1= 1, passagennummer_2= 2)
    Anschlusspassage2 = Anschlusspassage(passagennummer_1= 2, passagennummer_2= 1)

    # Add the Anschlusspassage to the database
    db.session.add(Anschlusspassage1)
    db.session.add(Anschlusspassage2)
    db.session.commit()

    # Create some test Schifftyp
    Schifftyp1 = Schifftyp(Typennummer= 1, Bruttoregistertonnen= 1000, Besatzungsstaerke= 50, Typenbezeichnung= "AAK", Name= "MS-Bounty")
    Schifftyp2 = Schifftyp(Typennummer= 2, Bruttoregistertonnen= 2000, Besatzungsstaerke= 100, Typenbezeichnung= "BBK", Name= "MS-BlackPearl")

    # Add the Schifftyp to the database
    db.session.add(Schifftyp1)
    db.session.add(Schifftyp2)
    db.session.commit()

    # Create some test Schiffe
    Schiff1 = Schiff(Inventarnummer= 1, Typennummer= 1, Jahr_der_Fertigung= 1980, Seemeilen= 1234)
    Schiff2 = Schiff(Inventarnummer= 2, Typennummer= 2, Jahr_der_Fertigung= 1990, Seemeilen= 5678)

    # Add the Schiffe to the database
    db.session.add(Schiff1)
    db.session.add(Schiff2)
    db.session.commit()

    # Create some test Buchungen
    Buchung1 = Buchung(Buchungsnummer= 1, Passagiernummer= 1, Passagennummer= 1, Klasse= 1, Buchungsdatum= datetime.utcnow())
    Buchung2 = Buchung(Buchungsnummer= 2, Passagiernummer= 2, Passagennummer= 2, Klasse= 2, Buchungsdatum= datetime.utcnow())

    # Add the Buchungen to the database
    db.session.add(Buchung1)
    db.session.add(Buchung2)
    db.session.commit()

    # Create some test Kapitaene
    Kapitaen1 = Kapitaen(Kapitaenspatentnummer= 1, Angestelltennummer= 1, Seemeilen= 12345)
    Kapitaen2 = Kapitaen(Kapitaenspatentnummer= 2, Angestelltennummer= 2, Seemeilen= 67890)

    # Add the Kapitaene to the database
    db.session.add(Kapitaen1)
    db.session.add(Kapitaen2)
    db.session.commit()

    # Create some test Logbuch
    Logbuch1 = Logbuch(Code= 1, Inventarnummer= 1, Angestelltennummer= 1)
    Logbuch2 = Logbuch(Code= 2, Inventarnummer= 2, Angestelltennummer= 2)

    # Add the Logbuch to the database
    db.session.add(Logbuch1)
    db.session.add(Logbuch2)
    db.session.commit()

    # Create some test Telefonnummern   
    Telefonnummer1 = Telefonnummer(Telefonnummer= 1, Sozialversicherungsnummer= 111111111)
    Telefonnummer2 = Telefonnummer(Telefonnummer= 2, Sozialversicherungsnummer= 222222222)

    # Add the Telefonnummern to the database
    db.session.add(Telefonnummer1)
    db.session.add(Telefonnummer2)
    db.session.commit()

    # Create some test Bank
    Bank1 = Bank(Bankleitzahl= 1, Bankname= 'Testbank')
    Bank2 = Bank(Bankleitzahl= 2, Bankname= 'Testbank2')

    # Add the Bank to the database
    db.session.add(Bank1)
    db.session.add(Bank2)
    db.session.commit()

    # Create some test Hersteller
    Hersteller1 = Hersteller(Name= 'Nasa')
    Hersteller2 = Hersteller(Name= 'Esa')

    # Add the Hersteller to the database
    db.session.add(Hersteller1)
    db.session.add(Hersteller2)
    db.session.commit()

    # Create some test Techniker
    Techniker1 = Techniker(Angestelltennummer= 1, Lizenznummer= 1, Grad_der_Ausbildung= "diplom", Typennummer= 1)
    Techniker2 = Techniker(Angestelltennummer= 2, Lizenznummer= 2, Grad_der_Ausbildung= "azubi", Typennummer= 2)

    # Add the Techniker to the database
    db.session.add(Techniker1)
    db.session.add(Techniker2)
    db.session.commit()

    # Create some test kapitän_Passage
    kapitaen_Passage1 = KapitaenPassage(Typennummer= 1, Passagennummer= 1, Kapitaenspatentnummer= 1)
    kapitaen_Passage2 = KapitaenPassage(Typennummer= 2, Passagennummer= 2, Kapitaenspatentnummer= 2)

    # Add the kapitän_Passage to the database
    db.session.add(kapitaen_Passage1)
    db.session.add(kapitaen_Passage2)
    db.session.commit()

