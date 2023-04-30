# Global Navigation Satellite System (GNSS) and GPS

Il y a 4 GNSS :

- GPS (USA)
- GLONASS (Russie)
- Galileo (Europe)
- Beidou (Chine)

## Les enjeux

- Positions ± $3m$
  - Navigation maritime (AIS)
  - Usages militaires
  - Logistique
- Le temps (± $3ns$, UTC ± $1\mu s$)
  - Synchronisaation des réseaux de télécommunications
  - Synchronisation des réseaux d'énergie
  - NTP (Network Time Protocol)
- ...


## Puces

Les puces GPS font des corrélations de signaux pour déterminer la position. Elles sont donc très sensibles aux interférences. Les interférences peuvent être :

- Physiques
  - Métal
  - Eau
  - Brouillage
- Logicielles
  - Mauvaise calibration
  - Mauvaise configuration
  - Mauvaise utilisation
- ...

## Trames NMEA

Les trames NMEA sont des trames de données GPS. Elles sont composées de champs séparés par des virgules. 

```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
```

## Les menaces

- Brouillage
- Rejeu
- Relais
- Leurrage