[MAIN](../README.md)
[https://plantuml.com/er-diagram](https://plantuml.com/er-diagram)

```plantuml

### Mapa ekranów sklepu internetowego

@startuml

skinparam linetype ortho
skinparam dpi 150
skinparam padding 20

[Strona główna] -down-> [Strona logowania] : "Zaloguj"
[Strona główna] -down-> [Strona z produktami] : "Przeglądaj produkty"
[Strona główna] -down-> [Koszyk] : "Przejdź do koszyka"

[Strona logowania] -right-> [Strona główna] : "Po zalogowaniu"
[Strona logowania] -down-> [Panel administracyjny] : "Logowanie jako administrator"

[Strona z produktami] -down-> [Koszyk] : "Dodaj do koszyka"
[Strona z produktami] -right-> [Strona produktu] : "Szczegóły produktu"
[Strona z produktami] -left-> [Strona główna] : "Powrót"

[Strona produktu] -left-> [Strona z produktami] : "Powrót"
[Strona produktu] -down-> [Koszyk] : "Dodaj do koszyka"

[Koszyk] -down-> [Kompletacja zamówienia] : "Przejdź do zamówienia"
[Koszyk] -up-> [Strona z produktami] : "Kontynuuj zakupy"
[Koszyk] -left-> [Strona główna] : "Powrót"

[Kompletacja zamówienia] -up-> [Strona główna] : "Złożone zamówienie"

[Panel administracyjny] -down-> [Zarządzanie produktami] : "Zarządzaj produktami"
[Panel administracyjny] -down-> [Zarządzanie klientami] : "Zarządzaj klientami"
[Panel administracyjny] -up-> [Strona główna] : "Wyloguj"

@enduml



```