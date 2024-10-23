CREATE TABLE miasto
(
	id NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) NOT NULL,
	nazwa VARCHAR2(100 BYTE) NOT NULL,
	CONSTRAINT miasto_pkey PRIMARY KEY (id)
);

CREATE TABLE statusa
(
	id NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) NOT NULL,
	nazwa VARCHAR2(150 BYTE) NOT NULL,
	CONSTRAINT status_pkey PRIMARY KEY (id)
);

CREATE TABLE formaPlatnosci
(
	id NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) NOT NULL,
	nazwa VARCHAR2(150 BYTE),
	CONSTRAINT formaPlatnosci_pkey PRIMARY KEY (id)
);

CREATE TABLE formaOdbioru
(	
	id NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) NOT NULL,
	nazwa VARCHAR2(150 BYTE),
	CONSTRAINT formaOdbioru_pkey PRIMARY KEY (id)
);

CREATE TABLE typ
(
	id NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) NOT NULL,
	nazwa VARCHAR2(150 BYTE) NOT NULL,
	CONSTRAINT typ_pkey PRIMARY KEY (id)
);

CREATE TABLE marka
(
	id NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) NOT NULL,
	nazwa VARCHAR2(150 BYTE) NOT NULL,
	CONSTRAINT marka_pkey PRIMARY KEY (id)
);

CREATE TABLE produkt
(
	id NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) NOT NULL,
	marka numeric(10) NOT NULL,
	typ numeric(10) NOT NULL,
	cena numeric(10) NOT NULL,
	nazwa VARCHAR2(150 BYTE) NOT NULL,
	ean VARCHAR2(13 BYTE) NOT NULL,
	ilosc_magazyn numeric(10) NOT NULL,
	CONSTRAINT produkt_pkey PRIMARY KEY (id),
    CONSTRAINT fk_produkt_typ FOREIGN KEY (typ)
		REFERENCES typ (id),	
	CONSTRAINT fk_produkt_marka FOREIGN KEY (marka)
		REFERENCES marka (id)
);

CREATE TABLE klient
(
	id NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) NOT NULL,
	imie VARCHAR2(150 BYTE) NOT NULL,
	nazwisko VARCHAR2(150 BYTE) NOT NULL,
	email VARCHAR2(50 BYTE) NOT NULL,
	telefon VARCHAR2(9 BYTE) NOT NULL,
	miasto numeric(10) NOT NULL,
	kod_pocztowy VARCHAR2(15 BYTE) NOT NULL,
	ulica VARCHAR2(15 BYTE) NOT NULL,
	nip VARCHAR2(12 BYTE),
	nazwa_firmy VARCHAR2(150 BYTE),
	CONSTRAINT klient_pkey PRIMARY KEY (id),
	CONSTRAINT fk_klient_miasto FOREIGN KEY (miasto)
		REFERENCES miasto (id)	
);

CREATE TABLE lista_zakupow
(
	id NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) NOT NULL,
	id_listy numeric(10) NOT NULL,
	produkt numeric(10) NOT NULL,
	ilosc numeric(10) NOT NULL,
	CONSTRAINT lista_zakupow_pkey PRIMARY KEY (id),
	CONSTRAINT fk_lista_zakupow_produkt FOREIGN KEY (produkt)
		REFERENCES produkt (id)	
	
);


CREATE TABLE zamowienie
(
id NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) NOT NULL,
klient numeric(10) NOT NULL,
nr_zamowienia VARCHAR2(20 BYTE) NOT NULL,
formaPlatnosci numeric(10) NOT NULL,
wartosc numeric(10) NOT NULL,
formaOdbioru numeric(10) NOT NULL,
data_zlozenia DATE NOT NULL,
data_wyslania DATE,
status numeric(10) NOT NULL,
lista_zak numeric(10) NOT NULL,
CONSTRAINT zamowienie_pkey PRIMARY KEY (id),
CONSTRAINT fk_zamowienie_klient FOREIGN KEY (klient)
		REFERENCES klient (id),
CONSTRAINT fk_zamowienie_formaPlatnosci FOREIGN KEY (formaPlatnosci)
		REFERENCES formaPlatnosci(id),
CONSTRAINT fk_zamowienie_formaOdbioru FOREIGN KEY (formaOdbioru)
		REFERENCES formaOdbioru(id),
CONSTRAINT fk_zamowienie_lista_zak FOREIGN KEY (lista_zak)
		REFERENCES lista_zakupow(id)

);

   CREATE TABLE logi
(
	uzytkownik varchar2(20) default user not null,
	opis VARCHAR2(300 BYTE) NOT NULL,
	kiedy timestamp default systimestamp
);

