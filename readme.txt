Readme pro aplikaci FastAPI
Toto je aplikace FastAPI, která poskytuje rozhraní REST API pro vytváření a správu uživatelů a jejich komunikačních zpráv pro můj budoucí projekt. Aplikace používá MySQL, která je na heroku, jako databázi pro ukládání uživatelských dat. Hlavními součástmi aplikace jsou:

main.py: Tento soubor obsahuje hlavní kód pro spuštění aplikace FastAPI pomocí webového serveru Uvicorn. Definuje také koncové body pro operace API.
mySql_connection.py: Tento soubor obsahuje kód pro navázání spojení s databází MySQL pomocí asynchronních I/O operací.
users.py: Tento soubor obsahuje kód pro vytváření a správu uživatelských dat v databázi. Definuje třídu UsersFunctions, která obsahuje metody pro vytváření, získávání a výpis uživatelských dat.
user_parametrs.py: Tento soubor obsahuje kód pro získání uživatelských dat na základě specifických parametrů, jako je jméno, e-mail atd. Definuje třídu UserParametrs, která obsahuje metody pro získání uživatelských dat na základě různých parametrů.
message.py: Tento soubor obsahuje kód pro vytváření a správu komunikačních zpráv mezi uživateli. Definuje třídu Message, která obsahuje metody pro vytváření, získávání a výpis komunikačních zpráv mezi uživateli.

Chcete-li aplikaci spustit, ujistěte se, že máte na počítači nainstalovaný Python 3.7 nebo vyšší a MySQL. Také se ujistěte, že jste vytvořili databázi a zadali údaje o konfiguraci databáze v souboru mySql_connection.py.
Chcete-li aplikaci spustit, spusťte aplikaci.
Spusťte aplikaci na adrese http://localhost:8000.
V aplikaci jsou k dispozici následující koncové body:

/: Toto je kořenový koncový bod, který vrací zprávu o tom, zda bylo připojení k databázi MySQL úspěšné.

/v1/users/user/create/{jméno}/{příjmení}: Tento koncový bod vytvoří v databázi nového uživatele se zadaným jménem a příjmením.

/v1/users/user/getUser/{id}: Tento koncový bod načte údaje o uživateli z databáze na základě zadaného ID uživatele.

/v1/users/user/getUserParametr/{id}/{parametr_hodnota}: Tento koncový bod načte uživatelská data z databáze na základě zadaného ID uživatele a hodnoty parametru.

/v1/users/user/getMessages/{id_sender}: Tento koncový bod načte komunikační zprávy mezi uživateli na základě zadaného ID odesílatele.

/v1/users/user/sendMessage/{id_sender}/{id_reciver}/{textMessage}: Tento koncový bod vytvoří novou komunikační zprávu mezi uživateli se zadaným ID odesílatele, ID příjemce a textem zprávy.

/v1/users/getAllUsers/: Tento koncový bod načte seznam všech uživatelů v databázi.

Každý koncový bod je dokumentován pomocí dokumentace Swagger UI a OpenAPI na adrese:http://127.0.0.1:8000/docs#/