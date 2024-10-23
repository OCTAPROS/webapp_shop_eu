insert into miasto (nazwa) values ('Warszawa');
insert into miasto (nazwa) values ('Pruszków');
insert into miasto (nazwa) values ('Zielonka');
insert into miasto (nazwa) values ('Legionowo');
insert into miasto (nazwa) values ('Milanówek');
insert into miasto (nazwa) values ('Poznań');
insert into miasto (nazwa) values ('Kostrzyn');
insert into miasto (nazwa) values ('Kleszczewo');
insert into miasto (nazwa) values ('Zborówko');
insert into miasto (nazwa) values ('Mrowino');
insert into miasto (nazwa) values ('Wrocław');
insert into miasto (nazwa) values ('Batowice');
insert into miasto (nazwa) values ('Dziekanowice');
insert into miasto (nazwa) values ('Czarnochowice');
insert into miasto (nazwa) values ('Brzegi');
commit;

insert into status (nazwa) values ('Wysłano');
insert into status (nazwa) values ('W realizacji');
insert into status (nazwa) values ('Anulowano');
commit;


insert into formaPlatnosci (nazwa) values ('Blik'); --1
insert into formaPlatnosci (nazwa) values ('Przelew'); --2
insert into formaPlatnosci (nazwa) values ('PayPal'); --3
insert into formaPlatnosci (nazwa) values ('Eprzelew'); --4
insert into formaPlatnosci (nazwa) values ('Pobranie'); --5
commit;

insert into typ (nazwa) values ('Kubek'); --1
insert into typ (nazwa) values ('Notes'); --2
insert into typ (nazwa) values ('Figurka'); --3
insert into typ (nazwa) values ('Wycieraczka'); --4
insert into typ (nazwa) values ('Naklejki'); --5
insert into typ (nazwa) values ('Magnesy'); --6
insert into typ (nazwa) values ('Koc'); --7
commit;

insert into formaOdbioru (nazwa) values ('KurierInPost'); --1
insert into formaOdbioru (nazwa) values ('KurierGLS'); --2
insert into formaOdbioru (nazwa) values ('PocztaPolska'); --3 
insert into formaOdbioru (nazwa) values ('Paczkomaty'); --4
insert into formaOdbioru (nazwa) values ('KurierDPD'); --5
insert into formaOdbioru (nazwa) values ('KurierDHL'); --6
insert into formaOdbioru (nazwa) values ('Odbior_osobisy'); --7
commit;

