## Google Cloud / Firestore Authentication
1. Place your service account API key JSON file in the `/server/keys` directory.
2. Navigate to the `server` directory and copy the `.env` file into a `.env-no-git` file
  * The `.env-no-git` file will not be automatically added to Git
  * Will not have to replace the service account file path every time.
```
cd ..
cp .env .env-no-git
```
