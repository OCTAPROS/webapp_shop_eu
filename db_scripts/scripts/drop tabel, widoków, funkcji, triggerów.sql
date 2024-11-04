drop index klient_x;
drop index status_x;

drop trigger po_update;
drop trigger adres_update;
drop trigger produkt_insert;
drop trigger po_zamowieniu;

drop function podsum_sprzedazy;
drop function dodaj_stan;
drop function zdejmij_stan;
drop procedure update_adres;
drop function pokaz_produkt;

drop table logi;

drop view podsumowanie_miesiaca;
drop view sprawdzmagazyn;

drop table zamowienie;
drop table formaPlatnosci;
drop table formaOdbioru;
drop table status;
drop table klient;
drop table miasto;
drop table lista_zakupow;
drop table produkt;
drop table typ;
drop table marka;