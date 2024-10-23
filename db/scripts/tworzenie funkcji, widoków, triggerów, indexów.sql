

--WIDOKI

Create or Replace view sprawdzmagazyn as
select m.nazwa "Marka", t.nazwa "Typ produktu", p.cena, p.nazwa "Nazwa produktu",
p.ean, p.ilosc_magazyn "Stan magazynowy"
from produkt p, marka m, typ t
where
p.marka = m.id and
p.typ = t.id
order by 
p.ilosc_magazyn asc;

/



Create or Replace view podsumowanie_miesiaca as
select to_char(TRUNC(TO_DATE(zamowienie.data_zlozenia, 'YYYY-MM-DD'))) as "Miesiąc",
formaPlatnosci.nazwa as "Forma płatności", count(formaPlatnosci.id) as "Ilość transakcji",
sum(zamowienie.wartosc) || ' ' || 'zł' as "Suma tranzakcji"
from zamowienie, formaPlatnosci
WHERE
zamowienie.formaPlatnosci = formaPlatnosci.id
group by formaplatnosci.nazwa, TRUNC(TO_DATE(zamowienie.data_zlozenia, 'YYYY-MM-DD'))
order by TRUNC(TO_DATE(zamowienie.data_zlozenia, 'YYYY-MM-DD')) asc;
ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD';

--FUNKCJE W SUMIE 5


create or replace function podsum_sprzedazy 
	return varchar2 as
	wynik number;

begin 
		select sum(zamowienie.wartosc) into wynik from zamowienie;
        return concat(wynik, ' zl');

end;

/

create or replace function dodaj_stan(prod in number, ile in number) return varchar2 is
PRAGMA AUTONOMOUS_TRANSACTION;
begin

update produkt
set ilosc_magazyn=ilosc_magazyn+ile
where produkt.id = prod;
commit;
return 'Pomyślnie dodano stan produktu';
EXCEPTION
when no_data_found then
	return 'Produkt o id= % nie istnieje w bazie danych.';
end;

/

create or replace function zdejmij_stan(prod in number, ile in number) return varchar2 is
PRAGMA AUTONOMOUS_TRANSACTION;
begin
update produkt
set ilosc_magazyn=ilosc_magazyn-ile
where produkt.id = prod;
commit;
return 'Pomyślnie odjęto stan produktu';
EXCEPTION
when no_data_found then
	return 'Produkt o id= % nie istnieje w bazie danych.';
end;

/

create or replace PROCEDURE update_adres
(idd number, miastoo number, kod_pocztowyy varchar2, ulicaa varchar2)
IS
BEGIN
UPDATE klient
SET miasto = miastoo,
	kod_pocztowy=kod_pocztowyy,
	ulica=ulicaa
WHERE id = idd;
END;

/

create or replace function pokaz_produkt(idd in number)
return  varchar2 as
wynik varchar2(150 byte);
numer number;

begin
select p.nazwa, p.ilosc_magazyn into wynik,numer from produkt p
where p.id = idd;

return concat(wynik||' ', 'Stan na magazynie: '||numer);

end;

/

--PRZYKŁADY UŻYCIA FUNKCJI

                  --id, ilość
--select zdejmij_stan(1, 10) from dual;
--select dodaj_stan(1, 10) from dual;
                  
--select podsum_sprzedazy() from dual;             
                 --id klienta, miasto, kod_pocztowy, ulica
--execute update_adres(1, 1, '12-345', 'Ulica');
                     --id produktu
--select pokaz_produkt(2) from dual;

--FUNKCJE TRIGGERUJĄCE I TRIGGERY

create or replace trigger po_update
 AFTER UPDATE
  ON produkt
  FOR EACH ROW
  BEGIN
 INSERT into logi VALUES (user, 'Aktualizacja stanu produktu: ' ||
         :OLD.nazwa ||' Poprzednia wartość :' ||:OLD.ilosc_magazyn ||' Aktualny stan: ' ||
         :NEW.ilosc_magazyn, systimestamp);
  END;

/

create or replace trigger adres_update
 AFTER UPDATE
  ON klient
  FOR EACH ROW
  BEGIN
  INSERT into logi VALUES (user, 'Aktualizacja danych klienta. Miasto: ' ||:NEW.miasto
  || ', Kod pocztowy: ' ||:NEW.kod_pocztowy||', Ulica: '||:NEW.ulica, systimestamp);
  END;

/

create or replace trigger produkt_insert
 AFTER insert
  ON produkt
  FOR EACH ROW
  BEGIN
  INSERT INTO logi
         VALUES(user, CONCAT('Dodano nowy podukt o nazwie: ',:NEW.nazwa), systimestamp);
  END;

/
  
create or replace trigger po_zamowieniu
 AFTER insert
  ON zamowienie
  FOR EACH ROW
  BEGIN
  INSERT INTO logi
         VALUES(user, 'Dodano nowe zamówienie. Nr zamowienia: '||:NEW.nr_zamowienia||
         ', Wartość: '||:NEW.wartosc||'zl', systimestamp);
  END;
  
/

create index klient_x on zamowienie(klient);
/
create index status_x on zamowienie(status);
  
                   
--insert into lista_zakupow (id_listy, produkt, ilosc) values ('21','4', '3');
--insert into zamowienie (klient, nr_zamowienia, formaPlatnosci, wartosc, formaOdbioru, data_zlozenia, data_wyslania, status, lista_zak)
--values ('1', 'A1021', '1', '135', '7', '2021-07-01', '2021-07-05', '1', '21')

