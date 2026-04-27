# API Choice - Atelier Monitoring QoS

- **Étudiant** : Enzo
- **API choisie** : Agify
- **URL base** : https://api.agify.io
- **Documentation officielle** : https://agify.io/
- **Auth** : None (No Auth)
- **Endpoints testés** :
  - `GET https://api.agify.io?name=enzo` : Prédit l'âge à partir d'un prénom.
- **Hypothèses de contrat (champs attendus, types, codes)** :
  - Le code de retour HTTP doit être **200**.
  - Le corps de la réponse doit être au format **JSON**.
  - Le champ `name` doit être une chaîne de caractères (**string**).
  - Le champ `age` doit être un entier (**int**) ou `null`.
  - Le champ `count` doit être un entier (**int**).
- **Limites / rate limiting connu** : Limite gratuite à 1000 noms par jour.
- **Risques (instabilité, downtime, CORS, etc.) :** - Latence réseau variable.
  - Possibilité de réponse vide si le prénom est inconnu (à gérer dans les tests).
