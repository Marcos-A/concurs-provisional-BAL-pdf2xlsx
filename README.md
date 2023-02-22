# concurs-provisional-BAL-pdf2xlsx

- [Català](#què-fa)

- [English](#deployment)

## Què fa

A partir del PDF amb el llistat provisional d'aspirants admesos al concurs de mèrits de les Illes Balears convocat per resolució de 3 de novembre de 2022 ([BOIB núm. 147, 15 de novembre de 2022](https://www.caib.es/sites/estabilitzacio/f/405203)) es genera un fitxer XLSX amb els següents camps:

- nom: Nom de l'aspirant.
- especialitat: Codi i nom de l'especialitat a la qual es presenta l'aspirant.
- puntuació: Resultat provisional de la baremació.
- posició: Posició de l'aspirant a l'especialitat en qüestió.
- observacions: En cas d'empat en la baremació obtinguda per diversos aspirants dins d'una mateixa especialitat, mostra un avís indicant que la posició d'aquests és merament alfabètica. Per tal d'obtenir un nombre de posició més acurat en aquests casos, s'indica que han de consultar-se els criteris de desempat de la convocatòria.
- altres especialitats: Conté altres especialitats on l'aspirant ha estat admès/a, així com la seva posició respectiva a cadascuna d'elles.

L'esmentada resolució de 3 de novembre de 2022 convoca el procés selectiu d'estabilització, mitjançant el sistema excepcional de concurs de mèrits per a l'ingrés als cossos docents de professors d'ensenyament secundari, de professors d'escoles oficials d'idiomes, de professors de música i arts escèniques, de professors d'arts plàstiques i disseny, de mestres de taller d'arts plàstiques i disseny, de mestres i de professors especialistes en sectors singulars de formació professional a les Illes Balears.

## Limitacions

- En cas d'empat de puntuació entre diversos aspirants a una mateixa especialitat, el llistat resultant no ordena aquests d'acord amb els criteris de desempat de la [convocatòria](https://www.caib.es/sites/estabilitzacio/f/405203) (Annex 1, punt 7.2, «Criteris de desempat»), sinó que ordena les seves posicions alfabèticament pel nom de l'aspirant.
- En cas que un aspirant s'hagi presentat a més d'una especialitat, el llistat resultant no reflecteix l'ordre de preferència en què aquestes van ser demanades, donat que aquesta informació no ha estat publicada al llista provisional.
- El llistat resultant no té en compte si l'aspirant s'ha presentat al concurs de mèrits del procés d'estabilització en altres comunitats autònomes.
- Per últim, la natura del barem no és definitiva, atès que el llistat publicat és provisional i està subjecte a la possibilitat de reclamacions per part dels aspirants.

## Requisits

- Docker.

## Desplegament

1. Descarregar el repositori a un directori qualsevol amb permissos d'escriptura:
  `$ curl -O https://github.com/Marcos-A/concurs-provisional-BAL-pdf2xlsx/archive/refs/heads/master.zip`

2. Crear la imatge i iniciar el contenidor:
  `$ docker-compose up --build -d`

Tan bon punt el contenidor estigui en execució, la aplicació s'executarà en segon pla. El contenidor s'aturarà un cop s'exporti el fitxer XLSX resultant a la carpeta `processed`.

## Fonts

- Llista provisional d'aspirants admesos: [Baremació Convocatòria extraordinària mèrits [PROVISIONAL] Punt 6.1 de la convocatôria](https://intranet.caib.es/sites/estabilitzacio/f/413838)
- Resolució de 3 de novembre de 2022 per la qual es convoca el procés selectiu d'estabilització, mitjançant el sistema excepcional de concurs de mèrits per a l'ingrés als cossos docents de professors d'ensenyament secundari, de professors d'escoles oficials d'idiomes, de professors de música i arts escèniques, de professors d'arts plàstiques i disseny, de mestres de taller d'arts plàstiques i disseny, de mestres i de professors especialistes en sectors singulars de formació professional a les Illes Balears: [BOIB núm. 147, 15 de novembre de 2022](https://www.caib.es/sites/estabilitzacio/f/405203)

## Fitxer resultant

XLSX resultant disponible per la seva consulta a [bit.ly/concurs-prov-bal](https://docs.google.com/spreadsheets/d/1TMORKPcVO2CwsxkFuOdPb31-QATAuABh/edit?usp=sharing&ouid=115479152041016418632&rtpof=true&sd=true).

---

---

## Requirements

- Docker.

## Deployment

1. Download the repository to any directory with writing permissions:
`$ curs -O https://github.com/Marcos-A/concurs-provisional-BAL-pdf2xlsx/archive/refs/heads/master.zip`

2. Build the image and start the container:
`$ docker-compose up --build -d`

As soon as the container starts, the application will run in dettached mode. The container will stop once the resulting XLSX file has been exported to the `processed` folder.

## Sources

- Provisional list of admitted applicants: [Baremació Convocatòria extraordinària mèrits [PROVISIONAL] Punt 6.1 de la convocatòria](https://intranet.caib.es/sites/estabilitzacio/f/413838)