insert into marka (nazwa) values ('FineCup'); --1
insert into marka (nazwa) values ('Kubeczki'); --2
insert into marka (nazwa) values ('Mechanikk'); --3
insert into marka (nazwa) values ('CoolNotes'); --4
insert into marka (nazwa) values ('Funpo'); --5
insert into marka (nazwa) values ('StarWorse'); --6
insert into marka (nazwa) values ('NiceMat'); --7
insert into marka (nazwa) values ('NaklejSE'); --8
insert into marka (nazwa) values ('DoLodówy'); --9
insert into marka (nazwa) values ('BedzieCiepło'); --9
--///////////////////
--1
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('1', '1', '30', 'Silny kubek', '2278286065268', '31');
--2
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('2', '1', '40', 'Kubek wieża', '9920688266042', '5');
--3
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('3', '1', '45', 'Kubek granat', '7131065633841', '9');
--4
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('2', '1', '35', 'Czołgowy kubek', '2973987188987', '30');
--5
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('1', '1', '50', 'Kubek twardziela', '7134158762497', '6');
--///////////////////
--6
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('4', '2', '25', 'Świecący notesik', '0308487326874', '10');
--7
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('4', '2', '20', 'Magnesowy notes', '2093483028379', '43');
--8
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('4', '2', '40', 'Pancerny notes', '6960594009213', '45');
--9
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('4', '2', '70', 'Notes z lampką', '7600244607237', '20');
--10
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('4', '2', '70', 'Notes Harry Plotter', '0844741072915', '60');
--///////////////////
--11
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('5', '3', '55', 'Pop HarryPlotter 01', '1759823312768', '70');
--12
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('5', '3', '55', 'Pop RonWeaslu 02', '7568591617777', '32');
--13
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('5', '3', '55', 'Pop WandaVision 05', '2341466512194', '1');
--14
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('5', '3', '55', 'Pop Zgredek 06', '5312061004824', '12');
--15
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('5', '3', '55', 'Pop DarkPhoenix 01', '6552470921964', '9');
--///////////////////
--16
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('6', '4', '30', 'StrongForce', '2242415381451', '51');
--17
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('6', '4', '30', 'JodaWita', '9657561134715', '22');
--18
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('7', '4', '30', 'IćStont', '8955471095166', '11');
--19
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('7', '4', '30', 'DzieńDobry', '6941628282567', '9');
--20
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('7', '4', '30', 'WitajŻengaj', '9959398039813', '46');
--///////////////////
--21
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('8', '5', '15', 'Naklejki samochodziki', '1295026731055', '45');
--22
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('8', '5', '15', 'Naklejki domki', '2552333590720', '63');
--23
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('8', '5', '15', 'Naklejki superbohaterzy', '7027493994749', '2');
--24
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('8', '5', '15', 'Naklejki HarryPlotter', '3761536210758', '33');
--25
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('8', '5', '15', 'Naklejki wyścigówki', '9773611413644', '69');
--///////////////////
--26
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('9', '6', '15', 'Magnesy plażowe', '4590402559832', '43');
--27
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('9', '6', '15', 'Magnesy górskie', '8027976321368', '5');
--28
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('9', '6', '15', 'Magnesy zachód słońca', '5670923962379', '1');
--29
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('9', '6', '15', 'Magnesy fast food', '5998270636621', '25');
--30
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('9', '6', '15', 'Magnesy miasta', '5368684830081', '14');
--///////////////////
--31
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('10', '7', '50', 'Zielony koc', '2978382010222', '57');
--32
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('10', '7', '50', 'Czerwony koc', '2978382010223', '21');
--33
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('10', '7', '50', 'Biały koc', '2978382010224', '34');
--34
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('10', '7', '50', 'Czarny koc', '2978382010225', '5');
--35
insert into produkt (marka, typ, cena, nazwa, ean, ilosc_magazyn) values ('10', '7', '50', 'Fioletowy koc', '2978382010226', '98');
commit;
--///////////////////


insert into klient (imie, nazwisko, email, telefon, miasto, ulica, kod_pocztowy) values ('Arnold', 'Boczek', 'boczek@gmail.com', '624728288', '15', 'Górna', '43-332');
insert into klient (imie, nazwisko, email, telefon, miasto, ulica, kod_pocztowy) values ('Marian', 'Nowak', 'kiepskiezycie@gmail.com', '740231220', '4', 'Olsztyńska', '32-342');
insert into klient (imie, nazwisko, email, telefon, miasto, ulica, kod_pocztowy) values ('Jakub', 'Wiśniewski', 'kubaxx@gmail.com', '016672223', '12', 'Solna', '12-232');
insert into klient (imie, nazwisko, email, telefon, miasto, ulica, kod_pocztowy) values ('Kacper', 'Wójcik', 'kacpir67@gmail.com', '089729729', '5', 'Zielona', '12-440');
insert into klient (imie, nazwisko, email, telefon, miasto, ulica, kod_pocztowy) values ('Filip', 'Kowalczyk', 'xfilipoox@gmail.com', '534388663', '8', 'Pola Wincentego', '01-922');
insert into klient (imie, nazwisko, email, telefon, miasto, ulica, kod_pocztowy) values ('Jan', 'Zieliński', 'jannusz@gmail.com', '312674006', '11', 'Żytnia', '03-443');
insert into klient (imie, nazwisko, email, telefon, miasto, ulica, kod_pocztowy) values ('Zuzanna', 'Kamińska', 'zuza@gmail.com', '529803322', '7', 'Morelowa', '22-123');
insert into klient (imie, nazwisko, email, telefon, miasto, ulica, kod_pocztowy, nip, nazwa_firmy) values ('Maja', 'Jabłońska', 'maja.jablon@gmail.com', '673932826', '1', 'Senatorska', '12-750', '1214941232', 'Kwiaty i te inne');
insert into klient (imie, nazwisko, email, telefon, miasto, ulica, kod_pocztowy) values ('Lena', 'Woźniak', 'wozna@gmail.com', '191797997', '10', 'Księżycowa', '32-777');
insert into klient (imie, nazwisko, email, telefon, miasto, ulica, kod_pocztowy, nip, nazwa_firmy) values ('Marek', 'Cichy', 'jednakglosny@gmail.com', '599066247', '9', 'Spokojna', '53-666', '8111177929', 'BiuroSzofera');
insert into klient (imie, nazwisko, email, telefon, miasto, ulica, kod_pocztowy) values ('Karolina', 'Nowak', 'nowak.karo@gmail.com', '296588068', '6', 'Piwna', '85-993');
insert into klient (imie, nazwisko, email, telefon, miasto, ulica, kod_pocztowy) values ('Aleksandra', 'Nowakowska', 'alex.nowak@gmail.com', '881882908', '13', 'Jastrzębia', '12-234');
commit;   

