# sort saved spotify albums by release date because spotify doesn't have the option to

1. create an app and get your credentials from https://developer.spotify.com/dashboard
2. source .venv/bin/activate
3. pip install
4. set creds with export CLIENT_ID='' ; export CLIENT_SECRET=''
5. python -m src.workflows.sort_albums_by_release_date src/workflows/sort_albums_by_release_date.py
