# o projekcie webapp_shop_eu
Projekt szkoleniowy z zakresu admistracji bazami Oracle

# project setup
## anaconda i środowiska wirtualne
```
[PowerShell]
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

## zmienne środowiskowe

sciągnąć plik .env i umieścić go w głównym folderze projektu
upewnić się że plik jest w .gitignore (nie wgrywać go )

### plantUML

zainstalować PlantUML od jebbs extension do VSCode
dodać w ustawieniach server do "markdown-preview-enhanced.plantumlServer": "https://kroki.io/plantuml/svg"
wzorować się na przykładach ze strony https://plantuml.com/


## Docker

Zainstalować zgodnie z instrukcją https://www.docker.com/products/docker-desktop/
Zainstalować rozszerzenie do VSCode Docker od Microsoft

## Dokumentacja

### pliki .md

każda część projektu ma swój plik z dokumentacją
[backend](./backend/doc_backend_main.md)
[frontend](./frontend/doc_frontend_main.md)
[db](./db/doc_db_main.md)

## Diagramy UML i inne

[UC](./_docu/use_case.md)
[Deployment](./_docu/deployment.md)


## Makefile
https://gnuwin32.sourceforge.net/packages/make.htm
make-3.81.exe