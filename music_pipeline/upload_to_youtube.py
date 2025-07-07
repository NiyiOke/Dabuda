"""Upload a video to YouTube using the YouTube Data API."""
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']


def authenticate():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('youtube', 'v3', credentials=creds)


def upload(video_file, title='Automated Music', description='Automatically generated music'):
    youtube = authenticate()
    body = {
        'snippet': {
            'title': title,
            'description': description,
        },
        'status': {
            'privacyStatus': 'public'
        }
    }
    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)
    request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=media
    )
    response = request.execute()
    print(response)


if __name__ == '__main__':
    import sys
    upload(sys.argv[1] if len(sys.argv) > 1 else 'output.mp4')
