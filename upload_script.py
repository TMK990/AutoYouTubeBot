import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CLIENT_SECRETS_FILE = "client_secrets.json"
CREDENTIAL_FILE = "youtube_credentials.json"

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    with open(CREDENTIAL_FILE, "w") as f:
        json.dump(creds.to_json(), f)
    return build("youtube", "v3", credentials=creds)

def upload_video(filepath, title, description, privacy="public"):
    youtube = get_authenticated_service()
    body = {"snippet": {"title": title, "description": description, "categoryId": "10"},
            "status": {"privacyStatus": privacy}}
    media = MediaFileUpload(filepath)
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    response = request.execute()
    print("Uploaded video ID:", response.get("id"))
