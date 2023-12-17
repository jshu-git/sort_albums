a simple python program to sort your saved spotify albums by release date (because spotify doesn't provide the option to)

#### Setup
1. create an app from https://developer.spotify.com/dashboard
    - copy `CLIENT_ID` and `CLIENT_SECRET` credentials
2. `pip install -r requirements.txt`
4. `export CLIENT_ID='' ; export CLIENT_SECRET=''`

#### Usage
1. `python main.py`
    - this script sorts your albums by release date
    - it will also backup your current album order to a json file (defaults to `backup.json`) in case you want to restore it later

2. `python backup.py`
    - this script backs up your current album order to a json file

3. `python restore.py`
    - this script restores your album order from a json file

#### some notes
- the very first time the script is run, you may need to open a link in your browser to authorize spotify
    - it may open and close automatically if you are already logged into spotify
- the backup file location can be changed through the `BACKUP_PATH` environment variable
    - `export BACKUP_PATH='~/Documents/albums.json'`
