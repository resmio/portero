# portero

Manage your secrets and configurations for multiple deploys

1. Deploy to heroku or other
2. Set configurations with web interface
3. Load them:
`os.environ.update(requests.get(os.environ['PORTERO']).json())` where `PORTERO='https://secretmasterpwd:production@resmio-portero.herokuapp.com/'`
