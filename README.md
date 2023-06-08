# Epost

## Tag and push

Utfør i rekkefølge, husk å endre versjonstall (1.0.0)
Husk å docker compose før du gjør dette
Du må være logget inn i Docker Desktop

```bash
docker tag epost-flask-server:latest olischio/email-tracker:1.0.4
docker push olischio/email-tracker:1.0.4
```

Dette skal velges i Azure image, husk å endre versjonstall
olischio/email-tracker:1.0.4
Login server
index.docker.io

Token - dckr_pat_jAoBj0ZOEUw8eo3oyVyW9JLy8LU

## Tracking Pixel For Epost

##Installere Flask

*Serveren skal hoste ett bilde av en tracking pixel (eller annet bilde slik at man kan se det)
*Serveren skal ha: Muligheten til å serve ett bilde, Sende en Epost ved bruk av Python (outlook har ekstrapassord for dette)
  *App-passord




  