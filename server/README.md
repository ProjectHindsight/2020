## Google Cloud / Firestore Authentication
1. Obtain the `projecthindsight.json` Firebase key from the team and add it into the `/server/keys` directory.
  * Make the `/server/keys` directory if it does not exist.
2. Create a `.env-no-git` file in the `server` directory and inside write the following:
```
## API & Credentials
FIREBASE_SERVICE_ACCOUNT_PATH='./keys/projecthindsight.json'
```
  * The `.env-no-git` file will not be automatically added to Git
  * Will not have to replace the service account file path every time.