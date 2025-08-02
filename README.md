# AutoYouTubeBot

This bot automatically reposts top-viewed Creative Commons YouTube videos daily with optional intros and uploads them to your channel.

## Setup

1. Get your YouTube API key and paste it into `config.py`.
2. Create OAuth credentials on Google Cloud. Download `client_secrets.json` into the root folder.
3. Install requirements:
   ```
   pip install -r requirements.txt
   ```
4. Run:
   ```
   python main.py
   ```

On first run, you'll be asked to log into your Google account to authorize the upload.
