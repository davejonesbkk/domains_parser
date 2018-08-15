
from __future__ import print_function
import httplib2
import os, sys, io


from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'DomainParser'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    DRIVE = discovery.build('drive', 'v3', http=http)

 
    
    page_token = None

    while True:

        results = DRIVE.files().list(q="mimeType='application/vnd.google-apps.spreadsheet'",
                                        spaces='drive',
                                        fields='nextPageToken, files(id, name)',
                                        pageToken=page_token).execute()

        for file in results.get('files', []):
        
            if file.get('id') == '1wFDMRyo-NUj5dNDnq1MAMD9CBZ-P8cdxJCha2J3vR5w':
                print('Found file %s' % (file.get('name')))
                my_file_id = file.get('id')
                my_file_name = file.get('name')
                print(my_file_id, my_file_name)
        

        request = DRIVE.files().export(fileId=my_file_id, mimeType=mimeType)
        
        fn = '%s.csv' % (my_file_name)
        data = request.execute()
        with open(fn, 'wb') as fh:
            fh.write(data)
        print('Finished')
    




if __name__ == '__main__':
    main()








