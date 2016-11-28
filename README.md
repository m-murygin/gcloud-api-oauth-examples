# Google Cloud API auth examples

### Getting started

1. Install requirements

  ```
  pip install -r requirements.txt
  ```

2. Create OAuth 2.0 client ID: `console.cloud.google.com => API Manager => Create credential => OAuth client Id => Other => Create`

3. Download created key as JSON and move it to project folder with name `client_secret.json`

### Run

```
./storage/oauth_flow.py
```