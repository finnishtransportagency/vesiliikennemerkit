![Väyläviraston logo](https://vayla.fi/documents/25230764/35412219/vayla_sivussa_fi_sv_rgb.png)
# Suomen vesiliikennemerkit QGIS-kuvakirjastona
[See below for summary in English](https://github.com/finnishtransportagency/vesiliikennemerkit#summary-in-english)

### Sisältö
Tämä repositorio sisältää PNG-kuvakokoelman Suomen vesiliikennemerkeistä sekä Python-skriptin, jolla voidaan muuttaa QGIS-tason pistesymbolit vesiliikennemerkeiksi. Lisää merkeistä [Väyläviraston](https://vayla.fi/vaylista/vesivaylat/vesiliikennemerkit) ja [Traficomin](https://www.traficom.fi/fi/liikenne/merenkulku/vesiliikennemerkit-ja-valo-opasteet) verkkosivuilla.

### Käyttöönotto QGIS 3 -ohjelmassa
Kirjasto on räätälöity käytettäväksi QGIS-paikkatieto-ohjelmassa. Merkit sekä Python-skripti ladataan QGIS:iin [Resource sharing](http://qgis-contribution.github.io/QGIS-ResourceSharing/) -nimisen laajennoksen (plugin) kautta.

1. Asenna Resource sharing QGIS:n laajennosjakelusta (*Plugins* > *Manage and install plugins*).
2. Avaa Resource sharing (*Plugins* > *Resource sharing*). Plugin näyttää listauksen saatavilla olevista kokoelmista. Näiden joukossa on useampi *Väylävirasto...*-alkuinen kokoelma. Voit rajata kokoelmia myös yläosan hakupalkista.
3. Asenna haluamasi kokoelmat.

### Kirjastojen käyttö
Pistemuotoiset datat voi visualisoida PNG-kuvilla avaamalla tason symbologian ja asettamalla symbolityypiksi *Raster Image Marker*. Rasterikuvasymbolin lähde asetetaan klikkaamalla *...* ja valitsemalla haluttu kuva. 

Jos tason pisteissä on attribuuttitietona, mitä merkkiä ne esittävät, ne voi visualisoida automaattisesti oikealla merkillä Python-skriptillä. Avaa skripti työkaluvalikosta (*Processing*>*Toolbox*), jossa sen on *Scripts* alavalikon alla (*Finnish Waterway Sign Stylizer (PNG)*). Valitse skriptin parametrit:
1. Pistemuotoinen taso (esimerkiksi Digiroadin liikennemerkkipisteet).
2. Sarake, jossa merkkikoodit ovat. Esimerkiksi Haavin aineistoissa tämä on *vlmlajityyppi* tai *vesiliikennemerkin laji*. Koodit ovat numeroita 0–37.
3. Skripti voi myös asettaa kuvat skaalautumaan karttanäkymän mittakaavan mukaan. 

Jos kaikki menee kuten pitää, pisteet korvautuvat välittömästi oikealla merkeillä karttaikkunassa. Jos kuvapisteissä näkyy vain mustia kysymysmerkkejä, varmista valitseesi oikean tason ja sarakkeet.

### Käyttöehdot
Liikennemerkkikuvat jaetaan avoimena datana ilman muita vaatimuksia (CC0). Lue lisää lausumasta [Creative Commonsin verkkosivuilla](https://creativecommons.org/publicdomain/zero/1.0/deed.fi).

### Palaute
Kehitysehdotuksia tai bugi-ilmoituksia, ruusuja tai risuja? Lähetä ne osoitteeseen paikkatieto(ät)vayla.fi tai avaa uusi keskustelu tämän repositorion *Issues*-välilehdellä.

### Summary in English
This repository houses PNG image libraries of Finnish waterway signs (read more on the signs [here](https://vayla.fi/en/transport-network/waterways/navigation-marks) and [here](https://www.traficom.fi/en/transport/maritime/waterway-signs-and-light-signals)). The images are identified by a unique numeral code. The libraries can be imported to QGIS using the [Resource sharing plugin](http://qgis-contribution.github.io/QGIS-ResourceSharing/). The collections also include a prosessing script for easily visualizing a point layer with the images.

The image data is provided by Finnish Transport Infrastructure Agency and is shared under CC0. Read more on the deed [here](https://creativecommons.org/publicdomain/zero/1.0/deed.en).
