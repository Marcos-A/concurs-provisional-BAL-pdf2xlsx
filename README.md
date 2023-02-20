# concurs-provisional-BAL-pdf2xlsx

[català]()#què-fa)

[english]()#deployment)

## Què fa

A partir del PDF amb el llistat provisional d'aspirants admesos al concurs de mèrits de les Illes Balears convocat per resolució de 3 de novembre de 2022 ([BOIB núm. 147, 15 de novembre de 2022](https://www.caib.es/sites/estabilitzacio/f/405203)) es genera un fitxer XLSX amb els següents camps:

- nom: Nom de l'aspirant.
- especialitat: Codi i nom de l'especialitat a la qual es presenta l'aspirant.
- puntuació: Resultat provisional de la baremació.
- posició: Posició de l'aspirant a l'especialitat en qüestió.
- observacions: En cas d'empat en la baremació obtinguda per diversos aspirants dins d'una mateixa especialitat, mostra un avís indicant que la posició d'aquests és merament alfabètica. Per tal d'obtenir un nombre de posició més acurat en aquests casos, s'indica que han de consultar-se els criteris de desempat de la convocatòria.
- altres especialitats: Conté altres especialitats on l'aspirant ha estat admès/a, així com la seva posició respectiva a cadascuna d'elles.

L'esmentada resolució de 3 de novembre de 2022 convoca el procés selectiu d'estabilització, mitjançant el sistema excepcional de concurs de mèrits per a l'ingrés als cossos docents de professors d'ensenyament secundari, de professors d'escoles oficials d'idiomes, de professors de música i arts escèniques, de professors d'arts plàstiques i disseny, de mestres de taller d'arts plàstiques i disseny, de mestres i de professors especialistes en sectors singulars de formació professional a les Illes Balears.

## Desplegament

Descarregar el repositori a un directori qualsevol amb permissos d'escriptura:

`$ curl -O `

Crear la imatge i iniciar el contenidor:
`$ docker-compose up --build -d`

Tan bon punt el contenidor estigui en execució, la aplicació s'executarà en segon pla. El contenidor s'aturarà un cop s'exporti el fitxer XLSX resultant a la carpeta `processed`.

## Fonts

- Llista provisional d'aspirants admesos: [Baremació Convocatòria extraordinària mèrits [PROVISIONAL] Punt 6.1 de la convocatôria](https://intranet.caib.es/sites/estabilitzacio/f/413838)

---

---

## Deployment

Download the repository to any directory with writing permissions:

`$ curs -O`

Build the image and start the container:

`$ docker-compose up --build -d`

As soon as the container starts, the application will run in dettached mode. The container will stop once the resulting XLSX file has been exported to the `processed` folder.

## Sources

- Provisional list of admitted applicants: [Baremació Convocatòria extraordinària mèrits [PROVISIONAL] Punt 6.1 de la convocatòria](https://intranet.caib.es/sites/estabilitzacio/f/413838)
