# API Choice

- Étudiant : Mehdi Mazouz
- API choisie : Agify
- URL base : https://api.agify.io
- Documentation officielle / README :
- Auth : None / API Key / OAuth
- Endpoints testés : GET /?name=mehdi
  - GET ...
  - GET ...
- Hypothèses de contrat (champs attendus, types, codes) :
  Champs attendus : name (string), age (integer), count (integer)
  Code de succès : 200 OK
- Limites / rate limiting connu : Environ 1000 requêtes gratuites par jour
- Risques (instabilité, downtime, CORS, etc.) : Instabilité si l'API tombe, données nulles si le prénom est inconnu