insert into lista_zakupow (id_listy, produkt, ilosc) values ('1','1', '2'); -- 35 produktów
insert into lista_zakupow (id_listy, produkt, ilosc) values ('2','2', '1'); --
insert into lista_zakupow (id_listy, produkt, ilosc) values ('3','5', '2'); --
insert into lista_zakupow (id_listy, produkt, ilosc) values ('3','9', '3');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('4','8', '1');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('5','4', '5');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('6','12', '1');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('7','17', '1');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('8','19', '3');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('9','33', '1');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('10','31', '2');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('11','22', '1');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('12','20', '2');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('13','2', '1');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('14','4', '3');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('15','11', '1');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('16','10', '1');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('17','1', '3');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('18','12', '1');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('19','17', '1');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('19','1', '1');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('20','17', '1');
insert into lista_zakupow (id_listy, produkt, ilosc) values ('20','6', '1');
commit;
                                                                                                                      --klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('1', 'A1001', '1', '60', '7', '2021-04-01', '2021-04-05', '1', '1');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('2', 'A1002', '1', '40', '2', '2021-04-05', '2021-04-06', '1', '2');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, status, lista_zak) 
values ('3', 'A1003', '1', '310', '1', '2021-7-04', '3', '3');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('4', 'A1004', '5', '40', '2', '2021-04-08', '2021-04-09', '1', '4');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('5', 'A1005', '1', '175', '5', '2021-04-08', '2021-04-09', '1', '5');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, status, lista_zak) 
values ('6', 'A1006', '2', '55', '1', '2021-10-04', '5', '6');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('7', 'A1007', '1', '30', '4', '2021-04-11', '2021-04-13', '1', '7');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('8', 'A1008', '1', '90', '1', '2021-05-11', '2021-05-13', '1', '8');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('9', 'A1009', '4', '50', '2', '2021-05-11', '2021-05-13', '1', '9');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('10', 'A1010', '5', '100', '1', '2021-05-12', '2021-05-13', '1', '10');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('11', 'A1011', '1', '15', '1', '2021-05-13', '2021-05-14', '1', '11');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('12', 'A1012', '3', '60', '6', '2021-06-14', '2021-06-15', '1', '12');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('6', 'A1013', '1', '40', '1', '2021-06-15', '2021-06-16', '1', '13');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, status, lista_zak) 
values ('4', 'A1014', '3', '105', '1', '2021-06-04', '3', '14');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('12', 'A1015', '2', '55', '6', '2021-06-15', '2021-06-16', '1', '15');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('1', 'A1016', '2', '70', '2', '2021-06-15', '2021-06-16', '1', '16');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('2', 'A1017', '1', '90', '5', '2021-06-18', '2021-06-20', '1', '17');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('3', 'A1018', '4', '55', '4', '2021-06-18', '2021-06-20', '1', '18');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('6', 'A1019', '1', '60', '1', '2021-06-20', '2021-06-21', '1', '19');
insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak) 
values ('4', 'A1020', '5', '55', '3', '2021-06-20', '2021-06-21', '1', '20');
commit;