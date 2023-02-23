### WHO global air quality guidelines: particulate matter (‎PM2.5 and PM10)‎, ozone, nitrogen dioxide, sulfur dioxide and carbon monoxide
[9789240034228-eng.pdf (who.int)](https://apps.who.int/iris/bitstream/handle/10665/345329/9789240034228-eng.pdf?sequence=1&isAllowed=y) 

# Vreme

arhiv vseh

https://meteo.arso.gov.si/met/sl/app/webmet/#webmet==8Sdwx2bhR2cv0WZ0V2bvEGcw9ydlJWblR3LwVnaz9SYtVmYh9iclFGbt9SaulGdugXbsx3cs9mdl5WahxXYyNGapZXZ8tHZv1WYp5mOnMHbvZXZulWYnwCchJXYtVGdlJnOn0UQQdSf;

Vsega je tukaj dosti https://meteo.arso.gov.si/met/sl/aviation/

# Voda
## Water flow
Pretok arhiv (nisem delal scraperja, ker se mi ne zdi preveč pomemben)
http://vode.arso.gov.si/hidarhiv/pov_arhiv_tab.php

## Water quality 
A little bit bigger of a collection for all water, mainly the water quality https://www.arso.gov.si/vode/podatki/
POMEMBNO JE, da je ta arhiv pod licenco [licenco CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/deed.sl) in to res nisem ziher kaj pomeni za naš projekt
All si already in an exel format and is rather fun

I think it is a rather good question which water qualities we would be looking at because I think that looking at how clean a river is will not have a big effect on our health (although I am open to having my opinion changed) but something like underground water could be a very important thing

There is also this link that I found but I seem to have some diffilculties trying to navigate it
https://www.gov.si/teme/onesnazevanje-voda/


# Zrak

https://www.arso.gov.si/zrak/kakovost%20zraka/podatki/

https://www.ljubljana.si/sl/moja-ljubljana/varstvo-okolja/stanje-okolja/kakovost-zraka/?AirMonitoringPointID=3

There seems to be a fair bit of information on air quality using sensor.community.com but I just have to figure out how to access it properly

## sensor.community
https://archive.sensor.community/csv_per_month/ Is the link that will be used, I think I can get a fair bit of use out of it, especially if I manage to actually open and close excel files and zip files using python.

```txt
bme280  - Digital humidity, pressure and temperature sensor
bmp180  - Digital pressure and temperature sensor
bmp280  - Digital, barometric pressure sensor
dht22   - Temperature and Humidity Sensor 
ds18b20 - Digital Thermometer
hpm     - Particulate Matter Sensor (PM)
htu21d  - relative humidity and temperature sensors 
laerm   - No idea, should not exist
nextpm  - Particulate Matter Sensor
pms1003 - Air Quality Sensor (AQ)
pms3003 - Air Quality Sensor
pms5003 - Air Quality Sensor
pms6003 - Air Quality Sensor
pms7003 - Air Quality Sensor
ppd42ns - Air Quality Sensor
radiation 
scd30   - CO2, Humidity, Temperature
sds011  - Air Quality Sensor
sht11   - Digital humidity and temperature sensor
sht15   - Digital humidity and temperature sensor
sht30   - Digital humidity and temperature sensor
sht31   - Digital humidity and temperature sensor
sht35   - Digital humidity and temperature sensor
sht85   - Digital humidity and temperature sensor
sps30   - PM and Air Quality Sensor
ppd42ns - Dust Sensor (PM)
```

https://archive.sensor.community/sensors_per_country_per_day.json'
Also here, I can see how man sensors were active in each county that I am looking at, meaning that this could give us even more information on EU values

We also have the EUs data set [Users’ corner (europa.eu)](https://aqportal.discomap.eea.europa.eu/index.php/users-corner/)

Ampak v okviru slovenije pa je dokaj pomembno omeniti, da je v resnici EU spletna stran narejena preko ARSO podatkov

[Kakovost zraka - aktualni podatki » Mestna občina Ljubljana](https://www.ljubljana.si/sl/moja-ljubljana/varstvo-okolja/stanje-okolja/kakovost-zraka/?Date=6.1.2022&AirMonitoringPointID=3)
Tukaj lahko za nazaj poberemo ogromne količine podatkov


## ARSO
[www.arso.gov.si - Dnevni podatki](http://www.arso.gov.si/xml/zrak/ones_zrak_dnevni_podatki_zadnji.xml) 
Tukaj lahko najdemo za trenuten dan PM10 in PM2.5 za par postaj ter za par drugih postaj tudi podatke kot so co, o3, no2

[Indeks in podatki o kakovosti zraka: Ljubljana Bežigrad, tabela za 30 dni (gov.si)](https://www.arso.gov.si/zrak/kakovost%20zraka/podatki/amp/e00_t_30.html)
Delci PM10, Delci PM2.5, dušikov dioksid, ogljikov monoksid, ozon, benzen. Imamo še za par drugih postaj, samo imajo veliko manj podatkov. Ampak je pa recimo še kaka stvar, kot na primer žveplo itd
Druge postaje so:
1. MS Cankarjeva
2. MS Rakiceva
3. MB Vrbanski
4. MB Titova
5. Ptuj
6. CE Ljubljanska
7. CE Bolnica
8. Trbovlje
9. Zagorjke
10. Krvavec
11. Kranj
12. LJ Celovska
13. LJ Bezigread
14. LJ Vic
15. Novo mesto
16. Iskrba
17. Rezica v slovenski bistrici
18. Kopert
19. NG Grcna
20. Otlica?
Tukaj imamo podatke za 30 dni nazaj

[Zadnje urne in dnevne ravni onesnaževal (gov.si)](https://www.arso.gov.si/zrak/kakovost%20zraka/podatki/dnevne_koncentracije.html)
Tukaj najdemo za nek dan vse skupaj skoncentrirano,  
PM10,PM2,5,SO2,CO,Ozon,NO2,Benzen

[Ioni_D_PM2.5_IS_2022.pdf (gov.si)](https://www.arso.gov.si/zrak/kakovost%20zraka/podatki/Ioni_D_PM2.5_IS_2022.pdf)
Podatki za leto 2022 o dnevnih ravneh ionov v delcih PM 2.5

[Arhiv podatkov o kakovosti zraka (gov.si)](https://www.arso.gov.si/zrak/kakovost%20zraka/podatki/arhiv.html)
- Ozon, 
- PM10, 
- PM2.5, 
- Kemijska analiza delcev PM10, 
- Kemijska analiza delcev PM2,5,
- Kemijska analiza padavin,
- Lahkohlapni ogljikovodiki

[Microsoft Word - Porocilo Kemis ARSO 30.6. (gov.si)](https://www.arso.gov.si/Porocilo%20Kemis%20ARSO%2030.6..pdf)
Poročilo o analizah stanja voda, tal in zraka po požaru v podjetju Kemis na Vrhniki (15. 5. 2017 ob 20h)


[Microsoft Word - AIRPECOinPEOPLEporocilo.doc (gov.si)](https://www.arso.gov.si/zrak/kakovost%20zraka/poro%c4%8dila%20in%20publikacije/AIRPECOinPEOPLEporocilo.pdf)
Tukaj lahko primerjamo naše najdbe z najdbami 


[Kakovost zraka - aktualni podatki » Mestna občina Ljubljana](https://www.ljubljana.si/sl/moja-ljubljana/varstvo-okolja/stanje-okolja/kakovost-zraka/?AirMonitoringPointID=3)
Mestna občina Ljubljana spremlja to natančno in mislim, da bi se dalo z malo dela dobiti proper scrape vsega skupaj.,
SO2, NO, NO2, PM10, Benzen, Toluen, Paraksilen, Trdni delci PM2, 
Prav tako imamo dve lokaciji

