# Epost

## Tag and push

Utfør i rekkefølge, husk å endre versjonstall (1.0.0)
Husk å docker compose før du gjør dette

```bash
docker tag epost-flask-server:latest olischio/email-tracker:1.0.0
docker push olischio/email-tracker:1.0.0
```

Dette skal velges i Azure image, husk å endre versjonstall
olischio/email-tracker:1.0.1
Login server
index.docker.io

Token - dckr_pat_jAoBj0ZOEUw8eo3oyVyW9JLy8LU

## Tracking Pixel For Epost

##Installere Flask

*Dette skal runne en python server slik at det blir lettere en å lage en nginx server i docker vm eller Azure Resource Group
*Serveren skal hoste ett bilde av en tracking pixel (eller annet bilde slik at man kan se det)
*Serveren skal ha: Muligheten til å serve ett bilde, Sende en Epost ved bruk av Python (outlook har ekstrapassord for dette)
  *App-passord
  Enkelte apper og enheter (for eksempel Xbox 360, Windows Phone eller e-postapper på andre enheter) støtter ikke sikkerhetskoder     for totrinnskontroll. I disse tilfellene må du opprette et app-passord for å logge deg på. Lær mer om app-passord.
  Opprett et nytt app-passord
  Fjern eksisterende app-passord 
  (KAN BARE VISES EN GANG LAGRE PASSORDET)




  