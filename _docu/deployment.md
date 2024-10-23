[MAIN](../README.md)

```plantuml
@startuml
left to right direction
node "vuejs-app" as vjsapp 
node "fastapi-app"  as faapp
cloud Oracle as orcl

vjsapp -- faapp : dadsa
faapp -- orcl : dadsa
@enduml
```
