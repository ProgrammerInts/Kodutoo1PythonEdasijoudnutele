# Kodutoo1PythonEdasijoudnutele
1.kodutöö. API, Flask ja andmebaasid.

Ülesanne:

1) Looge Pythoniga SQLite andmebaas KOHVIKUD, mis sisaldab tabelit SOOKLA.

Tabeli väljad on: ID, Name, Location,  time_open, time_closed. Võite soovi korral omal äranägemisel lisada väljasid juurde.

Koduülesandega kaasas olevast .csv failist lisage Pythoniga andmed andmebaasi. Palun pöörake tähelepanu, et failis esinevad täpitähed, mis peaks ka andmebaasi üle kanduma (kodeering!).

Looge API, mis võimaldab:
1) Pärida kõiki kohvikuid andmebaasist (GET)
2) Pärida kohvikuid avamisaja järgi (GET)
3) Lisada uusi kohvikuid (POST)
4) Muuta kohviku andmeid (PUT)
5) Kustutada kohvik andmebaasist (DELETE)

2) Looge Flaski veebileht, mis pärib andmeid sellest API-st ja näitab neid brauseris. Veebileht peab võimaldama teha kõiki API-s olevaid päringuid, st peab saama näha kõigi kohvikute andmeid, pärida neid veebilehel sisestatud avamisaegade ajavahemiku järgi, lisada uusi söögikohtasid, olemasolevaid andmeid muuta ja kustutada.

Avamisaja järgne päring peab võimaldama pärida nii, et kui pärida näiteks söögikohtasid, mis on lahti 18.30-21.00, siis antakse vastuseks ainult Nuudel ja Tehnopoli Pizzakiosk.

14.02 loengu lõpuosas (nähtav Echo360-s) selgitan ma ülesande sisu täiendavalt.
------------
Suhtluses andmebaasiga võite kasutada kas Pythoniga SQL lausete kirjutamist või ORM-i, nii nagu Teile parem tundub.
Soovituslik on teha kaks erinevat projekti, ühe API ja andmebaas jaoks, teine veebilehe jaoks.
Moodlesse üleslaetud koodis (.zip) ei tohi sisalduda .idea, .venv, _pycache_ ja igasugust muud sodi!
